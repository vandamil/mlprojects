from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open('requirements.txt') as file:
        requirements=file.readlines()
        requirements=[rec.replace("\n"," ") for rec in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')




setup(
    name='mlprojects',
    version='0.0.1',
    author='Vandamizh',
    author_email='vandamizh21@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)