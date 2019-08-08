from setuptools import find_packages
from setuptools import setup


REQUIRED_PACKAGES = [
    'numpy',
    'torch',
    'torchvision',
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