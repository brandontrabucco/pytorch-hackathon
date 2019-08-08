### How-to use this API
1. install dependencies (see below)
2. run `translator.py`

### translator.py API

```
import torch

# List available models
torch.hub.list('pytorch/fairseq')  # [..., 'transformer.wmt16.en-de', ... ]

# Load a transformer trained on WMT'16 En-De
en2de = torch.hub.load('pytorch/fairseq', 'transformer.wmt16.en-de', tokenizer='moses', bpe='subword_nmt')

# The underlying model is available under the *models* attribute
assert isinstance(en2de.models[0], fairseq.models.transformer.TransformerModel)

# Translate a sentence
en2de.translate('Hello world!')
# 'Hallo Welt!'
```

### Library
- [fairseq](https://github.com/pytorch/fairseq)
- [fairseq translation](https://github.com/pytorch/fairseq/blob/master/examples/translation/README.md)

### Dependencies
- !pip install -q torch==1.2.0 torchvision
- !pip install fairseq
- !pip install sacremoses
- !pip install subword-nmt
- !pip install regex