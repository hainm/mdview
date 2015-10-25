#!/usr/bin/env python

from __future__ import print_function, absolute_import
from distutils.core import setup

CLASSIFIERS = """
Development Status :: 1 - Planning
Intended Audience :: Science/Research
Intended Audience :: Developers
License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)
Programming Language :: JavaScript
Programming Language :: Python
Topic :: Scientific/Engineering :: Bio-Informatics
Topic :: Scientific/Engineering :: Chemistry
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: Unix
Operating System :: MacOS
"""

__version__ = '0.1.dev'

packages = ['mdview', 'mdview.html']

setup(name='mdview',
      author='mdview developers',
      description='not yet',
      version=__version__,
      license='LGPLv2.1+',
      url='https://github.com/hainm/mdview',
      download_url = "https://github.com/hainm/mdview",
      platforms=['Linux', 'Mac OS-X', 'Unix', 'Windows'],
      package_data={'mdview.html': ['static/*']},
      packages=packages,
)
