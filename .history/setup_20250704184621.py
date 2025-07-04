from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirement_lst = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("Error: requirements.txt was not found.")
    return requirement_lst

print(get_requirements('requirements.txt'))

setup(
    name='your_package_name',
    version='0.0.1',
    author='Ankit Gochhayat',
    author_email='ankit.gochhayat90@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)