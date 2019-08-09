#!/bin/sh

mkdir model_data
wget -O model_data/vocabulary_captioning_thresh5.txt https://dl.fbaipublicfiles.com/pythia/data/vocabulary_captioning_thresh5.txt
wget -O model_data/detectron_model.pth  https://dl.fbaipublicfiles.com/pythia/detectron_model/detectron_model.pth 
wget -O model_data/butd.pth https://dl.fbaipublicfiles.com/pythia/pretrained_models/coco_captions/butd.pth
wget -O model_data/butd.yaml https://dl.fbaipublicfiles.com/pythia/pretrained_models/coco_captions/butd.yml
wget -O model_data/detectron_model.yaml https://dl.fbaipublicfiles.com/pythia/detectron_model/detectron_model.yaml
wget -O model_data/detectron_weights.tar.gz https://dl.fbaipublicfiles.com/pythia/data/detectron_weights.tar.gz
tar xf model_data/detectron_weights.tar.gz

# Install dependencies
pip install ninja yacs cython matplotlib demjson
pip install git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI

git clone https://github.com/facebookresearch/fastText.git fastText
pip install -e fastText

git clone https://github.com/facebookresearch/pythia.git pythia
sed -i '/torch/d' requirements.txt
pip install -e pythia

git clone https://gitlab.com/meetshah1995/vqa-maskrcnn-benchmark.git
cd vqa-maskrcnn-benchmark
python setup.py build
python setup.py develop
cd ../

git clone https://github.com/NVIDIA/tacotron2.git
cd tacotron2
git submodule init; git submodule update
cd ../

wget https://www.dropbox.com/s/fsstcp9ygpr5t6w/tacotron2_statedict.pt
wget https://www.dropbox.com/s/jetxhcvwk5wf77u/waveglow_256channels.p
wget -O image.jpg http://farm1.staticflickr.com/36/119543586_0bec48d409_z.jpg
