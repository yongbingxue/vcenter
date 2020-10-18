import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vcenter", # Replace with your own username
    version="1.0.0",
    author="yongbingxue",
    author_email="yongbingxue@163.com",
    description="Vcenter Rest API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yongbingxue/vcenter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)