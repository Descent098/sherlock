import setuptools

# Code originally from https://github.com/aegirhall/console-menu/blob/develop/setup.py

import io
def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)



long_description = read("README.md")



setuptools.setup(
    name="sherlock",
    version="0.1.3",
    author="Siddharth Dushantha",
    author_email="siddharth.dushantha@gmail.com",
    description="Find usernames across social networks http://sherlock-project.github.io",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Descent098/sherlock",
    packages=setuptools.find_packages(),
    entry_points={
          'console_scripts': ['sherlock = sherlock.sherlock:main']
      },
    install_requires=[
        "beautifulsoup4>=4.8.0",
        "bs4>=0.0.1",
        "certifi>=2019.6.16",
        "colorama>=0.4.1",
        "lxml>=4.4.0",
        "PySocks>=1.7.0",
        "requests>=2.22.0",
        "requests-futures>=1.0.0",
        "soupsieve>=1.9.2",
        "stem>=1.7.1",
        "torrequest>=0.1.0"
        
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)