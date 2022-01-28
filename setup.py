# Import required functions
from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# Call setup function
setup(
    author="Javad Ebadi, Vahid Hoseinzade",
    author_email="javad.ebadi.1990@gmail.com, vahid.hoseinzade64@gmail.com",
    description="A simple python wrapper for inspirehep API",
    name="pyinspirehep",
    packages=find_packages(include=["pyinspirehep", "pyinspirehep.*"]),
    version="0.2.3",
    install_requires=['requests'],
    python_requires='>=3.7',
    license='MIT',
    url='https://github.com/javadebadi/pyinspirehep',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
