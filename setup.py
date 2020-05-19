from setuptools import setup, find_packages
import os.path

here = os.path.dirname(__file__)

descr_file = os.path.join(here, "README.rst")
version_file = os.path.join(here, "src", "riotwatcher", "__version__.py")

version_info = {}
with open(version_file, "r") as f:
    exec(f.read(), version_info)

dev_requirements = ["coverage", "pre-commit", "pytest", "pytest-cov", "tox"]

setup(
    name=version_info["__title__"].lower(),
    version=version_info["__version__"],
    packages=find_packages("src", exclude=["test"]),
    package_dir={"": "src"},
    description=f"{version_info['__title__']} is a thin wrapper on top of the Riot Games API for League of Legends.",
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
