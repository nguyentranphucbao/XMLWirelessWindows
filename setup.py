import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="XMLWirelessWindows", # Replace with your own username
    version="0.1.3",
    author="@KudoKuro",
    author_email="nguyentranphucbao@gmail.com",
    description="Create, Edit and Change Infomation of XML File",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nguyentranphucbao/XMLWirelessWindows",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
