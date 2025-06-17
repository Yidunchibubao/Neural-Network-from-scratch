# Neural-Network-from-scratch
This project consists of a complete implementation of a deep neural network. If "high-level" deep learning libraries exist today (and will be used in class), a complete implementation of a simple network is a very good way to master the topic. 

- **Core Layers**:  
  - **LinearLayer**: affine transforms with learnable weights & biases  
  - **ActivationFunction**: ReLU, Sigmoid, Tanh, Softmax (with built-in cross-entropy gradient)

- **Embedding Support**:  
  - **EmbeddingLayer**: fine-tunable look-up embeddings via one-hot inputs

- **Utility Functions** (in `nnscratch.utils`):  
  - `build_vocab`  
  - `one_hot_vector`  
  - `sentence_to_onehot`  
  - `tags_to_onehot`  
  - `build_windowed_dataset`

- **Dual Backend**:  
  - **CPU**: uses NumPy (`numpy`)  
  - **GPU**: uses CuPy (`cupy`) when available (optional install)

---

## Installation

Requires Python ≥ 3.7.

### CPU-only

```bash
pip install nnscratch
or, #if installing from GitHub:

bash
Copy
Edit
pip install git+https://github.com/Yidunchibubao/Neural-Network-from-scratch.git
GPU-enabled
bash
Copy
Edit
pip install nnscratch[gpu]
or from GitHub with GPU extras:

bash
Copy
Edit
pip install "git+https://github.com/Yidunchibubao/Neural-Network-from-scratch.git#egg=nnscratch[gpu]"
Tip: If you run into CuPy driver errors, you can still use the CPU version by omitting [gpu], or uninstalling cupy in your environment.

