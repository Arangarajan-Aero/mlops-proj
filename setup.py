from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements=f.read().splitlines()
setup(
    name="mlops_proj-1",
    version="0.1.0",
    author="Aero",
    packages=find_packages(),
    install_requires=requirements,
    )
