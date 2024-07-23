import logging

import requests

from src.definitions.credentials import Credentials
from src.services.google import GoogleAPI

logger = logging.getLogger(__name__)


class Meeting:
    def __init__(self):
        self.google = GoogleAPI()
        self._calendly_api_key = Credentials.calendly_api_key()
        self.calendly_base_url = 'https://api.calendly.com'
        self.headers = {
            "Authorization": f"Bearer {self._calendly_api_key}",
            "Content-Type": "application/json"
        }
        self.user_uri = self.get_user_uri()
        self.last_recorded_customer_name = ""
        self.last_recorded_meeting_start = ""
        self.last_recorded_meeting_end = ""


    def get_user_uri(self):
        endpoint = self.calendly_base_url + "/users/me"
        response = requests.get(endpoint, headers=self.headers)
        return response.json()['resource']['uri']

    def list_user_availability_schedules(self):
        endpoint = self.calendly_base_url + "/user_availability_schedules"
        params = {"user": self.user_uri}
        response = requests.get(endpoint, params=params, headers=self.headers)
        if response.status_code == 200:
            response_json = response.json()
            available_schedule = {}
            schedules = response_json['collection'][0]['rules']
            timezone = response_json['collection'][0]['timezone']
            for schedule in schedules:
                if len(schedule['intervals']) == 0:
                    continue
                available_schedule[schedule['wday']] = schedule['intervals']
            # return self.to_readable_schedule(available_schedule, timezone)
            return available_schedule
        else:
            print("Something went wrong")

    def set_meeting(self, meeting_start: str, meeting_end: str, customer_name: str) -> bool:
        # Ignore empty inputs
        if meeting_start == "" or meeting_end == "" or customer_name == "":
            logger.error(f"Failed to set meeting. Meeting information cannot be empty. Meeting Start: {meeting_start}, "
                         f"Meeting End: {meeting_end}, Customer Name: {customer_name}")
            return False
        # Ignore repeat requests
        if (self.last_recorded_meeting_start == meeting_start and
                self.last_recorded_meeting_end == meeting_end and
                self.last_recorded_customer_name == customer_name):
            logger.error(f"Failed to set meeting. Duplicate requests")
            return False
        self.last_recorded_meeting_start = meeting_start
        self.last_recorded_meeting_end = meeting_end
        self.last_recorded_customer_name = customer_name
        logger.info(f"Setting meeting for: {customer_name} from {meeting_start} to {meeting_end}")
        return self.google.create_meeting(meeting_start, meeting_end)
