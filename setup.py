from setuptools import setup, find_packages

setup(
    name='aiomax',
    version='0.0.1',
    description='Max async api',
    author='oaa dpnspn',
    packages=find_packages(),
    install_requires=['requests'],
    zip_safe=False
)