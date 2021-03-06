from setuptools import find_packages, setup

setup(
    name='aoc',
    version='1.0',
    url='https://github.com/RazerM/advent-of-code-2018',
    author='Frazer McLean',
    author_email='frazer@frazermclean.co.uk',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'attrs ~= 18.2',
        'click ~= 7.0',
        'python-dotenv >= 0.9.1',
        'requests ~= 2.20',
        'sortedcontainers ~= 2.1',
        'tqdm ~= 4.28',
    ],
    extras_require={
        'test': [
            'pytest ~= 4.0',
        ],
    },
)
