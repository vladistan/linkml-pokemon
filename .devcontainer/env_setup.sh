#!/bin/bash


STARTUP_DIR=$(pwd)

set -e # Exit on error



# Clone linkml
if [ ! -d "../linkml" ]; then
  git clone https://github.com/vladistan/linkml.git ../linkml
fi

echo "PWD: $PWD"

if [[ "$PWD" == *"/workspaces/"* ]]; then
  echo "Running in VSCode Dev Container"
elif [[ "$PWD" == *"/IdeaProjects/"* ]]; then
  echo "Running in JetBrains IDE"
fi

# Configure LinkML
cd ../linkml
pre-commit install || true
poetry install --all-extras
pre-commit run -a || true
# Configure Pokemon
cd "${STARTUP_DIR}"
poetry install --all-extras
pip install -e ../linkml
