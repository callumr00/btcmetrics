# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='btcmetrics',
    version='0.2.0',
    description='Bitcoin blockchain data extraction and visualization',
    long_description=readme,
    author='Callum Rafter',
    author_email='callum.rafter@gmail.com',
    url='https://github.com/callumr00/btcmetrics',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)