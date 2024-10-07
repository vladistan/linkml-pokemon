#!/bin/bash


STARTUP_DIR=$(pwd)


python -m pip install -U pip


# Clone linkml
if [ ! -d "../linkml" ]; then
  git clone https://github.com/vladistan/linkml.git ../linkml
fi


pipx install pre-commit
pipx install poetry

poetry config virtualenvs.in-project true


echo "PWD: $PWD"

if [[ "$PWD" == *"/workspaces/"* ]]; then
  echo "Running in VSCode Dev Container"
elif [[ "$PWD" == *"/IdeaProjects/"* ]]; then
  echo "Running in JetBrains IDE"
fi

# Configure LinkML
pre-commit install || true
poetry install --with-extras
pre-commit run -a || true
# Configure Pokemon
cd "${STARTUP_DIR}"
poetry install --with-extras
pip install -e ../linkml

