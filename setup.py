from setuptools import setup, find_packages

setup(
    name="my_ch200_project",
    version="0.1.0",
    author="Arthur Bongini, Emna Belgharbia, Oriane Azalbert",
    author_email="arthur.bongini@epfl.ch",
    description="A tool to apply some reaction see in FRO I class at EPFL to molecules. This project was carried out as part of the Practical Programming in chemistry CH200 course.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/abongini/FROI_PPC_Project/",
    packages=find_packages(),
    install_requires=[
        "rdkit",
        "pandas",
        "pathlib",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)