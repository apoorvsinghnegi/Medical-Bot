#to create our project as local package
from setuptools import find_packages, setup

setup(
    name = 'Generative AI Project',
    version= '0.0.0',
    author= 'Apoorv Singh Negi',
    author_email= 'apoorvsinghnegi18@gmail.com',
    packages= find_packages(), #it will find __init__.py and whenever this file is present it will consider it as a local package
    install_requires = []

)
#after doing pip install -r requirements.txt then .egg-info file will be created which means that this package will is setup as local package