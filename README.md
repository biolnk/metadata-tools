# 🔍 Metadata Tools - Advanced Metadata Analysis & Sanitization

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)

A powerful Python tool for scanning, analyzing, and removing metadata from various file types. Protect your privacy by stripping sensitive information from your files before sharing them online.

![Metadata Tool Demo](demo.gif)

## ✨ Features

- **📸 Image Metadata** - Extract EXIF data (GPS, camera settings, dates)
- **📄 Document Analysis** - Scan PDFs and Word documents for hidden properties
- **🎵 Audio Tag Reader** - View ID3 tags, bitrate, duration, and more
- **🧹 Metadata Removal** - Strip all metadata from supported files
- **📊 JSON Export** - Generate detailed reports for forensic analysis
- **🎨 Beautiful CLI** - User-friendly menu system with ASCII art

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/larpmadegoy/metadata-tool.git
cd metadata-tool

# Install dependencies
pip install -r requirements.txt

# Run the tool
python metadata_tool.py
