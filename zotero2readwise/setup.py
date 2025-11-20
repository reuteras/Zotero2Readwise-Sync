from setuptools import setup, find_packages

setup(
    name='zotero2readwise',
    version='0.1.0',
    packages=find_packages(),
    author='Jules-the-AI',
    author_email='jules@example.com',
    description='A forked Zotero to Readwise sync tool with improved error reporting.',
    url='https://github.com/Jules-the-AI/Zotero2Readwise-Sync',
    install_requires=[
        'pyzotero',
        # Add other dependencies here
    ],
)
