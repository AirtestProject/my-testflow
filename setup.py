# coding=utf-8

import os
import sys
import inspect
from setuptools import setup, find_packages
from pip.req import parse_requirements

project_name = find_packages()[0]
if '.' in project_name:
    project_name = project_name.split('.', 1)[0]

if os.path.exists('requirements.txt'):
    # parse_requirements() returns generator of pip.req.InstallRequirement objects
    install_reqs = parse_requirements('requirements.txt', session=False)

    # reqs is a list of requirement
    reqs = [str(ir.req) for ir in install_reqs if ir.req]
else:
    reqs = []

setup(
    name='testflow_' + project_name,
    version='1.0.0',
    description='A test automation project using poco and pocounit.',
    packages=find_packages(),
    include_package_data=True,
    install_requires=reqs,
)
