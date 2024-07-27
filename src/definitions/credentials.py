import os

from dotenv import load_dotenv

load_dotenv()


class Credentials:

    @classmethod
    def openai_api_key(cls) -> str:
        return os.getenv("OPENAI_API_KEY")

    @classmethod
    def calendly_api_key(cls) -> str:
        return os.getenv("CALENDLY_API_KEY")

    @classmethod
    def google_token(cls) -> str:
        return os.getenv("GOOGLE_TOKEN")

    @classmethod
    def pinecone_api_key(cls) -> str:
        return os.getenv("PINECONE_API_KEY")


class EnvVariables:

    @classmethod
    def chat_model(cls) -> str:
        return os.getenv("CHAT_MODEL", "gpt-4o")