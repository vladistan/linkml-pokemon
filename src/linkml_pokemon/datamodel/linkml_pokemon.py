# Auto generated from linkml_pokemon.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-10-07T00:42:24
# Schema: linkml-pokemon
#
# id: https://pokemonkg.org/ontology
# description: Ontology covering the Pokémon world as it is presented in games and anime television series
# license: MIT

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime, time
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Integer, String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LINKML_POKEMON = CurieNamespace('linkml_pokemon', 'https://w3id.org/vladistan/linkml-pokemon/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
POKEMON = CurieNamespace('pokemon', 'https://pokemonkg.org/ontology#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
XML = CurieNamespace('xml', 'http://www.w3.org/XML/1998/namespace')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = POKEMON


# Types

# Class references



class Ability(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Ability"]
    class_class_curie: ClassVar[str] = "pokemon:Ability"
    class_name: ClassVar[str] = "Ability"
    class_model_uri: ClassVar[URIRef] = POKEMON.Ability


class EggGroup(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["EggGroup"]
    class_class_curie: ClassVar[str] = "pokemon:EggGroup"
    class_name: ClassVar[str] = "EggGroup"
    class_model_uri: ClassVar[URIRef] = POKEMON.EggGroup


class Colour(YAMLRoot):
    """
    Colors are categories that certain Pokemon belong to, which determine which Pokemon they can breed with.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Colour"]
    class_class_curie: ClassVar[str] = "pokemon:Colour"
    class_name: ClassVar[str] = "Colour"
    class_model_uri: ClassVar[URIRef] = POKEMON.Colour


class Flavor(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Flavor"]
    class_class_curie: ClassVar[str] = "pokemon:Flavor"
    class_name: ClassVar[str] = "Flavor"
    class_model_uri: ClassVar[URIRef] = POKEMON.Flavor


class Game(YAMLRoot):
    """
    A game is a type of media that can be played by people.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Game"]
    class_class_curie: ClassVar[str] = "pokemon:Game"
    class_name: ClassVar[str] = "Game"
    class_model_uri: ClassVar[URIRef] = POKEMON.Game


class Generation(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Generation"]
    class_class_curie: ClassVar[str] = "pokemon:Generation"
    class_name: ClassVar[str] = "Generation"
    class_model_uri: ClassVar[URIRef] = POKEMON.Generation


class Habitat(YAMLRoot):
    """
    A habitat is a type of environment that certain Pokemon belong to.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Habitat"]
    class_class_curie: ClassVar[str] = "pokemon:Habitat"
    class_name: ClassVar[str] = "Habitat"
    class_model_uri: ClassVar[URIRef] = POKEMON.Habitat


class Item(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Item"]
    class_class_curie: ClassVar[str] = "pokemon:Item"
    class_name: ClassVar[str] = "Item"
    class_model_uri: ClassVar[URIRef] = POKEMON.Item


class BattleItem(Item):
    """
    Battle items are items that can be used during battles.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["BattleItem"]
    class_class_curie: ClassVar[str] = "pokemon:BattleItem"
    class_name: ClassVar[str] = "BattleItem"
    class_model_uri: ClassVar[URIRef] = POKEMON.BattleItem


class Food(Item):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Food"]
    class_class_curie: ClassVar[str] = "pokemon:Food"
    class_name: ClassVar[str] = "Food"
    class_model_uri: ClassVar[URIRef] = POKEMON.Food


class Berry(Food):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Berry"]
    class_class_curie: ClassVar[str] = "pokemon:Berry"
    class_name: ClassVar[str] = "Berry"
    class_model_uri: ClassVar[URIRef] = POKEMON.Berry


class HM(Item):
    """
    Hidden Machine
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["HM"]
    class_class_curie: ClassVar[str] = "pokemon:HM"
    class_name: ClassVar[str] = "HM"
    class_model_uri: ClassVar[URIRef] = POKEMON.HM


class HoldItem(Item):
    """
    A hold item is an item that can be held by a Pokemon.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["HoldItem"]
    class_class_curie: ClassVar[str] = "pokemon:HoldItem"
    class_name: ClassVar[str] = "HoldItem"
    class_model_uri: ClassVar[URIRef] = POKEMON.HoldItem


class Pokedex(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Pokedex"]
    class_class_curie: ClassVar[str] = "pokemon:Pokedex"
    class_name: ClassVar[str] = "Pokedex"
    class_model_uri: ClassVar[URIRef] = POKEMON.Pokedex


class Pokemon(YAMLRoot):
    """
    A Pokemon
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Pokemon"]
    class_class_curie: ClassVar[str] = "pokemon:Pokemon"
    class_name: ClassVar[str] = "Pokemon"
    class_model_uri: ClassVar[URIRef] = POKEMON.Pokemon


class PokedexEntry(YAMLRoot):
    """
    A pokedex entry is a description of a Pokemon.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["PokedexEntry"]
    class_class_curie: ClassVar[str] = "pokemon:PokedexEntry"
    class_name: ClassVar[str] = "PokedexEntry"
    class_model_uri: ClassVar[URIRef] = POKEMON.PokedexEntry


class Pokeball(Item):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Pokeball"]
    class_class_curie: ClassVar[str] = "pokemon:Pokeball"
    class_name: ClassVar[str] = "Pokeball"
    class_model_uri: ClassVar[URIRef] = POKEMON.Pokeball


class Place(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Place"]
    class_class_curie: ClassVar[str] = "pokemon:Place"
    class_name: ClassVar[str] = "Place"
    class_model_uri: ClassVar[URIRef] = POKEMON.Place


class Gym(Place):
    """
    A gym is a location that can be battled at.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Gym"]
    class_class_curie: ClassVar[str] = "pokemon:Gym"
    class_name: ClassVar[str] = "Gym"
    class_model_uri: ClassVar[URIRef] = POKEMON.Gym


class Shape(YAMLRoot):
    """
    Shapes are categories that certain Pokemon belong to, which determine which Pokemon they can breed with.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Shape"]
    class_class_curie: ClassVar[str] = "pokemon:Shape"
    class_name: ClassVar[str] = "Shape"
    class_model_uri: ClassVar[URIRef] = POKEMON.Shape


class Region(Place):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Region"]
    class_class_curie: ClassVar[str] = "pokemon:Region"
    class_name: ClassVar[str] = "Region"
    class_model_uri: ClassVar[URIRef] = POKEMON.Region


class Species(YAMLRoot):
    """
    A species is a category of Pokemon that share common features.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Species"]
    class_class_curie: ClassVar[str] = "pokemon:Species"
    class_name: ClassVar[str] = "Species"
    class_model_uri: ClassVar[URIRef] = POKEMON.Species


class Move(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Move"]
    class_class_curie: ClassVar[str] = "pokemon:Move"
    class_name: ClassVar[str] = "Move"
    class_model_uri: ClassVar[URIRef] = POKEMON.Move


class MoveLearning(YAMLRoot):
    """
    A move learning is a way that a Pokemon can learn a move.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["MoveLearning"]
    class_class_curie: ClassVar[str] = "pokemon:MoveLearning"
    class_name: ClassVar[str] = "MoveLearning"
    class_model_uri: ClassVar[URIRef] = POKEMON.MoveLearning


class LearningByLevelingUp(MoveLearning):
    """
    A move that is learned by leveling up.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["LearningByLevelingUp"]
    class_class_curie: ClassVar[str] = "pokemon:LearningByLevelingUp"
    class_name: ClassVar[str] = "LearningByLevelingUp"
    class_model_uri: ClassVar[URIRef] = POKEMON.LearningByLevelingUp


class LearningThroughBreeding(MoveLearning):
    """
    A move that is learned by breeding.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["LearningThroughBreeding"]
    class_class_curie: ClassVar[str] = "pokemon:LearningThroughBreeding"
    class_name: ClassVar[str] = "LearningThroughBreeding"
    class_model_uri: ClassVar[URIRef] = POKEMON.LearningThroughBreeding


class Medicine(Item):
    """
    A medicine is an item that can be used to heal a Pokemon.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Medicine"]
    class_class_curie: ClassVar[str] = "pokemon:Medicine"
    class_name: ClassVar[str] = "Medicine"
    class_model_uri: ClassVar[URIRef] = POKEMON.Medicine


class SpecialMove(Move):
    """
    A special move is a type of move that can be used during battles.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["SpecialMove"]
    class_class_curie: ClassVar[str] = "pokemon:SpecialMove"
    class_name: ClassVar[str] = "SpecialMove"
    class_model_uri: ClassVar[URIRef] = POKEMON.SpecialMove


class PhysicalMove(Move):
    """
    A physical move is a type of move that can be used during battles.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["PhysicalMove"]
    class_class_curie: ClassVar[str] = "pokemon:PhysicalMove"
    class_name: ClassVar[str] = "PhysicalMove"
    class_model_uri: ClassVar[URIRef] = POKEMON.PhysicalMove


class StatusMove(Move):
    """
    A status move is a type of move that can be used during battles.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["StatusMove"]
    class_class_curie: ClassVar[str] = "pokemon:StatusMove"
    class_name: ClassVar[str] = "StatusMove"
    class_model_uri: ClassVar[URIRef] = POKEMON.StatusMove


class TM(Item):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["TM"]
    class_class_curie: ClassVar[str] = "pokemon:TM"
    class_name: ClassVar[str] = "TM"
    class_model_uri: ClassVar[URIRef] = POKEMON.TM


class Town(Place):
    """
    A town is a type of place that can be visited.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Town"]
    class_class_curie: ClassVar[str] = "pokemon:Town"
    class_name: ClassVar[str] = "Town"
    class_model_uri: ClassVar[URIRef] = POKEMON.Town


class Trainer(YAMLRoot):
    """
    A trainer is a person who is able to catch Pokemon.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Trainer"]
    class_class_curie: ClassVar[str] = "pokemon:Trainer"
    class_name: ClassVar[str] = "Trainer"
    class_model_uri: ClassVar[URIRef] = POKEMON.Trainer


class GymLeader(Trainer):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["GymLeader"]
    class_class_curie: ClassVar[str] = "pokemon:GymLeader"
    class_name: ClassVar[str] = "GymLeader"
    class_model_uri: ClassVar[URIRef] = POKEMON.GymLeader


class Type(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Type"]
    class_class_curie: ClassVar[str] = "pokemon:Type"
    class_name: ClassVar[str] = "Type"
    class_model_uri: ClassVar[URIRef] = POKEMON.Type


# Enumerations


# Slots
class slots:
    pass

slots.containsPlace = Slot(uri=POKEMON.contains_place, name="containsPlace", curie=POKEMON.curie('contains_place'),
                   model_uri=POKEMON.containsPlace, domain=Place, range=Optional[Union[Union[dict, "Place"], List[Union[dict, "Place"]]]])

slots.describedInPokedex = Slot(uri=POKEMON.describedInPokedex, name="describedInPokedex", curie=POKEMON.curie('describedInPokedex'),
                   model_uri=POKEMON.describedInPokedex, domain=Species, range=Optional[Union[Union[dict, PokedexEntry], List[Union[dict, PokedexEntry]]]])

slots.describesPokemon = Slot(uri=POKEMON.describesPokemon, name="describesPokemon", curie=POKEMON.curie('describesPokemon'),
                   model_uri=POKEMON.describesPokemon, domain=PokedexEntry, range=Optional[Union[Union[dict, "Species"], List[Union[dict, "Species"]]]])

slots.featuresSpecies = Slot(uri=POKEMON.featuresSpecies, name="featuresSpecies", curie=POKEMON.curie('featuresSpecies'),
                   model_uri=POKEMON.featuresSpecies, domain=PokedexEntry, range=Optional[Union[Union[dict, "Species"], List[Union[dict, "Species"]]]])

slots.hasPokedexEntry = Slot(uri=POKEMON.hasPokedexEntry, name="hasPokedexEntry", curie=POKEMON.curie('hasPokedexEntry'),
                   model_uri=POKEMON.hasPokedexEntry, domain=Pokedex, range=Optional[Union[Union[dict, "PokedexEntry"], List[Union[dict, "PokedexEntry"]]]])

slots.evolvesFrom = Slot(uri=POKEMON.evolvesFrom, name="evolvesFrom", curie=POKEMON.curie('evolvesFrom'),
                   model_uri=POKEMON.evolvesFrom, domain=Species, range=Optional[Union[dict, "Species"]])

slots.evolvesTo = Slot(uri=POKEMON.evolvesTo, name="evolvesTo", curie=POKEMON.curie('evolvesTo'),
                   model_uri=POKEMON.evolvesTo, domain=Species, range=Optional[Union[Union[dict, "Species"], List[Union[dict, "Species"]]]])

slots.foundIn = Slot(uri=POKEMON.foundIn, name="foundIn", curie=POKEMON.curie('foundIn'),
                   model_uri=POKEMON.foundIn, domain=Species, range=Optional[Union[Union[dict, Habitat], List[Union[dict, Habitat]]]])

slots.hasColour = Slot(uri=POKEMON.hasColour, name="hasColour", curie=POKEMON.curie('hasColour'),
                   model_uri=POKEMON.hasColour, domain=None, range=Optional[Union[Union[dict, Colour], List[Union[dict, Colour]]]])

slots.hasFlavor = Slot(uri=POKEMON.hasFlavor, name="hasFlavor", curie=POKEMON.curie('hasFlavor'),
                   model_uri=POKEMON.hasFlavor, domain=Food, range=Optional[Union[Union[dict, Flavor], List[Union[dict, Flavor]]]])

slots.hasType = Slot(uri=POKEMON.hasType, name="hasType", curie=POKEMON.curie('hasType'),
                   model_uri=POKEMON.hasType, domain=None, range=Optional[Union[Union[dict, Type], List[Union[dict, Type]]]])

slots.hasSize = Slot(uri=POKEMON.hasSize, name="hasSize", curie=POKEMON.curie('hasSize'),
                   model_uri=POKEMON.hasSize, domain=None, range=Optional[str])

slots.hasShape = Slot(uri=POKEMON.hasShape, name="hasShape", curie=POKEMON.curie('hasShape'),
                   model_uri=POKEMON.hasShape, domain=Species, range=Optional[Union[dict, Shape]])

slots.learnsMove = Slot(uri=POKEMON.learnsMove, name="learnsMove", curie=POKEMON.curie('learnsMove'),
                   model_uri=POKEMON.learnsMove, domain=MoveLearning, range=Optional[Union[Union[dict, Move], List[Union[dict, Move]]]])

slots.locatedIn = Slot(uri=POKEMON.locatedIn, name="locatedIn", curie=POKEMON.curie('locatedIn'),
                   model_uri=POKEMON.locatedIn, domain=Place, range=Optional[Union[Union[dict, "Place"], List[Union[dict, "Place"]]]])

slots.inEggGroup = Slot(uri=POKEMON.inEggGroup, name="inEggGroup", curie=POKEMON.curie('inEggGroup'),
                   model_uri=POKEMON.inEggGroup, domain=Species, range=Optional[Union[Union[dict, EggGroup], List[Union[dict, EggGroup]]]])

slots.mayHaveAbility = Slot(uri=POKEMON.mayHaveAbility, name="mayHaveAbility", curie=POKEMON.curie('mayHaveAbility'),
                   model_uri=POKEMON.mayHaveAbility, domain=Species, range=Optional[Union[Union[dict, Ability], List[Union[dict, Ability]]]])

slots.mayHaveHiddenAbility = Slot(uri=POKEMON.mayHaveHiddenAbility, name="mayHaveHiddenAbility", curie=POKEMON.curie('mayHaveHiddenAbility'),
                   model_uri=POKEMON.mayHaveHiddenAbility, domain=Species, range=Optional[Union[Union[dict, Ability], List[Union[dict, Ability]]]])

slots.firmness = Slot(uri=POKEMON.firmness, name="firmness", curie=POKEMON.curie('firmness'),
                   model_uri=POKEMON.firmness, domain=Food, range=Optional[int])

slots.accuracy = Slot(uri=POKEMON.accuracy, name="accuracy", curie=POKEMON.curie('accuracy'),
                   model_uri=POKEMON.accuracy, domain=Move, range=Optional[int])

slots.basePower = Slot(uri=POKEMON.basePower, name="basePower", curie=POKEMON.curie('basePower'),
                   model_uri=POKEMON.basePower, domain=Move, range=Optional[int])

slots.basePowerPoints = Slot(uri=POKEMON.basePowerPoints, name="basePowerPoints", curie=POKEMON.curie('basePowerPoints'),
                   model_uri=POKEMON.basePowerPoints, domain=Move, range=Optional[int])

slots.entryNumber = Slot(uri=POKEMON.entryNumber, name="entryNumber", curie=POKEMON.curie('entryNumber'),
                   model_uri=POKEMON.entryNumber, domain=PokedexEntry, range=Optional[int])

slots.hasGenus = Slot(uri=POKEMON.hasGenus, name="hasGenus", curie=POKEMON.curie('hasGenus'),
                   model_uri=POKEMON.hasGenus, domain=Species, range=Optional[str])

slots.maxPowerPoints = Slot(uri=POKEMON.maxPowerPoints, name="maxPowerPoints", curie=POKEMON.curie('maxPowerPoints'),
                   model_uri=POKEMON.maxPowerPoints, domain=Move, range=Optional[int])

slots.minLevelToLearn = Slot(uri=POKEMON.minLevelToLearn, name="minLevelToLearn", curie=POKEMON.curie('minLevelToLearn'),
                   model_uri=POKEMON.minLevelToLearn, domain=None, range=Optional[int])

slots.smoothness = Slot(uri=POKEMON.smoothness, name="smoothness", curie=POKEMON.curie('smoothness'),
                   model_uri=POKEMON.smoothness, domain=Food, range=Optional[int])