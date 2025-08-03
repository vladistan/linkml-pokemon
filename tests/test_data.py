"""Data test."""

import os
import glob

from linkml_runtime.loaders import yaml_loader
from linkml_pokemon.datamodel.linkml_pokemon import PokemonCollection
from pathlib import Path

ROOT = os.path.join(os.path.dirname(__file__), "..")
DATA_DIR = os.path.join(ROOT, "src", "data", "examples")

EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR, "*.yaml"))


ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "src" / "data" / "examples"

EXAMPLE_FILES = list(DATA_DIR.glob("*.yaml"))


def test_data():
    """Data test."""
    for path in EXAMPLE_FILES:
        obj = yaml_loader.load(str(path), target_class=PokemonCollection)
        assert obj
