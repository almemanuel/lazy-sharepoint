from setuptools import setup, find_packages

setup(
    name='sharepoint-lib',
    version='0.1',
    description='Library for interacting with SharePoint',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Emanuel Almeida',
    author_email='emanuel.almeida1998@outlook.com',
    url='https://github.com/almemanuel/pypoint/pypoint',
    packages=find_packages(),
    install_requires=[
        'office365-rest-python-client == 2.2.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
