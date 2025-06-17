# nnscratch/__init__.py
import numpy as np

try:
    import cupy as _cp
    _cp.zeros((1,))
    _cp.cuda.runtime.getDeviceCount() 
    cp = _cp
except Exception:
    cp = np

from .layers import LinearLayer, ActivationFunction
from .embeddings import EmbeddingLayer
from .network import NeuralNetwork
from .utils import (
    load_conllu, build_vocab,
    one_hot_vector, sentence_to_onehot,
    tags_to_onehot, build_windowed_dataset,
)

__all__ = [
    "cp", "np",
    "LinearLayer", "ActivationFunction", "EmbeddingLayer", "NeuralNetwork",
    "load_conllu", "build_vocab",
    "one_hot_vector", "sentence_to_onehot", "tags_to_onehot", "build_windowed_dataset"
]
