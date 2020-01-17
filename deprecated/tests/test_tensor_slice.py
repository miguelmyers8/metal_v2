import unittest
from autograd.tensor import Tensor
import numpy as np

class TestTensorSlice(unittest.TestCase):
    def test_simple_Slice(self):
        t1 = Tensor([1, 2, 3], requires_grad=True, name="t1")
        t2 = Tensor([4, 5, 6], requires_grad=True, name="t2")
        t3= t1[:2]
        t4= t2[:2]

        t6 = t3/t4
        t7 = t6.sum()
        t7.backward()

        assert t3.data.tolist() == [1, 2]
        assert t4.data.tolist() == [4, 5]
        assert t2.grad.data.tolist() == np.float32([-0.0625, -0.08, 0.0]).tolist()
        assert t1.grad.data.tolist() == np.float32([0.25, 0.2, 0.0]).tolist()