import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sqlalchemy-nav-dsbowen",
    version="0.0.1",
    author="Dillon Bowen",
    author_email="dsbowen@wharton.upenn.edu",
    description="Navigation bar SQLAlchemy Mixin for use with Bootstrap",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dsbowen/sqlalchemy-nav",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)