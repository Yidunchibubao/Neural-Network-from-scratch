# setup.py
from setuptools import setup, find_packages
import io
import os

here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="nnscratch",                                 
    version="0.1.0",                                  
    author="Lyu CHEN, Shuyue GU, Varvara SMIRNOVA",  
    description="Neural network from scratch toolkit for NLP tasks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Yidunchibubao/Neural-Network-from-scratch",
    packages=find_packages(),                        
    include_package_data=True,                     
    python_requires=">=3.7",
    install_requires=[
        "numpy>=1.18",
    ],
    extras_require={
        "gpu": [
            "cupy-cuda11x>=11.0.0",  
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License", 
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
