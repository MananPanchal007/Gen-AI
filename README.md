# Gen AI Project

A comprehensive collection of resources, code, and tutorials for learning and experimenting with Generative AI, Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), fine-tuning, and more. This repository is organized into multiple modules, each focusing on a specific aspect of AI and machine learning.

## Table of Contents

- [01_Basics of Python](#01_basics-of-python)
- [02_Basic AI chat](#02_basic-ai-chat)
- [03_Prompting Technics](#03_prompting-technics)
- [04_Local LLM](#04_local-llm)
- [05_AI Agent](#05_ai-agent)
- [06_Fine Tuning](#06_fine-tuning)
- [07_RAG](#07_rag)
- [08_Advance RAG](#08_advance-rag)
- [09_Memory](#09_memory)
- [10_Lang Graph](#10_lang-graph)
- [11_Speach to Text](#11_speach-to-text)
- [12_MyMCP](#12_mymcp)
- [study.txt](#study.txt)

## Folder Descriptions

### 01_Basics of Python
Fundamental Python programming concepts and exercises for beginners. Contains basic examples covering variables, data types, operators, loops, functions, and more.

### 02_Basic AI chat
Simple AI chatbot implementations and experiments. Includes examples of zero-shot prompting, embeddings, and tokenization.

### 03_Prompting Technics
Techniques and best practices for prompt engineering with LLMs. Contains examples of system prompts and automated prompting strategies.

### 04_Local LLM
Running and experimenting with large language models locally. Includes an API for interacting with Ollama and Docker setup.

### 05_AI Agent
Building and deploying AI agents for various tasks. Contains an example of an AI agent that can perform actions based on user queries.

### 06_Fine Tuning
Fine-tuning pre-trained models for custom tasks and datasets. Includes notes and examples for fine-tuning models using Hugging Face Transformers.

### 07_RAG
Introduction to Retrieval-Augmented Generation (RAG) techniques. Contains examples of document loading, text splitting, and vector store integration.

### 08_Advance RAG
Advanced RAG methods and applications. Includes examples of parallel querying and Reciprocal Rank Fusion (RRF).

### 09_Memory
Implementing memory and context retention in AI systems. Contains examples of using memory-aware agents and Docker setup for MongoDB and Neo4j.

### 10_Lang Graph
Exploring language graphs and their applications in AI. Contains examples of building and using LangGraph for complex AI workflows.

### 11_Speach to Text
Speech-to-text models and related experiments. Includes examples of speech recognition and integration with AI chat systems.

### 12_MyMCP
Implementation of a basic Model Context Protocol (MCP) server using FastMCP. Provides reusable tools for AI assistants including calculator, time operations, text processing, file operations, and list manipulations. Can be integrated with Claude Desktop and other MCP-compatible applications.

### study.txt
Notes and study material related to the project. Contains setup instructions and additional resources.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd "Gen AI"
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Unix or MacOS:
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements, bug fixes, or new modules.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details. 