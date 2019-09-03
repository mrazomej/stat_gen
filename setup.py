import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="statgen",
    version="0.0.1",
    author="Manuel Razo",
    author_email="mrazomej {at} caltech {dot} edu",
    description="This library is the set of standard functions used to generate the statistical genetics notes. It includes plotting style and other useful functions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mrazomej/pop_gen.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
