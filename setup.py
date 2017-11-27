"""EVE Glue."""


from setuptools import setup, find_packages
from setuphelpers import long_description, git_version, test_command


setup(
    name="eve-glue",
    version=git_version(),
    description="eve-glue",
    long_description=long_description(),
    cmdclass=test_command(),
    packages=find_packages(),
    author="Team Tech Co",
    author_email="teamtechco@ccpgames.com",
    url="https://github.com/ccpgames/eve-glue",
    setup_requires=["setuphelpers"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Flask",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: MIT License",
    ],
)
