from typing import List
import numpy as np
from autograd.node import Node
from autograd.dependency import Dependency

class Tensor(Node):
    """docstring for Tensor."""
    def __init__(self, data: np.ndarray, requires_grad: bool = False, depends_on: List[Dependency] = None, name: str = " "):
        super().__init__(data=data,requires_grad=requires_grad, depends_on=depends_on)
        self.name = name
