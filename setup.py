#!/usr/bin/env python3
from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('LICENSE') as license_file:
    license = license_file.read()

setup(name='domainbigdata',
      version='1.0.1',
      description='Python wrapper for DomainBigData.com (no API available)',
      long_description=readme,
      long_description_content_type='text/markdown',
      url='https://github.com/wesinator/domainbigdata-python',
      author='wesinator',
      keywords='domainbigdata',
      packages=['domainbigdata'],
      entry_points={
        'console_scripts': [
            'domainbigdata=domainbigdata.cli:main',
        ],
      },
      classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
      ],
      zip_safe=True)
