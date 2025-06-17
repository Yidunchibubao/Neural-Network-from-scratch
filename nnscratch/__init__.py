# nnscratch/__init__.py

import numpy as np

def _get_array_module():
    try:
        import cupy as cp_mod
        if cp_mod.cuda.runtime.getDeviceCount() > 0:
            return cp_mod
    except Exception:
        pass
    return np

cp = _get_array_module()

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
