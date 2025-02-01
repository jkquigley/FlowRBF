#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="FlowRBF",
    version="0.1.0",
    author="J. Keane Quigley",
    author_email="keaneq@protonmail.com",
    description="Radial Basis Function CFD Solver.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jkquigley/FlowRBF",
    packages=[
        "FlowRbf",
        "FlowRbf.functions",
        "FlowRbf.regions",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
