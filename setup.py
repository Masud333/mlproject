from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ." # This particular str is located at the end of requirments.txt, automatically builds as it tells system that setup.py is available

def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", " ") for req in requirements] # readlines() func will add \n after each line is read, needs to be replaced with empty str

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    name = 'mlproject',
    version = '0.0.1',
    description='My frist end to end ML project',
    author = 'Masud Jahan',
    author_email = 'masud_5@msn.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt'),
)