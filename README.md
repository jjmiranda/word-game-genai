# Smart Research / Code Reverse Documentation

## Prerequisites

This project requires Python to be installed and available on the system's PATH.

## Setup Environment

1. Go to the proyect folder and create a virtual environment named `gpt`:
   ```bash
   python -m venv gpt
   ```

Note: Unless we want to install the venv in another folder, if we want to change its name we will need to modify the `.gitignore`.

2. Activate the virtual environment on the proyect folder:
   - On Windows:
     ```bash
     gpt\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source gpt/bin/activate
     ```

3. Install the required packages from the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

## Starting the App

1. Activate the virtual environment on the proyect folder:
   - On Windows:
     ```bash
     gpt\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source gpt/bin/activate
     ```

2. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

3. In the Jupyter Notebook interface, select the notebook named "v4 Fixed Outline Research and Code Documentation.ipynb" to begin your work.

4. Executes the cells, the final result should be located on REPOSITORY/build.
