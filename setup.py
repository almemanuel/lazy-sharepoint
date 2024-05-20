from setuptools import setup
setup(
    name='sharepoint-crud',
    version='2.0',
    description='Library for interacting with SharePoint',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Emanuel Almeida',
    author_email='emanuel.almeida1998@outlook.com',
    url='https://github.com/almemanuel/sharepoint-crud',
    packages=['sharepoint_crud'],
    keywords='sharepoint office365',
    install_requires=[
        'office365-rest-python-client == 2.2.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
