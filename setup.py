from setuptools import setup, find_packages

def readme():
    with open('README.md', 'r') as f:
        return f.read()

setup(
    name='aiomax',
    version='0.6.0',
    description='Max asynchronous API',
    author='oaa dpnspn',
    author_email='mbutsk@icloud.com',
    packages=find_packages(),
    install_requires=['aiohttp'],
    zip_safe=False,
    url = "https://github.com/dpnspn/aiomax",
    license="MIT License, see LICENSE.md file",
    long_description=readme(),
    long_description_content_type='text/markdown',
    project_urls={
        "GitBook docs": "https://dpnspn.gitbook.io/aiomax"
    }
)