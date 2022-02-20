from setuptools import find_packages, setup


def long_description():
    with open("README.md", "r") as readme:
        return readme.read()


setup(
    name="diogi",
    packages=find_packages(include=["diogi"]),
    version="0.1.0",
    author="Michal Poreba",
    license="MIT",
    description="A library of tiny little functions to make development that little bit easier.",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/michalporeba/diogi",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
    ],
    install_requires=[],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    test_suite="tests",
)
