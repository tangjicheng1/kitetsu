from setuptools import setup, find_packages

setup(
    name='kitetsu',
    version='0.0.1',
    author='tangjicheng',
    author_email='tangjch15@gmail.com',
    packages=find_packages(),
    install_requires=[
        'quickfix',  # 确保这里的依赖是正确的，根据QuickFIX Python绑定的实际包名
    ],
    entry_points={
        'console_scripts': [
            'kitetsu=kitetsu.client:main',
        ],
    },
)
