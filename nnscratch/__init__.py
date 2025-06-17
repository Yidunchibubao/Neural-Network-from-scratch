# nnscratch/__init__.py

import numpy as np

try:
    import cupy
    if cupy.cuda.is_available():
        cp = cupy
    else:
        cp = np
except ImportError:
    cp = np

from .layers      import LinearLayer, ActivationFunction
from .embeddings  import EmbeddingLayer
from .network     import NeuralNetwork
from .utils       import (
    build_vocab,
    one_hot_vector,
    sentence_to_onehot,
    tags_to_onehot,
    build_windowed_dataset,
)


__all__ = [
    "cp", "np",
    "LinearLayer", "ActivationFunction", "EmbeddingLayer", "NeuralNetwork", "build_vocab",
    "one_hot_vector", "sentence_to_onehot", "tags_to_onehot", "build_windowed_dataset",
]
