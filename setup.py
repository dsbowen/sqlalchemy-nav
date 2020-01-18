import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sqlalchemy-nav",
    version="0.0.3",
    author="Dillon Bowen",
    author_email="dsbowen@wharton.upenn.edu",
    description="SQLAlchemy-Nav provides SQLAlchemy Mixins for creating navigation bars compatible with Bootstrap",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dsbowen/sqlalchemy-nav",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'flask==1.1.1',
        'sqlalchemy==1.3.12',
        'sqlalchemy-modelid==0.0.2',
        'sqlalchemy-mutablesoup==0.0.5',
        'sqlalchemy-orderingitem==0.0.3',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)