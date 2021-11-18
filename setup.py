from setuptools import setup, find_packages

setup(
    name = 'mypackage',
    version = '0.1',
    packages = find_packages(exclude = ['tests*']),
    licence = 'MIT',
    description = 'MY example python package',
    long_description = open('readme.MD').read(),
    install_requires = ['numpy'],
    url = 'https://hothub.com/<username>/<package-name>',
    author = '<Your name>',
    author_email = '<Your email>'
)