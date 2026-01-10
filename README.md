# AI Email Assistant

AI Email Assistant is a starter application from the **AI.Accelerate Bootcamp** designed to help users build intelligent email helper tools using Streamlit and Python. The app provides a foundation for creating actions that assist with common email tasks using AI, such as generating responses or summarizing content.

This repository was created as part of the **AI.Accelerate Bootcamp** and includes starter code and datasets to get you working quickly on your AI email assistant applications.

## Project Overview

The goal of this project is to provide a foundation for building email assistant features using Python and Streamlit. It includes a simple web app (`app.py`) and supporting scripts to generate and evaluate AI‑driven email helper actions.

## Features

- Starter Streamlit application for email assistant UI  
- Dataset folder to support multiple email actions  
- Helper scripts for generation and classification  
- Easy local setup and development  

## Tech Stack

- Python  
- Streamlit  
- YAML configuration  
- AI model integration (via prompts and helper scripts)  

## Repository Structure

```text
ai_email_assistant/
├── .devcontainer/           # Development container config
├── datasets/                # Example datasets for email actions
├── .gitignore
├── README.md
├── app.py                  # Starter Streamlit app
├── create_emails.yaml      # Email creation config
├── generate.py             # Script to generate email content
├── judge_prompts.yaml      # Prompt config for judging outputs
├── notes/                  # Notes and ideas
├── prompts.yaml            # Prompt definitions
└── requirements.txt
```
Getting Started
---------------

The following steps describe how to set up and run the project locally.

### Prerequisites

*   Python 3.9 or higher
    
*   Git
    

### Installation

Clone the repository:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   git clone https://github.com/Daniel-ct27/ai_email_assistant.git   `

Navigate into the project directory:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   cd ai_email_assistant   `

Create and activate a virtual environment (recommended):

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python -m venv .venv  source .venv/bin/activate   # On Windows: .venv\Scripts\activate   `

Install dependencies:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install -r requirements.txt   `

### Running the Application

Start the Streamlit app:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   streamlit run app.py   `

Open your browser and visit:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   http://localhost:8501   `

Contributors
------------

*   Daniel Chukwudera
