# Copyright (c) Facebook, Inc. and its affiliates.
# This is a minimal subset of the beanmachine PPL necessary to demo LIC
from torch.distributions import Distribution

from . import experimental
from .model import get_logger, random_variable


LOGGER = get_logger()
Distribution.set_default_validate_args(False)

__all__ = [
    "experimental",
    "random_variable",
]
