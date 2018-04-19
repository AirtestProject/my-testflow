# coding=utf-8

import os
from setuptools import setup, find_packages


def parse_requirements(filename='requirements.txt'):
    """ load requirements from a pip requirements file. (replacing from pip.req import parse_requirements)"""
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


project_name = find_packages()[0]
if '.' in project_name:
    project_name = project_name.split('.', 1)[0]

if os.path.exists('requirements.txt'):
    reqs = parse_requirements()
else:
    reqs = []

setup(
    name='testflow_' + project_name,
    version='1.0.2',
    description='A test automation project using poco and pocounit.',
    packages=find_packages(),
    include_package_data=True,
    install_requires=reqs,
)
