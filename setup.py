import setuptools

with open("README.txt", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='bioUtilities',
    version='0.1dev',
    author = 'Liam Abrahams',
    author_email = 'la466@bath.ac.uk',
    url = 'https://github.com/la466/utilities',
    description = 'Utilities package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    license='GNU GENERAL PUBLIC LICENSE Version 3',
)
