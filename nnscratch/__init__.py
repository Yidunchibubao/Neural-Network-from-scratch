# -*- coding: utf-8 -*-
"""nnscratch/__init__.py"""

import numpy as np

def _get_array_module():
    try:
        import cupy
        try:
            # 只有在驱动、runtime 全部 OK 时才返回 cupy
            if cupy.cuda.is_available():
                return cupy
        except Exception:
            pass
    except Exception:
        pass
    return np

cp = _get_array_module()

from .layers      import LinearLayer, ActivationFunction
from .embeddings  import EmbeddingLayer
from .network     import NeuralNetwork
from .utils       import (
    load_conllu,
    build_vocab,
    one_hot_vector,
    sentence_to_onehot,
    tags_to_onehot,
    build_windowed_dataset,
)

__all__ = [
    "cp", "np",
    "LinearLayer", "ActivationFunction", "EmbeddingLayer", "NeuralNetwork",
    "load_conllu", "build_vocab",
    "one_hot_vector", "sentence_to_onehot", "tags_to_onehot", "build_windowed_dataset",
]
