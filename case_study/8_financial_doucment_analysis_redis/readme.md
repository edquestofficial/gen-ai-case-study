# Invoice Data Extraction and RAG Bot

This project uses Retrieval-Augmented Generation (RAG) technology to extract data from Financial Documents. The data is stored in a Redis Vector Database, and the application is containerized using Docker.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)

## Introduction

This project aims to automate the extraction of unstructured data from Financial Documents. The extracted data is stored as embeddings in a Redis Vector Database, enabling efficient retrieval and interaction using RAG technology.

## Features

- Extracts data from Financial Documents
- Stores data embeddings in Redis Vector Database
- Uses RAG technology for intelligent data retrieval and interaction
- Containerized using Docker for easy deployment

## Technologies Used

- **Python**: For data extraction, processing, and embedding generation
- **Redis Vector Database**: For storing data embeddings
- **Docker**: For containerization of the application
- **HuggingFace Embedding Model**: For generating embeddings from the documents
- **Gemini-1.5-pro Model**: For retrieving the data efficiently
- **Gradio**: For User Interface

### Prerequisites

- Docker installed on your machine
- Python 3.10+ installed

### Steps
1. Prepare the data for analysis.
2. Setting up the Docker.
3. Create a Redis database to store embeddings.
4. Using parallel processing for rapid processing of data.
5. Generating Embeddings of the Documents using HuggingFace Embedding Model.
6. Combine everything together to make a complete application or bot.
7. Create a user-friendly interface using Gradio.
8. Pushing the code along with the proper documentation to Github repository.
