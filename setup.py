from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='kitetsu',
    version='0.0.1',
    author='tangjicheng',
    author_email='tangjch15@gmail.com',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'kitetsu=kitetsu.client:main',
        ],
    },
)
