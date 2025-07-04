from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and not requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("Error: requirements.txt was not found.")
    return requirement_lst

print(requirements())