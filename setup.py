#!/usr/bin/env python

from setuptools import setup


description = "Unofficial packaged vivisect vstruct mirror."
setup(name="vivisect-vstruct-wb",
      version="1.0.3",
      description=description,
      long_description=description,
      url="https://github.com/williballenthin/vivisect-vstruct",
      author="invisig0th, mirrored by Willi Ballenthin",
      author_email="willi.ballenthin@gmail.com",
      packages=["vstruct"],
      classifiers=[
          "Intended Audience :: Developers",
          'Programming Language :: Python :: 2.7',
      ])
