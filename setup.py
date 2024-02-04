from setuptools import find_packages, setup
from typing import List
HYPHEN = '-e .'
def get_requirements(file:str)->List[str]:
    with open(file) as filename:
        requirements = filename.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPHEN in requirements:
            requirements.remove(HYPHEN)
    
    return requirements

setup(
    name = 'demo',
    version = '0.0.1',
    author = 'Hari',
    author_email = 'hariprashaadsrofficial@gmail.com',
    packages = find_packages(),
    requires = get_requirements('requirements.txt')
)