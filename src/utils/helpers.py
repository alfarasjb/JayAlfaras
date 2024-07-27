from typing import List, Dict, Any


def projects_to_string(projects: List[Dict[str, Any]]):
    projects = '\n\n'.join([get_project_string(project) for project in projects])
    return projects


def get_project_string(project: Dict[str, Any]):
    project_string = ""
    for key, value in project.items():
        project_string += f'{key}: {value}\n'
    return project_string.strip()

