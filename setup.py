from setuptools import setup, find_packages

setup(
    name='hvo_sequence',
    version='0.1.1',
    author='Behzad Haki, Marina Nieto, Teresa Pelinski',
    description="A Piano Roll Representation for Drums Similar to Sequence Representations in Magenta's GrooVAE",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dafg05/hvo_sequence',
    packages=find_packages(),
    install_requires=[
        'note_seq',
        'pretty_midi',
        'bokeh',
        'soundfile',
        'librosa',
        'matplotlib',
        'scipy',
        'numpy'
    ],
    classifiers=[
        # Choose classifiers as appropriate for your project
        'Intended Audience :: Developers',
    ],
    python_requires='>=3.6',  # Specify compatible Python versions
)
