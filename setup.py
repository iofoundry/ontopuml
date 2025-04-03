from setuptools import setup, find_packages

setup(
    name="nowl",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "click",
        "owlready2",
        "networkx",
        "matplotlib",
    ],
    entry_points={
        "console_scripts": [
            "nowl=translator:main",
        ],
    },
)