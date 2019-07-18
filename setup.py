import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='kms',
     version='1.0.0.2',
     author="Ar$h1a",
     author_email="1arhacker1@gmail.com",
     description="A Hacking Library That Helps You To Create Hacking Tools.",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/ArshiaPRG/kms",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
