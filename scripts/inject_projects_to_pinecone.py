import pinecone
from langchain.embeddings import OpenAIEmbeddings
from src.definitions.credentials import Credentials
from src.definitions.projects import PROJECTS
from typing import Dict, Any


class Database:
    def __init__(self):
        self.client = pinecone.Pinecone(api_key=Credentials.pinecone_api_key())
        self.index_name = "portfolio-website"
        self.index = pinecone.Index('https://portfolio-website-cvum9mn.svc.aped-4627-b74a.pinecone.io', self.index_name)
        self.embeddings = OpenAIEmbeddings()

    def store_to_pinecone(self):
        for project in PROJECTS:
            project_string = self.project_to_string(project)
            embedding = self.get_embedding(project_string)


    def get_embedding(self, project_string: str):
        pass

def project_to_string(project: Dict[str, Any]):
    project_string = ""
    for key, value in project.items():
        project_string += f'{key}: {value}\n'
    return project_string

if __name__ == "__main__":
    projects = '\n\n'.join([project_to_string(project) for project in PROJECTS])
    print(projects)