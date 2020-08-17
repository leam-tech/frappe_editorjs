# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in frappe_editorjs/__init__.py
from frappe_editorjs import __version__ as version

setup(
	name='frappe_editorjs',
	version=version,
	description='EditorJS backend',
	author='Leam Technology Systems',
	author_email='admin@leam.ae',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
