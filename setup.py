from setuptools import setup, find_packages
import os.path

import sys

__version__ = "2.7.1"

descr_file = os.path.join(os.path.dirname(__file__), "README.rst")

dev_requirements = ["coverage", "pre-commit", "pytest", "pytest-cov", "tox"]

if sys.version_info < (3, 0):
    dev_requirements.append("mock")

setup(
    name="riotwatcher",
    version=__version__,
    packages=find_packages("src", exclude=["test"]),
    package_dir={"": "src"},
    description="RiotWatcher is a thin wrapper on top of the Riot Games API for League of Legends.",
    long_description=open(descr_file).read(),
    author="AG Stephan",
    url="https://github.com/pseudonym117/Riot-Watcher",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing",
        "Topic :: Games/Entertainment :: Real Time Strategy",
        "Topic :: Games/Entertainment :: Role-Playing",
    ],
    license="MIT",
    install_requires=["requests"],
    extras_require={"dev": dev_requirements},
)
