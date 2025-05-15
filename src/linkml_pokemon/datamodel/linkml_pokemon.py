# Auto generated from linkml_pokemon.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-05-14T22:28:23
# Schema: linkml-pokemon
#
# id: https://pokemonkg.org/ontology
# description: Ontology covering the Pokémon world as it is presented in games and anime television series
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Integer, String, Uri
from linkml_runtime.utils.metamodelcore import URI

metamodel_version = "1.7.0"
version = None

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LINKML_COMMON = CurieNamespace('linkml_common', 'https://w3id.org/linkml/common/')
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
class ThingId(URI):
    pass


class NamedThingId(ThingId):
    pass


class EntityId(URI):
    pass


class AbilityId(EntityId):
    pass


class MoveId(EntityId):
    pass


class SpecialMoveId(MoveId):
    pass


class PhysicalMoveId(MoveId):
    pass


class StatusMoveId(MoveId):
    pass


@dataclass(repr=False)
class Thing(YAMLRoot):
    """
    A generic grouping for any identifiable attributes with an id
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_POKEMON["Thing"]
    class_class_curie: ClassVar[str] = "linkml_pokemon:Thing"
    class_name: ClassVar[str] = "Thing"
    class_model_uri: ClassVar[URIRef] = POKEMON.Thing

    id: Union[str, ThingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ThingId):
            self.id = ThingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NamedThing(Thing):
    """
    A generic grouping for any identifiable entity that has a name
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_POKEMON["NamedThing"]
    class_class_curie: ClassVar[str] = "linkml_pokemon:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = POKEMON.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Entity(YAMLRoot):
    """
    A grouping of attributes that can be reffered to
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_POKEMON["Entity"]
    class_class_curie: ClassVar[str] = "linkml_pokemon:Entity"
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = POKEMON.Entity

    id: Union[str, EntityId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityId):
            self.id = EntityId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Ability(Entity):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Ability"]
    class_class_curie: ClassVar[str] = "pokemon:Ability"
    class_name: ClassVar[str] = "Ability"
    class_model_uri: ClassVar[URIRef] = POKEMON.Ability

    id: Union[str, AbilityId] = None
    effectDescription: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AbilityId):
            self.id = AbilityId(self.id)

        if not isinstance(self.effectDescription, list):
            self.effectDescription = [self.effectDescription] if self.effectDescription is not None else []
        self.effectDescription = [v if isinstance(v, str) else str(v) for v in self.effectDescription]

        super().__post_init__(**kwargs)


class EggGroup(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["EggGroup"]
    class_class_curie: ClassVar[str] = "pokemon:EggGroup"
    class_name: ClassVar[str] = "EggGroup"
    class_model_uri: ClassVar[URIRef] = POKEMON.EggGroup


class Colour(YAMLRoot):
    """
    Colors are categories that certain Pokemon belong to, which determine which Pokemon they can breed with.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Colour"]
    class_class_curie: ClassVar[str] = "pokemon:Colour"
    class_name: ClassVar[str] = "Colour"
    class_model_uri: ClassVar[URIRef] = POKEMON.Colour


class Flavor(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Flavor"]
    class_class_curie: ClassVar[str] = "pokemon:Flavor"
    class_name: ClassVar[str] = "Flavor"
    class_model_uri: ClassVar[URIRef] = POKEMON.Flavor


class Game(YAMLRoot):
    """
    A game is a type of media that can be played by people.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Game"]
    class_class_curie: ClassVar[str] = "pokemon:Game"
    class_name: ClassVar[str] = "Game"
    class_model_uri: ClassVar[URIRef] = POKEMON.Game


@dataclass(repr=False)
class Generation(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Generation"]
    class_class_curie: ClassVar[str] = "pokemon:Generation"
    class_name: ClassVar[str] = "Generation"
    class_model_uri: ClassVar[URIRef] = POKEMON.Generation

    featuresSpecies: Optional[Union[Union[dict, "Species"], list[Union[dict, "Species"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.featuresSpecies, list):
            self.featuresSpecies = [self.featuresSpecies] if self.featuresSpecies is not None else []
        self.featuresSpecies = [v if isinstance(v, Species) else Species(**as_dict(v)) for v in self.featuresSpecies]

        super().__post_init__(**kwargs)


class Habitat(YAMLRoot):
    """
    A habitat is a type of environment that certain Pokemon belong to.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Habitat"]
    class_class_curie: ClassVar[str] = "pokemon:Habitat"
    class_name: ClassVar[str] = "Habitat"
    class_model_uri: ClassVar[URIRef] = POKEMON.Habitat


class Item(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Item"]
    class_class_curie: ClassVar[str] = "pokemon:Item"
    class_name: ClassVar[str] = "Item"
    class_model_uri: ClassVar[URIRef] = POKEMON.Item


class BattleItem(Item):
    """
    Battle items are items that can be used during battles.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["BattleItem"]
    class_class_curie: ClassVar[str] = "pokemon:BattleItem"
    class_name: ClassVar[str] = "BattleItem"
    class_model_uri: ClassVar[URIRef] = POKEMON.BattleItem


class Food(Item):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Food"]
    class_class_curie: ClassVar[str] = "pokemon:Food"
    class_name: ClassVar[str] = "Food"
    class_model_uri: ClassVar[URIRef] = POKEMON.Food


@dataclass(repr=False)
class Berry(Food):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Berry"]
    class_class_curie: ClassVar[str] = "pokemon:Berry"
    class_name: ClassVar[str] = "Berry"
    class_model_uri: ClassVar[URIRef] = POKEMON.Berry

    hasSize: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.hasSize is not None and not isinstance(self.hasSize, str):
            self.hasSize = str(self.hasSize)

        super().__post_init__(**kwargs)


class HM(Item):
    """
    Hidden Machine
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["HM"]
    class_class_curie: ClassVar[str] = "pokemon:HM"
    class_name: ClassVar[str] = "HM"
    class_model_uri: ClassVar[URIRef] = POKEMON.HM


class HoldItem(Item):
    """
    A hold item is an item that can be held by a Pokemon.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["HoldItem"]
    class_class_curie: ClassVar[str] = "pokemon:HoldItem"
    class_name: ClassVar[str] = "HoldItem"
    class_model_uri: ClassVar[URIRef] = POKEMON.HoldItem


class Pokedex(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Pokedex"]
    class_class_curie: ClassVar[str] = "pokemon:Pokedex"
    class_name: ClassVar[str] = "Pokedex"
    class_model_uri: ClassVar[URIRef] = POKEMON.Pokedex


class Pokemon(YAMLRoot):
    """
    A Pokemon
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Pokemon"]
    class_class_curie: ClassVar[str] = "pokemon:Pokemon"
    class_name: ClassVar[str] = "Pokemon"
    class_model_uri: ClassVar[URIRef] = POKEMON.Pokemon


class PokedexEntry(YAMLRoot):
    """
    A pokedex entry is a description of a Pokemon.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["PokedexEntry"]
    class_class_curie: ClassVar[str] = "pokemon:PokedexEntry"
    class_name: ClassVar[str] = "PokedexEntry"
    class_model_uri: ClassVar[URIRef] = POKEMON.PokedexEntry


class Pokeball(Item):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Pokeball"]
    class_class_curie: ClassVar[str] = "pokemon:Pokeball"
    class_name: ClassVar[str] = "Pokeball"
    class_model_uri: ClassVar[URIRef] = POKEMON.Pokeball


class Place(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Place"]
    class_class_curie: ClassVar[str] = "pokemon:Place"
    class_name: ClassVar[str] = "Place"
    class_model_uri: ClassVar[URIRef] = POKEMON.Place


class Gym(Place):
    """
    A gym is a location that can be battled at.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Gym"]
    class_class_curie: ClassVar[str] = "pokemon:Gym"
    class_name: ClassVar[str] = "Gym"
    class_model_uri: ClassVar[URIRef] = POKEMON.Gym


class Shape(YAMLRoot):
    """
    Shapes are categories that certain Pokemon belong to, which determine which Pokemon they can breed with.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Shape"]
    class_class_curie: ClassVar[str] = "pokemon:Shape"
    class_name: ClassVar[str] = "Shape"
    class_model_uri: ClassVar[URIRef] = POKEMON.Shape


class Region(Place):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Region"]
    class_class_curie: ClassVar[str] = "pokemon:Region"
    class_name: ClassVar[str] = "Region"
    class_model_uri: ClassVar[URIRef] = POKEMON.Region


class Species(YAMLRoot):
    """
    A species is a category of Pokemon that share common features.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Species"]
    class_class_curie: ClassVar[str] = "pokemon:Species"
    class_name: ClassVar[str] = "Species"
    class_model_uri: ClassVar[URIRef] = POKEMON.Species


@dataclass(repr=False)
class Move(Entity):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Move"]
    class_class_curie: ClassVar[str] = "pokemon:Move"
    class_name: ClassVar[str] = "Move"
    class_model_uri: ClassVar[URIRef] = POKEMON.Move

    id: Union[str, MoveId] = None
    effectDescription: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MoveId):
            self.id = MoveId(self.id)

        if not isinstance(self.effectDescription, list):
            self.effectDescription = [self.effectDescription] if self.effectDescription is not None else []
        self.effectDescription = [v if isinstance(v, str) else str(v) for v in self.effectDescription]

        super().__post_init__(**kwargs)


class MoveLearning(YAMLRoot):
    """
    A move learning is a way that a Pokemon can learn a move.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["MoveLearning"]
    class_class_curie: ClassVar[str] = "pokemon:MoveLearning"
    class_name: ClassVar[str] = "MoveLearning"
    class_model_uri: ClassVar[URIRef] = POKEMON.MoveLearning


class LearningByLevelingUp(MoveLearning):
    """
    A move that is learned by leveling up.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["LearningByLevelingUp"]
    class_class_curie: ClassVar[str] = "pokemon:LearningByLevelingUp"
    class_name: ClassVar[str] = "LearningByLevelingUp"
    class_model_uri: ClassVar[URIRef] = POKEMON.LearningByLevelingUp


class LearningThroughBreeding(MoveLearning):
    """
    A move that is learned by breeding.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["LearningThroughBreeding"]
    class_class_curie: ClassVar[str] = "pokemon:LearningThroughBreeding"
    class_name: ClassVar[str] = "LearningThroughBreeding"
    class_model_uri: ClassVar[URIRef] = POKEMON.LearningThroughBreeding


class Medicine(Item):
    """
    Medicine items can heal various afflictions of a Pokemon.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Medicine"]
    class_class_curie: ClassVar[str] = "pokemon:Medicine"
    class_name: ClassVar[str] = "Medicine"
    class_model_uri: ClassVar[URIRef] = POKEMON.Medicine


@dataclass(repr=False)
class SpecialMove(Move):
    """
    A special move is a type of move that can be used during battles.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["SpecialMove"]
    class_class_curie: ClassVar[str] = "pokemon:SpecialMove"
    class_name: ClassVar[str] = "SpecialMove"
    class_model_uri: ClassVar[URIRef] = POKEMON.SpecialMove

    id: Union[str, SpecialMoveId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpecialMoveId):
            self.id = SpecialMoveId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhysicalMove(Move):
    """
    A physical move is a type of move that can be used during battles.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["PhysicalMove"]
    class_class_curie: ClassVar[str] = "pokemon:PhysicalMove"
    class_name: ClassVar[str] = "PhysicalMove"
    class_model_uri: ClassVar[URIRef] = POKEMON.PhysicalMove

    id: Union[str, PhysicalMoveId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhysicalMoveId):
            self.id = PhysicalMoveId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StatusMove(Move):
    """
    A status move is a type of move that can be used during battles.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["StatusMove"]
    class_class_curie: ClassVar[str] = "pokemon:StatusMove"
    class_name: ClassVar[str] = "StatusMove"
    class_model_uri: ClassVar[URIRef] = POKEMON.StatusMove

    id: Union[str, StatusMoveId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StatusMoveId):
            self.id = StatusMoveId(self.id)

        super().__post_init__(**kwargs)


class TM(Item):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["TM"]
    class_class_curie: ClassVar[str] = "pokemon:TM"
    class_name: ClassVar[str] = "TM"
    class_model_uri: ClassVar[URIRef] = POKEMON.TM


class Town(Place):
    """
    A town is a type of place that can be visited.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Town"]
    class_class_curie: ClassVar[str] = "pokemon:Town"
    class_name: ClassVar[str] = "Town"
    class_model_uri: ClassVar[URIRef] = POKEMON.Town


class Trainer(YAMLRoot):
    """
    A trainer is a person who is able to catch Pokemon.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Trainer"]
    class_class_curie: ClassVar[str] = "pokemon:Trainer"
    class_name: ClassVar[str] = "Trainer"
    class_model_uri: ClassVar[URIRef] = POKEMON.Trainer


class GymLeader(Trainer):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["GymLeader"]
    class_class_curie: ClassVar[str] = "pokemon:GymLeader"
    class_name: ClassVar[str] = "GymLeader"
    class_model_uri: ClassVar[URIRef] = POKEMON.GymLeader


class Type(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Type"]
    class_class_curie: ClassVar[str] = "pokemon:Type"
    class_name: ClassVar[str] = "Type"
    class_model_uri: ClassVar[URIRef] = POKEMON.Type


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=POKEMON.id, name="id", curie=POKEMON.curie('id'),
                   model_uri=POKEMON.id, domain=None, range=URIRef)

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=POKEMON.name, domain=None, range=Optional[str])

slots.description = Slot(uri=RDFS.comment, name="description", curie=RDFS.curie('comment'),
                   model_uri=POKEMON.description, domain=None, range=Optional[str])

slots.effectDescription = Slot(uri=POKEMON.effectDescription, name="effectDescription", curie=POKEMON.curie('effectDescription'),
                   model_uri=POKEMON.effectDescription, domain=None, range=Optional[Union[str, list[str]]])

slots.containsPlace = Slot(uri=POKEMON.contains_place, name="containsPlace", curie=POKEMON.curie('contains_place'),
                   model_uri=POKEMON.containsPlace, domain=Place, range=Optional[Union[Union[dict, "Place"], list[Union[dict, "Place"]]]])

slots.describedInPokedex = Slot(uri=POKEMON.describedInPokedex, name="describedInPokedex", curie=POKEMON.curie('describedInPokedex'),
                   model_uri=POKEMON.describedInPokedex, domain=Species, range=Optional[Union[Union[dict, PokedexEntry], list[Union[dict, PokedexEntry]]]])

slots.describesPokemon = Slot(uri=POKEMON.describesPokemon, name="describesPokemon", curie=POKEMON.curie('describesPokemon'),
                   model_uri=POKEMON.describesPokemon, domain=PokedexEntry, range=Optional[Union[Union[dict, "Species"], list[Union[dict, "Species"]]]])

slots.featuresSpecies = Slot(uri=POKEMON.featuresSpecies, name="featuresSpecies", curie=POKEMON.curie('featuresSpecies'),
                   model_uri=POKEMON.featuresSpecies, domain=None, range=Optional[Union[Union[dict, Species], list[Union[dict, Species]]]])

slots.hasPokedexEntry = Slot(uri=POKEMON.hasPokedexEntry, name="hasPokedexEntry", curie=POKEMON.curie('hasPokedexEntry'),
                   model_uri=POKEMON.hasPokedexEntry, domain=Pokedex, range=Optional[Union[Union[dict, "PokedexEntry"], list[Union[dict, "PokedexEntry"]]]])

slots.evolvesFrom = Slot(uri=POKEMON.evolvesFrom, name="evolvesFrom", curie=POKEMON.curie('evolvesFrom'),
                   model_uri=POKEMON.evolvesFrom, domain=Species, range=Optional[Union[dict, "Species"]])

slots.evolvesTo = Slot(uri=POKEMON.evolvesTo, name="evolvesTo", curie=POKEMON.curie('evolvesTo'),
                   model_uri=POKEMON.evolvesTo, domain=Species, range=Optional[Union[Union[dict, "Species"], list[Union[dict, "Species"]]]])

slots.foundIn = Slot(uri=POKEMON.foundIn, name="foundIn", curie=POKEMON.curie('foundIn'),
                   model_uri=POKEMON.foundIn, domain=Species, range=Optional[Union[Union[dict, Habitat], list[Union[dict, Habitat]]]])

slots.hasColour = Slot(uri=POKEMON.hasColour, name="hasColour", curie=POKEMON.curie('hasColour'),
                   model_uri=POKEMON.hasColour, domain=None, range=Optional[Union[Union[dict, Colour], list[Union[dict, Colour]]]])

slots.hasFlavor = Slot(uri=POKEMON.hasFlavor, name="hasFlavor", curie=POKEMON.curie('hasFlavor'),
                   model_uri=POKEMON.hasFlavor, domain=Food, range=Optional[Union[Union[dict, Flavor], list[Union[dict, Flavor]]]])

slots.hasType = Slot(uri=POKEMON.hasType, name="hasType", curie=POKEMON.curie('hasType'),
                   model_uri=POKEMON.hasType, domain=None, range=Optional[Union[Union[dict, Type], list[Union[dict, Type]]]])

slots.hasSize = Slot(uri=POKEMON.hasSize, name="hasSize", curie=POKEMON.curie('hasSize'),
                   model_uri=POKEMON.hasSize, domain=None, range=Optional[str])

slots.hasShape = Slot(uri=POKEMON.hasShape, name="hasShape", curie=POKEMON.curie('hasShape'),
                   model_uri=POKEMON.hasShape, domain=Species, range=Optional[Union[dict, Shape]])

slots.learnsMove = Slot(uri=POKEMON.learnsMove, name="learnsMove", curie=POKEMON.curie('learnsMove'),
                   model_uri=POKEMON.learnsMove, domain=MoveLearning, range=Optional[Union[Union[str, MoveId], list[Union[str, MoveId]]]])

slots.locatedIn = Slot(uri=POKEMON.locatedIn, name="locatedIn", curie=POKEMON.curie('locatedIn'),
                   model_uri=POKEMON.locatedIn, domain=Place, range=Optional[Union[Union[dict, "Place"], list[Union[dict, "Place"]]]])

slots.inEggGroup = Slot(uri=POKEMON.inEggGroup, name="inEggGroup", curie=POKEMON.curie('inEggGroup'),
                   model_uri=POKEMON.inEggGroup, domain=Species, range=Optional[Union[Union[dict, EggGroup], list[Union[dict, EggGroup]]]])

slots.mayHaveAbility = Slot(uri=POKEMON.mayHaveAbility, name="mayHaveAbility", curie=POKEMON.curie('mayHaveAbility'),
                   model_uri=POKEMON.mayHaveAbility, domain=Species, range=Optional[Union[Union[str, AbilityId], list[Union[str, AbilityId]]]])

slots.mayHaveHiddenAbility = Slot(uri=POKEMON.mayHaveHiddenAbility, name="mayHaveHiddenAbility", curie=POKEMON.curie('mayHaveHiddenAbility'),
                   model_uri=POKEMON.mayHaveHiddenAbility, domain=Species, range=Optional[Union[Union[str, AbilityId], list[Union[str, AbilityId]]]])

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

slots.entity__id = Slot(uri=LINKML_COMMON.identifier, name="entity__id", curie=LINKML_COMMON.curie('identifier'),
                   model_uri=POKEMON.entity__id, domain=None, range=URIRef)