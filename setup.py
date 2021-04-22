long_description = open('README.txt').read()

from setuptools import setup, find_packages

requires = ["requests"]

setup(
    name='bigbluebutton-api',
    version='0.8.0',
    author='Reimar Bauer',
    author_email='rb.proj@gmail.com',
    maintainer='Eduard Luca',
    maintainer_email='edu2004eu@gmail.com',
    url='https://github.com/edu2004eu/bigbluebutton-python-api',
    description='Python API for BigBlueButton.',
    long_description=long_description,
    keywords='bigbluebutton',
    license='MIT',
    packages=find_packages(),
    install_requires=requires,
)
