from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    try:
        with open(file_path, 'r') as file:
            requirements = file.readlines()
        return [req.strip() for req in requirements if req.strip() and not req.startswith('#')]