# Email Threat Detection  

This project implements a Python-based pipeline for detecting fraudulent emails, extracting relevant information using parsing techniques, and automating the forwarding of these emails to appropriate departments for immediate action.

## Overview

The pipeline consists of two primary components: **Triage** and **Email & Number Extraction**. These components work in tandem to streamline the process of identifying and responding to email fraud. This version focuses on parsing for data extraction, rather than machine learning for triage.

## Components

### 1. Triage 

* **Purpose:** The Triage component is responsible for analyzing incoming emails and classifying them as potentially fraudulent or legitimate, using parsing.
 
* **Functionality:**
    * Applies a set of predefined rules and patterns to analyze email headers and body content.
    * Identifies suspicious keywords, phrases, and structural anomalies (e.g., mismatched sender domains, unusual subject lines, urgent requests).
    * Uses regular expressions and string manipulation to detect patterns.
    * Filters emails based on these rules, marking those that match suspicious patterns as potentially fraudulent.
          

### 2. Email & Number Extraction

* **Purpose:** This component extracts critical information from emails flagged as potentially fraudulent by the Triage component.
  
* **Functionality:**
    * Parses email content to identify and extract email addresses, phone numbers, URLs, and other relevant details.
    * Validates extracted information using regular expressions and other validation techniques.
    * Formats extracted data into a structured format (e.g., JSON).
    * Automatically routes the extracted information and the original email to the designated departments (e.g., security, legal).
      
   
## Workflow

1.  **Email Reception:** The pipeline receives incoming emails.
2.  **Triage Analysis (Parsing):** The Triage component analyzes the email using rule-based parsing.
3.  **Fraud Classification:** Emails matching suspicious patterns are marked as potentially fraudulent.
4.  **Information Extraction:** The Email & Number Extraction component extracts key details from the flagged emails.
5.  **Data Structuring:** Extracted data is formatted into a structured format.
6.  **Automated Routing:** The extracted information and the original email are sent to the relevant departments.
7.  **Action & Investigation:** The designated departments take appropriate action based on the provided information.




## Usage

(Include instructions for setting up the environment, installing dependencies, and running the pipeline. Include configuration details for email servers, department routing, and the rules used for the Triage component.)

