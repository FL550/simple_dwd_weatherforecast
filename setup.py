import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple_dwd_weatherforecast",
    version="2.1.5",
    author="Max Fermor",
    description="A simple tool to retrieve a weather forecast from DWD OpenData",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FL550/simple_dwd_weatherforecast.git",
    packages=setuptools.find_packages(),
    package_data={"": ["stations.json", "uv_stations.json"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["lxml", "requests", "Pillow", "arrow", "stream-unzip", "httpx"],
)
