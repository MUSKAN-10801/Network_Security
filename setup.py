'''
the setup.py file is used to define the package
metadata and dependencies for a Python project.
It typically includes information such as the package
name, version, author, description, and any required 
dependencies. The requirements.txt file lists the 
specific packages and their versions that are needed to 
run the project. In this case, the requirements.txt file 
includes python-dotenv, pandas, and numpy as dependencies.
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """Read the requirements.txt file and return a list of dependencies."""
    requirements_lst: List[str] = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirements=line.strip()

                if requirements and requirements!= '-e .':
                    requirements_lst.append(requirements)
    except FileNotFoundError:
        print(f"File not found: {file_path}")

    return requirements_lst

setup(
    name='Network_Security',
    version='0.0.1',
    author='Muskan',
    author_email='muskangupta08022007@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)