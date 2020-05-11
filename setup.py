import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-timestamps",
    version="0.0.1",
    author="Adrian Cataldo",
    author_email="adrian.cataldo093@gmail.com",
    description="timestamps for django models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adrian-cataldo/django-timestamps",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)