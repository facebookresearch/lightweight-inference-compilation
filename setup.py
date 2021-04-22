# Copyright (c) Facebook, Inc. and its affiliates.
# This is a minimal subset of the beanmachine PPL necessary to demo LIC

import sys

from setuptools import find_packages, setup


REQUIRED_MAJOR = 3
REQUIRED_MINOR = 6


TEST_REQUIRES = ["pytest", "pytest-cov"]
DEV_REQUIRES = TEST_REQUIRES + [
    "black==20.8b1",
    "isort",
    "flake8",
    "flake8-bugbear",
    "sphinx",
    "sphinx-autodoc-typehints",
]

# Check for python version
if sys.version_info < (REQUIRED_MAJOR, REQUIRED_MINOR):
    error = (
        "Your version of python ({major}.{minor}) is too old. You need "
        "python >= {required_major}.{required_minor}."
    ).format(
        major=sys.version_info.major,
        minor=sys.version_info.minor,
        required_minor=REQUIRED_MINOR,
        required_major=REQUIRED_MAJOR,
    )
    sys.exit(error)

setup(
    name="LIC",
    description="Lightweight Inference Compilation Research Prototype",
    author="Facebook, Inc.",
    license="MIT",
    python_requires=">={}.{}".format(REQUIRED_MAJOR, REQUIRED_MINOR),
    install_requires=[
        "torch>=1.7.0",
        "numpy>=1.18.1",
        "pandas>=0.24.2",
        "plotly>=2.2.1",
        "pplbench==0.0.2",
        "scipy>=0.16",
        "statsmodels>=0.12.0",
        "tqdm>=4.46.0",
        "astor>=0.7.1",
        "black>=19.3b0",
        "gpytorch>=1.3.0",
        "botorch>=0.3.3",
    ],
    packages=find_packages("src/"),
    package_dir={"": "src"},
    extras_require={
        "dev": DEV_REQUIRES,
        "test": TEST_REQUIRES,
    },
)
