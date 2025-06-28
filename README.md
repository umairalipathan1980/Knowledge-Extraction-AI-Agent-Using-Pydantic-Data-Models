# 🤖 AI-Powered Document Extraction System

> **Transform unstructured documents into structured business intelligence using LlamaExtract**


## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## 🎯 Overview

This code teaches how to automate the extraction of structured information from unstructured reports using **LlamaExtract**. As a sample data and use-case, this code uses example data of AI consultancy reports. The code can be easily modified for other documents. 


## ✨ Features

- **🧠 AI-Powered Extraction**: Uses LlamaExtract for intelligent document processing
- **📊 Structured Output**: Converts unstructured reports to structured Excel data
- **🎯 Schema-Based**: Pydantic models ensure data consistency and validation
- **📈 Analytics Ready**: Generates structured documents ready for analysis
- **🔄 Batch Processing**: Handles multiple documents simultaneously
- **🛡️ Error Handling**: Robust fallback mechanisms for data quality
- **🌍 Multi-Field Support**: Extracts different data fields per document

## 🏗️ System Architecture

![System Architecture](images/system-architecture.png)


## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- LlamaCloud API key

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/ai-document-extraction.git
cd ai-document-extraction
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

### 1. LlamaCloud API Setup

1. Sign up at [LlamaCloud](https://cloud.llamaindex.ai/)
2. Generate your API key
3. Create a `.streamlit/secrets.toml` file:

```toml
[secrets]
LLAMA_CLOUD_API_KEY_EU = "your-api-key-here"
```

### 2. Directory Structure

Create the following directories in your project root:
```
project/
├── input/          # Place your .docx files here
├── output/         # Processed results will be saved here
├── models.py       # Data models and schemas
└── main.py         # Main processing script
```

## 🎮 Usage

### Command Line Processing

```bash
# Run the main extraction process
python main.py
```

### Processing Pipeline

1. **Document Input**: Place `.docx` files in the `input/` directory
2. **Automated Processing**: Run the extraction script
3. **Structured Output**: Find results in `output/company_analysis_llama_extract.xlsx`

### Example Output for the sample data (AI consultancy reports)

The system generates comprehensive Excel reports with columns including:
- Company Name, Country, Consultation Date
- Domain, AI Field, Company Type
- AI Maturity Level, Technical Expertise
- Target Market, Data Requirements
- FAIR Services Sought, Recommendations

## 📁 Project Structure

```
ai-document-extraction/
├── 📄 main.py                 # Main processing script
├── 📄 models.py               # Pydantic data models
├── 📄 requirements.txt        # Python dependencies
├── 📄 README.md              # Project documentation
├── 📁 input/                 # Input documents directory
├── 📁 output/                # Output results directory
├── 📁 .streamlit/            # Streamlit configuration
│   └── secrets.toml          # API keys and secrets
└── 📁 docs/                  # Additional documentation
```

## 🔧 Advanced Configuration

### Custom Schema Modification

To add new fields or modify existing ones:

1. Update the Pydantic models in `models.py`
2. Add corresponding enum values if needed
3. Update the data cleaning functions in `main.py`
4. Test with sample documents


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📬 Contact

**Author**: Umair Ali Khan
**Email**: umairali.khan@haaga-helia.fi 
**Project Link**: [https://github.com/your-username/ai-document-extraction](https://github.com/your-username/ai-document-extraction)

---

⭐ **Star this repository if you find it helpful!**