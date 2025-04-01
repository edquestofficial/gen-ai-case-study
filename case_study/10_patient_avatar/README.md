# Patient Avatar

This project is an AI-driven platform designed to enhance medical students' clinical interaction and diagnostic skills using voice interaction. Leveraging the advanced capabilities of ChatGPT 4.0 and sophisticated prompt engineering, this simulator creates realistic patient scenarios.


**Key Features:**

* **Simulated Patient Interactions:** Medical students engage with an AI simulator that presents diverse patient symptoms and medical histories.
* **Skill Development:** Students practice patient interviewing, symptom analysis, and treatment prescription in a safe, controlled environment.
* **ChatGPT 4.0 Integration:** Utilizes the advanced language model for realistic and dynamic patient responses.
* **Conversation Storage:** All interactions are securely stored in the backend for review and analysis.
* **Performance Evaluation:** A comprehensive evaluation report is generated at the end of each simulation, providing feedback on the student's performance and identifying areas for improvement.
* **Prompt Engineering Implementation:** The system's effectiveness relies on carefully crafted prompts to ensure accurate and relevant patient simulations.
  

## Installation

Steps
1. **Clone the Repository:**

git clone <repository-url>
cd <repository-name>

2. **Setup Backend:**
 
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
pip install -r requirements.txt


3.  **Set up API keys :**

    * The Patient Avatar requires API keys for Open AI ChatGPT-4.0 services. 
      

## Usage

1.  **Run the application:**

    * Execute the main script of the Patient Avatar. For example, if the main script is `main.py`:

        ```bash
        python main.py
        ```

2.  **Interact with the Patient:**

Patient (AI Simulator): "Doc, I feel terrible. My throat's on fire, I can't stop sneezing, and my head's pounding."

Medical Student: "Alright, let's get some details. When did this start?"

Patient (AI Simulator): "About three days ago. It started with a tickle in my throat, then the sneezing began. Now, I have a runny nose, a cough, and I'm just exhausted."

Medical Student: "Any fever or chills?"

Patient (AI Simulator): "Yeah, I've felt warm, especially at night, and I had chills last evening."

Medical Student: "Okay. And any muscle aches or congestion?"

Patient (AI Simulator): "A little achy, especially my back, and my nose is completely stuffed up."

Medical Student: "Sounds like a common cold. Rest is crucial, drink plenty of fluids, and use over-the-counter pain relievers for the headache and aches. Gargle with warm salt water for the sore throat and use saline nasal spray for the congestion. For the cough, a cough suppressant can help. If your fever rises, or you have trouble breathing, please return immediately."

Patient (AI Simulator): "Okay, thank you, Doctor."


   





