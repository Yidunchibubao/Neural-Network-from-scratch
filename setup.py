# setup.py
from setuptools import setup, find_packages

setup(
    name="nnscratch",
    version="0.1.0",
    description="Neural nets from scratch toolkit for NLP tasks",
    author="Yidunchibubao",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "numpy>=1.20", 
    ],
    extras_require={
        "gpu": ["cupy"], 
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
