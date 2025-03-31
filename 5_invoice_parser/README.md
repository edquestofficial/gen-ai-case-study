# Project Step-wise Setup and Usage

## Step 1: Download and Extract the Code
Download and extract the code, then open it in your code editor (e.g. Visual Studio Code).

## Step 2: Create a Virtual Environment and activate it
In the project folder, create and activate a virtual environment by running this command in the terminal:
```sh
python -m venv venv
venv\Scripts\activate
```

## Step 3: Configure Your Gemini API Key
Create a .env file and add your Gemini API key:
```sh
GEMINI_API_KEY='enter_your_api_key'
```

## Step 4: Install Necessary Modules and Libraries
Install the required modules and libraries:
```sh
pip install -r requirements.txt
```

## Step 5: Run pdfparser.py
Run pdfparser.py:
```sh
python pdfparser.py
```