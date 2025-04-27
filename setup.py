from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="spaita",
    version="0.0.1",
    description="Description",
    long_description=readme(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    keywords="spaita",
    url="https://github.com/Bailey3D/spaita",
    author="Bailey3D",
    author_email="bailey@bailey3d.com",
    license="MIT",
    packages=["spaita"],
    install_requires=[
        "numpy",
        "scipy"
    ],
    include_package_data=True,
    zip_safe=False
)