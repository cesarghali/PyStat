from setuptools import setup, find_packages
from pystat import version

setup(
    name="pystat",
    version=version,
    description="Pystat is a simple module that provides statistical computations on running stream of values.",
    author="Cesar Ghali",
    author_email="cesarghali.p@gmail.com",
    license="GNU License",
    url="http://github.com/cesarghali/PyStat",
    packages=find_packages()
)
