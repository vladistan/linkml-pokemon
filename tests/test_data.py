from pathlib import Path

import pytest
from linkml_runtime.loaders import yaml_loader
from linkml_pokemon.datamodel.linkml_pokemon import (
    Ability,
    Color,
    EggGroup,
    Habitat,
    Move,
    Shape,
    Species,
    Type,
)


ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "src" / "data" / "examples"

# Map example files to their target classes
EXAMPLES = [
    (DATA_DIR / "Species-Pikachu.yaml", Species),
    (DATA_DIR / "Move-Thunderbolt.yaml", Move),
    (DATA_DIR / "Type-Electric.yaml", Type),
    (DATA_DIR / "Ability-Static.yaml", Ability),
    (DATA_DIR / "Shape-Quadruped.yaml", Shape),
    (DATA_DIR / "EggGroup-Field.yaml", EggGroup),
    (DATA_DIR / "Habitat-Forest.yaml", Habitat),
    (DATA_DIR / "Color-Yellow.yaml", Color),
]


@pytest.mark.parametrize(
    "example_file,target_class",
    EXAMPLES,
    ids=[f[0].stem for f in EXAMPLES],
)
def test_example_validates(example_file, target_class):
    obj = yaml_loader.load(str(example_file), target_class=target_class)
    assert obj is not None
    assert obj.id is not None
    assert obj.name is not None
