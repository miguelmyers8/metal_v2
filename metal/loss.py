from metal.module import Module
from metal.tensor import Tensor, Dependency
from metal.linear import Linear
import numpy as np


def CEL(predicted: Tensor, actual: Tensor, module: Module = None) -> Tensor:

    m = actual.shape[1]

    data = (1.0 / m) * (
        -np.dot(actual.data, np.log(predicted.data).T)
        - np.dot(1 - actual.data, np.log(1 - predicted.data).T)
    )
    requires_grad = predicted.requires_grad

    if requires_grad:

        def grad_fn(grad: np.ndarray) -> np.ndarray:
            return grad * (
                -(
                    np.divide(actual.data, predicted.data)
                    - np.divide(1 - actual.data, 1 - predicted.data)
                )
            )

        depends_on = [Dependency(predicted, grad_fn)]
    else:

        depends_on = []

    return Tensor(data, requires_grad, depends_on)