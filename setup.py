from setuptools import setup, find_packages

setup(
    name='aiomax',
    version='0.5.0',
    description='Max asynchronous API',
    author='oaa dpnspn',
    packages=find_packages(),
    install_requires=['aiohttp'],
    zip_safe=False
)