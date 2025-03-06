from setuptools import find_packages, setup

setup(
    name="traxion-domain",
    version="1.0.0",
    author="Luis Gerardo Fosado Baños",
    author_email="yeralway1@gmail.com",
    description="traxion Domain Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="traxion, domain, library, python",
    license="MIT",
    packages=find_packages(),
    package_data={"": ["*.json"]},
    namespace_packages=["traxion"],
    python_requires=">=3.11",
    install_requires=[
        "pydantic==2.5.3",
    ],
    classifiers=["Programming Language :: Python :: 3"],
    extras_require={
        "dev": [
            "pytest==7.2.0",
            "pytest-mock==3.10.0",
        ]
    },
    zip_safe=True,
    test_suite="tests",
    url="https://github.com/GerardoX1/traxion-domain.git",
)
