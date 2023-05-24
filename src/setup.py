from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.6'
DESCRIPTION = 'Julia with Python'
LONG_DESCRIPTION = 'A package that allows to use Julia within Python.'

# Setting up
setup(
    name="Pyjulia",
    version=VERSION,
    author="Stefan Arsic",
    author_email="<stiefelwoods@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['python', 'julia', 'pyaudio'],
    keywords=['python', 'julia'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.05",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)