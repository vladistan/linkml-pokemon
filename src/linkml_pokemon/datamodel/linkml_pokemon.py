# Auto generated from linkml_pokemon.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-10-25T15:09:08
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

from linkml_runtime.linkml_model.types import Float, Integer, String, Uri
from linkml_runtime.utils.metamodelcore import URI

metamodel_version = "1.7.0"
version = None

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
DBPEDIA = CurieNamespace('dbpedia', 'http://dbpedia.org/ontology/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LINKML_COMMON = CurieNamespace('linkml_common', 'https://w3id.org/linkml/common/')
LINKML_POKEMON = CurieNamespace('linkml_pokemon', 'https://w3id.org/vladistan/linkml-pokemon/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
POKEMON = CurieNamespace('pokemon', 'https://pokemonkg.org/ontology#')
QUDT = CurieNamespace('qudt', 'http://qudt.org/schema/qudt/')
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


class AbilityId(ThingId):
    pass


class GameId(ThingId):
    pass


class GenerationId(ThingId):
    pass


class ItemId(ThingId):
    pass


class BattleItemId(ItemId):
    pass


class FoodId(ItemId):
    pass


class BerryId(FoodId):
    pass


class HMId(ItemId):
    pass


class HoldItemId(ItemId):
    pass


class PokedexId(ThingId):
    pass


class PokedexEntryId(ThingId):
    pass


class PokeballId(ItemId):
    pass


class PlaceId(ThingId):
    pass


class GymId(PlaceId):
    pass


class RegionId(PlaceId):
    pass


class MoveId(ThingId):
    pass


class MedicineId(ItemId):
    pass


class SpecialMoveId(MoveId):
    pass


class PhysicalMoveId(MoveId):
    pass


class StatusMoveId(MoveId):
    pass


class TMId(ItemId):
    pass


class TownId(PlaceId):
    pass


class ColourId(ThingId):
    pass


class NamedIndividualId(ThingId):
    pass


class EggGroupId(NamedIndividualId):
    pass


class FlavorId(NamedIndividualId):
    pass


class HabitatId(NamedIndividualId):
    pass


class ShapeId(NamedIndividualId):
    pass


class SpeciesId(NamedIndividualId):
    pass


class TypeId(NamedIndividualId):
    pass


class PersonId(NamedIndividualId):
    pass


class TrainerId(PersonId):
    pass


class GymLeaderId(TrainerId):
    pass


class QuantityId(ThingId):
    pass


class UnitId(ThingId):
    pass


class Pokemon(YAMLRoot):
    """
    A Pokemon
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Pokemon"]
    class_class_curie: ClassVar[str] = "pokemon:Pokemon"
    class_name: ClassVar[str] = "Pokemon"
    class_model_uri: ClassVar[URIRef] = POKEMON.Pokemon


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


@dataclass(repr=False)
class Thing(YAMLRoot):
    """
    An rdfs:Resource that defines name and description
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL["Thing"]
    class_class_curie: ClassVar[str] = "owl:Thing"
    class_name: ClassVar[str] = "Thing"
    class_model_uri: ClassVar[URIRef] = POKEMON.Thing

    id: Union[str, ThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ThingId):
            self.id = ThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Ability(Thing):
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


@dataclass(repr=False)
class Game(Thing):
    """
    A game is a type of media that can be played by people.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Game"]
    class_class_curie: ClassVar[str] = "pokemon:Game"
    class_name: ClassVar[str] = "Game"
    class_model_uri: ClassVar[URIRef] = POKEMON.Game

    id: Union[str, GameId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GameId):
            self.id = GameId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Generation(Thing):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Generation"]
    class_class_curie: ClassVar[str] = "pokemon:Generation"
    class_name: ClassVar[str] = "Generation"
    class_model_uri: ClassVar[URIRef] = POKEMON.Generation

    id: Union[str, GenerationId] = None
    featuresSpecies: Optional[Union[Union[str, SpeciesId], list[Union[str, SpeciesId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GenerationId):
            self.id = GenerationId(self.id)

        if not isinstance(self.featuresSpecies, list):
            self.featuresSpecies = [self.featuresSpecies] if self.featuresSpecies is not None else []
        self.featuresSpecies = [v if isinstance(v, SpeciesId) else SpeciesId(v) for v in self.featuresSpecies]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Item(Thing):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Item"]
    class_class_curie: ClassVar[str] = "pokemon:Item"
    class_name: ClassVar[str] = "Item"
    class_model_uri: ClassVar[URIRef] = POKEMON.Item

    id: Union[str, ItemId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ItemId):
            self.id = ItemId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BattleItem(Item):
    """
    Battle items are items that can be used during battles.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["BattleItem"]
    class_class_curie: ClassVar[str] = "pokemon:BattleItem"
    class_name: ClassVar[str] = "BattleItem"
    class_model_uri: ClassVar[URIRef] = POKEMON.BattleItem

    id: Union[str, BattleItemId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BattleItemId):
            self.id = BattleItemId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Food(Item):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Food"]
    class_class_curie: ClassVar[str] = "pokemon:Food"
    class_name: ClassVar[str] = "Food"
    class_model_uri: ClassVar[URIRef] = POKEMON.Food

    id: Union[str, FoodId] = None
    hasFlavor: Optional[Union[Union[str, FlavorId], list[Union[str, FlavorId]]]] = empty_list()
    firmness: Optional[int] = None
    smoothness: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FoodId):
            self.id = FoodId(self.id)

        if not isinstance(self.hasFlavor, list):
            self.hasFlavor = [self.hasFlavor] if self.hasFlavor is not None else []
        self.hasFlavor = [v if isinstance(v, FlavorId) else FlavorId(v) for v in self.hasFlavor]

        if self.firmness is not None and not isinstance(self.firmness, int):
            self.firmness = int(self.firmness)

        if self.smoothness is not None and not isinstance(self.smoothness, int):
            self.smoothness = int(self.smoothness)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Berry(Food):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Berry"]
    class_class_curie: ClassVar[str] = "pokemon:Berry"
    class_name: ClassVar[str] = "Berry"
    class_model_uri: ClassVar[URIRef] = POKEMON.Berry

    id: Union[str, BerryId] = None
    hasSize: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BerryId):
            self.id = BerryId(self.id)

        if self.hasSize is not None and not isinstance(self.hasSize, str):
            self.hasSize = str(self.hasSize)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HM(Item):
    """
    Hidden Machine
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["HM"]
    class_class_curie: ClassVar[str] = "pokemon:HM"
    class_name: ClassVar[str] = "HM"
    class_model_uri: ClassVar[URIRef] = POKEMON.HM

    id: Union[str, HMId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HMId):
            self.id = HMId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HoldItem(Item):
    """
    A hold item is an item that can be held by a Pokemon.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["HoldItem"]
    class_class_curie: ClassVar[str] = "pokemon:HoldItem"
    class_name: ClassVar[str] = "HoldItem"
    class_model_uri: ClassVar[URIRef] = POKEMON.HoldItem

    id: Union[str, HoldItemId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HoldItemId):
            self.id = HoldItemId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Pokedex(Thing):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Pokedex"]
    class_class_curie: ClassVar[str] = "pokemon:Pokedex"
    class_name: ClassVar[str] = "Pokedex"
    class_model_uri: ClassVar[URIRef] = POKEMON.Pokedex

    id: Union[str, PokedexId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PokedexId):
            self.id = PokedexId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PokedexEntry(Thing):
    """
    A pokedex entry is a description of a Pokemon.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["PokedexEntry"]
    class_class_curie: ClassVar[str] = "pokemon:PokedexEntry"
    class_name: ClassVar[str] = "PokedexEntry"
    class_model_uri: ClassVar[URIRef] = POKEMON.PokedexEntry

    id: Union[str, PokedexEntryId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PokedexEntryId):
            self.id = PokedexEntryId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Pokeball(Item):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Pokeball"]
    class_class_curie: ClassVar[str] = "pokemon:Pokeball"
    class_name: ClassVar[str] = "Pokeball"
    class_model_uri: ClassVar[URIRef] = POKEMON.Pokeball

    id: Union[str, PokeballId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PokeballId):
            self.id = PokeballId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Place(Thing):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Place"]
    class_class_curie: ClassVar[str] = "pokemon:Place"
    class_name: ClassVar[str] = "Place"
    class_model_uri: ClassVar[URIRef] = POKEMON.Place

    id: Union[str, PlaceId] = None

@dataclass(repr=False)
class Gym(Place):
    """
    A gym is a location that can be battled at.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Gym"]
    class_class_curie: ClassVar[str] = "pokemon:Gym"
    class_name: ClassVar[str] = "Gym"
    class_model_uri: ClassVar[URIRef] = POKEMON.Gym

    id: Union[str, GymId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GymId):
            self.id = GymId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Region(Place):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Region"]
    class_class_curie: ClassVar[str] = "pokemon:Region"
    class_name: ClassVar[str] = "Region"
    class_model_uri: ClassVar[URIRef] = POKEMON.Region

    id: Union[str, RegionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RegionId):
            self.id = RegionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Move(Thing):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Move"]
    class_class_curie: ClassVar[str] = "pokemon:Move"
    class_name: ClassVar[str] = "Move"
    class_model_uri: ClassVar[URIRef] = POKEMON.Move

    id: Union[str, MoveId] = None
    effectDescription: Optional[Union[str, list[str]]] = empty_list()
    hasType: Optional[Union[dict[Union[str, TypeId], Union[dict, "Type"]], list[Union[dict, "Type"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MoveId):
            self.id = MoveId(self.id)

        if not isinstance(self.effectDescription, list):
            self.effectDescription = [self.effectDescription] if self.effectDescription is not None else []
        self.effectDescription = [v if isinstance(v, str) else str(v) for v in self.effectDescription]

        self._normalize_inlined_as_list(slot_name="hasType", slot_type=Type, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Medicine(Item):
    """
    Medicine items can heal various afflictions of a Pokemon.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Medicine"]
    class_class_curie: ClassVar[str] = "pokemon:Medicine"
    class_name: ClassVar[str] = "Medicine"
    class_model_uri: ClassVar[URIRef] = POKEMON.Medicine

    id: Union[str, MedicineId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MedicineId):
            self.id = MedicineId(self.id)

        super().__post_init__(**kwargs)


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


@dataclass(repr=False)
class TM(Item):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["TM"]
    class_class_curie: ClassVar[str] = "pokemon:TM"
    class_name: ClassVar[str] = "TM"
    class_model_uri: ClassVar[URIRef] = POKEMON.TM

    id: Union[str, TMId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TMId):
            self.id = TMId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Town(Place):
    """
    A town is a type of place that can be visited.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Town"]
    class_class_curie: ClassVar[str] = "pokemon:Town"
    class_name: ClassVar[str] = "Town"
    class_model_uri: ClassVar[URIRef] = POKEMON.Town

    id: Union[str, TownId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TownId):
            self.id = TownId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Colour(Thing):
    """
    Color or colour is the visual perceptual property corresponding in humans to the categories called red, yellow,
    blue and others.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DBPEDIA["Colour"]
    class_class_curie: ClassVar[str] = "dbpedia:Colour"
    class_name: ClassVar[str] = "Colour"
    class_model_uri: ClassVar[URIRef] = POKEMON.Colour

    id: Union[str, ColourId] = None
    black: Optional[float] = None
    cyanic: Optional[float] = None
    magenta: Optional[float] = None
    yellow: Optional[float] = None
    hue: Optional[float] = None
    saturation: Optional[float] = None
    value: Optional[float] = None
    red: Optional[int] = None
    green: Optional[int] = None
    blue: Optional[int] = None
    wavelength: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ColourId):
            self.id = ColourId(self.id)

        if self.black is not None and not isinstance(self.black, float):
            self.black = float(self.black)

        if self.cyanic is not None and not isinstance(self.cyanic, float):
            self.cyanic = float(self.cyanic)

        if self.magenta is not None and not isinstance(self.magenta, float):
            self.magenta = float(self.magenta)

        if self.yellow is not None and not isinstance(self.yellow, float):
            self.yellow = float(self.yellow)

        if self.hue is not None and not isinstance(self.hue, float):
            self.hue = float(self.hue)

        if self.saturation is not None and not isinstance(self.saturation, float):
            self.saturation = float(self.saturation)

        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        if self.red is not None and not isinstance(self.red, int):
            self.red = int(self.red)

        if self.green is not None and not isinstance(self.green, int):
            self.green = int(self.green)

        if self.blue is not None and not isinstance(self.blue, int):
            self.blue = int(self.blue)

        if self.wavelength is not None and not isinstance(self.wavelength, float):
            self.wavelength = float(self.wavelength)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NamedIndividual(Thing):
    """
    A Thing that requires a name
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL["NamedIndividual"]
    class_class_curie: ClassVar[str] = "owl:NamedIndividual"
    class_name: ClassVar[str] = "NamedIndividual"
    class_model_uri: ClassVar[URIRef] = POKEMON.NamedIndividual

    id: Union[str, NamedIndividualId] = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EggGroup(NamedIndividual):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["EggGroup"]
    class_class_curie: ClassVar[str] = "pokemon:EggGroup"
    class_name: ClassVar[str] = "EggGroup"
    class_model_uri: ClassVar[URIRef] = POKEMON.EggGroup

    id: Union[str, EggGroupId] = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EggGroupId):
            self.id = EggGroupId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Flavor(NamedIndividual):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Flavor"]
    class_class_curie: ClassVar[str] = "pokemon:Flavor"
    class_name: ClassVar[str] = "Flavor"
    class_model_uri: ClassVar[URIRef] = POKEMON.Flavor

    id: Union[str, FlavorId] = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FlavorId):
            self.id = FlavorId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Habitat(NamedIndividual):
    """
    A habitat is a type of environment that certain Pokemon belong to.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Habitat"]
    class_class_curie: ClassVar[str] = "pokemon:Habitat"
    class_name: ClassVar[str] = "Habitat"
    class_model_uri: ClassVar[URIRef] = POKEMON.Habitat

    id: Union[str, HabitatId] = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HabitatId):
            self.id = HabitatId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Shape(NamedIndividual):
    """
    Shapes are categories that certain Pokemon belong to, which determine which Pokemon they can breed with.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Shape"]
    class_class_curie: ClassVar[str] = "pokemon:Shape"
    class_name: ClassVar[str] = "Shape"
    class_model_uri: ClassVar[URIRef] = POKEMON.Shape

    id: Union[str, ShapeId] = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ShapeId):
            self.id = ShapeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Species(NamedIndividual):
    """
    A species is a category of Pokemon that share common features.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Species"]
    class_class_curie: ClassVar[str] = "pokemon:Species"
    class_name: ClassVar[str] = "Species"
    class_model_uri: ClassVar[URIRef] = POKEMON.Species

    id: Union[str, SpeciesId] = None
    name: str = None
    hasColour: Optional[Union[str, ColourId]] = None
    mayHaveHiddenAbility: Optional[Union[Union[str, AbilityId], list[Union[str, AbilityId]]]] = empty_list()
    mayHaveAbility: Optional[Union[Union[str, AbilityId], list[Union[str, AbilityId]]]] = empty_list()
    isAbleToApply: Optional[Union[Union[str, MoveId], list[Union[str, MoveId]]]] = empty_list()
    hasHeight: Optional[Union[dict, "Quantity"]] = None
    hasWeight: Optional[Union[dict, "Quantity"]] = None
    depiction: Optional[str] = None
    inEggGroup: Optional[Union[Union[str, EggGroupId], list[Union[str, EggGroupId]]]] = empty_list()
    hasType: Optional[Union[dict[Union[str, TypeId], Union[dict, "Type"]], list[Union[dict, "Type"]]]] = empty_dict()
    hasShape: Optional[Union[str, ShapeId]] = None
    hasGenus: Optional[str] = None
    hasCatchRate: Optional[int] = None
    foundIn: Optional[Union[Union[str, HabitatId], list[Union[str, HabitatId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpeciesId):
            self.id = SpeciesId(self.id)

        if self.hasColour is not None and not isinstance(self.hasColour, ColourId):
            self.hasColour = ColourId(self.hasColour)

        if not isinstance(self.mayHaveHiddenAbility, list):
            self.mayHaveHiddenAbility = [self.mayHaveHiddenAbility] if self.mayHaveHiddenAbility is not None else []
        self.mayHaveHiddenAbility = [v if isinstance(v, AbilityId) else AbilityId(v) for v in self.mayHaveHiddenAbility]

        if not isinstance(self.mayHaveAbility, list):
            self.mayHaveAbility = [self.mayHaveAbility] if self.mayHaveAbility is not None else []
        self.mayHaveAbility = [v if isinstance(v, AbilityId) else AbilityId(v) for v in self.mayHaveAbility]

        if not isinstance(self.isAbleToApply, list):
            self.isAbleToApply = [self.isAbleToApply] if self.isAbleToApply is not None else []
        self.isAbleToApply = [v if isinstance(v, MoveId) else MoveId(v) for v in self.isAbleToApply]

        if self.hasHeight is not None and not isinstance(self.hasHeight, Quantity):
            self.hasHeight = Quantity(**as_dict(self.hasHeight))

        if self.hasWeight is not None and not isinstance(self.hasWeight, Quantity):
            self.hasWeight = Quantity(**as_dict(self.hasWeight))

        if self.depiction is not None and not isinstance(self.depiction, str):
            self.depiction = str(self.depiction)

        if not isinstance(self.inEggGroup, list):
            self.inEggGroup = [self.inEggGroup] if self.inEggGroup is not None else []
        self.inEggGroup = [v if isinstance(v, EggGroupId) else EggGroupId(v) for v in self.inEggGroup]

        self._normalize_inlined_as_list(slot_name="hasType", slot_type=Type, key_name="id", keyed=True)

        if self.hasShape is not None and not isinstance(self.hasShape, ShapeId):
            self.hasShape = ShapeId(self.hasShape)

        if self.hasGenus is not None and not isinstance(self.hasGenus, str):
            self.hasGenus = str(self.hasGenus)

        if self.hasCatchRate is not None and not isinstance(self.hasCatchRate, int):
            self.hasCatchRate = int(self.hasCatchRate)

        if not isinstance(self.foundIn, list):
            self.foundIn = [self.foundIn] if self.foundIn is not None else []
        self.foundIn = [v if isinstance(v, HabitatId) else HabitatId(v) for v in self.foundIn]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Type(NamedIndividual):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Type"]
    class_class_curie: ClassVar[str] = "pokemon:Type"
    class_name: ClassVar[str] = "Type"
    class_model_uri: ClassVar[URIRef] = POKEMON.Type

    id: Union[str, TypeId] = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TypeId):
            self.id = TypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Person(NamedIndividual):
    """
    A person is a human being
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOAF["Person"]
    class_class_curie: ClassVar[str] = "foaf:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = POKEMON.Person

    id: Union[str, PersonId] = None
    name: str = None
    depiction: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self.depiction is not None and not isinstance(self.depiction, str):
            self.depiction = str(self.depiction)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Trainer(Person):
    """
    A trainer is a person who is able to catch Pokemon.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Trainer"]
    class_class_curie: ClassVar[str] = "pokemon:Trainer"
    class_name: ClassVar[str] = "Trainer"
    class_model_uri: ClassVar[URIRef] = POKEMON.Trainer

    id: Union[str, TrainerId] = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TrainerId):
            self.id = TrainerId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GymLeader(Trainer):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["GymLeader"]
    class_class_curie: ClassVar[str] = "pokemon:GymLeader"
    class_name: ClassVar[str] = "GymLeader"
    class_model_uri: ClassVar[URIRef] = POKEMON.GymLeader

    id: Union[str, GymLeaderId] = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GymLeaderId):
            self.id = GymLeaderId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Quantity(Thing):
    """
    A physical quantity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "Quantity"
    class_model_uri: ClassVar[URIRef] = POKEMON.Quantity

    id: Union[str, QuantityId] = None
    hasUnit: Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]] = empty_list()
    hasQuantityKind: Optional[Union[dict, "QuantityKind"]] = None
    hasValue: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, QuantityId):
            self.id = QuantityId(self.id)

        if not isinstance(self.hasUnit, list):
            self.hasUnit = [self.hasUnit] if self.hasUnit is not None else []
        self.hasUnit = [v if isinstance(v, UnitId) else UnitId(v) for v in self.hasUnit]

        if self.hasQuantityKind is not None and not isinstance(self.hasQuantityKind, QuantityKind):
            self.hasQuantityKind = QuantityKind()

        if self.hasValue is not None and not isinstance(self.hasValue, str):
            self.hasValue = str(self.hasValue)

        super().__post_init__(**kwargs)


class QuantityKind(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["QuantityKind"]
    class_class_curie: ClassVar[str] = "qudt:QuantityKind"
    class_name: ClassVar[str] = "QuantityKind"
    class_model_uri: ClassVar[URIRef] = POKEMON.QuantityKind


@dataclass(repr=False)
class Unit(Thing):
    """
    A unit of measure.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Unit"]
    class_class_curie: ClassVar[str] = "qudt:Unit"
    class_name: ClassVar[str] = "Unit"
    class_model_uri: ClassVar[URIRef] = POKEMON.Unit

    id: Union[str, UnitId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UnitId):
            self.id = UnitId(self.id)

        super().__post_init__(**kwargs)


# Enumerations
class HabitatEnum(EnumDefinitionImpl):

    Cave = PermissibleValue(
        text="Cave",
        meaning=POKEMON["Habitat_Cave"])
    Forest = PermissibleValue(
        text="Forest",
        meaning=POKEMON["Habitat_Forest"])
    Grassland = PermissibleValue(
        text="Grassland",
        meaning=POKEMON["Habitat_Grassland"])

    _defn = EnumDefinition(
        name="HabitatEnum",
    )

# Slots
class slots:
    pass

slots.effectDescription = Slot(uri=POKEMON.effectDescription, name="effectDescription", curie=POKEMON.curie('effectDescription'),
                   model_uri=POKEMON.effectDescription, domain=None, range=Optional[Union[str, list[str]]])

slots.containsPlace = Slot(uri=POKEMON.contains_place, name="containsPlace", curie=POKEMON.curie('contains_place'),
                   model_uri=POKEMON.containsPlace, domain=Place, range=Optional[Union[Union[str, PlaceId], list[Union[str, PlaceId]]]])

slots.describedInPokedex = Slot(uri=POKEMON.describedInPokedex, name="describedInPokedex", curie=POKEMON.curie('describedInPokedex'),
                   model_uri=POKEMON.describedInPokedex, domain=Species, range=Optional[Union[Union[str, PokedexEntryId], list[Union[str, PokedexEntryId]]]])

slots.describesPokemon = Slot(uri=POKEMON.describesPokemon, name="describesPokemon", curie=POKEMON.curie('describesPokemon'),
                   model_uri=POKEMON.describesPokemon, domain=PokedexEntry, range=Optional[Union[Union[str, SpeciesId], list[Union[str, SpeciesId]]]])

slots.featuresSpecies = Slot(uri=POKEMON.featuresSpecies, name="featuresSpecies", curie=POKEMON.curie('featuresSpecies'),
                   model_uri=POKEMON.featuresSpecies, domain=None, range=Optional[Union[Union[str, SpeciesId], list[Union[str, SpeciesId]]]])

slots.hasPokedexEntry = Slot(uri=POKEMON.hasPokedexEntry, name="hasPokedexEntry", curie=POKEMON.curie('hasPokedexEntry'),
                   model_uri=POKEMON.hasPokedexEntry, domain=Pokedex, range=Optional[Union[Union[str, PokedexEntryId], list[Union[str, PokedexEntryId]]]])

slots.evolvesFrom = Slot(uri=POKEMON.evolvesFrom, name="evolvesFrom", curie=POKEMON.curie('evolvesFrom'),
                   model_uri=POKEMON.evolvesFrom, domain=Species, range=Optional[Union[str, SpeciesId]])

slots.evolvesTo = Slot(uri=POKEMON.evolvesTo, name="evolvesTo", curie=POKEMON.curie('evolvesTo'),
                   model_uri=POKEMON.evolvesTo, domain=Species, range=Optional[Union[Union[str, SpeciesId], list[Union[str, SpeciesId]]]])

slots.foundIn = Slot(uri=POKEMON.foundIn, name="foundIn", curie=POKEMON.curie('foundIn'),
                   model_uri=POKEMON.foundIn, domain=Species, range=Optional[Union[Union[str, HabitatId], list[Union[str, HabitatId]]]])

slots.hasColour = Slot(uri=POKEMON.hasColour, name="hasColour", curie=POKEMON.curie('hasColour'),
                   model_uri=POKEMON.hasColour, domain=None, range=Optional[Union[str, ColourId]])

slots.hasFlavor = Slot(uri=POKEMON.hasFlavor, name="hasFlavor", curie=POKEMON.curie('hasFlavor'),
                   model_uri=POKEMON.hasFlavor, domain=Food, range=Optional[Union[Union[str, FlavorId], list[Union[str, FlavorId]]]])

slots.hasType = Slot(uri=POKEMON.hasType, name="hasType", curie=POKEMON.curie('hasType'),
                   model_uri=POKEMON.hasType, domain=None, range=Optional[Union[dict[Union[str, TypeId], Union[dict, Type]], list[Union[dict, Type]]]])

slots.hasSize = Slot(uri=POKEMON.hasSize, name="hasSize", curie=POKEMON.curie('hasSize'),
                   model_uri=POKEMON.hasSize, domain=None, range=Optional[str])

slots.hasHeight = Slot(uri=POKEMON.hasHeight, name="hasHeight", curie=POKEMON.curie('hasHeight'),
                   model_uri=POKEMON.hasHeight, domain=Species, range=Optional[Union[dict, "Quantity"]])

slots.hasWeight = Slot(uri=POKEMON.hasWeight, name="hasWeight", curie=POKEMON.curie('hasWeight'),
                   model_uri=POKEMON.hasWeight, domain=Species, range=Optional[Union[dict, "Quantity"]])

slots.hasCatchRate = Slot(uri=POKEMON.hasCatchRate, name="hasCatchRate", curie=POKEMON.curie('hasCatchRate'),
                   model_uri=POKEMON.hasCatchRate, domain=Species, range=Optional[int])

slots.hasShape = Slot(uri=POKEMON.hasShape, name="hasShape", curie=POKEMON.curie('hasShape'),
                   model_uri=POKEMON.hasShape, domain=Species, range=Optional[Union[str, ShapeId]])

slots.learnsMove = Slot(uri=POKEMON.learnsMove, name="learnsMove", curie=POKEMON.curie('learnsMove'),
                   model_uri=POKEMON.learnsMove, domain=MoveLearning, range=Optional[Union[Union[str, MoveId], list[Union[str, MoveId]]]])

slots.locatedIn = Slot(uri=POKEMON.locatedIn, name="locatedIn", curie=POKEMON.curie('locatedIn'),
                   model_uri=POKEMON.locatedIn, domain=Place, range=Optional[Union[Union[str, PlaceId], list[Union[str, PlaceId]]]])

slots.inEggGroup = Slot(uri=POKEMON.inEggGroup, name="inEggGroup", curie=POKEMON.curie('inEggGroup'),
                   model_uri=POKEMON.inEggGroup, domain=Species, range=Optional[Union[Union[str, EggGroupId], list[Union[str, EggGroupId]]]])

slots.mayHaveAbility = Slot(uri=POKEMON.mayHaveAbility, name="mayHaveAbility", curie=POKEMON.curie('mayHaveAbility'),
                   model_uri=POKEMON.mayHaveAbility, domain=Species, range=Optional[Union[Union[str, AbilityId], list[Union[str, AbilityId]]]])

slots.mayHaveHiddenAbility = Slot(uri=POKEMON.mayHaveHiddenAbility, name="mayHaveHiddenAbility", curie=POKEMON.curie('mayHaveHiddenAbility'),
                   model_uri=POKEMON.mayHaveHiddenAbility, domain=Species, range=Optional[Union[Union[str, AbilityId], list[Union[str, AbilityId]]]])

slots.isAbleToApply = Slot(uri=POKEMON.isAbleToApply, name="isAbleToApply", curie=POKEMON.curie('isAbleToApply'),
                   model_uri=POKEMON.isAbleToApply, domain=None, range=Optional[Union[Union[str, MoveId], list[Union[str, MoveId]]]])

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

slots.depiction = Slot(uri=FOAF.depiction, name="depiction", curie=FOAF.curie('depiction'),
                   model_uri=POKEMON.depiction, domain=None, range=Optional[str])

slots.black = Slot(uri=DBPEDIA.cmykCoordinateBlack, name="black", curie=DBPEDIA.curie('cmykCoordinateBlack'),
                   model_uri=POKEMON.black, domain=None, range=Optional[float])

slots.cyanic = Slot(uri=DBPEDIA.cmykCoordinateCyanic, name="cyanic", curie=DBPEDIA.curie('cmykCoordinateCyanic'),
                   model_uri=POKEMON.cyanic, domain=None, range=Optional[float])

slots.magenta = Slot(uri=DBPEDIA.cmykCoordinateMagenta, name="magenta", curie=DBPEDIA.curie('cmykCoordinateMagenta'),
                   model_uri=POKEMON.magenta, domain=None, range=Optional[float])

slots.yellow = Slot(uri=DBPEDIA.cmykCoordinateYellow, name="yellow", curie=DBPEDIA.curie('cmykCoordinateYellow'),
                   model_uri=POKEMON.yellow, domain=None, range=Optional[float])

slots.hue = Slot(uri=DBPEDIA.hsvCoordinateHue, name="hue", curie=DBPEDIA.curie('hsvCoordinateHue'),
                   model_uri=POKEMON.hue, domain=None, range=Optional[float])

slots.saturation = Slot(uri=DBPEDIA.hsvCoordinateSaturation, name="saturation", curie=DBPEDIA.curie('hsvCoordinateSaturation'),
                   model_uri=POKEMON.saturation, domain=None, range=Optional[float])

slots.value = Slot(uri=DBPEDIA.hsvCoordinateLightness, name="value", curie=DBPEDIA.curie('hsvCoordinateLightness'),
                   model_uri=POKEMON.value, domain=None, range=Optional[float])

slots.red = Slot(uri=DBPEDIA.rgbCoordinateRed, name="red", curie=DBPEDIA.curie('rgbCoordinateRed'),
                   model_uri=POKEMON.red, domain=None, range=Optional[int])

slots.green = Slot(uri=DBPEDIA.rgbCoordinateGreen, name="green", curie=DBPEDIA.curie('rgbCoordinateGreen'),
                   model_uri=POKEMON.green, domain=None, range=Optional[int])

slots.blue = Slot(uri=DBPEDIA.rgbCoordinateBlue, name="blue", curie=DBPEDIA.curie('rgbCoordinateBlue'),
                   model_uri=POKEMON.blue, domain=None, range=Optional[int])

slots.wavelength = Slot(uri=DBPEDIA.wavelength, name="wavelength", curie=DBPEDIA.curie('wavelength'),
                   model_uri=POKEMON.wavelength, domain=None, range=Optional[float])

slots.id = Slot(uri=LINKML_COMMON.identifier, name="id", curie=LINKML_COMMON.curie('identifier'),
                   model_uri=POKEMON.id, domain=None, range=URIRef)

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=POKEMON.name, domain=None, range=Optional[str])

slots.description = Slot(uri=RDFS.comment, name="description", curie=RDFS.curie('comment'),
                   model_uri=POKEMON.description, domain=None, range=Optional[str])

slots.hasQuantityKind = Slot(uri=QUDT.hasQuantityKind, name="hasQuantityKind", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=POKEMON.hasQuantityKind, domain=None, range=Optional[str])

slots.hasUnit = Slot(uri=QUDT.hasUnit, name="hasUnit", curie=QUDT.curie('hasUnit'),
                   model_uri=POKEMON.hasUnit, domain=None, range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]])

slots.hasValue = Slot(uri=QUDT.quantityValue, name="hasValue", curie=QUDT.curie('quantityValue'),
                   model_uri=POKEMON.hasValue, domain=None, range=Optional[str])

slots.NamedIndividual_name = Slot(uri=RDFS.label, name="NamedIndividual_name", curie=RDFS.curie('label'),
                   model_uri=POKEMON.NamedIndividual_name, domain=NamedIndividual, range=str)

slots.Quantity_hasQuantityKind = Slot(uri=QUDT.hasQuantityKind, name="Quantity_hasQuantityKind", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=POKEMON.Quantity_hasQuantityKind, domain=Quantity, range=Optional[Union[dict, "QuantityKind"]])
