from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erpnext_custom_field/__init__.py
from erpnext_custom_field import __version__ as version

setup(
	name="erpnext_custom_field",
	version=version,
	description="custom fields",
	author="nextash",
	author_email="support@nextash.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
