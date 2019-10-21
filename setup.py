from setuptools import setup, find_packages
from Cython.Build import cythonize

ext = cythonize(['passpredictor/_sgp4.pyx'])

setup(
    name="passpredictor",
    version="0.0.1",
    packages=find_packages(),

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=[
        'docutils>=0.3',
        'numpy'
    ],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
    },

    # metadata to display on PyPI
    author="Sam Friedman",
    author_email="samtx@outlook.com",
    description="Predict upcoming satellite overpasses",
    keywords="iss predict orbit sgp4",
    url="https://www.github.com/samtx/pass-predictor",   # project home page, if any
    classifiers=[
        'License :: OSI Approved :: Python Software Foundation License'
    ],
    # could also include long_description, download_url, etc.
    zip_safe = False,
    extensions = ext,
)