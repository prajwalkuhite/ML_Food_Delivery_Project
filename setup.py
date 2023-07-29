from setuptools import setup , find_packages
from typing import List

PROJECT_NAME = "ML FOOD DELIVERY"
VERSION = "0.0.1"
DESCRIPTION = "FOOD DELIVERY ML PROJECT WITH MODULAR CODING APPROACH"
AUTHOR_NAME = "PRAJWAL KUHITE"
AUTHOR_EMAIL = "prajwalkuhite50@gmail.com"

# requirements.txt open
# read
# /n replace with ""
requirements = "requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements()->List[str]:
    with open(requirements) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("/n","") for requirement_name in requirement_list]
    
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)


    return requirement_list


setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(),
      install_requires = get_requirements())
