from setuptools import setup


setup(
    name='chartserver',
    version='1.0',
    install_requires=[
        'numpy',
        'matplotlib',
        'flask'
    ],
    packages=[
        'chartserver'
    ],
    entry_points={
        'console_scripts': [
        ]
    }
)
