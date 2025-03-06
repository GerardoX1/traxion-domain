from setuptools import setup, find_packages

setup(
    name="traxion-domain",
    version="1.0.0",
    author="Luis Gerardo Fosado Baños",
    author_email="yeralway1@gmail.com",
    description="traxion Domain Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(include=["traxion*"]),
    package_data={"traxion_domain": ["*.json"]},
    python_requires=">=3.11",
    install_requires=[
        "pydantic==2.10.6",
    ],
    extras_require={
        "dev": [
            "pytest==7.2.0",
            "pytest-mock==3.10.0",
        ]
    },
    url="https://github.com/GerardoX1/traxion-domain.git",
)
