from setuptools import setup, find_packages

setup(
    name='elena',
    version='0.0.1',
    packages=find_packages(exclude=['tests']),
    url='https://github.com/rpg711/Elena1st',
    license='MIT',
    author='Elena #1',
    author_email='',
    description='EleNa COMPSCI520',
    install_requires=['geopy', 'overpy'],
)
