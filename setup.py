# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

requirements=["nbformat>=4","nbconvert>=5","pandas","requests>=2","openpyxl","docs","lint","black","isort"]

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='geneeaAPI',
    version='0.0.1',
    description='text file sender and result gatherer to Geneea API',
    long_description=readme,
    author='Kryštof Pešek',
    author_email='krystof.pesek@gmail.com',
    url='project_url',
    license=license,
    packages=find_packages(where='src',include=['pkg*']),
    package_dir={"":"src"},
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.10.2",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
# write third package here

