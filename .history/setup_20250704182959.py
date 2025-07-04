from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    try:
        with open('requirements.txt', 'r') as file:
            return [line.strip() for line in file if line.strip() and not line.startswith('#')]