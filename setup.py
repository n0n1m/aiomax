from setuptools import setup, find_packages

setup(
    name='aiomax',
    version='0.0.2',
    description='Max asynchronous API',
    author='oaa dpnspn',
    packages=find_packages(),
    install_requires=['requests'],
    zip_safe=False
)