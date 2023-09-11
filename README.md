# Word Game with GenAI - by JJ

## Prerequisites

This project requires Python to be installed and available on the system's PATH.

This version use Azure OpenAI and needs this environments variables:
* OPENAI_AZURE=True
* OPENAI_API_KEY_AZURE=your_api_key_here
* PORT=8000 # if you run the App using python app.py

## Setup Environment

1. Go to the proyect folder and create a virtual environment named `venv-wordgame`:
   ```bash
   python -m venv venv-wordgame
   ```

Note: Unless we want to install the venv in another folder, if we want to change its name we will need to modify the `.gitignore`.

2. Activate the virtual environment on the proyect folder:
   - On Windows:
     ```bash
     venv-wordgame\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv-wordgame/bin/activate
     ```

3. Install the required packages from the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

## Starting the App

1. Activate the virtual environment on the proyect folder:
   - On Windows:
     ```bash
     venv-wordgame\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv-wordgame/bin/activate
     ```

2. Launch Flask App:
   ```bash
   flask run --port 8000
   ```

3. Access to the APP fron your web browser using port 8000 
