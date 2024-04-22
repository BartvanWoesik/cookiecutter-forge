import subprocess

# Define the name of the new conda environment
env_name = "{{ cookiecutter.project_slug }}"


poetry_install = "pip install poetry"

subprocess.run(poetry_install, shell=True)

poetry_install = "poetry install"
subprocess.run(poetry_install, shell=True)

