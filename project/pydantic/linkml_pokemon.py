from __future__ import annotations 

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal 
from enum import Enum 
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    field_validator
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass




class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'pokemon',
     'default_range': 'string',
     'description': 'Ontology covering the Pokémon world as it is presented in '
                    'games and anime television series',
     'id': 'https://pokemonkg.org/ontology',
     'imports': ['linkml:types', './foaf'],
     'license': 'MIT',
     'name': 'linkml-pokemon',
     'prefixes': {'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'example': {'prefix_prefix': 'example',
                              'prefix_reference': 'https://example.org/'},
                  'foaf': {'prefix_prefix': 'foaf',
                           'prefix_reference': 'http://xmlns.com/foaf/0.1/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'linkml_common': {'prefix_prefix': 'linkml_common',
                                    'prefix_reference': 'https://w3id.org/linkml/common/'},
                  'linkml_pokemon': {'prefix_prefix': 'linkml_pokemon',
                                     'prefix_reference': 'https://w3id.org/vladistan/linkml-pokemon/'},
                  'owl': {'prefix_prefix': 'owl',
                          'prefix_reference': 'http://www.w3.org/2002/07/owl#'},
                  'pokemon': {'prefix_prefix': 'pokemon',
                              'prefix_reference': 'https://pokemonkg.org/ontology#'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'},
                  'rdfs': {'prefix_prefix': 'rdfs',
                           'prefix_reference': 'http://www.w3.org/2000/01/rdf-schema#'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'xml': {'prefix_prefix': 'xml',
                          'prefix_reference': 'http://www.w3.org/XML/1998/namespace'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['https://vladistan.github.io/linkml-pokemon'],
     'source_file': 'src/linkml_pokemon/schema/linkml_pokemon.yaml',
     'title': 'linkml-pokemon'} )


class Thing(ConfiguredBaseModel):
    """
    A generic grouping for any identifiable attributes with an id
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'linkml_pokemon:Thing',
         'from_schema': 'https://pokemonkg.org/ontology'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing', 'Entity']} })


class NamedThing(Thing):
    """
    A generic grouping for any identifiable entity that has a name
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'linkml_pokemon:NamedThing',
         'from_schema': 'https://pokemonkg.org/ontology'})

    name: Optional[str] = Field(default=None, description="""Unique human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['NamedThing', 'Entity'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing', 'Entity'],
         'slot_uri': 'rdfs:comment'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing', 'Entity']} })


class Entity(ConfiguredBaseModel):
    """
    A grouping of attributes that can be reffered to
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'linkml_pokemon:Entity',
         'from_schema': 'https://pokemonkg.org/ontology'})

    name: Optional[str] = Field(default=None, description="""Unique human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['NamedThing', 'Entity'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing', 'Entity'],
         'slot_uri': 'rdfs:comment'} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['Thing', 'Entity'],
         'slot_uri': 'linkml_common:identifier'} })


class Ability(Entity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'Abilities were introduced in '
                                                   'Generation III as an all new game '
                                                   'mechanic. Each and every Pokemon '
                                                   'has an ability, and can only have '
                                                   'one at a time. Some abilities are '
                                                   'exclusive to certain Pokemon and '
                                                   'Evolution lines, while others are '
                                                   'known by many Pokemon.'}},
         'class_uri': 'pokemon:Ability',
         'from_schema': 'https://pokemonkg.org/ontology'})

    effectDescription: Optional[list[str]] = Field(default=None, description="""A description of the effect of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'effectDescription',
         'domain_of': ['Ability', 'Move'],
         'slot_uri': 'pokemon:effectDescription'} })
    name: Optional[str] = Field(default=None, description="""Unique human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['NamedThing', 'Entity'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing', 'Entity'],
         'slot_uri': 'rdfs:comment'} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['Thing', 'Entity'],
         'slot_uri': 'linkml_common:identifier'} })


class EggGroup(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'Egg group is a category that '
                                                   'determines which Pokemon are able '
                                                   'to interbreed. The concept was '
                                                   'introduced in Generation II, along '
                                                   'with breeding. Similar to types, a '
                                                   'Pokémon may belong to either one '
                                                   'or two egg groups.'}},
         'from_schema': 'https://pokemonkg.org/ontology'})

    pass


class Colour(ConfiguredBaseModel):
    """
    Colors are categories that certain Pokemon belong to, which determine which Pokemon they can breed with.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    pass


class Flavor(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'Flavor is a special set of '
                                                   'attributes that certain foods in '
                                                   'the Pokémon world have. Most of '
                                                   'the foods can have more than one '
                                                   'flavor, and the flavor determines '
                                                   'which Pokemon can eat them.'}},
         'from_schema': 'https://pokemonkg.org/ontology'})

    pass


class Game(ConfiguredBaseModel):
    """
    A game is a type of media that can be played by people.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    pass


class Generation(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'Generations refers to the Pokemon '
                                                   'game series. It is a group of '
                                                   'games that were released at or '
                                                   'around the same time. It also '
                                                   'means that games in the same '
                                                   'generation are compatible with the '
                                                   'others, containing the same '
                                                   'Pokemon and the number of moves '
                                                   'there are to be learned.'}},
         'from_schema': 'https://pokemonkg.org/ontology'})

    featuresSpecies: Optional[list[str]] = Field(default=None, description="""['A Pokedex entry features a species']""", json_schema_extra = { "linkml_meta": {'alias': 'featuresSpecies',
         'domain_of': ['Generation'],
         'slot_uri': 'pokemon:featuresSpecies'} })


class Habitat(ConfiguredBaseModel):
    """
    A habitat is a type of environment that certain Pokemon belong to.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    pass


class Item(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'An item is an object in the '
                                                   'Pokémon games which the player can '
                                                   'pick up, keep in their Bag, and '
                                                   'use in some manner. They have '
                                                   'various uses, including healing, '
                                                   'powering up, helping one to catch '
                                                   'Pokémon, or to access a new '
                                                   'area.'}},
         'from_schema': 'https://pokemonkg.org/ontology'})

    pass


class BattleItem(Item):
    """
    Battle items are items that can be used during battles.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    pass


class Food(Item):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    pass


class Berry(Food):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'Berries are small, juicy, fleshy '
                                                   'fruit. As in the real world, a '
                                                   'large variety exists in the '
                                                   'Pokémon world, with a large range '
                                                   'of flavors, names, and effects. '
                                                   'First found in the Generation II '
                                                   'games, many Berries have since '
                                                   'became critical help items in '
                                                   'battle, where their various '
                                                   'effects include HP and status '
                                                   'condition restoration, stat '
                                                   'enhancement, and even damage '
                                                   'negation.'}},
         'from_schema': 'https://pokemonkg.org/ontology'})

    hasSize: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'hasSize', 'domain_of': ['Berry'], 'slot_uri': 'pokemon:hasSize'} })


class HM(Item):
    """
    Hidden Machine
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    pass


class HoldItem(Item):
    """
    A hold item is an item that can be held by a Pokemon.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    pass


class Pokedex(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'The Pokedex is an electronic '
                                                   'device designed to catalogue and '
                                                   'provide information regarding the '
                                                   'various species of Pokemon '
                                                   'featured in the Pokemon video '
                                                   'game, anime and manga series.'}},
         'from_schema': 'https://pokemonkg.org/ontology'})

    pass


class Pokemon(ConfiguredBaseModel):
    """
    A Pokemon
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:seeAlso': {'tag': 'rdfs:seeAlso',
                                          'value': '<https://dbpedia.org/resource/Pokémon>'}},
         'from_schema': 'https://pokemonkg.org/ontology',
         'union_of': ['Pokedex', 'Type']})

    pass


class PokedexEntry(ConfiguredBaseModel):
    """
    A pokedex entry is a description of a Pokemon.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    pass


class Pokeball(Item):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'A Poké Ball is a type of item that '
                                                   "is critical to a Trainer's quest, "
                                                   'used for catching and storing '
                                                   'Pokémon.'}},
         'from_schema': 'https://pokemonkg.org/ontology'})

    pass


class Place(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'Entities that have a somewhat '
                                                   'fixed, physical extension.'}},
         'from_schema': 'https://pokemonkg.org/ontology'})

    pass


class Gym(Place):
    """
    A gym is a location that can be battled at.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    pass


class Shape(ConfiguredBaseModel):
    """
    Shapes are categories that certain Pokemon belong to, which determine which Pokemon they can breed with.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    pass


class Region(Place):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'Regions are areas in the Pokémon '
                                                   'universe that are smaller parts of '
                                                   'a nation.'}},
         'from_schema': 'https://pokemonkg.org/ontology'})

    pass


class Species(NamedThing):
    """
    A species is a category of Pokemon that share common features.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    hasColour: Optional[list[Colour]] = Field(default=None, description="""['A Pokemon has a color']""", json_schema_extra = { "linkml_meta": {'alias': 'hasColour',
         'domain_of': ['Species'],
         'slot_uri': 'pokemon:hasColour'} })
    mayHaveHiddenAbility: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'mayHaveHiddenAbility',
         'domain': 'Species',
         'domain_of': ['Species'],
         'slot_uri': 'pokemon:mayHaveHiddenAbility',
         'subproperty_of': 'mayHaveAbility'} })
    mayHaveAbility: Optional[list[str]] = Field(default=None, description="""['A Pokemon may have an ability']""", json_schema_extra = { "linkml_meta": {'alias': 'mayHaveAbility',
         'domain': 'Species',
         'domain_of': ['Species'],
         'slot_uri': 'pokemon:mayHaveAbility'} })
    isAbleToApply: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'isAbleToApply',
         'domain_of': ['Species'],
         'slot_uri': 'pokemon:isAbleToApply'} })
    hasHeight: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'hasHeight',
         'domain': 'Species',
         'domain_of': ['Species'],
         'slot_uri': 'pokemon:hasHeight'} })
    hasWeight: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'hasWeight',
         'domain': 'Species',
         'domain_of': ['Species'],
         'slot_uri': 'pokemon:hasWeight'} })
    depiction: Optional[str] = Field(default=None, description="""A depiction of the person""", json_schema_extra = { "linkml_meta": {'alias': 'depiction', 'domain_of': ['Species'], 'slot_uri': 'foaf:depiction'} })
    inEggGroup: Optional[list[EggGroup]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'inEggGroup',
         'domain': 'Species',
         'domain_of': ['Species'],
         'slot_uri': 'pokemon:inEggGroup'} })
    hasType: Optional[list[Type]] = Field(default=None, description="""['A Pokemon has a type']""", json_schema_extra = { "linkml_meta": {'alias': 'hasType',
         'domain_of': ['Species', 'Move'],
         'slot_uri': 'pokemon:hasType'} })
    hasShape: Optional[Shape] = Field(default=None, description="""The shape of a berry is a measure of how good it is for making a Potion.""", json_schema_extra = { "linkml_meta": {'alias': 'hasShape',
         'domain': 'Species',
         'domain_of': ['Species'],
         'slot_uri': 'pokemon:hasShape'} })
    hasGenus: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'hasGenus', 'domain': 'Species', 'domain_of': ['Species']} })
    hasCatchRate: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'hasCatchRate',
         'domain': 'Species',
         'domain_of': ['Species'],
         'slot_uri': 'pokemon:hasCatchRate'} })
    foundIn: Optional[list[Habitat]] = Field(default=None, description="""['A place is found in a location']""", json_schema_extra = { "linkml_meta": {'alias': 'foundIn',
         'domain': 'Species',
         'domain_of': ['Species'],
         'slot_uri': 'pokemon:foundIn'} })
    name: Optional[str] = Field(default=None, description="""Unique human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['NamedThing', 'Entity'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing', 'Entity'],
         'slot_uri': 'rdfs:comment'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['Thing', 'Entity']} })


class Move(Entity):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'A move is a special ability of a '
                                                   'Pokemon.'}},
         'class_uri': 'pokemon:Move',
         'from_schema': 'https://pokemonkg.org/ontology'})

    effectDescription: Optional[list[str]] = Field(default=None, description="""A description of the effect of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'effectDescription',
         'domain_of': ['Ability', 'Move'],
         'slot_uri': 'pokemon:effectDescription'} })
    hasType: Optional[list[Type]] = Field(default=None, description="""['A Pokemon has a type']""", json_schema_extra = { "linkml_meta": {'alias': 'hasType',
         'domain_of': ['Species', 'Move'],
         'slot_uri': 'pokemon:hasType'} })
    name: Optional[str] = Field(default=None, description="""Unique human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['NamedThing', 'Entity'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing', 'Entity'],
         'slot_uri': 'rdfs:comment'} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['Thing', 'Entity'],
         'slot_uri': 'linkml_common:identifier'} })


class MoveLearning(ConfiguredBaseModel):
    """
    A move learning is a way that a Pokemon can learn a move.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    pass


class LearningByLevelingUp(MoveLearning):
    """
    A move that is learned by leveling up.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    pass


class LearningThroughBreeding(MoveLearning):
    """
    A move that is learned by breeding.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    pass


class Medicine(Item):
    """
    Medicine items can heal various afflictions of a Pokemon.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    pass


class SpecialMove(Move):
    """
    A special move is a type of move that can be used during battles.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    effectDescription: Optional[list[str]] = Field(default=None, description="""A description of the effect of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'effectDescription',
         'domain_of': ['Ability', 'Move'],
         'slot_uri': 'pokemon:effectDescription'} })
    hasType: Optional[list[Type]] = Field(default=None, description="""['A Pokemon has a type']""", json_schema_extra = { "linkml_meta": {'alias': 'hasType',
         'domain_of': ['Species', 'Move'],
         'slot_uri': 'pokemon:hasType'} })
    name: Optional[str] = Field(default=None, description="""Unique human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['NamedThing', 'Entity'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing', 'Entity'],
         'slot_uri': 'rdfs:comment'} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['Thing', 'Entity'],
         'slot_uri': 'linkml_common:identifier'} })


class PhysicalMove(Move):
    """
    A physical move is a type of move that can be used during battles.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    effectDescription: Optional[list[str]] = Field(default=None, description="""A description of the effect of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'effectDescription',
         'domain_of': ['Ability', 'Move'],
         'slot_uri': 'pokemon:effectDescription'} })
    hasType: Optional[list[Type]] = Field(default=None, description="""['A Pokemon has a type']""", json_schema_extra = { "linkml_meta": {'alias': 'hasType',
         'domain_of': ['Species', 'Move'],
         'slot_uri': 'pokemon:hasType'} })
    name: Optional[str] = Field(default=None, description="""Unique human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['NamedThing', 'Entity'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing', 'Entity'],
         'slot_uri': 'rdfs:comment'} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['Thing', 'Entity'],
         'slot_uri': 'linkml_common:identifier'} })


class StatusMove(Move):
    """
    A status move is a type of move that can be used during battles.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    effectDescription: Optional[list[str]] = Field(default=None, description="""A description of the effect of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'effectDescription',
         'domain_of': ['Ability', 'Move'],
         'slot_uri': 'pokemon:effectDescription'} })
    hasType: Optional[list[Type]] = Field(default=None, description="""['A Pokemon has a type']""", json_schema_extra = { "linkml_meta": {'alias': 'hasType',
         'domain_of': ['Species', 'Move'],
         'slot_uri': 'pokemon:hasType'} })
    name: Optional[str] = Field(default=None, description="""Unique human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['NamedThing', 'Entity'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'domain_of': ['NamedThing', 'Entity'],
         'slot_uri': 'rdfs:comment'} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id',
         'domain_of': ['Thing', 'Entity'],
         'slot_uri': 'linkml_common:identifier'} })


class TM(Item):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'A Technical Machine is an item '
                                                   'that can be used to teach a '
                                                   'Pokemon a move.'}},
         'from_schema': 'https://pokemonkg.org/ontology'})

    pass


class Town(Place):
    """
    A town is a type of place that can be visited.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    pass


class Trainer(ConfiguredBaseModel):
    """
    A trainer is a person who is able to catch Pokemon.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    pass


class GymLeader(Trainer):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'A gym leader is a highest ranking '
                                                   'member and owner of an official '
                                                   'Pokémon gym. Gym leaders use their '
                                                   'gym and their Pokemon to test the '
                                                   'skills of trainers that challenge '
                                                   'them, and if said trainers win a '
                                                   'battle, the gym leader will gift '
                                                   "them a badge that's unique to that "
                                                   'specific gym.'}},
         'from_schema': 'https://pokemonkg.org/ontology'})

    pass


class Type(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'All Pokemon creatures and their '
                                                   'moves are assigned certain types. '
                                                   'Each type has several strengths '
                                                   'and weaknesses in both attack and '
                                                   'defense.'}},
         'from_schema': 'https://pokemonkg.org/ontology'})

    pass


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Thing.model_rebuild()
NamedThing.model_rebuild()
Entity.model_rebuild()
Ability.model_rebuild()
EggGroup.model_rebuild()
Colour.model_rebuild()
Flavor.model_rebuild()
Game.model_rebuild()
Generation.model_rebuild()
Habitat.model_rebuild()
Item.model_rebuild()
BattleItem.model_rebuild()
Food.model_rebuild()
Berry.model_rebuild()
HM.model_rebuild()
HoldItem.model_rebuild()
Pokedex.model_rebuild()
Pokemon.model_rebuild()
PokedexEntry.model_rebuild()
Pokeball.model_rebuild()
Place.model_rebuild()
Gym.model_rebuild()
Shape.model_rebuild()
Region.model_rebuild()
Species.model_rebuild()
Move.model_rebuild()
MoveLearning.model_rebuild()
LearningByLevelingUp.model_rebuild()
LearningThroughBreeding.model_rebuild()
Medicine.model_rebuild()
SpecialMove.model_rebuild()
PhysicalMove.model_rebuild()
StatusMove.model_rebuild()
TM.model_rebuild()
Town.model_rebuild()
Trainer.model_rebuild()
GymLeader.model_rebuild()
Type.model_rebuild()

