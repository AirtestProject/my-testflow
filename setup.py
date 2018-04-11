# coding=utf-8

import os
import sys
from setuptools import setup, find_packages
from pip.req import parse_requirements

current_frame = sys._getframe(0)
caller = current_frame.f_back
this_filename = caller.f_code.co_filename
this_dir = os.path.abspath(os.path.join(this_filename, '..'))
project_name = os.path.basename(this_dir)
print('project name is {}'.format(project_name))


if os.path.exists('requirements.txt'):
    # parse_requirements() returns generator of pip.req.InstallRequirement objects
    install_reqs = parse_requirements('requirements.txt', session=False)

    # reqs is a list of requirement
    reqs = [str(ir.req) for ir in install_reqs if ir.req]
else:
    reqs = []

setup(
    name=project_name,
    version='1.0.0',
    description='A test automation project using poco and pocounit.',
    packages=find_packages(),
    include_package_data=True,
    install_requires=reqs,
)
