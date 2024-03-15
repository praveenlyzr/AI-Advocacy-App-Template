# Instructions for the developers while working with this template

## Steps to Follow:

- Paste your API Key inside the `.streamlit/secrets.toml`.
- Add `.streamlit/secrets.toml` to the `.gitingnore` file while starting and before pushing your code to remote repository, this practice will keep your OpenAI API Key secret.
- `app.py` will be the entry point of your streamlit app, the main functionalities are written inside this script.
- `utils.py` script consist all of the common functions, so the helping functions will be written inside this script.
- Use the `lyzr-logo-cut.png` and `lyzr-logo.png` in your app.
- Always create and activate virtual environment before installing dependecies.
- Make sure that requirements.txt file updated before pushing the code to remote repo, for updating the file run `pip freeze > requirements.txt` command.

Remove these above Instructions before pushing your code to remote repository

# Welcome to the {name of you app}!

![Lyzr Logo](lyzr-logo.png)

Write a description of your app.

*Note: For this application to function properly in your local system, ensure that the required dependencies are installed and configured correctly, and make sure that you have your OpenAI API Key.*

### Create Virtual Environment 
- `python3 -m venv venv` - Ubuntu/MacOs
- `python -m venv venv` - Windows

### Activate the environment
- `source venv/bin/activate`  - Ubuntu/MaOS
- `venv/Script/acitvate` - Windows

### Installing Dependencies
- `pip3 install -r requirements.txt`- Ubuntu/MacOs
- `pip install -r requirements.txt` - Windows


### Run the application on local server
`streamlit run app.py`

# About Lyzr
Lyzr is a low-code agent framework that follows an **‘agentic’** way to build LLM apps, contrary to Langchain’s ‘functions and chains’ way and DSPy’s ‘programmatic’ way of building LLM apps. 

- [Lyzr](https://www.lyzr.ai/)
- [Book a Demo](https://www.lyzr.ai/book-demo/)
- [Discord](https://discord.gg/nm7zSyEFA2)