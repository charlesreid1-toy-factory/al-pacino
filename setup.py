from setuptools import setup, find_packages
from src import __version__

with open("requirements.txt") as f:
    all_deps = [x for x in f.read().splitlines() if not x.startswith("#")]
with open("requirements-dev.txt") as f:
    dev_deps = [x for x in f.read().splitlines() if not x.startswith("#")]

setup(
    name="al-pacino",
    version=__version__,
    description="a python package demonstrating how to implement and manage tests with unittest",
    author="Chaz Reid",
    author_email="charlesreid1@gmail.com",
    url="https://github.com/charlesreid1-toy-factory/al-pacino",
    packages=["al_pacino"],
    package_dir={"al_pacino": "src"},
    package_data={},
    entry_points={},
    license="MIT",
    install_requires=all_deps,
    extras_require={
        "test": dev_deps,
    }
)
