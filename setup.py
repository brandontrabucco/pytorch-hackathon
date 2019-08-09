from setuptools import find_packages
from setuptools import setup


REQUIRED_PACKAGES = [
    'pillow',
    'opencv-python',
    'pyyaml',
    'numpy',
    'torch==1.2.0',
    'torchvision',
    'torchtext',
    'fairseq',
    'sacremoses',
    'subword-nmt',
    'regex',
    'glow',
]


setup(
    name='hack',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    include_package_data=True,
    packages=[
        p for p in find_packages() if p.startswith('hack')
    ],
    description='Hackathon project'
)