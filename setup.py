from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="metadata-tools",
    version="1.0.0",
    author="larpmadegoy",
    author_email="noahpluxsh@gmail.com",
    description="Advanced Metadata Analysis & Sanitization Tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/biolnk/metadata-tools",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Office/Business",
        "Topic :: Multimedia :: Sound/Audio",
    ],
    python_requires=">=3.8",
    install_requires=[
        "Pillow>=10.0.0",
        "exifread>=3.0.0",
        "piexif>=1.1.3",
        "PyPDF2>=3.0.0",
        "mutagen>=1.47.0",
        "python-docx>=0.8.11",
    ],
    entry_points={
        "console_scripts": [
            "metadata-tool=metadata_tool:main",
        ],
    },
)
