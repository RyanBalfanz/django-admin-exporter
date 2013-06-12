# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages


README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
	name='django-admin-exporter',
	version='0.2.1',
	url='https://github.com/RyanBalfanz/django-admin-exporter',
	author='Ryan Balfanz',
	author_email='ryan@ryanbalfanz.net',
	description='Simple admin actions to download/export selected items in CSV, JSON, XML, etc.',
	long_description=README,
	packages = find_packages(exclude=("example_project",)),
	zip_safe=False,
	include_package_data=True,
	platforms='any',
	install_requires=['unicodecsv'],
	classifiers=[
		'Environment :: Web Environment',
		'Intended Audience :: Developers',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
		'Topic :: Software Development :: Libraries :: Python Modules'
	]
)
