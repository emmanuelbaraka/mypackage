from setuptools import setup, find_packages

setup(
    name  = 'mypackage',
    version= '0.1',
    packages= find_packages(exclude=['test*']),
    license= 'MIT',
    description='EDSA example python package',
    long_description=open('ReadMe.md').read(),
    install_requires= ['numpy'],
    url='https://github.com/emmanuelbaraka/packagestrial',
    author= 'Emmanuel Baraka',
    author_email='emmanuelbaraka53@gmail.com'
)