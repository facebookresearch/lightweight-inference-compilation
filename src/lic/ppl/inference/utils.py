# Copyright (c) Facebook, Inc. and its affiliates.
# This is a minimal subset of the beanmachine PPL necessary to demo LIC
from dataclasses import dataclass
from enum import Enum
from typing import List

from ..model.rv_identifier import RVIdentifier
from torch import Tensor, tensor


class BlockType(Enum):
    """
    Enum for Block types: can be single node, or sequential block where nodes are
    sequentially re-sampled, or joint, where nodes are jointly re-sampled.
    """

    SINGLENODE = 1
    SEQUENTIAL = 2
    JOINT = 3


@dataclass(eq=True, frozen=True)
class Block:
    """
    Block class, which contains: the RVIdentifier of the first_node, type of the
    Block and list of random variables in the block in strings.
    """

    first_node: RVIdentifier
    type: BlockType
    block: List[str]


def safe_log_prob_sum(distrib, value: Tensor) -> Tensor:
    "Computes log_prob, converting out of support exceptions to -Infinity."
    try:
        return distrib.log_prob(value).sum()
    except (RuntimeError, ValueError) as e:
        return tensor(float("-Inf")).to(value.device)
