import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="Better file system",
    version="1.0.2",
    description="A better file system",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/RandomTheFirst/Better-file-system",
    author="Tzur Soffer",
    author_email="tzur.soffer@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10"
    ],
    packages=[],
    include_package_data=True,
    install_requires=[],
)
