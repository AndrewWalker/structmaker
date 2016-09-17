from setuptools import setup, find_packages
import re
import io
import os
import sys


def read_version():
    with io.open('./structmaker/version.py', encoding='utf8') as version_file:
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M)
        if version_match:
            version = version_match.group(1)
        else:
            raise RuntimeError("unable to find version string.")
    return version


def read(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    with io.open(path, encoding='utf8') as fh:
        return fh.read()


setup(
    name="structmaker",
    install_requires=["numpy", "jinja2"],
    description="Tools for generating random C structures",
    long_description=read('README.rst'),
    version=read_version(),
    packages=find_packages(),
    author="Andrew Walker",
    author_email="walker.ab@gmail.com",
    url="http://github.com/AndrewWalker/structmaker",
    license="MIT",
    keywords=["c", "codegen"],
    entry_points = {
        'console_scripts': [
            'structmaker = structmaker.main:main'
        ]
    },
    classifiers=[
        "Topic :: Software Development :: Code Generators",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Operating System :: POSIX :: Linux",
    ],
)
