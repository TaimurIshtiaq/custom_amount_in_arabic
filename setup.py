from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in custom_amount_in_arabic/__init__.py
from custom_amount_in_arabic import __version__ as version

setup(
	name="custom_amount_in_arabic",
	version=version,
	description="Shows amount in arabic",
	author="Taimur Ishtiaq",
	author_email="engrrtaimurishtiaq@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
