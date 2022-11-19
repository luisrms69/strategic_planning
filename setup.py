from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in strategic_planning/__init__.py
from strategic_planning import __version__ as version

setup(
	name="strategic_planning",
	version=version,
	description="Modulo de planeacion estrategica basada en OKRs y KPIs bajo plataforma ERPNEXT",
	author="buzola",
	author_email="it@buzola.mx",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
