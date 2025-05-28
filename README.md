# 📝 Blog Generator (Agent-Based)

This Python application generates well-structured blogs based on a given topic using Wikipedia and DuckDuckGo for research and GPT-2 for text generation.

---

## 🚀 Features

- Uses **Wikipedia** and **DuckDuckGo** as research tools.
- Generates blogs with sections:
  - Heading
  - Introduction
  - Content
  - Summary
- Utilizes HuggingFace Transformers (`GPT-2`)

---

## 🛠 Installation

1. Create and activate a virtual environment:
   python -m venv venv
   venv\Scripts\activate     # On Windows
   source venv/bin/activate  # On Linux/Mac

2. Install dependencies:
   pip install torch transformers duckduckgo-search

-------------
🚀 Usage:
1. Run the script:
   python main.py

2. When prompted, enter a blog topic (e.g., "Benefits of Remote Work").

