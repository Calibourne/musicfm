from setuptools import setup, find_packages

setup(
    name='musicfm',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'torch',
        'torchaudio',
        'numpy',
        'librosa',
        'transformers',
        'einops',
    ]
)