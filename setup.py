#!/usr/bin/env python
"""
cloudyqueue 
======


Right now cloud file access in Python is about where database access
was in the mid 90's.  Each database wrapper author has their very own
nomenclature, sets of commands for doing things that are basically the
same - creating cursors, executing commands and reading rows.


cloudyqueue seeks to do for cloud file providers what the Python
Database API does for database access.  Cloud file style servces like
Rackspace's cloud files and Amazon's S3 really are nothing more than
dictionaries that map fixed strings to

"""

from setuptools import setup

setup(
    name='cloudyqueue',
    version='0.0.0',
    author='Adam DePrince',
    author_email='adeprince@nypublicradio.org',
    description='Dictionary interface to cloud providers.',
    long_description=__doc__,
    py_modules=[
        "cloudyqueue/__init__",
        # "cloudyqueue/s3",
        "cloudyqueue/queue",
    ],
    # packages=["cloudyqueue "],
    zip_safe=True,
    license='GPL',
    include_package_data=True,
    classifiers=[
    ],
    scripts=[
    ],
    url="https://github.com/wnyc/cloudyqueue ",
    install_requires=[
        "boto",
    ]
)
