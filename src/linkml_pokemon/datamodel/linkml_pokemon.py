# Auto generated from linkml_pokemon.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-01-15T18:42:47
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

from linkml_runtime.linkml_model.types import Boolean, Decimal, Double, Float, Integer, String, Uri
from linkml_runtime.utils.metamodelcore import Bool, Decimal, URI

metamodel_version = "1.7.0"
version = None

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
DBPEDIA = CurieNamespace('dbpedia', 'http://dbpedia.org/ontology/')
DC = CurieNamespace('dc', 'http://purl.org/dc/elements/1.1/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
DTYPE = CurieNamespace('dtype', 'http://www.linkedmodel.org/schema/dtype#')
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


class AspectId(ThingId):
    pass


class QuantifiableId(AspectId):
    pass


class QuantityId(QuantifiableId):
    pass


class PhysicalConstantId(QuantityId):
    pass


class ConceptId(ThingId):
    pass


class SystemOfQuantityKindsId(ConceptId):
    pass


class EncodingId(ConceptId):
    pass


class EnumerationId(ConceptId):
    pass


class AbstractQuantityKindId(ConceptId):
    pass


class QuantityValueId(QuantifiableId):
    pass


class DataEncodingId(AspectId):
    pass


class UCUMcsId(ThingId):
    pass


class DatatypeId(ConceptId):
    pass


class VerifiableId(AspectId):
    pass


class SystemOfUnitsId(VerifiableId):
    pass


class PrefixId(VerifiableId):
    pass


class EnumeratedValueId(VerifiableId):
    pass


class EndianTypeId(EnumeratedValueId):
    pass


class RuleTypeId(EnumeratedValueId):
    pass


class CardinalityTypeId(EnumeratedValueId):
    pass


class OrderedTypeId(EnumeratedValueId):
    pass


class UnitId(VerifiableId):
    pass


class QuantityKindId(VerifiableId):
    pass


class UCUMcs-termId(ThingId):
    pass


class QuantityKindDimensionVectorId(ConceptId):
    pass


class QuantityKindDimensionVectorSIId(QuantityKindDimensionVectorId):
    pass


class RuleId(VerifiableId):
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
class Aspect(Thing):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Aspect"]
    class_class_curie: ClassVar[str] = "qudt:Aspect"
    class_name: ClassVar[str] = "Aspect"
    class_model_uri: ClassVar[URIRef] = POKEMON.Aspect

    id: Union[str, AspectId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AspectId):
            self.id = AspectId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Quantifiable(Aspect):
    """
    <p><em>Quantifiable</em> ascribes to some thing the capability of being measured, observed, or counted.</p>
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantifiable"]
    class_class_curie: ClassVar[str] = "qudt:Quantifiable"
    class_name: ClassVar[str] = "Quantifiable"
    class_model_uri: ClassVar[URIRef] = POKEMON.Quantifiable

    id: Union[str, QuantifiableId] = None
    dataEncoding: Optional[Union[Union[str, DataEncodingId], list[Union[str, DataEncodingId]]]] = empty_list()
    datatype: Optional[Union[Union[str, DatatypeId], list[Union[str, DatatypeId]]]] = empty_list()
    hasUnit: Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]] = empty_list()
    relativeStandardUncertainty: Optional[Union[float, list[float]]] = empty_list()
    standardUncertainty: Optional[Union[Decimal, list[Decimal]]] = empty_list()
    standardUncertaintySN: Optional[Union[float, list[float]]] = empty_list()
    qudt_value: Optional[Union[str, list[str]]] = empty_list()
    valueSN: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, QuantifiableId):
            self.id = QuantifiableId(self.id)

        if not isinstance(self.dataEncoding, list):
            self.dataEncoding = [self.dataEncoding] if self.dataEncoding is not None else []
        self.dataEncoding = [v if isinstance(v, DataEncodingId) else DataEncodingId(v) for v in self.dataEncoding]

        if not isinstance(self.datatype, list):
            self.datatype = [self.datatype] if self.datatype is not None else []
        self.datatype = [v if isinstance(v, DatatypeId) else DatatypeId(v) for v in self.datatype]

        if not isinstance(self.hasUnit, list):
            self.hasUnit = [self.hasUnit] if self.hasUnit is not None else []
        self.hasUnit = [v if isinstance(v, UnitId) else UnitId(v) for v in self.hasUnit]

        if not isinstance(self.relativeStandardUncertainty, list):
            self.relativeStandardUncertainty = [self.relativeStandardUncertainty] if self.relativeStandardUncertainty is not None else []
        self.relativeStandardUncertainty = [v if isinstance(v, float) else float(v) for v in self.relativeStandardUncertainty]

        if not isinstance(self.standardUncertainty, list):
            self.standardUncertainty = [self.standardUncertainty] if self.standardUncertainty is not None else []
        self.standardUncertainty = [v if isinstance(v, Decimal) else Decimal(v) for v in self.standardUncertainty]

        if not isinstance(self.standardUncertaintySN, list):
            self.standardUncertaintySN = [self.standardUncertaintySN] if self.standardUncertaintySN is not None else []
        self.standardUncertaintySN = [v if isinstance(v, float) else float(v) for v in self.standardUncertaintySN]

        if not isinstance(self.qudt_value, list):
            self.qudt_value = [self.qudt_value] if self.qudt_value is not None else []
        self.qudt_value = [v if isinstance(v, str) else str(v) for v in self.qudt_value]

        if not isinstance(self.valueSN, list):
            self.valueSN = [self.valueSN] if self.valueSN is not None else []
        self.valueSN = [v if isinstance(v, str) else str(v) for v in self.valueSN]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Quantity(Quantifiable):
    """
    <p class="lm-para">A <b>quantity</b> is the measurement of an observable property of a particular object, event,
    or physical system.
    A quantity is always associated with the context of measurement (i.e. the thing measured, the measured value, the
    accuracy of measurement, etc.) whereas the
    underlying <b>quantity kind</b> is independent of any particular measurement. Thus, length is a quantity kind
    while the height of a rocket is a specific
    quantity of length; its magnitude that may be expressed in meters, feet, inches, etc. Examples of physical
    quantities include physical constants, such as
    the speed of light in a vacuum, Planck's constant, the electric permittivity of free space, and the fine structure
    constant. </p>
    <p class="lm-para">In other words, quantities are quantifiable aspects of the world, such as the duration of a
    movie, the distance between two points,
    velocity of a car, the pressure of the atmosphere, and a person's weight; and units are used to describe their
    numerical measure.</p>
    <p class="lm-para">Many <b>quantity kinds</b> are related to each other by various physical laws, and as a result,
    the associated units of some quantity
    kinds can be expressed as products (or ratios) of powers of other quantity kinds (e.g., momentum is mass times
    velocity and velocity is defined as distance
    divided by time). In this way, some quantities can be calculated from other measured quantities using their
    associations to the quantity kinds in these
    expressions. These quantity kind relationships are also discussed in dimensional analysis. Those that cannot be so
    expressed can be regarded
    as "fundamental" in this sense.</p>
    <p class="lm-para">A quantity is distinguished from a "quantity kind" in that the former carries a value and the
    latter is a type specifier.</p>
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "Quantity"
    class_model_uri: ClassVar[URIRef] = POKEMON.Quantity

    id: Union[str, QuantityId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    hasQuantityKind: Optional[Union[Union[str, QuantityKindId], list[Union[str, QuantityKindId]]]] = empty_list()
    quantityValue: Optional[Union[Union[str, QuantityValueId], list[Union[str, QuantityValueId]]]] = empty_list()
    isDeltaQuantity: Optional[Union[Union[bool, Bool], list[Union[bool, Bool]]]] = empty_list()
    guidance: Optional[Union[str, list[str]]] = empty_list()
    qudt_id: Optional[Union[str, list[str]]] = empty_list()
    hasRule: Optional[Union[Union[str, RuleId], list[Union[str, RuleId]]]] = empty_list()
    isReplacedBy: Optional[Union[str, list[str]]] = empty_list()
    qudt_description: Optional[Union[str, list[str]]] = empty_list()
    abbreviation: Optional[Union[str, list[str]]] = empty_list()
    deprecated: Optional[Union[str, list[str]]] = empty_list()
    plainTextDescription: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, QuantityId):
            self.id = QuantityId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.hasQuantityKind, list):
            self.hasQuantityKind = [self.hasQuantityKind] if self.hasQuantityKind is not None else []
        self.hasQuantityKind = [v if isinstance(v, QuantityKindId) else QuantityKindId(v) for v in self.hasQuantityKind]

        if not isinstance(self.quantityValue, list):
            self.quantityValue = [self.quantityValue] if self.quantityValue is not None else []
        self.quantityValue = [v if isinstance(v, QuantityValueId) else QuantityValueId(v) for v in self.quantityValue]

        if not isinstance(self.isDeltaQuantity, list):
            self.isDeltaQuantity = [self.isDeltaQuantity] if self.isDeltaQuantity is not None else []
        self.isDeltaQuantity = [v if isinstance(v, Bool) else Bool(v) for v in self.isDeltaQuantity]

        if not isinstance(self.guidance, list):
            self.guidance = [self.guidance] if self.guidance is not None else []
        self.guidance = [v if isinstance(v, str) else str(v) for v in self.guidance]

        if not isinstance(self.qudt_id, list):
            self.qudt_id = [self.qudt_id] if self.qudt_id is not None else []
        self.qudt_id = [v if isinstance(v, str) else str(v) for v in self.qudt_id]

        if not isinstance(self.hasRule, list):
            self.hasRule = [self.hasRule] if self.hasRule is not None else []
        self.hasRule = [v if isinstance(v, RuleId) else RuleId(v) for v in self.hasRule]

        if not isinstance(self.isReplacedBy, list):
            self.isReplacedBy = [self.isReplacedBy] if self.isReplacedBy is not None else []
        self.isReplacedBy = [v if isinstance(v, str) else str(v) for v in self.isReplacedBy]

        if not isinstance(self.qudt_description, list):
            self.qudt_description = [self.qudt_description] if self.qudt_description is not None else []
        self.qudt_description = [v if isinstance(v, str) else str(v) for v in self.qudt_description]

        if not isinstance(self.abbreviation, list):
            self.abbreviation = [self.abbreviation] if self.abbreviation is not None else []
        self.abbreviation = [v if isinstance(v, str) else str(v) for v in self.abbreviation]

        if not isinstance(self.deprecated, list):
            self.deprecated = [self.deprecated] if self.deprecated is not None else []
        self.deprecated = [v if isinstance(v, str) else str(v) for v in self.deprecated]

        if not isinstance(self.plainTextDescription, list):
            self.plainTextDescription = [self.plainTextDescription] if self.plainTextDescription is not None else []
        self.plainTextDescription = [v if isinstance(v, str) else str(v) for v in self.plainTextDescription]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhysicalConstant(Quantity):
    """
    A physical constant is a physical quantity that is generally believed to be both universal in nature and constant
    in time. It can be contrasted with a mathematical constant, which is a fixed numerical value but does not directly
    involve any physical measurement. There are many physical constants in science, some of the most widely recognized
    being the speed of light in vacuum c, Newton's gravitational constant G, Planck's constant h, the electric
    permittivity of free space ε0, and the elementary charge e. Physical constants can take many dimensional forms, or
    may be dimensionless depending on the system of quantities and units used.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["PhysicalConstant"]
    class_class_curie: ClassVar[str] = "qudt:PhysicalConstant"
    class_name: ClassVar[str] = "PhysicalConstant"
    class_model_uri: ClassVar[URIRef] = POKEMON.PhysicalConstant

    id: Union[str, PhysicalConstantId] = None
    applicableSystem: Optional[Union[Union[str, SystemOfUnitsId], list[Union[str, SystemOfUnitsId]]]] = empty_list()
    applicableUnit: Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]] = empty_list()
    exactMatch: Optional[Union[Union[str, PhysicalConstantId], list[Union[str, PhysicalConstantId]]]] = empty_list()
    hasDimensionVector: Optional[Union[Union[str, QuantityKindDimensionVectorId], list[Union[str, QuantityKindDimensionVectorId]]]] = empty_list()
    ucumCode: Optional[Union[str, list[str]]] = empty_list()
    exactConstant: Optional[Union[Union[bool, Bool], list[Union[bool, Bool]]]] = empty_list()
    altSymbol: Optional[Union[str, list[str]]] = empty_list()
    isoNormativeReference: Optional[Union[str, list[str]]] = empty_list()
    latexSymbol: Optional[Union[str, list[str]]] = empty_list()
    normativeReference: Optional[Union[str, list[str]]] = empty_list()
    symbol: Optional[Union[str, list[str]]] = empty_list()
    latexDefinition: Optional[Union[str, list[str]]] = empty_list()
    mathMLdefinition: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhysicalConstantId):
            self.id = PhysicalConstantId(self.id)

        if not isinstance(self.applicableSystem, list):
            self.applicableSystem = [self.applicableSystem] if self.applicableSystem is not None else []
        self.applicableSystem = [v if isinstance(v, SystemOfUnitsId) else SystemOfUnitsId(v) for v in self.applicableSystem]

        if not isinstance(self.applicableUnit, list):
            self.applicableUnit = [self.applicableUnit] if self.applicableUnit is not None else []
        self.applicableUnit = [v if isinstance(v, UnitId) else UnitId(v) for v in self.applicableUnit]

        if not isinstance(self.exactMatch, list):
            self.exactMatch = [self.exactMatch] if self.exactMatch is not None else []
        self.exactMatch = [v if isinstance(v, PhysicalConstantId) else PhysicalConstantId(v) for v in self.exactMatch]

        if not isinstance(self.hasDimensionVector, list):
            self.hasDimensionVector = [self.hasDimensionVector] if self.hasDimensionVector is not None else []
        self.hasDimensionVector = [v if isinstance(v, QuantityKindDimensionVectorId) else QuantityKindDimensionVectorId(v) for v in self.hasDimensionVector]

        if not isinstance(self.ucumCode, list):
            self.ucumCode = [self.ucumCode] if self.ucumCode is not None else []
        self.ucumCode = [v if isinstance(v, str) else str(v) for v in self.ucumCode]

        if not isinstance(self.exactConstant, list):
            self.exactConstant = [self.exactConstant] if self.exactConstant is not None else []
        self.exactConstant = [v if isinstance(v, Bool) else Bool(v) for v in self.exactConstant]

        if not isinstance(self.altSymbol, list):
            self.altSymbol = [self.altSymbol] if self.altSymbol is not None else []
        self.altSymbol = [v if isinstance(v, str) else str(v) for v in self.altSymbol]

        if not isinstance(self.isoNormativeReference, list):
            self.isoNormativeReference = [self.isoNormativeReference] if self.isoNormativeReference is not None else []
        self.isoNormativeReference = [v if isinstance(v, str) else str(v) for v in self.isoNormativeReference]

        if not isinstance(self.latexSymbol, list):
            self.latexSymbol = [self.latexSymbol] if self.latexSymbol is not None else []
        self.latexSymbol = [v if isinstance(v, str) else str(v) for v in self.latexSymbol]

        if not isinstance(self.normativeReference, list):
            self.normativeReference = [self.normativeReference] if self.normativeReference is not None else []
        self.normativeReference = [v if isinstance(v, str) else str(v) for v in self.normativeReference]

        if not isinstance(self.symbol, list):
            self.symbol = [self.symbol] if self.symbol is not None else []
        self.symbol = [v if isinstance(v, str) else str(v) for v in self.symbol]

        if not isinstance(self.latexDefinition, list):
            self.latexDefinition = [self.latexDefinition] if self.latexDefinition is not None else []
        self.latexDefinition = [v if isinstance(v, str) else str(v) for v in self.latexDefinition]

        if not isinstance(self.mathMLdefinition, list):
            self.mathMLdefinition = [self.mathMLdefinition] if self.mathMLdefinition is not None else []
        self.mathMLdefinition = [v if isinstance(v, str) else str(v) for v in self.mathMLdefinition]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Concept(Thing):
    """
    The root class for all QUDT concepts.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Concept"]
    class_class_curie: ClassVar[str] = "qudt:Concept"
    class_name: ClassVar[str] = "Concept"
    class_model_uri: ClassVar[URIRef] = POKEMON.Concept

    id: Union[str, ConceptId] = None
    guidance: Optional[Union[str, list[str]]] = empty_list()
    qudt_id: Optional[Union[str, list[str]]] = empty_list()
    hasRule: Optional[Union[Union[str, RuleId], list[Union[str, RuleId]]]] = empty_list()
    isReplacedBy: Optional[Union[str, list[str]]] = empty_list()
    qudt_description: Optional[Union[str, list[str]]] = empty_list()
    abbreviation: Optional[Union[str, list[str]]] = empty_list()
    deprecated: Optional[Union[str, list[str]]] = empty_list()
    plainTextDescription: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConceptId):
            self.id = ConceptId(self.id)

        if not isinstance(self.guidance, list):
            self.guidance = [self.guidance] if self.guidance is not None else []
        self.guidance = [v if isinstance(v, str) else str(v) for v in self.guidance]

        if not isinstance(self.qudt_id, list):
            self.qudt_id = [self.qudt_id] if self.qudt_id is not None else []
        self.qudt_id = [v if isinstance(v, str) else str(v) for v in self.qudt_id]

        if not isinstance(self.hasRule, list):
            self.hasRule = [self.hasRule] if self.hasRule is not None else []
        self.hasRule = [v if isinstance(v, RuleId) else RuleId(v) for v in self.hasRule]

        if not isinstance(self.isReplacedBy, list):
            self.isReplacedBy = [self.isReplacedBy] if self.isReplacedBy is not None else []
        self.isReplacedBy = [v if isinstance(v, str) else str(v) for v in self.isReplacedBy]

        if not isinstance(self.qudt_description, list):
            self.qudt_description = [self.qudt_description] if self.qudt_description is not None else []
        self.qudt_description = [v if isinstance(v, str) else str(v) for v in self.qudt_description]

        if not isinstance(self.abbreviation, list):
            self.abbreviation = [self.abbreviation] if self.abbreviation is not None else []
        self.abbreviation = [v if isinstance(v, str) else str(v) for v in self.abbreviation]

        if not isinstance(self.deprecated, list):
            self.deprecated = [self.deprecated] if self.deprecated is not None else []
        self.deprecated = [v if isinstance(v, str) else str(v) for v in self.deprecated]

        if not isinstance(self.plainTextDescription, list):
            self.plainTextDescription = [self.plainTextDescription] if self.plainTextDescription is not None else []
        self.plainTextDescription = [v if isinstance(v, str) else str(v) for v in self.plainTextDescription]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SystemOfQuantityKinds(Concept):
    """
    A system of quantity kinds is a set of one or more quantity kinds together with a set of zero or more algebraic
    equations that define relationships between quantity kinds in the set. In the physical sciences, the equations
    relating quantity kinds are typically physical laws and definitional relations, and constants of proportionality.
    Examples include Newton’s First Law of Motion, Coulomb’s Law, and the definition of velocity as the instantaneous
    change in position. In almost all cases, the system identifies a subset of base quantity kinds. The base set is
    chosen so that all other quantity kinds of interest can be derived from the base quantity kinds and the algebraic
    equations. If the unit system is explicitly associated with a quantity kind system, then the unit system must
    define at least one unit for each quantity kind. From a scientific point of view, the division of quantities into
    base quantities and derived quantities is a matter of convention.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["SystemOfQuantityKinds"]
    class_class_curie: ClassVar[str] = "qudt:SystemOfQuantityKinds"
    class_name: ClassVar[str] = "SystemOfQuantityKinds"
    class_model_uri: ClassVar[URIRef] = POKEMON.SystemOfQuantityKinds

    id: Union[str, SystemOfQuantityKindsId] = None
    baseDimensionEnumeration: Optional[Union[Union[str, EnumerationId], list[Union[str, EnumerationId]]]] = empty_list()
    hasBaseQuantityKind: Optional[Union[Union[str, QuantityKindId], list[Union[str, QuantityKindId]]]] = empty_list()
    hasQuantityKind: Optional[Union[Union[str, QuantityKindId], list[Union[str, QuantityKindId]]]] = empty_list()
    hasUnitSystem: Optional[Union[Union[str, SystemOfUnitsId], list[Union[str, SystemOfUnitsId]]]] = empty_list()
    systemDerivedQuantityKind: Optional[Union[Union[str, QuantityKindId], list[Union[str, QuantityKindId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SystemOfQuantityKindsId):
            self.id = SystemOfQuantityKindsId(self.id)

        if not isinstance(self.baseDimensionEnumeration, list):
            self.baseDimensionEnumeration = [self.baseDimensionEnumeration] if self.baseDimensionEnumeration is not None else []
        self.baseDimensionEnumeration = [v if isinstance(v, EnumerationId) else EnumerationId(v) for v in self.baseDimensionEnumeration]

        if not isinstance(self.hasBaseQuantityKind, list):
            self.hasBaseQuantityKind = [self.hasBaseQuantityKind] if self.hasBaseQuantityKind is not None else []
        self.hasBaseQuantityKind = [v if isinstance(v, QuantityKindId) else QuantityKindId(v) for v in self.hasBaseQuantityKind]

        if not isinstance(self.hasQuantityKind, list):
            self.hasQuantityKind = [self.hasQuantityKind] if self.hasQuantityKind is not None else []
        self.hasQuantityKind = [v if isinstance(v, QuantityKindId) else QuantityKindId(v) for v in self.hasQuantityKind]

        if not isinstance(self.hasUnitSystem, list):
            self.hasUnitSystem = [self.hasUnitSystem] if self.hasUnitSystem is not None else []
        self.hasUnitSystem = [v if isinstance(v, SystemOfUnitsId) else SystemOfUnitsId(v) for v in self.hasUnitSystem]

        if not isinstance(self.systemDerivedQuantityKind, list):
            self.systemDerivedQuantityKind = [self.systemDerivedQuantityKind] if self.systemDerivedQuantityKind is not None else []
        self.systemDerivedQuantityKind = [v if isinstance(v, QuantityKindId) else QuantityKindId(v) for v in self.systemDerivedQuantityKind]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Encoding(Concept):
    """
    An encoding is a rule or algorithm that is used to convert data from a native, or unspecified form into a specific
    form that satisfies the encoding rules. Examples of encodings include character encodings, such as UTF-8.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Encoding"]
    class_class_curie: ClassVar[str] = "qudt:Encoding"
    class_name: ClassVar[str] = "Encoding"
    class_model_uri: ClassVar[URIRef] = POKEMON.Encoding

    id: Union[str, EncodingId] = None
    bits: Optional[Union[str, list[str]]] = empty_list()
    bytes: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EncodingId):
            self.id = EncodingId(self.id)

        if not isinstance(self.bits, list):
            self.bits = [self.bits] if self.bits is not None else []
        self.bits = [v if isinstance(v, str) else str(v) for v in self.bits]

        if not isinstance(self.bytes, list):
            self.bytes = [self.bytes] if self.bytes is not None else []
        self.bytes = [v if isinstance(v, str) else str(v) for v in self.bytes]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Enumeration(Concept):
    """
    <p>An enumeration is a set of literals from which a single value is selected. Each literal can have a tag as an
    integer within a standard encoding appropriate to the range of integer values. Consistency of enumeration types
    will allow them, and the enumerated values, to be referred to unambiguously either through symbolic name or
    encoding. Enumerated values are also controlled vocabularies and as such need to be standardized. Without this
    consistency enumeration literals can be stated differently and result in data conflicts and
    misinterpretations.</p>

    <p>The tags are a set of positive whole numbers, not necessarily contiguous and having no numerical significance,
    each corresponding to the associated literal identifier. An order attribute can also be given on the enumeration
    elements. An enumeration can itself be a member of an enumeration. This allows enumerations to be enumerated in a
    selection. Enumerations are also subclasses of <em>Scalar Datatype</em>. This allows them to be used as the
    reference of a datatype specification.</p>
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Enumeration"]
    class_class_curie: ClassVar[str] = "qudt:Enumeration"
    class_name: ClassVar[str] = "Enumeration"
    class_model_uri: ClassVar[URIRef] = POKEMON.Enumeration

    id: Union[str, EnumerationId] = None
    element: Union[Union[str, EnumeratedValueId], list[Union[str, EnumeratedValueId]]] = None
    default: Optional[Union[Union[str, EnumeratedValueId], list[Union[str, EnumeratedValueId]]]] = empty_list()
    abbreviation: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnumerationId):
            self.id = EnumerationId(self.id)

        if self._is_empty(self.element):
            self.MissingRequiredField("element")
        if not isinstance(self.element, list):
            self.element = [self.element] if self.element is not None else []
        self.element = [v if isinstance(v, EnumeratedValueId) else EnumeratedValueId(v) for v in self.element]

        if not isinstance(self.default, list):
            self.default = [self.default] if self.default is not None else []
        self.default = [v if isinstance(v, EnumeratedValueId) else EnumeratedValueId(v) for v in self.default]

        if not isinstance(self.abbreviation, list):
            self.abbreviation = [self.abbreviation] if self.abbreviation is not None else []
        self.abbreviation = [v if isinstance(v, str) else str(v) for v in self.abbreviation]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AbstractQuantityKind(Concept):
    """
    Quantity Kind (abstract)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["AbstractQuantityKind"]
    class_class_curie: ClassVar[str] = "qudt:AbstractQuantityKind"
    class_name: ClassVar[str] = "AbstractQuantityKind"
    class_model_uri: ClassVar[URIRef] = POKEMON.AbstractQuantityKind

    id: Union[str, AbstractQuantityKindId] = None
    broader: Optional[Union[str, QuantityKindId]] = None
    altSymbol: Optional[Union[str, list[str]]] = empty_list()
    latexSymbol: Optional[Union[str, list[str]]] = empty_list()
    symbol: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AbstractQuantityKindId):
            self.id = AbstractQuantityKindId(self.id)

        if self.broader is not None and not isinstance(self.broader, QuantityKindId):
            self.broader = QuantityKindId(self.broader)

        if not isinstance(self.altSymbol, list):
            self.altSymbol = [self.altSymbol] if self.altSymbol is not None else []
        self.altSymbol = [v if isinstance(v, str) else str(v) for v in self.altSymbol]

        if not isinstance(self.latexSymbol, list):
            self.latexSymbol = [self.latexSymbol] if self.latexSymbol is not None else []
        self.latexSymbol = [v if isinstance(v, str) else str(v) for v in self.latexSymbol]

        if not isinstance(self.symbol, list):
            self.symbol = [self.symbol] if self.symbol is not None else []
        self.symbol = [v if isinstance(v, str) else str(v) for v in self.symbol]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantityValue(Quantifiable):
    """
    A <i>Quantity Value</i> expresses the magnitude and kind of a quantity and is given by the product of a numerical
    value <code>n</code> and a unit of measure <code>U</code>. The number multiplying the unit is referred to as the
    numerical value of the quantity expressed in that unit. Refer to <a
    href="http://physics.nist.gov/Pubs/SP811/sec07.html">NIST SP 811 section 7</a> for more on quantity values.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["QuantityValue"]
    class_class_curie: ClassVar[str] = "qudt:QuantityValue"
    class_name: ClassVar[str] = "QuantityValue"
    class_model_uri: ClassVar[URIRef] = POKEMON.QuantityValue

    id: Union[str, QuantityValueId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    hasUnit: Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]] = empty_list()
    guidance: Optional[Union[str, list[str]]] = empty_list()
    qudt_id: Optional[Union[str, list[str]]] = empty_list()
    hasRule: Optional[Union[Union[str, RuleId], list[Union[str, RuleId]]]] = empty_list()
    isReplacedBy: Optional[Union[str, list[str]]] = empty_list()
    qudt_description: Optional[Union[str, list[str]]] = empty_list()
    abbreviation: Optional[Union[str, list[str]]] = empty_list()
    deprecated: Optional[Union[str, list[str]]] = empty_list()
    plainTextDescription: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, QuantityValueId):
            self.id = QuantityValueId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.hasUnit, list):
            self.hasUnit = [self.hasUnit] if self.hasUnit is not None else []
        self.hasUnit = [v if isinstance(v, UnitId) else UnitId(v) for v in self.hasUnit]

        if not isinstance(self.guidance, list):
            self.guidance = [self.guidance] if self.guidance is not None else []
        self.guidance = [v if isinstance(v, str) else str(v) for v in self.guidance]

        if not isinstance(self.qudt_id, list):
            self.qudt_id = [self.qudt_id] if self.qudt_id is not None else []
        self.qudt_id = [v if isinstance(v, str) else str(v) for v in self.qudt_id]

        if not isinstance(self.hasRule, list):
            self.hasRule = [self.hasRule] if self.hasRule is not None else []
        self.hasRule = [v if isinstance(v, RuleId) else RuleId(v) for v in self.hasRule]

        if not isinstance(self.isReplacedBy, list):
            self.isReplacedBy = [self.isReplacedBy] if self.isReplacedBy is not None else []
        self.isReplacedBy = [v if isinstance(v, str) else str(v) for v in self.isReplacedBy]

        if not isinstance(self.qudt_description, list):
            self.qudt_description = [self.qudt_description] if self.qudt_description is not None else []
        self.qudt_description = [v if isinstance(v, str) else str(v) for v in self.qudt_description]

        if not isinstance(self.abbreviation, list):
            self.abbreviation = [self.abbreviation] if self.abbreviation is not None else []
        self.abbreviation = [v if isinstance(v, str) else str(v) for v in self.abbreviation]

        if not isinstance(self.deprecated, list):
            self.deprecated = [self.deprecated] if self.deprecated is not None else []
        self.deprecated = [v if isinstance(v, str) else str(v) for v in self.deprecated]

        if not isinstance(self.plainTextDescription, list):
            self.plainTextDescription = [self.plainTextDescription] if self.plainTextDescription is not None else []
        self.plainTextDescription = [v if isinstance(v, str) else str(v) for v in self.plainTextDescription]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataEncoding(Aspect):
    """
    <p><em>Data Encoding</em> expresses the properties that specify how data is represented at the bit and byte level.
    These properties are applicable to describing raw data.</p>
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["DataEncoding"]
    class_class_curie: ClassVar[str] = "qudt:DataEncoding"
    class_name: ClassVar[str] = "DataEncoding"
    class_model_uri: ClassVar[URIRef] = POKEMON.DataEncoding

    id: Union[str, DataEncodingId] = None
    bitOrder: Optional[Union[Union[str, EndianTypeId], list[Union[str, EndianTypeId]]]] = empty_list()
    encoding: Optional[Union[Union[str, EncodingId], list[Union[str, EncodingId]]]] = empty_list()
    byteOrder: Optional[Union[Union[str, EndianTypeId], list[Union[str, EndianTypeId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataEncodingId):
            self.id = DataEncodingId(self.id)

        if not isinstance(self.bitOrder, list):
            self.bitOrder = [self.bitOrder] if self.bitOrder is not None else []
        self.bitOrder = [v if isinstance(v, EndianTypeId) else EndianTypeId(v) for v in self.bitOrder]

        if not isinstance(self.encoding, list):
            self.encoding = [self.encoding] if self.encoding is not None else []
        self.encoding = [v if isinstance(v, EncodingId) else EncodingId(v) for v in self.encoding]

        if not isinstance(self.byteOrder, list):
            self.byteOrder = [self.byteOrder] if self.byteOrder is not None else []
        self.byteOrder = [v if isinstance(v, EndianTypeId) else EndianTypeId(v) for v in self.byteOrder]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UCUMcs(Thing):
    """
    Lexical pattern for the case-sensitive version of UCUM code
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["UCUMcs"]
    class_class_curie: ClassVar[str] = "qudt:UCUMcs"
    class_name: ClassVar[str] = "UCUMcs"
    class_model_uri: ClassVar[URIRef] = POKEMON.UCUMcs

    id: Union[str, UCUMcsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UCUMcsId):
            self.id = UCUMcsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Datatype(Concept):
    """
    <p>A <em>Datatype</em> is a definition of the type of the "value" of a data item (for example, "all integers
    between 0 and 10"),
    and the allowable operations on those values; the meaning of the data; and the way values of that type can be
    stored.
    Some types are primitive - built-in to the language, with no visible internal structure.
    For example "Boolean"; others are composite - constructed from one or more other types (of either kind).
    For example lists, arrays, structures, unions.
    Some languages provide strong typing, others allow implicit type conversion and/or explicit type conversion.
    </p>
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RDFS["Datatype"]
    class_class_curie: ClassVar[str] = "rdfs:Datatype"
    class_name: ClassVar[str] = "Datatype"
    class_model_uri: ClassVar[URIRef] = POKEMON.Datatype

    id: Union[str, DatatypeId] = None
    basis: Optional[Union[Union[str, DatatypeId], list[Union[str, DatatypeId]]]] = empty_list()
    cardinality: Optional[Union[Union[str, CardinalityTypeId], list[Union[str, CardinalityTypeId]]]] = empty_list()
    orderedType: Optional[Union[Union[str, OrderedTypeId], list[Union[str, OrderedTypeId]]]] = empty_list()
    ansiSQLName: Optional[Union[str, list[str]]] = empty_list()
    cName: Optional[Union[str, list[str]]] = empty_list()
    oracleSQLName: Optional[Union[str, list[str]]] = empty_list()
    protocolBuffersName: Optional[Union[str, list[str]]] = empty_list()
    pythonName: Optional[Union[str, list[str]]] = empty_list()
    vbName: Optional[Union[str, list[str]]] = empty_list()
    bounded: Optional[Union[str, list[str]]] = empty_list()
    qudt_id: Optional[Union[str, list[str]]] = empty_list()
    javaName: Optional[Union[str, list[str]]] = empty_list()
    jsName: Optional[Union[str, list[str]]] = empty_list()
    matlabName: Optional[Union[str, list[str]]] = empty_list()
    microsoftSQLServerName: Optional[Union[str, list[str]]] = empty_list()
    mySQLName: Optional[Union[str, list[str]]] = empty_list()
    odbcName: Optional[Union[str, list[str]]] = empty_list()
    oleDBName: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatatypeId):
            self.id = DatatypeId(self.id)

        if not isinstance(self.basis, list):
            self.basis = [self.basis] if self.basis is not None else []
        self.basis = [v if isinstance(v, DatatypeId) else DatatypeId(v) for v in self.basis]

        if not isinstance(self.cardinality, list):
            self.cardinality = [self.cardinality] if self.cardinality is not None else []
        self.cardinality = [v if isinstance(v, CardinalityTypeId) else CardinalityTypeId(v) for v in self.cardinality]

        if not isinstance(self.orderedType, list):
            self.orderedType = [self.orderedType] if self.orderedType is not None else []
        self.orderedType = [v if isinstance(v, OrderedTypeId) else OrderedTypeId(v) for v in self.orderedType]

        if not isinstance(self.ansiSQLName, list):
            self.ansiSQLName = [self.ansiSQLName] if self.ansiSQLName is not None else []
        self.ansiSQLName = [v if isinstance(v, str) else str(v) for v in self.ansiSQLName]

        if not isinstance(self.cName, list):
            self.cName = [self.cName] if self.cName is not None else []
        self.cName = [v if isinstance(v, str) else str(v) for v in self.cName]

        if not isinstance(self.oracleSQLName, list):
            self.oracleSQLName = [self.oracleSQLName] if self.oracleSQLName is not None else []
        self.oracleSQLName = [v if isinstance(v, str) else str(v) for v in self.oracleSQLName]

        if not isinstance(self.protocolBuffersName, list):
            self.protocolBuffersName = [self.protocolBuffersName] if self.protocolBuffersName is not None else []
        self.protocolBuffersName = [v if isinstance(v, str) else str(v) for v in self.protocolBuffersName]

        if not isinstance(self.pythonName, list):
            self.pythonName = [self.pythonName] if self.pythonName is not None else []
        self.pythonName = [v if isinstance(v, str) else str(v) for v in self.pythonName]

        if not isinstance(self.vbName, list):
            self.vbName = [self.vbName] if self.vbName is not None else []
        self.vbName = [v if isinstance(v, str) else str(v) for v in self.vbName]

        if not isinstance(self.bounded, list):
            self.bounded = [self.bounded] if self.bounded is not None else []
        self.bounded = [v if isinstance(v, str) else str(v) for v in self.bounded]

        if not isinstance(self.qudt_id, list):
            self.qudt_id = [self.qudt_id] if self.qudt_id is not None else []
        self.qudt_id = [v if isinstance(v, str) else str(v) for v in self.qudt_id]

        if not isinstance(self.javaName, list):
            self.javaName = [self.javaName] if self.javaName is not None else []
        self.javaName = [v if isinstance(v, str) else str(v) for v in self.javaName]

        if not isinstance(self.jsName, list):
            self.jsName = [self.jsName] if self.jsName is not None else []
        self.jsName = [v if isinstance(v, str) else str(v) for v in self.jsName]

        if not isinstance(self.matlabName, list):
            self.matlabName = [self.matlabName] if self.matlabName is not None else []
        self.matlabName = [v if isinstance(v, str) else str(v) for v in self.matlabName]

        if not isinstance(self.microsoftSQLServerName, list):
            self.microsoftSQLServerName = [self.microsoftSQLServerName] if self.microsoftSQLServerName is not None else []
        self.microsoftSQLServerName = [v if isinstance(v, str) else str(v) for v in self.microsoftSQLServerName]

        if not isinstance(self.mySQLName, list):
            self.mySQLName = [self.mySQLName] if self.mySQLName is not None else []
        self.mySQLName = [v if isinstance(v, str) else str(v) for v in self.mySQLName]

        if not isinstance(self.odbcName, list):
            self.odbcName = [self.odbcName] if self.odbcName is not None else []
        self.odbcName = [v if isinstance(v, str) else str(v) for v in self.odbcName]

        if not isinstance(self.oleDBName, list):
            self.oleDBName = [self.oleDBName] if self.oleDBName is not None else []
        self.oleDBName = [v if isinstance(v, str) else str(v) for v in self.oleDBName]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Verifiable(Aspect):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Verifiable"]
    class_class_curie: ClassVar[str] = "qudt:Verifiable"
    class_name: ClassVar[str] = "Verifiable"
    class_model_uri: ClassVar[URIRef] = POKEMON.Verifiable

    id: Union[str, VerifiableId] = None
    isoNormativeReference: Optional[Union[str, list[str]]] = empty_list()
    normativeReference: Optional[Union[str, list[str]]] = empty_list()
    wikidataMatch: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    dbpediaMatch: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VerifiableId):
            self.id = VerifiableId(self.id)

        if not isinstance(self.isoNormativeReference, list):
            self.isoNormativeReference = [self.isoNormativeReference] if self.isoNormativeReference is not None else []
        self.isoNormativeReference = [v if isinstance(v, str) else str(v) for v in self.isoNormativeReference]

        if not isinstance(self.normativeReference, list):
            self.normativeReference = [self.normativeReference] if self.normativeReference is not None else []
        self.normativeReference = [v if isinstance(v, str) else str(v) for v in self.normativeReference]

        if not isinstance(self.wikidataMatch, list):
            self.wikidataMatch = [self.wikidataMatch] if self.wikidataMatch is not None else []
        self.wikidataMatch = [v if isinstance(v, URI) else URI(v) for v in self.wikidataMatch]

        if not isinstance(self.dbpediaMatch, list):
            self.dbpediaMatch = [self.dbpediaMatch] if self.dbpediaMatch is not None else []
        self.dbpediaMatch = [v if isinstance(v, URI) else URI(v) for v in self.dbpediaMatch]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SystemOfUnits(Verifiable):
    """
    A system of units is a set of units which are chosen as the reference scales for some set of quantity kinds
    together with the definitions of each unit. Units may be defined by experimental observation or by proportion to
    another unit not included in the system. If the unit system is explicitly associated with a quantity kind system,
    then the unit system must define at least one unit for each quantity kind.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["SystemOfUnits"]
    class_class_curie: ClassVar[str] = "qudt:SystemOfUnits"
    class_name: ClassVar[str] = "SystemOfUnits"
    class_model_uri: ClassVar[URIRef] = POKEMON.SystemOfUnits

    id: Union[str, SystemOfUnitsId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    applicablePhysicalConstant: Optional[Union[Union[str, PhysicalConstantId], list[Union[str, PhysicalConstantId]]]] = empty_list()
    hasAllowedUnit: Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]] = empty_list()
    hasBaseUnit: Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]] = empty_list()
    hasCoherentUnit: Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]] = empty_list()
    hasDefinedUnit: Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]] = empty_list()
    hasDerivedCoherentUnit: Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]] = empty_list()
    hasDerivedUnit: Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]] = empty_list()
    hasUnit: Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]] = empty_list()
    prefix: Optional[Union[Union[str, PrefixId], list[Union[str, PrefixId]]]] = empty_list()
    guidance: Optional[Union[str, list[str]]] = empty_list()
    qudt_id: Optional[Union[str, list[str]]] = empty_list()
    hasRule: Optional[Union[Union[str, RuleId], list[Union[str, RuleId]]]] = empty_list()
    isReplacedBy: Optional[Union[str, list[str]]] = empty_list()
    qudt_description: Optional[Union[str, list[str]]] = empty_list()
    abbreviation: Optional[Union[str, list[str]]] = empty_list()
    deprecated: Optional[Union[str, list[str]]] = empty_list()
    plainTextDescription: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SystemOfUnitsId):
            self.id = SystemOfUnitsId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.applicablePhysicalConstant, list):
            self.applicablePhysicalConstant = [self.applicablePhysicalConstant] if self.applicablePhysicalConstant is not None else []
        self.applicablePhysicalConstant = [v if isinstance(v, PhysicalConstantId) else PhysicalConstantId(v) for v in self.applicablePhysicalConstant]

        if not isinstance(self.hasAllowedUnit, list):
            self.hasAllowedUnit = [self.hasAllowedUnit] if self.hasAllowedUnit is not None else []
        self.hasAllowedUnit = [v if isinstance(v, UnitId) else UnitId(v) for v in self.hasAllowedUnit]

        if not isinstance(self.hasBaseUnit, list):
            self.hasBaseUnit = [self.hasBaseUnit] if self.hasBaseUnit is not None else []
        self.hasBaseUnit = [v if isinstance(v, UnitId) else UnitId(v) for v in self.hasBaseUnit]

        if not isinstance(self.hasCoherentUnit, list):
            self.hasCoherentUnit = [self.hasCoherentUnit] if self.hasCoherentUnit is not None else []
        self.hasCoherentUnit = [v if isinstance(v, UnitId) else UnitId(v) for v in self.hasCoherentUnit]

        if not isinstance(self.hasDefinedUnit, list):
            self.hasDefinedUnit = [self.hasDefinedUnit] if self.hasDefinedUnit is not None else []
        self.hasDefinedUnit = [v if isinstance(v, UnitId) else UnitId(v) for v in self.hasDefinedUnit]

        if not isinstance(self.hasDerivedCoherentUnit, list):
            self.hasDerivedCoherentUnit = [self.hasDerivedCoherentUnit] if self.hasDerivedCoherentUnit is not None else []
        self.hasDerivedCoherentUnit = [v if isinstance(v, UnitId) else UnitId(v) for v in self.hasDerivedCoherentUnit]

        if not isinstance(self.hasDerivedUnit, list):
            self.hasDerivedUnit = [self.hasDerivedUnit] if self.hasDerivedUnit is not None else []
        self.hasDerivedUnit = [v if isinstance(v, UnitId) else UnitId(v) for v in self.hasDerivedUnit]

        if not isinstance(self.hasUnit, list):
            self.hasUnit = [self.hasUnit] if self.hasUnit is not None else []
        self.hasUnit = [v if isinstance(v, UnitId) else UnitId(v) for v in self.hasUnit]

        if not isinstance(self.prefix, list):
            self.prefix = [self.prefix] if self.prefix is not None else []
        self.prefix = [v if isinstance(v, PrefixId) else PrefixId(v) for v in self.prefix]

        if not isinstance(self.guidance, list):
            self.guidance = [self.guidance] if self.guidance is not None else []
        self.guidance = [v if isinstance(v, str) else str(v) for v in self.guidance]

        if not isinstance(self.qudt_id, list):
            self.qudt_id = [self.qudt_id] if self.qudt_id is not None else []
        self.qudt_id = [v if isinstance(v, str) else str(v) for v in self.qudt_id]

        if not isinstance(self.hasRule, list):
            self.hasRule = [self.hasRule] if self.hasRule is not None else []
        self.hasRule = [v if isinstance(v, RuleId) else RuleId(v) for v in self.hasRule]

        if not isinstance(self.isReplacedBy, list):
            self.isReplacedBy = [self.isReplacedBy] if self.isReplacedBy is not None else []
        self.isReplacedBy = [v if isinstance(v, str) else str(v) for v in self.isReplacedBy]

        if not isinstance(self.qudt_description, list):
            self.qudt_description = [self.qudt_description] if self.qudt_description is not None else []
        self.qudt_description = [v if isinstance(v, str) else str(v) for v in self.qudt_description]

        if not isinstance(self.abbreviation, list):
            self.abbreviation = [self.abbreviation] if self.abbreviation is not None else []
        self.abbreviation = [v if isinstance(v, str) else str(v) for v in self.abbreviation]

        if not isinstance(self.deprecated, list):
            self.deprecated = [self.deprecated] if self.deprecated is not None else []
        self.deprecated = [v if isinstance(v, str) else str(v) for v in self.deprecated]

        if not isinstance(self.plainTextDescription, list):
            self.plainTextDescription = [self.plainTextDescription] if self.plainTextDescription is not None else []
        self.plainTextDescription = [v if isinstance(v, str) else str(v) for v in self.plainTextDescription]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Prefix(Verifiable):
    """
    Prefix
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Prefix"]
    class_class_curie: ClassVar[str] = "qudt:Prefix"
    class_name: ClassVar[str] = "Prefix"
    class_model_uri: ClassVar[URIRef] = POKEMON.Prefix

    id: Union[str, PrefixId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    exactMatch: Optional[Union[Union[str, PrefixId], list[Union[str, PrefixId]]]] = empty_list()
    ucumCode: Optional[Union[Union[str, UCUMcs-termId], list[Union[str, UCUMcs-termId]]]] = empty_list()
    altSymbol: Optional[Union[str, list[str]]] = empty_list()
    latexSymbol: Optional[Union[str, list[str]]] = empty_list()
    symbol: Optional[Union[str, list[str]]] = empty_list()
    prefixMultiplier: Optional[Union[str, list[str]]] = empty_list()
    guidance: Optional[Union[str, list[str]]] = empty_list()
    qudt_id: Optional[Union[str, list[str]]] = empty_list()
    hasRule: Optional[Union[Union[str, RuleId], list[Union[str, RuleId]]]] = empty_list()
    isReplacedBy: Optional[Union[str, list[str]]] = empty_list()
    qudt_description: Optional[Union[str, list[str]]] = empty_list()
    abbreviation: Optional[Union[str, list[str]]] = empty_list()
    deprecated: Optional[Union[str, list[str]]] = empty_list()
    plainTextDescription: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrefixId):
            self.id = PrefixId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.exactMatch, list):
            self.exactMatch = [self.exactMatch] if self.exactMatch is not None else []
        self.exactMatch = [v if isinstance(v, PrefixId) else PrefixId(v) for v in self.exactMatch]

        if not isinstance(self.ucumCode, list):
            self.ucumCode = [self.ucumCode] if self.ucumCode is not None else []
        self.ucumCode = [v if isinstance(v, UCUMcs-termId) else UCUMcs-termId(v) for v in self.ucumCode]

        if not isinstance(self.altSymbol, list):
            self.altSymbol = [self.altSymbol] if self.altSymbol is not None else []
        self.altSymbol = [v if isinstance(v, str) else str(v) for v in self.altSymbol]

        if not isinstance(self.latexSymbol, list):
            self.latexSymbol = [self.latexSymbol] if self.latexSymbol is not None else []
        self.latexSymbol = [v if isinstance(v, str) else str(v) for v in self.latexSymbol]

        if not isinstance(self.symbol, list):
            self.symbol = [self.symbol] if self.symbol is not None else []
        self.symbol = [v if isinstance(v, str) else str(v) for v in self.symbol]

        if not isinstance(self.prefixMultiplier, list):
            self.prefixMultiplier = [self.prefixMultiplier] if self.prefixMultiplier is not None else []
        self.prefixMultiplier = [v if isinstance(v, str) else str(v) for v in self.prefixMultiplier]

        if not isinstance(self.guidance, list):
            self.guidance = [self.guidance] if self.guidance is not None else []
        self.guidance = [v if isinstance(v, str) else str(v) for v in self.guidance]

        if not isinstance(self.qudt_id, list):
            self.qudt_id = [self.qudt_id] if self.qudt_id is not None else []
        self.qudt_id = [v if isinstance(v, str) else str(v) for v in self.qudt_id]

        if not isinstance(self.hasRule, list):
            self.hasRule = [self.hasRule] if self.hasRule is not None else []
        self.hasRule = [v if isinstance(v, RuleId) else RuleId(v) for v in self.hasRule]

        if not isinstance(self.isReplacedBy, list):
            self.isReplacedBy = [self.isReplacedBy] if self.isReplacedBy is not None else []
        self.isReplacedBy = [v if isinstance(v, str) else str(v) for v in self.isReplacedBy]

        if not isinstance(self.qudt_description, list):
            self.qudt_description = [self.qudt_description] if self.qudt_description is not None else []
        self.qudt_description = [v if isinstance(v, str) else str(v) for v in self.qudt_description]

        if not isinstance(self.abbreviation, list):
            self.abbreviation = [self.abbreviation] if self.abbreviation is not None else []
        self.abbreviation = [v if isinstance(v, str) else str(v) for v in self.abbreviation]

        if not isinstance(self.deprecated, list):
            self.deprecated = [self.deprecated] if self.deprecated is not None else []
        self.deprecated = [v if isinstance(v, str) else str(v) for v in self.deprecated]

        if not isinstance(self.plainTextDescription, list):
            self.plainTextDescription = [self.plainTextDescription] if self.plainTextDescription is not None else []
        self.plainTextDescription = [v if isinstance(v, str) else str(v) for v in self.plainTextDescription]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnumeratedValue(Verifiable):
    """
    <p>This class is for all enumerated and/or coded values. For example, it contains the dimension objects that are
    the basis elements in some abstract vector space associated with a quantity kind system. Another use is for the
    base dimensions for quantity systems. Each quantity kind system that defines a base set has a corresponding
    ordered enumeration whose elements are the dimension objects for the base quantity kinds. The order of the
    dimensions in the enumeration determines the canonical order of the basis elements in the corresponding abstract
    vector space.</p>

    <p>An enumeration is a set of literals from which a single value is selected. Each literal can have a tag as an
    integer within a standard encoding appropriate to the range of integer values. Consistency of enumeration types
    will allow them, and the enumerated values, to be referred to unambiguously either through symbolic name or
    encoding. Enumerated values are also controlled vocabularies and as such need to be standardized. Without this
    consistency enumeration literals can be stated differently and result in data conflicts and
    misinterpretations.</p>

    <p>The tags are a set of positive whole numbers, not necessarily contiguous and having no numerical significance,
    each corresponding to the associated literal identifier. An order attribute can also be given on the enumeration
    elements. An enumeration can itself be a member of an enumeration. This allows enumerations to be enumerated in a
    selection. Enumerations are also subclasses of Scalar Datatype. This allows them to be used as the reference of a
    datatype specification.</p>
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["EnumeratedValue"]
    class_class_curie: ClassVar[str] = "qudt:EnumeratedValue"
    class_name: ClassVar[str] = "EnumeratedValue"
    class_model_uri: ClassVar[URIRef] = POKEMON.EnumeratedValue

    id: Union[str, EnumeratedValueId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    altSymbol: Optional[Union[str, list[str]]] = empty_list()
    qudt_description: Optional[Union[str, list[str]]] = empty_list()
    abbreviation: Optional[Union[str, list[str]]] = empty_list()
    symbol: Optional[Union[str, list[str]]] = empty_list()
    guidance: Optional[Union[str, list[str]]] = empty_list()
    qudt_id: Optional[Union[str, list[str]]] = empty_list()
    hasRule: Optional[Union[Union[str, RuleId], list[Union[str, RuleId]]]] = empty_list()
    isReplacedBy: Optional[Union[str, list[str]]] = empty_list()
    deprecated: Optional[Union[str, list[str]]] = empty_list()
    plainTextDescription: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnumeratedValueId):
            self.id = EnumeratedValueId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.altSymbol, list):
            self.altSymbol = [self.altSymbol] if self.altSymbol is not None else []
        self.altSymbol = [v if isinstance(v, str) else str(v) for v in self.altSymbol]

        if not isinstance(self.qudt_description, list):
            self.qudt_description = [self.qudt_description] if self.qudt_description is not None else []
        self.qudt_description = [v if isinstance(v, str) else str(v) for v in self.qudt_description]

        if not isinstance(self.abbreviation, list):
            self.abbreviation = [self.abbreviation] if self.abbreviation is not None else []
        self.abbreviation = [v if isinstance(v, str) else str(v) for v in self.abbreviation]

        if not isinstance(self.symbol, list):
            self.symbol = [self.symbol] if self.symbol is not None else []
        self.symbol = [v if isinstance(v, str) else str(v) for v in self.symbol]

        if not isinstance(self.guidance, list):
            self.guidance = [self.guidance] if self.guidance is not None else []
        self.guidance = [v if isinstance(v, str) else str(v) for v in self.guidance]

        if not isinstance(self.qudt_id, list):
            self.qudt_id = [self.qudt_id] if self.qudt_id is not None else []
        self.qudt_id = [v if isinstance(v, str) else str(v) for v in self.qudt_id]

        if not isinstance(self.hasRule, list):
            self.hasRule = [self.hasRule] if self.hasRule is not None else []
        self.hasRule = [v if isinstance(v, RuleId) else RuleId(v) for v in self.hasRule]

        if not isinstance(self.isReplacedBy, list):
            self.isReplacedBy = [self.isReplacedBy] if self.isReplacedBy is not None else []
        self.isReplacedBy = [v if isinstance(v, str) else str(v) for v in self.isReplacedBy]

        if not isinstance(self.deprecated, list):
            self.deprecated = [self.deprecated] if self.deprecated is not None else []
        self.deprecated = [v if isinstance(v, str) else str(v) for v in self.deprecated]

        if not isinstance(self.plainTextDescription, list):
            self.plainTextDescription = [self.plainTextDescription] if self.plainTextDescription is not None else []
        self.plainTextDescription = [v if isinstance(v, str) else str(v) for v in self.plainTextDescription]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EndianType(EnumeratedValue):
    """
    Endian Type
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["EndianType"]
    class_class_curie: ClassVar[str] = "qudt:EndianType"
    class_name: ClassVar[str] = "EndianType"
    class_model_uri: ClassVar[URIRef] = POKEMON.EndianType

    id: Union[str, EndianTypeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EndianTypeId):
            self.id = EndianTypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RuleType(EnumeratedValue):
    """
    Rule Type
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["RuleType"]
    class_class_curie: ClassVar[str] = "qudt:RuleType"
    class_name: ClassVar[str] = "RuleType"
    class_model_uri: ClassVar[URIRef] = POKEMON.RuleType

    id: Union[str, RuleTypeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RuleTypeId):
            self.id = RuleTypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CardinalityType(EnumeratedValue):
    """
    In mathematics, the cardinality of a set is a measure of the number of elements of the set.
    For example, the set $A = {2, 4, 6}$ contains 3 elements, and therefore $A$ has a cardinality of 3.
    There are two approaches to cardinality: one which compares sets directly using bijections and injections,
    and another which uses cardinal numbers.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["CardinalityType"]
    class_class_curie: ClassVar[str] = "qudt:CardinalityType"
    class_name: ClassVar[str] = "CardinalityType"
    class_model_uri: ClassVar[URIRef] = POKEMON.CardinalityType

    id: Union[str, CardinalityTypeId] = None
    literal: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CardinalityTypeId):
            self.id = CardinalityTypeId(self.id)

        if not isinstance(self.literal, list):
            self.literal = [self.literal] if self.literal is not None else []
        self.literal = [v if isinstance(v, str) else str(v) for v in self.literal]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrderedType(EnumeratedValue):
    """
    Describes how a data or information structure is ordered.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["OrderedType"]
    class_class_curie: ClassVar[str] = "qudt:OrderedType"
    class_name: ClassVar[str] = "OrderedType"
    class_model_uri: ClassVar[URIRef] = POKEMON.OrderedType

    id: Union[str, OrderedTypeId] = None
    literal: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrderedTypeId):
            self.id = OrderedTypeId(self.id)

        if not isinstance(self.literal, list):
            self.literal = [self.literal] if self.literal is not None else []
        self.literal = [v if isinstance(v, str) else str(v) for v in self.literal]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Unit(Verifiable):
    """
    A unit of measure, or unit, is a particular quantity value that has been chosen as a scale for measuring other
    quantities the same kind (more generally of equivalent dimension).
    For example, the meter is a quantity of length that has been rigorously defined and standardized by the BIPM
    (International Board of Weights and Measures).
    Any measurement of the length can be expressed as a number multiplied by the unit meter.
    More formally, the value of a physical quantity Q with respect to a unit (U) is expressed as the scalar multiple
    of a real number (n) and U, as $Q = nU$.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Unit"]
    class_class_curie: ClassVar[str] = "qudt:Unit"
    class_name: ClassVar[str] = "Unit"
    class_model_uri: ClassVar[URIRef] = POKEMON.Unit

    id: Union[str, UnitId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    hasReciprocalUnit: Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]] = empty_list()
    isUnitOfSystem: Optional[Union[Union[str, SystemOfUnitsId], list[Union[str, SystemOfUnitsId]]]] = empty_list()
    omUnit: Optional[Union[str, list[str]]] = empty_list()
    unitFor: Optional[Union[str, list[str]]] = empty_list()
    applicableSystem: Optional[Union[Union[str, SystemOfUnitsId], list[Union[str, SystemOfUnitsId]]]] = empty_list()
    definedUnitOfSystem: Optional[Union[Union[str, SystemOfUnitsId], list[Union[str, SystemOfUnitsId]]]] = empty_list()
    derivedCoherentUnitOfSystem: Optional[Union[Union[str, SystemOfUnitsId], list[Union[str, SystemOfUnitsId]]]] = empty_list()
    derivedUnitOfSystem: Optional[Union[Union[str, SystemOfUnitsId], list[Union[str, SystemOfUnitsId]]]] = empty_list()
    exactMatch: Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]] = empty_list()
    hasDimensionVector: Optional[Union[Union[str, QuantityKindDimensionVectorId], list[Union[str, QuantityKindDimensionVectorId]]]] = empty_list()
    hasFactorUnit: Optional[Union[str, list[str]]] = empty_list()
    hasQuantityKind: Optional[Union[Union[str, QuantityKindId], list[Union[str, QuantityKindId]]]] = empty_list()
    iec61360Code: Optional[Union[str, list[str]]] = empty_list()
    prefix: Optional[Union[Union[str, PrefixId], list[Union[str, PrefixId]]]] = empty_list()
    qkdvDenominator: Optional[Union[Union[str, QuantityKindDimensionVectorId], list[Union[str, QuantityKindDimensionVectorId]]]] = empty_list()
    qkdvNumerator: Optional[Union[Union[str, QuantityKindDimensionVectorId], list[Union[str, QuantityKindDimensionVectorId]]]] = empty_list()
    scalingOf: Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]] = empty_list()
    ucumCode: Optional[Union[Union[str, UCUMcsId], list[Union[str, UCUMcsId]]]] = empty_list()
    udunitsCode: Optional[Union[str, list[str]]] = empty_list()
    uneceCommonCode: Optional[Union[str, list[str]]] = empty_list()
    altSymbol: Optional[Union[str, list[str]]] = empty_list()
    latexDefinition: Optional[Union[str, list[str]]] = empty_list()
    latexSymbol: Optional[Union[str, list[str]]] = empty_list()
    siUnitsExpression: Optional[Union[str, list[str]]] = empty_list()
    symbol: Optional[Union[str, list[str]]] = empty_list()
    conversionMultiplier: Optional[Union[str, list[str]]] = empty_list()
    conversionMultiplierSN: Optional[Union[str, list[str]]] = empty_list()
    conversionOffset: Optional[Union[str, list[str]]] = empty_list()
    conversionOffsetSN: Optional[Union[str, list[str]]] = empty_list()
    factorUnitScalar: Optional[Union[str, list[str]]] = empty_list()
    mathMLdefinition: Optional[Union[str, list[str]]] = empty_list()
    guidance: Optional[Union[str, list[str]]] = empty_list()
    qudt_id: Optional[Union[str, list[str]]] = empty_list()
    hasRule: Optional[Union[Union[str, RuleId], list[Union[str, RuleId]]]] = empty_list()
    isReplacedBy: Optional[Union[str, list[str]]] = empty_list()
    qudt_description: Optional[Union[str, list[str]]] = empty_list()
    abbreviation: Optional[Union[str, list[str]]] = empty_list()
    deprecated: Optional[Union[str, list[str]]] = empty_list()
    plainTextDescription: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UnitId):
            self.id = UnitId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.hasReciprocalUnit, list):
            self.hasReciprocalUnit = [self.hasReciprocalUnit] if self.hasReciprocalUnit is not None else []
        self.hasReciprocalUnit = [v if isinstance(v, UnitId) else UnitId(v) for v in self.hasReciprocalUnit]

        if not isinstance(self.isUnitOfSystem, list):
            self.isUnitOfSystem = [self.isUnitOfSystem] if self.isUnitOfSystem is not None else []
        self.isUnitOfSystem = [v if isinstance(v, SystemOfUnitsId) else SystemOfUnitsId(v) for v in self.isUnitOfSystem]

        if not isinstance(self.omUnit, list):
            self.omUnit = [self.omUnit] if self.omUnit is not None else []
        self.omUnit = [v if isinstance(v, str) else str(v) for v in self.omUnit]

        if not isinstance(self.unitFor, list):
            self.unitFor = [self.unitFor] if self.unitFor is not None else []
        self.unitFor = [v if isinstance(v, str) else str(v) for v in self.unitFor]

        if not isinstance(self.applicableSystem, list):
            self.applicableSystem = [self.applicableSystem] if self.applicableSystem is not None else []
        self.applicableSystem = [v if isinstance(v, SystemOfUnitsId) else SystemOfUnitsId(v) for v in self.applicableSystem]

        if not isinstance(self.definedUnitOfSystem, list):
            self.definedUnitOfSystem = [self.definedUnitOfSystem] if self.definedUnitOfSystem is not None else []
        self.definedUnitOfSystem = [v if isinstance(v, SystemOfUnitsId) else SystemOfUnitsId(v) for v in self.definedUnitOfSystem]

        if not isinstance(self.derivedCoherentUnitOfSystem, list):
            self.derivedCoherentUnitOfSystem = [self.derivedCoherentUnitOfSystem] if self.derivedCoherentUnitOfSystem is not None else []
        self.derivedCoherentUnitOfSystem = [v if isinstance(v, SystemOfUnitsId) else SystemOfUnitsId(v) for v in self.derivedCoherentUnitOfSystem]

        if not isinstance(self.derivedUnitOfSystem, list):
            self.derivedUnitOfSystem = [self.derivedUnitOfSystem] if self.derivedUnitOfSystem is not None else []
        self.derivedUnitOfSystem = [v if isinstance(v, SystemOfUnitsId) else SystemOfUnitsId(v) for v in self.derivedUnitOfSystem]

        if not isinstance(self.exactMatch, list):
            self.exactMatch = [self.exactMatch] if self.exactMatch is not None else []
        self.exactMatch = [v if isinstance(v, UnitId) else UnitId(v) for v in self.exactMatch]

        if not isinstance(self.hasDimensionVector, list):
            self.hasDimensionVector = [self.hasDimensionVector] if self.hasDimensionVector is not None else []
        self.hasDimensionVector = [v if isinstance(v, QuantityKindDimensionVectorId) else QuantityKindDimensionVectorId(v) for v in self.hasDimensionVector]

        if not isinstance(self.hasFactorUnit, list):
            self.hasFactorUnit = [self.hasFactorUnit] if self.hasFactorUnit is not None else []
        self.hasFactorUnit = [v if isinstance(v, str) else str(v) for v in self.hasFactorUnit]

        if not isinstance(self.hasQuantityKind, list):
            self.hasQuantityKind = [self.hasQuantityKind] if self.hasQuantityKind is not None else []
        self.hasQuantityKind = [v if isinstance(v, QuantityKindId) else QuantityKindId(v) for v in self.hasQuantityKind]

        if not isinstance(self.iec61360Code, list):
            self.iec61360Code = [self.iec61360Code] if self.iec61360Code is not None else []
        self.iec61360Code = [v if isinstance(v, str) else str(v) for v in self.iec61360Code]

        if not isinstance(self.prefix, list):
            self.prefix = [self.prefix] if self.prefix is not None else []
        self.prefix = [v if isinstance(v, PrefixId) else PrefixId(v) for v in self.prefix]

        if not isinstance(self.qkdvDenominator, list):
            self.qkdvDenominator = [self.qkdvDenominator] if self.qkdvDenominator is not None else []
        self.qkdvDenominator = [v if isinstance(v, QuantityKindDimensionVectorId) else QuantityKindDimensionVectorId(v) for v in self.qkdvDenominator]

        if not isinstance(self.qkdvNumerator, list):
            self.qkdvNumerator = [self.qkdvNumerator] if self.qkdvNumerator is not None else []
        self.qkdvNumerator = [v if isinstance(v, QuantityKindDimensionVectorId) else QuantityKindDimensionVectorId(v) for v in self.qkdvNumerator]

        if not isinstance(self.scalingOf, list):
            self.scalingOf = [self.scalingOf] if self.scalingOf is not None else []
        self.scalingOf = [v if isinstance(v, UnitId) else UnitId(v) for v in self.scalingOf]

        if not isinstance(self.ucumCode, list):
            self.ucumCode = [self.ucumCode] if self.ucumCode is not None else []
        self.ucumCode = [v if isinstance(v, UCUMcsId) else UCUMcsId(v) for v in self.ucumCode]

        if not isinstance(self.udunitsCode, list):
            self.udunitsCode = [self.udunitsCode] if self.udunitsCode is not None else []
        self.udunitsCode = [v if isinstance(v, str) else str(v) for v in self.udunitsCode]

        if not isinstance(self.uneceCommonCode, list):
            self.uneceCommonCode = [self.uneceCommonCode] if self.uneceCommonCode is not None else []
        self.uneceCommonCode = [v if isinstance(v, str) else str(v) for v in self.uneceCommonCode]

        if not isinstance(self.altSymbol, list):
            self.altSymbol = [self.altSymbol] if self.altSymbol is not None else []
        self.altSymbol = [v if isinstance(v, str) else str(v) for v in self.altSymbol]

        if not isinstance(self.latexDefinition, list):
            self.latexDefinition = [self.latexDefinition] if self.latexDefinition is not None else []
        self.latexDefinition = [v if isinstance(v, str) else str(v) for v in self.latexDefinition]

        if not isinstance(self.latexSymbol, list):
            self.latexSymbol = [self.latexSymbol] if self.latexSymbol is not None else []
        self.latexSymbol = [v if isinstance(v, str) else str(v) for v in self.latexSymbol]

        if not isinstance(self.siUnitsExpression, list):
            self.siUnitsExpression = [self.siUnitsExpression] if self.siUnitsExpression is not None else []
        self.siUnitsExpression = [v if isinstance(v, str) else str(v) for v in self.siUnitsExpression]

        if not isinstance(self.symbol, list):
            self.symbol = [self.symbol] if self.symbol is not None else []
        self.symbol = [v if isinstance(v, str) else str(v) for v in self.symbol]

        if not isinstance(self.conversionMultiplier, list):
            self.conversionMultiplier = [self.conversionMultiplier] if self.conversionMultiplier is not None else []
        self.conversionMultiplier = [v if isinstance(v, str) else str(v) for v in self.conversionMultiplier]

        if not isinstance(self.conversionMultiplierSN, list):
            self.conversionMultiplierSN = [self.conversionMultiplierSN] if self.conversionMultiplierSN is not None else []
        self.conversionMultiplierSN = [v if isinstance(v, str) else str(v) for v in self.conversionMultiplierSN]

        if not isinstance(self.conversionOffset, list):
            self.conversionOffset = [self.conversionOffset] if self.conversionOffset is not None else []
        self.conversionOffset = [v if isinstance(v, str) else str(v) for v in self.conversionOffset]

        if not isinstance(self.conversionOffsetSN, list):
            self.conversionOffsetSN = [self.conversionOffsetSN] if self.conversionOffsetSN is not None else []
        self.conversionOffsetSN = [v if isinstance(v, str) else str(v) for v in self.conversionOffsetSN]

        if not isinstance(self.factorUnitScalar, list):
            self.factorUnitScalar = [self.factorUnitScalar] if self.factorUnitScalar is not None else []
        self.factorUnitScalar = [v if isinstance(v, str) else str(v) for v in self.factorUnitScalar]

        if not isinstance(self.mathMLdefinition, list):
            self.mathMLdefinition = [self.mathMLdefinition] if self.mathMLdefinition is not None else []
        self.mathMLdefinition = [v if isinstance(v, str) else str(v) for v in self.mathMLdefinition]

        if not isinstance(self.guidance, list):
            self.guidance = [self.guidance] if self.guidance is not None else []
        self.guidance = [v if isinstance(v, str) else str(v) for v in self.guidance]

        if not isinstance(self.qudt_id, list):
            self.qudt_id = [self.qudt_id] if self.qudt_id is not None else []
        self.qudt_id = [v if isinstance(v, str) else str(v) for v in self.qudt_id]

        if not isinstance(self.hasRule, list):
            self.hasRule = [self.hasRule] if self.hasRule is not None else []
        self.hasRule = [v if isinstance(v, RuleId) else RuleId(v) for v in self.hasRule]

        if not isinstance(self.isReplacedBy, list):
            self.isReplacedBy = [self.isReplacedBy] if self.isReplacedBy is not None else []
        self.isReplacedBy = [v if isinstance(v, str) else str(v) for v in self.isReplacedBy]

        if not isinstance(self.qudt_description, list):
            self.qudt_description = [self.qudt_description] if self.qudt_description is not None else []
        self.qudt_description = [v if isinstance(v, str) else str(v) for v in self.qudt_description]

        if not isinstance(self.abbreviation, list):
            self.abbreviation = [self.abbreviation] if self.abbreviation is not None else []
        self.abbreviation = [v if isinstance(v, str) else str(v) for v in self.abbreviation]

        if not isinstance(self.deprecated, list):
            self.deprecated = [self.deprecated] if self.deprecated is not None else []
        self.deprecated = [v if isinstance(v, str) else str(v) for v in self.deprecated]

        if not isinstance(self.plainTextDescription, list):
            self.plainTextDescription = [self.plainTextDescription] if self.plainTextDescription is not None else []
        self.plainTextDescription = [v if isinstance(v, str) else str(v) for v in self.plainTextDescription]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantityKind(Verifiable):
    """
    A <b>Quantity Kind</b> is any observable property that can be measured and quantified numerically. Familiar
    examples include physical properties such as length, mass, time, force, energy, power, electric charge, etc. Less
    familiar examples include currency, interest rate, price to earning ratio, and information capacity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["QuantityKind"]
    class_class_curie: ClassVar[str] = "qudt:QuantityKind"
    class_name: ClassVar[str] = "QuantityKind"
    class_model_uri: ClassVar[URIRef] = POKEMON.QuantityKind

    id: Union[str, QuantityKindId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    belongsToSystemOfQuantities: Optional[Union[Union[str, SystemOfQuantityKindsId], list[Union[str, SystemOfQuantityKindsId]]]] = empty_list()
    dimensionVectorForSI: Optional[Union[Union[str, QuantityKindDimensionVectorSIId], list[Union[str, QuantityKindDimensionVectorSIId]]]] = empty_list()
    exactMatch: Optional[Union[Union[str, QuantityKindId], list[Union[str, QuantityKindId]]]] = empty_list()
    hasDimensionVector: Optional[Union[Union[str, QuantityKindDimensionVectorId], list[Union[str, QuantityKindDimensionVectorId]]]] = empty_list()
    iec61360Code: Optional[Union[str, list[str]]] = empty_list()
    applicableCGSUnit: Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]] = empty_list()
    applicableISOUnit: Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]] = empty_list()
    applicableImperialUnit: Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]] = empty_list()
    applicableSIUnit: Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]] = empty_list()
    applicableUSCustomaryUnit: Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]] = empty_list()
    applicableUnit: Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]] = empty_list()
    qkdvDenominator: Optional[Union[Union[str, QuantityKindDimensionVectorId], list[Union[str, QuantityKindDimensionVectorId]]]] = empty_list()
    qkdvNumerator: Optional[Union[Union[str, QuantityKindDimensionVectorId], list[Union[str, QuantityKindDimensionVectorId]]]] = empty_list()
    latexDefinition: Optional[Union[str, list[str]]] = empty_list()
    mathMLdefinition: Optional[Union[str, list[str]]] = empty_list()
    guidance: Optional[Union[str, list[str]]] = empty_list()
    qudt_id: Optional[Union[str, list[str]]] = empty_list()
    hasRule: Optional[Union[Union[str, RuleId], list[Union[str, RuleId]]]] = empty_list()
    isReplacedBy: Optional[Union[str, list[str]]] = empty_list()
    qudt_description: Optional[Union[str, list[str]]] = empty_list()
    abbreviation: Optional[Union[str, list[str]]] = empty_list()
    deprecated: Optional[Union[str, list[str]]] = empty_list()
    plainTextDescription: Optional[Union[str, list[str]]] = empty_list()
    broader: Optional[Union[str, QuantityKindId]] = None
    altSymbol: Optional[Union[str, list[str]]] = empty_list()
    latexSymbol: Optional[Union[str, list[str]]] = empty_list()
    symbol: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, QuantityKindId):
            self.id = QuantityKindId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.belongsToSystemOfQuantities, list):
            self.belongsToSystemOfQuantities = [self.belongsToSystemOfQuantities] if self.belongsToSystemOfQuantities is not None else []
        self.belongsToSystemOfQuantities = [v if isinstance(v, SystemOfQuantityKindsId) else SystemOfQuantityKindsId(v) for v in self.belongsToSystemOfQuantities]

        if not isinstance(self.dimensionVectorForSI, list):
            self.dimensionVectorForSI = [self.dimensionVectorForSI] if self.dimensionVectorForSI is not None else []
        self.dimensionVectorForSI = [v if isinstance(v, QuantityKindDimensionVectorSIId) else QuantityKindDimensionVectorSIId(v) for v in self.dimensionVectorForSI]

        if not isinstance(self.exactMatch, list):
            self.exactMatch = [self.exactMatch] if self.exactMatch is not None else []
        self.exactMatch = [v if isinstance(v, QuantityKindId) else QuantityKindId(v) for v in self.exactMatch]

        if not isinstance(self.hasDimensionVector, list):
            self.hasDimensionVector = [self.hasDimensionVector] if self.hasDimensionVector is not None else []
        self.hasDimensionVector = [v if isinstance(v, QuantityKindDimensionVectorId) else QuantityKindDimensionVectorId(v) for v in self.hasDimensionVector]

        if not isinstance(self.iec61360Code, list):
            self.iec61360Code = [self.iec61360Code] if self.iec61360Code is not None else []
        self.iec61360Code = [v if isinstance(v, str) else str(v) for v in self.iec61360Code]

        if not isinstance(self.applicableCGSUnit, list):
            self.applicableCGSUnit = [self.applicableCGSUnit] if self.applicableCGSUnit is not None else []
        self.applicableCGSUnit = [v if isinstance(v, UnitId) else UnitId(v) for v in self.applicableCGSUnit]

        if not isinstance(self.applicableISOUnit, list):
            self.applicableISOUnit = [self.applicableISOUnit] if self.applicableISOUnit is not None else []
        self.applicableISOUnit = [v if isinstance(v, UnitId) else UnitId(v) for v in self.applicableISOUnit]

        if not isinstance(self.applicableImperialUnit, list):
            self.applicableImperialUnit = [self.applicableImperialUnit] if self.applicableImperialUnit is not None else []
        self.applicableImperialUnit = [v if isinstance(v, UnitId) else UnitId(v) for v in self.applicableImperialUnit]

        if not isinstance(self.applicableSIUnit, list):
            self.applicableSIUnit = [self.applicableSIUnit] if self.applicableSIUnit is not None else []
        self.applicableSIUnit = [v if isinstance(v, UnitId) else UnitId(v) for v in self.applicableSIUnit]

        if not isinstance(self.applicableUSCustomaryUnit, list):
            self.applicableUSCustomaryUnit = [self.applicableUSCustomaryUnit] if self.applicableUSCustomaryUnit is not None else []
        self.applicableUSCustomaryUnit = [v if isinstance(v, UnitId) else UnitId(v) for v in self.applicableUSCustomaryUnit]

        if not isinstance(self.applicableUnit, list):
            self.applicableUnit = [self.applicableUnit] if self.applicableUnit is not None else []
        self.applicableUnit = [v if isinstance(v, UnitId) else UnitId(v) for v in self.applicableUnit]

        if not isinstance(self.qkdvDenominator, list):
            self.qkdvDenominator = [self.qkdvDenominator] if self.qkdvDenominator is not None else []
        self.qkdvDenominator = [v if isinstance(v, QuantityKindDimensionVectorId) else QuantityKindDimensionVectorId(v) for v in self.qkdvDenominator]

        if not isinstance(self.qkdvNumerator, list):
            self.qkdvNumerator = [self.qkdvNumerator] if self.qkdvNumerator is not None else []
        self.qkdvNumerator = [v if isinstance(v, QuantityKindDimensionVectorId) else QuantityKindDimensionVectorId(v) for v in self.qkdvNumerator]

        if not isinstance(self.latexDefinition, list):
            self.latexDefinition = [self.latexDefinition] if self.latexDefinition is not None else []
        self.latexDefinition = [v if isinstance(v, str) else str(v) for v in self.latexDefinition]

        if not isinstance(self.mathMLdefinition, list):
            self.mathMLdefinition = [self.mathMLdefinition] if self.mathMLdefinition is not None else []
        self.mathMLdefinition = [v if isinstance(v, str) else str(v) for v in self.mathMLdefinition]

        if not isinstance(self.guidance, list):
            self.guidance = [self.guidance] if self.guidance is not None else []
        self.guidance = [v if isinstance(v, str) else str(v) for v in self.guidance]

        if not isinstance(self.qudt_id, list):
            self.qudt_id = [self.qudt_id] if self.qudt_id is not None else []
        self.qudt_id = [v if isinstance(v, str) else str(v) for v in self.qudt_id]

        if not isinstance(self.hasRule, list):
            self.hasRule = [self.hasRule] if self.hasRule is not None else []
        self.hasRule = [v if isinstance(v, RuleId) else RuleId(v) for v in self.hasRule]

        if not isinstance(self.isReplacedBy, list):
            self.isReplacedBy = [self.isReplacedBy] if self.isReplacedBy is not None else []
        self.isReplacedBy = [v if isinstance(v, str) else str(v) for v in self.isReplacedBy]

        if not isinstance(self.qudt_description, list):
            self.qudt_description = [self.qudt_description] if self.qudt_description is not None else []
        self.qudt_description = [v if isinstance(v, str) else str(v) for v in self.qudt_description]

        if not isinstance(self.abbreviation, list):
            self.abbreviation = [self.abbreviation] if self.abbreviation is not None else []
        self.abbreviation = [v if isinstance(v, str) else str(v) for v in self.abbreviation]

        if not isinstance(self.deprecated, list):
            self.deprecated = [self.deprecated] if self.deprecated is not None else []
        self.deprecated = [v if isinstance(v, str) else str(v) for v in self.deprecated]

        if not isinstance(self.plainTextDescription, list):
            self.plainTextDescription = [self.plainTextDescription] if self.plainTextDescription is not None else []
        self.plainTextDescription = [v if isinstance(v, str) else str(v) for v in self.plainTextDescription]

        if self.broader is not None and not isinstance(self.broader, QuantityKindId):
            self.broader = QuantityKindId(self.broader)

        if not isinstance(self.altSymbol, list):
            self.altSymbol = [self.altSymbol] if self.altSymbol is not None else []
        self.altSymbol = [v if isinstance(v, str) else str(v) for v in self.altSymbol]

        if not isinstance(self.latexSymbol, list):
            self.latexSymbol = [self.latexSymbol] if self.latexSymbol is not None else []
        self.latexSymbol = [v if isinstance(v, str) else str(v) for v in self.latexSymbol]

        if not isinstance(self.symbol, list):
            self.symbol = [self.symbol] if self.symbol is not None else []
        self.symbol = [v if isinstance(v, str) else str(v) for v in self.symbol]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UCUMcs-term(Thing):
    """
    Lexical pattern for the terminal symbols in the case-sensitive version of UCUM code
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["UCUMcs-term"]
    class_class_curie: ClassVar[str] = "qudt:UCUMcs-term"
    class_name: ClassVar[str] = "UCUMcs-term"
    class_model_uri: ClassVar[URIRef] = POKEMON.UCUMcs-term

    id: Union[str, UCUMcs-termId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UCUMcs-termId):
            self.id = UCUMcs-termId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantityKindDimensionVector(Concept):
    """
    <p class="lm-para">A <em>Quantity Kind Dimension Vector</em> describes the dimensionality of a quantity kind in
    the context of a system of units. In the SI system of units, the dimensions of a quantity kind are expressed as a
    product of the basic physical dimensions mass ($M$), length ($L$), time ($T$) current ($I$), amount of substance
    ($N$), luminous intensity ($J$) and absolute temperature ($\theta$) as $dim \, Q = L^{\alpha} \, M^{\beta} \,
    T^{\gamma} \, I ^{\delta} \, \theta ^{\epsilon} \, N^{\eta} \, J ^{\nu}$.</p>

    <p class="lm-para">The rational powers of the dimensional exponents, $\alpha, \, \beta, \, \gamma, \, \delta, \,
    \epsilon, \ , \eta, \, \nu$, are positive, negative, or zero.</p>

    <p class="lm-para">For example, the dimension of the physical quantity kind $\it{speed}$ is $\
    boxed{length/time}$, $L/T$ or $LT^{-1}$, and the dimension of the physical quantity kind force is $\boxed{mass
    \times acceleration}$ or $\boxed{mass \times (length/time)/time}$, $ML/T^2$ or $MLT^{-2}$ respectively.</p>
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["QuantityKindDimensionVector"]
    class_class_curie: ClassVar[str] = "qudt:QuantityKindDimensionVector"
    class_name: ClassVar[str] = "QuantityKindDimensionVector"
    class_model_uri: ClassVar[URIRef] = POKEMON.QuantityKindDimensionVector

    id: Union[str, QuantityKindDimensionVectorId] = None
    dimensionExponentForAmountOfSubstance: Union[str, list[str]] = None
    dimensionExponentForElectricCurrent: Union[str, list[str]] = None
    dimensionExponentForLength: Union[str, list[str]] = None
    dimensionExponentForLuminousIntensity: Union[str, list[str]] = None
    dimensionExponentForMass: Union[str, list[str]] = None
    dimensionExponentForThermodynamicTemperature: Union[str, list[str]] = None
    dimensionExponentForTime: Union[str, list[str]] = None
    dimensionlessExponent: Union[str, list[str]] = None
    hasReferenceQuantityKind: Optional[Union[Union[str, QuantityKindId], list[Union[str, QuantityKindId]]]] = empty_list()
    latexSymbol: Optional[Union[str, list[str]]] = empty_list()
    latexDefinition: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, QuantityKindDimensionVectorId):
            self.id = QuantityKindDimensionVectorId(self.id)

        if self._is_empty(self.dimensionExponentForAmountOfSubstance):
            self.MissingRequiredField("dimensionExponentForAmountOfSubstance")
        if not isinstance(self.dimensionExponentForAmountOfSubstance, list):
            self.dimensionExponentForAmountOfSubstance = [self.dimensionExponentForAmountOfSubstance] if self.dimensionExponentForAmountOfSubstance is not None else []
        self.dimensionExponentForAmountOfSubstance = [v if isinstance(v, str) else str(v) for v in self.dimensionExponentForAmountOfSubstance]

        if self._is_empty(self.dimensionExponentForElectricCurrent):
            self.MissingRequiredField("dimensionExponentForElectricCurrent")
        if not isinstance(self.dimensionExponentForElectricCurrent, list):
            self.dimensionExponentForElectricCurrent = [self.dimensionExponentForElectricCurrent] if self.dimensionExponentForElectricCurrent is not None else []
        self.dimensionExponentForElectricCurrent = [v if isinstance(v, str) else str(v) for v in self.dimensionExponentForElectricCurrent]

        if self._is_empty(self.dimensionExponentForLength):
            self.MissingRequiredField("dimensionExponentForLength")
        if not isinstance(self.dimensionExponentForLength, list):
            self.dimensionExponentForLength = [self.dimensionExponentForLength] if self.dimensionExponentForLength is not None else []
        self.dimensionExponentForLength = [v if isinstance(v, str) else str(v) for v in self.dimensionExponentForLength]

        if self._is_empty(self.dimensionExponentForLuminousIntensity):
            self.MissingRequiredField("dimensionExponentForLuminousIntensity")
        if not isinstance(self.dimensionExponentForLuminousIntensity, list):
            self.dimensionExponentForLuminousIntensity = [self.dimensionExponentForLuminousIntensity] if self.dimensionExponentForLuminousIntensity is not None else []
        self.dimensionExponentForLuminousIntensity = [v if isinstance(v, str) else str(v) for v in self.dimensionExponentForLuminousIntensity]

        if self._is_empty(self.dimensionExponentForMass):
            self.MissingRequiredField("dimensionExponentForMass")
        if not isinstance(self.dimensionExponentForMass, list):
            self.dimensionExponentForMass = [self.dimensionExponentForMass] if self.dimensionExponentForMass is not None else []
        self.dimensionExponentForMass = [v if isinstance(v, str) else str(v) for v in self.dimensionExponentForMass]

        if self._is_empty(self.dimensionExponentForThermodynamicTemperature):
            self.MissingRequiredField("dimensionExponentForThermodynamicTemperature")
        if not isinstance(self.dimensionExponentForThermodynamicTemperature, list):
            self.dimensionExponentForThermodynamicTemperature = [self.dimensionExponentForThermodynamicTemperature] if self.dimensionExponentForThermodynamicTemperature is not None else []
        self.dimensionExponentForThermodynamicTemperature = [v if isinstance(v, str) else str(v) for v in self.dimensionExponentForThermodynamicTemperature]

        if self._is_empty(self.dimensionExponentForTime):
            self.MissingRequiredField("dimensionExponentForTime")
        if not isinstance(self.dimensionExponentForTime, list):
            self.dimensionExponentForTime = [self.dimensionExponentForTime] if self.dimensionExponentForTime is not None else []
        self.dimensionExponentForTime = [v if isinstance(v, str) else str(v) for v in self.dimensionExponentForTime]

        if self._is_empty(self.dimensionlessExponent):
            self.MissingRequiredField("dimensionlessExponent")
        if not isinstance(self.dimensionlessExponent, list):
            self.dimensionlessExponent = [self.dimensionlessExponent] if self.dimensionlessExponent is not None else []
        self.dimensionlessExponent = [v if isinstance(v, str) else str(v) for v in self.dimensionlessExponent]

        if not isinstance(self.hasReferenceQuantityKind, list):
            self.hasReferenceQuantityKind = [self.hasReferenceQuantityKind] if self.hasReferenceQuantityKind is not None else []
        self.hasReferenceQuantityKind = [v if isinstance(v, QuantityKindId) else QuantityKindId(v) for v in self.hasReferenceQuantityKind]

        if not isinstance(self.latexSymbol, list):
            self.latexSymbol = [self.latexSymbol] if self.latexSymbol is not None else []
        self.latexSymbol = [v if isinstance(v, str) else str(v) for v in self.latexSymbol]

        if not isinstance(self.latexDefinition, list):
            self.latexDefinition = [self.latexDefinition] if self.latexDefinition is not None else []
        self.latexDefinition = [v if isinstance(v, str) else str(v) for v in self.latexDefinition]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantityKindDimensionVectorSI(QuantityKindDimensionVector):
    """
    Quantity Kind Dimension vector (SI)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["QuantityKindDimensionVector_SI"]
    class_class_curie: ClassVar[str] = "qudt:QuantityKindDimensionVector_SI"
    class_name: ClassVar[str] = "QuantityKindDimensionVector_SI"
    class_model_uri: ClassVar[URIRef] = POKEMON.QuantityKindDimensionVectorSI

    id: Union[str, QuantityKindDimensionVectorSIId] = None
    dimensionExponentForAmountOfSubstance: Union[str, list[str]] = None
    dimensionExponentForElectricCurrent: Union[str, list[str]] = None
    dimensionExponentForLength: Union[str, list[str]] = None
    dimensionExponentForLuminousIntensity: Union[str, list[str]] = None
    dimensionExponentForMass: Union[str, list[str]] = None
    dimensionExponentForThermodynamicTemperature: Union[str, list[str]] = None
    dimensionExponentForTime: Union[str, list[str]] = None
    dimensionlessExponent: Union[str, list[str]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, QuantityKindDimensionVectorSIId):
            self.id = QuantityKindDimensionVectorSIId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Rule(Verifiable):
    """
    Rule
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Rule"]
    class_class_curie: ClassVar[str] = "qudt:Rule"
    class_name: ClassVar[str] = "Rule"
    class_model_uri: ClassVar[URIRef] = POKEMON.Rule

    id: Union[str, RuleId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    ruleType: Optional[Union[Union[str, RuleTypeId], list[Union[str, RuleTypeId]]]] = empty_list()
    rationale: Optional[Union[str, list[str]]] = empty_list()
    guidance: Optional[Union[str, list[str]]] = empty_list()
    qudt_id: Optional[Union[str, list[str]]] = empty_list()
    hasRule: Optional[Union[Union[str, RuleId], list[Union[str, RuleId]]]] = empty_list()
    isReplacedBy: Optional[Union[str, list[str]]] = empty_list()
    qudt_description: Optional[Union[str, list[str]]] = empty_list()
    abbreviation: Optional[Union[str, list[str]]] = empty_list()
    deprecated: Optional[Union[str, list[str]]] = empty_list()
    plainTextDescription: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RuleId):
            self.id = RuleId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.ruleType, list):
            self.ruleType = [self.ruleType] if self.ruleType is not None else []
        self.ruleType = [v if isinstance(v, RuleTypeId) else RuleTypeId(v) for v in self.ruleType]

        if not isinstance(self.rationale, list):
            self.rationale = [self.rationale] if self.rationale is not None else []
        self.rationale = [v if isinstance(v, str) else str(v) for v in self.rationale]

        if not isinstance(self.guidance, list):
            self.guidance = [self.guidance] if self.guidance is not None else []
        self.guidance = [v if isinstance(v, str) else str(v) for v in self.guidance]

        if not isinstance(self.qudt_id, list):
            self.qudt_id = [self.qudt_id] if self.qudt_id is not None else []
        self.qudt_id = [v if isinstance(v, str) else str(v) for v in self.qudt_id]

        if not isinstance(self.hasRule, list):
            self.hasRule = [self.hasRule] if self.hasRule is not None else []
        self.hasRule = [v if isinstance(v, RuleId) else RuleId(v) for v in self.hasRule]

        if not isinstance(self.isReplacedBy, list):
            self.isReplacedBy = [self.isReplacedBy] if self.isReplacedBy is not None else []
        self.isReplacedBy = [v if isinstance(v, str) else str(v) for v in self.isReplacedBy]

        if not isinstance(self.qudt_description, list):
            self.qudt_description = [self.qudt_description] if self.qudt_description is not None else []
        self.qudt_description = [v if isinstance(v, str) else str(v) for v in self.qudt_description]

        if not isinstance(self.abbreviation, list):
            self.abbreviation = [self.abbreviation] if self.abbreviation is not None else []
        self.abbreviation = [v if isinstance(v, str) else str(v) for v in self.abbreviation]

        if not isinstance(self.deprecated, list):
            self.deprecated = [self.deprecated] if self.deprecated is not None else []
        self.deprecated = [v if isinstance(v, str) else str(v) for v in self.deprecated]

        if not isinstance(self.plainTextDescription, list):
            self.plainTextDescription = [self.plainTextDescription] if self.plainTextDescription is not None else []
        self.plainTextDescription = [v if isinstance(v, str) else str(v) for v in self.plainTextDescription]

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

slots.protocolBuffersName = Slot(uri=QUDT.protocolBuffersName, name="protocolBuffersName", curie=QUDT.curie('protocolBuffersName'),
                   model_uri=POKEMON.protocolBuffersName, domain=None, range=Optional[Union[str, list[str]]])

slots.symbol = Slot(uri=QUDT.symbol, name="symbol", curie=QUDT.curie('symbol'),
                   model_uri=POKEMON.symbol, domain=None, range=Optional[Union[str, list[str]]])

slots.matlabName = Slot(uri=QUDT.matlabName, name="matlabName", curie=QUDT.curie('matlabName'),
                   model_uri=POKEMON.matlabName, domain=None, range=Optional[Union[str, list[str]]])

slots.uneceCommonCode = Slot(uri=QUDT.uneceCommonCode, name="uneceCommonCode", curie=QUDT.curie('uneceCommonCode'),
                   model_uri=POKEMON.uneceCommonCode, domain=None, range=Optional[Union[str, list[str]]])

slots.relativeStandardUncertainty = Slot(uri=QUDT.relativeStandardUncertainty, name="relativeStandardUncertainty", curie=QUDT.curie('relativeStandardUncertainty'),
                   model_uri=POKEMON.relativeStandardUncertainty, domain=None, range=Optional[Union[str, list[str]]])

slots.hasQuantityKind = Slot(uri=QUDT.hasQuantityKind, name="hasQuantityKind", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=POKEMON.hasQuantityKind, domain=None, range=Optional[Union[Union[str, QuantityKindId], list[Union[str, QuantityKindId]]]])

slots.default = Slot(uri=QUDT.default, name="default", curie=QUDT.curie('default'),
                   model_uri=POKEMON.default, domain=None, range=Optional[Union[str, list[str]]])

slots.quantityValue = Slot(uri=QUDT.quantityValue, name="quantityValue", curie=QUDT.curie('quantityValue'),
                   model_uri=POKEMON.quantityValue, domain=None, range=Optional[Union[Union[str, QuantityValueId], list[Union[str, QuantityValueId]]]])

slots.microsoftSQLServerName = Slot(uri=QUDT.microsoftSQLServerName, name="microsoftSQLServerName", curie=QUDT.curie('microsoftSQLServerName'),
                   model_uri=POKEMON.microsoftSQLServerName, domain=None, range=Optional[Union[str, list[str]]])

slots.hasDimensionVector = Slot(uri=QUDT.hasDimensionVector, name="hasDimensionVector", curie=QUDT.curie('hasDimensionVector'),
                   model_uri=POKEMON.hasDimensionVector, domain=None, range=Optional[Union[Union[str, QuantityKindDimensionVectorId], list[Union[str, QuantityKindDimensionVectorId]]]])

slots.dimensionExponentForTime = Slot(uri=QUDT.dimensionExponentForTime, name="dimensionExponentForTime", curie=QUDT.curie('dimensionExponentForTime'),
                   model_uri=POKEMON.dimensionExponentForTime, domain=None, range=Optional[Union[str, list[str]]])

slots.ucumCode = Slot(uri=QUDT.ucumCode, name="ucumCode", curie=QUDT.curie('ucumCode'),
                   model_uri=POKEMON.ucumCode, domain=None, range=Optional[Union[str, list[str]]])

slots.literal = Slot(uri=DTYPE.literal, name="literal", curie=DTYPE.curie('literal'),
                   model_uri=POKEMON.literal, domain=None, range=Optional[Union[str, list[str]]])

slots.hasFactorUnit = Slot(uri=QUDT.hasFactorUnit, name="hasFactorUnit", curie=QUDT.curie('hasFactorUnit'),
                   model_uri=POKEMON.hasFactorUnit, domain=None, range=Optional[Union[str, list[str]]])

slots.dimensionExponentForElectricCurrent = Slot(uri=QUDT.dimensionExponentForElectricCurrent, name="dimensionExponentForElectricCurrent", curie=QUDT.curie('dimensionExponentForElectricCurrent'),
                   model_uri=POKEMON.dimensionExponentForElectricCurrent, domain=None, range=Optional[Union[str, list[str]]])

slots.dimensionExponentForThermodynamicTemperature = Slot(uri=QUDT.dimensionExponentForThermodynamicTemperature, name="dimensionExponentForThermodynamicTemperature", curie=QUDT.curie('dimensionExponentForThermodynamicTemperature'),
                   model_uri=POKEMON.dimensionExponentForThermodynamicTemperature, domain=None, range=Optional[Union[str, list[str]]])

slots.systemDerivedQuantityKind = Slot(uri=QUDT.systemDerivedQuantityKind, name="systemDerivedQuantityKind", curie=QUDT.curie('systemDerivedQuantityKind'),
                   model_uri=POKEMON.systemDerivedQuantityKind, domain=None, range=Optional[Union[Union[str, QuantityKindId], list[Union[str, QuantityKindId]]]])

slots.dataEncoding = Slot(uri=QUDT.dataEncoding, name="dataEncoding", curie=QUDT.curie('dataEncoding'),
                   model_uri=POKEMON.dataEncoding, domain=None, range=Optional[Union[Union[str, DataEncodingId], list[Union[str, DataEncodingId]]]])

slots.applicableUnit = Slot(uri=QUDT.applicableUnit, name="applicableUnit", curie=QUDT.curie('applicableUnit'),
                   model_uri=POKEMON.applicableUnit, domain=None, range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]])

slots.orderedType = Slot(uri=QUDT.orderedType, name="orderedType", curie=QUDT.curie('orderedType'),
                   model_uri=POKEMON.orderedType, domain=None, range=Optional[Union[str, list[str]]])

slots.hasBaseQuantityKind = Slot(uri=QUDT.hasBaseQuantityKind, name="hasBaseQuantityKind", curie=QUDT.curie('hasBaseQuantityKind'),
                   model_uri=POKEMON.hasBaseQuantityKind, domain=None, range=Optional[Union[Union[str, QuantityKindId], list[Union[str, QuantityKindId]]]])

slots.prefix = Slot(uri=QUDT.prefix, name="prefix", curie=QUDT.curie('prefix'),
                   model_uri=POKEMON.prefix, domain=None, range=Optional[Union[Union[str, PrefixId], list[Union[str, PrefixId]]]])

slots.hasReferenceQuantityKind = Slot(uri=QUDT.hasReferenceQuantityKind, name="hasReferenceQuantityKind", curie=QUDT.curie('hasReferenceQuantityKind'),
                   model_uri=POKEMON.hasReferenceQuantityKind, domain=None, range=Optional[Union[str, list[str]]])

slots.latexSymbol = Slot(uri=QUDT.latexSymbol, name="latexSymbol", curie=QUDT.curie('latexSymbol'),
                   model_uri=POKEMON.latexSymbol, domain=None, range=Optional[Union[str, list[str]]])

slots.dimensionVectorForSI = Slot(uri=QUDT.dimensionVectorForSI, name="dimensionVectorForSI", curie=QUDT.curie('dimensionVectorForSI'),
                   model_uri=POKEMON.dimensionVectorForSI, domain=None, range=Optional[Union[Union[str, QuantityKindDimensionVectorSIId], list[Union[str, QuantityKindDimensionVectorSIId]]]])

slots.encoding = Slot(uri=QUDT.encoding, name="encoding", curie=QUDT.curie('encoding'),
                   model_uri=POKEMON.encoding, domain=None, range=Optional[Union[str, list[str]]])

slots.javaName = Slot(uri=QUDT.javaName, name="javaName", curie=QUDT.curie('javaName'),
                   model_uri=POKEMON.javaName, domain=None, range=Optional[Union[str, list[str]]])

slots.abbreviation = Slot(uri=QUDT.abbreviation, name="abbreviation", curie=QUDT.curie('abbreviation'),
                   model_uri=POKEMON.abbreviation, domain=None, range=Optional[Union[str, list[str]]])

slots.derivedUnitOfSystem = Slot(uri=QUDT.derivedUnitOfSystem, name="derivedUnitOfSystem", curie=QUDT.curie('derivedUnitOfSystem'),
                   model_uri=POKEMON.derivedUnitOfSystem, domain=None, range=Optional[Union[Union[str, SystemOfUnitsId], list[Union[str, SystemOfUnitsId]]]])

slots.valueSN = Slot(uri=QUDT.valueSN, name="valueSN", curie=QUDT.curie('valueSN'),
                   model_uri=POKEMON.valueSN, domain=None, range=Optional[Union[str, list[str]]])

slots.oleDBName = Slot(uri=QUDT.oleDBName, name="oleDBName", curie=QUDT.curie('oleDBName'),
                   model_uri=POKEMON.oleDBName, domain=None, range=Optional[Union[str, list[str]]])

slots.odbcName = Slot(uri=QUDT.odbcName, name="odbcName", curie=QUDT.curie('odbcName'),
                   model_uri=POKEMON.odbcName, domain=None, range=Optional[Union[str, list[str]]])

slots.unitFor = Slot(uri=QUDT.unitFor, name="unitFor", curie=QUDT.curie('unitFor'),
                   model_uri=POKEMON.unitFor, domain=None, range=Optional[Union[str, list[str]]])

slots.conversionMultiplier = Slot(uri=QUDT.conversionMultiplier, name="conversionMultiplier", curie=QUDT.curie('conversionMultiplier'),
                   model_uri=POKEMON.conversionMultiplier, domain=None, range=Optional[Union[str, list[str]]])

slots.isDeltaQuantity = Slot(uri=QUDT.isDeltaQuantity, name="isDeltaQuantity", curie=QUDT.curie('isDeltaQuantity'),
                   model_uri=POKEMON.isDeltaQuantity, domain=None, range=Optional[Union[str, list[str]]])

slots.applicableUSCustomaryUnit = Slot(uri=QUDT.applicableUSCustomaryUnit, name="applicableUSCustomaryUnit", curie=QUDT.curie('applicableUSCustomaryUnit'),
                   model_uri=POKEMON.applicableUSCustomaryUnit, domain=None, range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]])

slots.siUnitsExpression = Slot(uri=QUDT.siUnitsExpression, name="siUnitsExpression", curie=QUDT.curie('siUnitsExpression'),
                   model_uri=POKEMON.siUnitsExpression, domain=None, range=Optional[Union[str, list[str]]])

slots.conversionMultiplierSN = Slot(uri=QUDT.conversionMultiplierSN, name="conversionMultiplierSN", curie=QUDT.curie('conversionMultiplierSN'),
                   model_uri=POKEMON.conversionMultiplierSN, domain=None, range=Optional[Union[str, list[str]]])

slots.dimensionExponentForAmountOfSubstance = Slot(uri=QUDT.dimensionExponentForAmountOfSubstance, name="dimensionExponentForAmountOfSubstance", curie=QUDT.curie('dimensionExponentForAmountOfSubstance'),
                   model_uri=POKEMON.dimensionExponentForAmountOfSubstance, domain=None, range=Optional[Union[str, list[str]]])

slots.dimensionExponentForLength = Slot(uri=QUDT.dimensionExponentForLength, name="dimensionExponentForLength", curie=QUDT.curie('dimensionExponentForLength'),
                   model_uri=POKEMON.dimensionExponentForLength, domain=None, range=Optional[Union[str, list[str]]])

slots.bits = Slot(uri=QUDT.bits, name="bits", curie=QUDT.curie('bits'),
                   model_uri=POKEMON.bits, domain=None, range=Optional[Union[str, list[str]]])

slots.datatype = Slot(uri=QUDT.datatype, name="datatype", curie=QUDT.curie('datatype'),
                   model_uri=POKEMON.datatype, domain=None, range=Optional[Union[str, list[str]]])

slots.scalingOf = Slot(uri=QUDT.scalingOf, name="scalingOf", curie=QUDT.curie('scalingOf'),
                   model_uri=POKEMON.scalingOf, domain=None, range=Optional[Union[str, list[str]]])

slots.bytes = Slot(uri=QUDT.bytes, name="bytes", curie=QUDT.curie('bytes'),
                   model_uri=POKEMON.bytes, domain=None, range=Optional[Union[str, list[str]]])

slots.applicableISOUnit = Slot(uri=QUDT.applicableISOUnit, name="applicableISOUnit", curie=QUDT.curie('applicableISOUnit'),
                   model_uri=POKEMON.applicableISOUnit, domain=None, range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]])

slots.dbpediaMatch = Slot(uri=QUDT.dbpediaMatch, name="dbpediaMatch", curie=QUDT.curie('dbpediaMatch'),
                   model_uri=POKEMON.dbpediaMatch, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.dimensionlessExponent = Slot(uri=QUDT.dimensionlessExponent, name="dimensionlessExponent", curie=QUDT.curie('dimensionlessExponent'),
                   model_uri=POKEMON.dimensionlessExponent, domain=None, range=Optional[Union[str, list[str]]])

slots.qkdvDenominator = Slot(uri=QUDT.qkdvDenominator, name="qkdvDenominator", curie=QUDT.curie('qkdvDenominator'),
                   model_uri=POKEMON.qkdvDenominator, domain=None, range=Optional[Union[Union[str, QuantityKindDimensionVectorId], list[Union[str, QuantityKindDimensionVectorId]]]])

slots.udunitsCode = Slot(uri=QUDT.udunitsCode, name="udunitsCode", curie=QUDT.curie('udunitsCode'),
                   model_uri=POKEMON.udunitsCode, domain=None, range=Optional[Union[str, list[str]]])

slots.applicablePhysicalConstant = Slot(uri=QUDT.applicablePhysicalConstant, name="applicablePhysicalConstant", curie=QUDT.curie('applicablePhysicalConstant'),
                   model_uri=POKEMON.applicablePhysicalConstant, domain=None, range=Optional[Union[str, list[str]]])

slots.normativeReference = Slot(uri=QUDT.normativeReference, name="normativeReference", curie=QUDT.curie('normativeReference'),
                   model_uri=POKEMON.normativeReference, domain=None, range=Optional[Union[str, list[str]]])

slots.prefixMultiplier = Slot(uri=QUDT.prefixMultiplier, name="prefixMultiplier", curie=QUDT.curie('prefixMultiplier'),
                   model_uri=POKEMON.prefixMultiplier, domain=None, range=Optional[Union[str, list[str]]])

slots.hasAllowedUnit = Slot(uri=QUDT.hasAllowedUnit, name="hasAllowedUnit", curie=QUDT.curie('hasAllowedUnit'),
                   model_uri=POKEMON.hasAllowedUnit, domain=None, range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]])

slots.isoNormativeReference = Slot(uri=QUDT.isoNormativeReference, name="isoNormativeReference", curie=QUDT.curie('isoNormativeReference'),
                   model_uri=POKEMON.isoNormativeReference, domain=None, range=Optional[Union[str, list[str]]])

slots.omUnit = Slot(uri=QUDT.omUnit, name="omUnit", curie=QUDT.curie('omUnit'),
                   model_uri=POKEMON.omUnit, domain=None, range=Optional[Union[str, list[str]]])

slots.plainTextDescription = Slot(uri=QUDT.plainTextDescription, name="plainTextDescription", curie=QUDT.curie('plainTextDescription'),
                   model_uri=POKEMON.plainTextDescription, domain=None, range=Optional[Union[str, list[str]]])

slots.hasDefinedUnit = Slot(uri=QUDT.hasDefinedUnit, name="hasDefinedUnit", curie=QUDT.curie('hasDefinedUnit'),
                   model_uri=POKEMON.hasDefinedUnit, domain=None, range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]])

slots.oracleSQLName = Slot(uri=QUDT.oracleSQLName, name="oracleSQLName", curie=QUDT.curie('oracleSQLName'),
                   model_uri=POKEMON.oracleSQLName, domain=None, range=Optional[Union[str, list[str]]])

slots.byteOrder = Slot(uri=QUDT.byteOrder, name="byteOrder", curie=QUDT.curie('byteOrder'),
                   model_uri=POKEMON.byteOrder, domain=None, range=Optional[Union[Union[str, EndianTypeId], list[Union[str, EndianTypeId]]]])

slots.mathDefinition = Slot(uri=QUDT.mathDefinition, name="mathDefinition", curie=QUDT.curie('mathDefinition'),
                   model_uri=POKEMON.mathDefinition, domain=None, range=Optional[Union[str, list[str]]])

slots.conversionOffset = Slot(uri=QUDT.conversionOffset, name="conversionOffset", curie=QUDT.curie('conversionOffset'),
                   model_uri=POKEMON.conversionOffset, domain=None, range=Optional[Union[str, list[str]]])

slots.cardinality = Slot(uri=QUDT.cardinality, name="cardinality", curie=QUDT.curie('cardinality'),
                   model_uri=POKEMON.cardinality, domain=None, range=Optional[Union[str, list[str]]])

slots.applicableImperialUnit = Slot(uri=QUDT.applicableImperialUnit, name="applicableImperialUnit", curie=QUDT.curie('applicableImperialUnit'),
                   model_uri=POKEMON.applicableImperialUnit, domain=None, range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]])

slots.vbName = Slot(uri=QUDT.vbName, name="vbName", curie=QUDT.curie('vbName'),
                   model_uri=POKEMON.vbName, domain=None, range=Optional[Union[str, list[str]]])

slots.pythonName = Slot(uri=QUDT.pythonName, name="pythonName", curie=QUDT.curie('pythonName'),
                   model_uri=POKEMON.pythonName, domain=None, range=Optional[Union[str, list[str]]])

slots.wikidataMatch = Slot(uri=QUDT.wikidataMatch, name="wikidataMatch", curie=QUDT.curie('wikidataMatch'),
                   model_uri=POKEMON.wikidataMatch, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.latexDefinition = Slot(uri=QUDT.latexDefinition, name="latexDefinition", curie=QUDT.curie('latexDefinition'),
                   model_uri=POKEMON.latexDefinition, domain=None, range=Optional[Union[str, list[str]]])

slots.exactConstant = Slot(uri=QUDT.exactConstant, name="exactConstant", curie=QUDT.curie('exactConstant'),
                   model_uri=POKEMON.exactConstant, domain=None, range=Optional[Union[str, list[str]]])

slots.ansiSQLName = Slot(uri=QUDT.ansiSQLName, name="ansiSQLName", curie=QUDT.curie('ansiSQLName'),
                   model_uri=POKEMON.ansiSQLName, domain=None, range=Optional[Union[str, list[str]]])

slots.factorUnitScalar = Slot(uri=QUDT.factorUnitScalar, name="factorUnitScalar", curie=QUDT.curie('factorUnitScalar'),
                   model_uri=POKEMON.factorUnitScalar, domain=None, range=Optional[Union[str, list[str]]])

slots.dimensionExponentForMass = Slot(uri=QUDT.dimensionExponentForMass, name="dimensionExponentForMass", curie=QUDT.curie('dimensionExponentForMass'),
                   model_uri=POKEMON.dimensionExponentForMass, domain=None, range=Optional[Union[str, list[str]]])

slots.mySQLName = Slot(uri=QUDT.mySQLName, name="mySQLName", curie=QUDT.curie('mySQLName'),
                   model_uri=POKEMON.mySQLName, domain=None, range=Optional[Union[str, list[str]]])

slots.dimensionExponentForLuminousIntensity = Slot(uri=QUDT.dimensionExponentForLuminousIntensity, name="dimensionExponentForLuminousIntensity", curie=QUDT.curie('dimensionExponentForLuminousIntensity'),
                   model_uri=POKEMON.dimensionExponentForLuminousIntensity, domain=None, range=Optional[Union[str, list[str]]])

slots.hasCoherentUnit = Slot(uri=QUDT.hasCoherentUnit, name="hasCoherentUnit", curie=QUDT.curie('hasCoherentUnit'),
                   model_uri=POKEMON.hasCoherentUnit, domain=None, range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]])

slots.mathMLdefinition = Slot(uri=QUDT.mathMLdefinition, name="mathMLdefinition", curie=QUDT.curie('mathMLdefinition'),
                   model_uri=POKEMON.mathMLdefinition, domain=None, range=Optional[Union[str, list[str]]])

slots.bounded = Slot(uri=QUDT.bounded, name="bounded", curie=QUDT.curie('bounded'),
                   model_uri=POKEMON.bounded, domain=None, range=Optional[Union[str, list[str]]])

slots.hasReciprocalUnit = Slot(uri=QUDT.hasReciprocalUnit, name="hasReciprocalUnit", curie=QUDT.curie('hasReciprocalUnit'),
                   model_uri=POKEMON.hasReciprocalUnit, domain=None, range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]])

slots.applicableSystem = Slot(uri=QUDT.applicableSystem, name="applicableSystem", curie=QUDT.curie('applicableSystem'),
                   model_uri=POKEMON.applicableSystem, domain=None, range=Optional[Union[str, list[str]]])

slots.ruleType = Slot(uri=QUDT.ruleType, name="ruleType", curie=QUDT.curie('ruleType'),
                   model_uri=POKEMON.ruleType, domain=None, range=Optional[Union[str, list[str]]])

slots.isUnitOfSystem = Slot(uri=QUDT.isUnitOfSystem, name="isUnitOfSystem", curie=QUDT.curie('isUnitOfSystem'),
                   model_uri=POKEMON.isUnitOfSystem, domain=None, range=Optional[Union[Union[str, SystemOfUnitsId], list[Union[str, SystemOfUnitsId]]]])

slots.altSymbol = Slot(uri=QUDT.altSymbol, name="altSymbol", curie=QUDT.curie('altSymbol'),
                   model_uri=POKEMON.altSymbol, domain=None, range=Optional[Union[str, list[str]]])

slots.definedUnitOfSystem = Slot(uri=QUDT.definedUnitOfSystem, name="definedUnitOfSystem", curie=QUDT.curie('definedUnitOfSystem'),
                   model_uri=POKEMON.definedUnitOfSystem, domain=None, range=Optional[Union[Union[str, SystemOfUnitsId], list[Union[str, SystemOfUnitsId]]]])

slots.qkdvNumerator = Slot(uri=QUDT.qkdvNumerator, name="qkdvNumerator", curie=QUDT.curie('qkdvNumerator'),
                   model_uri=POKEMON.qkdvNumerator, domain=None, range=Optional[Union[Union[str, QuantityKindDimensionVectorId], list[Union[str, QuantityKindDimensionVectorId]]]])

slots.applicableSIUnit = Slot(uri=QUDT.applicableSIUnit, name="applicableSIUnit", curie=QUDT.curie('applicableSIUnit'),
                   model_uri=POKEMON.applicableSIUnit, domain=None, range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]])

slots.hasRule = Slot(uri=QUDT.hasRule, name="hasRule", curie=QUDT.curie('hasRule'),
                   model_uri=POKEMON.hasRule, domain=None, range=Optional[Union[str, list[str]]])

slots.basis = Slot(uri=QUDT.basis, name="basis", curie=QUDT.curie('basis'),
                   model_uri=POKEMON.basis, domain=None, range=Optional[Union[str, list[str]]])

slots.hasBaseUnit = Slot(uri=QUDT.hasBaseUnit, name="hasBaseUnit", curie=QUDT.curie('hasBaseUnit'),
                   model_uri=POKEMON.hasBaseUnit, domain=None, range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]])

slots.hasDerivedUnit = Slot(uri=QUDT.hasDerivedUnit, name="hasDerivedUnit", curie=QUDT.curie('hasDerivedUnit'),
                   model_uri=POKEMON.hasDerivedUnit, domain=None, range=Optional[Union[str, list[str]]])

slots.hasUnit = Slot(uri=QUDT.hasUnit, name="hasUnit", curie=QUDT.curie('hasUnit'),
                   model_uri=POKEMON.hasUnit, domain=None, range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]])

slots.baseDimensionEnumeration = Slot(uri=QUDT.baseDimensionEnumeration, name="baseDimensionEnumeration", curie=QUDT.curie('baseDimensionEnumeration'),
                   model_uri=POKEMON.baseDimensionEnumeration, domain=None, range=Optional[Union[Union[str, EnumerationId], list[Union[str, EnumerationId]]]])

slots.hasDerivedCoherentUnit = Slot(uri=QUDT.hasDerivedCoherentUnit, name="hasDerivedCoherentUnit", curie=QUDT.curie('hasDerivedCoherentUnit'),
                   model_uri=POKEMON.hasDerivedCoherentUnit, domain=None, range=Optional[Union[str, list[str]]])

slots.rationale = Slot(uri=QUDT.rationale, name="rationale", curie=QUDT.curie('rationale'),
                   model_uri=POKEMON.rationale, domain=None, range=Optional[Union[str, list[str]]])

slots.standardUncertainty = Slot(uri=QUDT.standardUncertainty, name="standardUncertainty", curie=QUDT.curie('standardUncertainty'),
                   model_uri=POKEMON.standardUncertainty, domain=None, range=Optional[Union[str, list[str]]])

slots.belongsToSystemOfQuantities = Slot(uri=QUDT.belongsToSystemOfQuantities, name="belongsToSystemOfQuantities", curie=QUDT.curie('belongsToSystemOfQuantities'),
                   model_uri=POKEMON.belongsToSystemOfQuantities, domain=None, range=Optional[Union[Union[str, SystemOfQuantityKindsId], list[Union[str, SystemOfQuantityKindsId]]]])

slots.iec61360Code = Slot(uri=QUDT.iec61360Code, name="iec61360Code", curie=QUDT.curie('iec61360Code'),
                   model_uri=POKEMON.iec61360Code, domain=None, range=Optional[Union[str, list[str]]])

slots.guidance = Slot(uri=QUDT.guidance, name="guidance", curie=QUDT.curie('guidance'),
                   model_uri=POKEMON.guidance, domain=None, range=Optional[Union[str, list[str]]])

slots.cName = Slot(uri=QUDT.cName, name="cName", curie=QUDT.curie('cName'),
                   model_uri=POKEMON.cName, domain=None, range=Optional[Union[str, list[str]]])

slots.bitOrder = Slot(uri=QUDT.bitOrder, name="bitOrder", curie=QUDT.curie('bitOrder'),
                   model_uri=POKEMON.bitOrder, domain=None, range=Optional[Union[Union[str, EndianTypeId], list[Union[str, EndianTypeId]]]])

slots.isReplacedBy = Slot(uri=DCTERMS.isReplacedBy, name="isReplacedBy", curie=DCTERMS.curie('isReplacedBy'),
                   model_uri=POKEMON.isReplacedBy, domain=None, range=Optional[Union[str, list[str]]])

slots.exactMatch = Slot(uri=QUDT.exactMatch, name="exactMatch", curie=QUDT.curie('exactMatch'),
                   model_uri=POKEMON.exactMatch, domain=None, range=Optional[Union[str, list[str]]])

slots.derivedCoherentUnitOfSystem = Slot(uri=QUDT.derivedCoherentUnitOfSystem, name="derivedCoherentUnitOfSystem", curie=QUDT.curie('derivedCoherentUnitOfSystem'),
                   model_uri=POKEMON.derivedCoherentUnitOfSystem, domain=None, range=Optional[Union[Union[str, SystemOfUnitsId], list[Union[str, SystemOfUnitsId]]]])

slots.element = Slot(uri=QUDT.element, name="element", curie=QUDT.curie('element'),
                   model_uri=POKEMON.element, domain=None, range=Optional[Union[str, list[str]]])

slots.jsName = Slot(uri=QUDT.jsName, name="jsName", curie=QUDT.curie('jsName'),
                   model_uri=POKEMON.jsName, domain=None, range=Optional[Union[str, list[str]]])

slots.conversionOffsetSN = Slot(uri=QUDT.conversionOffsetSN, name="conversionOffsetSN", curie=QUDT.curie('conversionOffsetSN'),
                   model_uri=POKEMON.conversionOffsetSN, domain=None, range=Optional[Union[str, list[str]]])

slots.hasUnitSystem = Slot(uri=QUDT.hasUnitSystem, name="hasUnitSystem", curie=QUDT.curie('hasUnitSystem'),
                   model_uri=POKEMON.hasUnitSystem, domain=None, range=Optional[Union[str, list[str]]])

slots.standardUncertaintySN = Slot(uri=QUDT.standardUncertaintySN, name="standardUncertaintySN", curie=QUDT.curie('standardUncertaintySN'),
                   model_uri=POKEMON.standardUncertaintySN, domain=None, range=Optional[Union[str, list[str]]])

slots.applicableCGSUnit = Slot(uri=QUDT.applicableCGSUnit, name="applicableCGSUnit", curie=QUDT.curie('applicableCGSUnit'),
                   model_uri=POKEMON.applicableCGSUnit, domain=None, range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]])

slots.deprecated = Slot(uri=QUDT.deprecated, name="deprecated", curie=QUDT.curie('deprecated'),
                   model_uri=POKEMON.deprecated, domain=None, range=Optional[Union[str, list[str]]])

slots.qudt_id = Slot(uri=QUDT.id, name="qudt_id", curie=QUDT.curie('id'),
                   model_uri=POKEMON.qudt_id, domain=None, range=Optional[Union[str, list[str]]])

slots.qudt_value = Slot(uri=QUDT.value, name="qudt_value", curie=QUDT.curie('value'),
                   model_uri=POKEMON.qudt_value, domain=None, range=Optional[Union[str, list[str]]])

slots.qudt_description = Slot(uri=DC.description, name="qudt_description", curie=DC.curie('description'),
                   model_uri=POKEMON.qudt_description, domain=None, range=Optional[Union[str, list[str]]])

slots.broader = Slot(uri=POKEMON.broader, name="broader", curie=POKEMON.curie('broader'),
                   model_uri=POKEMON.broader, domain=None, range=Optional[Union[str, QuantityKindId]])

slots.NamedIndividual_name = Slot(uri=RDFS.label, name="NamedIndividual_name", curie=RDFS.curie('label'),
                   model_uri=POKEMON.NamedIndividual_name, domain=NamedIndividual, range=str)

slots.SystemOfQuantityKinds_baseDimensionEnumeration = Slot(uri=QUDT.baseDimensionEnumeration, name="SystemOfQuantityKinds_baseDimensionEnumeration", curie=QUDT.curie('baseDimensionEnumeration'),
                   model_uri=POKEMON.SystemOfQuantityKinds_baseDimensionEnumeration, domain=SystemOfQuantityKinds, range=Optional[Union[Union[str, EnumerationId], list[Union[str, EnumerationId]]]])

slots.SystemOfQuantityKinds_hasBaseQuantityKind = Slot(uri=QUDT.hasBaseQuantityKind, name="SystemOfQuantityKinds_hasBaseQuantityKind", curie=QUDT.curie('hasBaseQuantityKind'),
                   model_uri=POKEMON.SystemOfQuantityKinds_hasBaseQuantityKind, domain=SystemOfQuantityKinds, range=Optional[Union[Union[str, QuantityKindId], list[Union[str, QuantityKindId]]]])

slots.SystemOfQuantityKinds_hasQuantityKind = Slot(uri=QUDT.hasQuantityKind, name="SystemOfQuantityKinds_hasQuantityKind", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=POKEMON.SystemOfQuantityKinds_hasQuantityKind, domain=SystemOfQuantityKinds, range=Optional[Union[Union[str, QuantityKindId], list[Union[str, QuantityKindId]]]])

slots.SystemOfQuantityKinds_hasUnitSystem = Slot(uri=QUDT.hasUnitSystem, name="SystemOfQuantityKinds_hasUnitSystem", curie=QUDT.curie('hasUnitSystem'),
                   model_uri=POKEMON.SystemOfQuantityKinds_hasUnitSystem, domain=SystemOfQuantityKinds, range=Optional[Union[Union[str, SystemOfUnitsId], list[Union[str, SystemOfUnitsId]]]])

slots.SystemOfQuantityKinds_systemDerivedQuantityKind = Slot(uri=QUDT.systemDerivedQuantityKind, name="SystemOfQuantityKinds_systemDerivedQuantityKind", curie=QUDT.curie('systemDerivedQuantityKind'),
                   model_uri=POKEMON.SystemOfQuantityKinds_systemDerivedQuantityKind, domain=SystemOfQuantityKinds, range=Optional[Union[Union[str, QuantityKindId], list[Union[str, QuantityKindId]]]])

slots.Quantity_hasQuantityKind = Slot(uri=QUDT.hasQuantityKind, name="Quantity_hasQuantityKind", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=POKEMON.Quantity_hasQuantityKind, domain=Quantity, range=Optional[Union[Union[str, QuantityKindId], list[Union[str, QuantityKindId]]]])

slots.Quantity_quantityValue = Slot(uri=QUDT.quantityValue, name="Quantity_quantityValue", curie=QUDT.curie('quantityValue'),
                   model_uri=POKEMON.Quantity_quantityValue, domain=Quantity, range=Optional[Union[Union[str, QuantityValueId], list[Union[str, QuantityValueId]]]])

slots.Quantity_isDeltaQuantity = Slot(uri=QUDT.isDeltaQuantity, name="Quantity_isDeltaQuantity", curie=QUDT.curie('isDeltaQuantity'),
                   model_uri=POKEMON.Quantity_isDeltaQuantity, domain=Quantity, range=Optional[Union[Union[bool, Bool], list[Union[bool, Bool]]]])

slots.Quantifiable_dataEncoding = Slot(uri=QUDT.dataEncoding, name="Quantifiable_dataEncoding", curie=QUDT.curie('dataEncoding'),
                   model_uri=POKEMON.Quantifiable_dataEncoding, domain=Quantifiable, range=Optional[Union[Union[str, DataEncodingId], list[Union[str, DataEncodingId]]]])

slots.Quantifiable_datatype = Slot(uri=QUDT.datatype, name="Quantifiable_datatype", curie=QUDT.curie('datatype'),
                   model_uri=POKEMON.Quantifiable_datatype, domain=Quantifiable, range=Optional[Union[Union[str, DatatypeId], list[Union[str, DatatypeId]]]])

slots.Quantifiable_hasUnit = Slot(uri=QUDT.hasUnit, name="Quantifiable_hasUnit", curie=QUDT.curie('hasUnit'),
                   model_uri=POKEMON.Quantifiable_hasUnit, domain=Quantifiable, range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]])

slots.Quantifiable_relativeStandardUncertainty = Slot(uri=QUDT.relativeStandardUncertainty, name="Quantifiable_relativeStandardUncertainty", curie=QUDT.curie('relativeStandardUncertainty'),
                   model_uri=POKEMON.Quantifiable_relativeStandardUncertainty, domain=Quantifiable, range=Optional[Union[float, list[float]]])

slots.Quantifiable_standardUncertainty = Slot(uri=QUDT.standardUncertainty, name="Quantifiable_standardUncertainty", curie=QUDT.curie('standardUncertainty'),
                   model_uri=POKEMON.Quantifiable_standardUncertainty, domain=Quantifiable, range=Optional[Union[Decimal, list[Decimal]]])

slots.Quantifiable_standardUncertaintySN = Slot(uri=QUDT.standardUncertaintySN, name="Quantifiable_standardUncertaintySN", curie=QUDT.curie('standardUncertaintySN'),
                   model_uri=POKEMON.Quantifiable_standardUncertaintySN, domain=Quantifiable, range=Optional[Union[float, list[float]]])

slots.Quantifiable_qudt_value = Slot(uri=QUDT.value, name="Quantifiable_qudt_value", curie=QUDT.curie('value'),
                   model_uri=POKEMON.Quantifiable_qudt_value, domain=Quantifiable, range=Optional[Union[str, list[str]]])

slots.Quantifiable_valueSN = Slot(uri=QUDT.valueSN, name="Quantifiable_valueSN", curie=QUDT.curie('valueSN'),
                   model_uri=POKEMON.Quantifiable_valueSN, domain=Quantifiable, range=Optional[Union[str, list[str]]])

slots.CardinalityType_literal = Slot(uri=DTYPE.literal, name="CardinalityType_literal", curie=DTYPE.curie('literal'),
                   model_uri=POKEMON.CardinalityType_literal, domain=CardinalityType, range=Optional[Union[str, list[str]]])

slots.PhysicalConstant_applicableSystem = Slot(uri=QUDT.applicableSystem, name="PhysicalConstant_applicableSystem", curie=QUDT.curie('applicableSystem'),
                   model_uri=POKEMON.PhysicalConstant_applicableSystem, domain=PhysicalConstant, range=Optional[Union[Union[str, SystemOfUnitsId], list[Union[str, SystemOfUnitsId]]]])

slots.PhysicalConstant_applicableUnit = Slot(uri=QUDT.applicableUnit, name="PhysicalConstant_applicableUnit", curie=QUDT.curie('applicableUnit'),
                   model_uri=POKEMON.PhysicalConstant_applicableUnit, domain=PhysicalConstant, range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]])

slots.PhysicalConstant_exactMatch = Slot(uri=QUDT.exactMatch, name="PhysicalConstant_exactMatch", curie=QUDT.curie('exactMatch'),
                   model_uri=POKEMON.PhysicalConstant_exactMatch, domain=PhysicalConstant, range=Optional[Union[Union[str, PhysicalConstantId], list[Union[str, PhysicalConstantId]]]])

slots.PhysicalConstant_hasDimensionVector = Slot(uri=QUDT.hasDimensionVector, name="PhysicalConstant_hasDimensionVector", curie=QUDT.curie('hasDimensionVector'),
                   model_uri=POKEMON.PhysicalConstant_hasDimensionVector, domain=PhysicalConstant, range=Optional[Union[Union[str, QuantityKindDimensionVectorId], list[Union[str, QuantityKindDimensionVectorId]]]])

slots.PhysicalConstant_ucumCode = Slot(uri=QUDT.ucumCode, name="PhysicalConstant_ucumCode", curie=QUDT.curie('ucumCode'),
                   model_uri=POKEMON.PhysicalConstant_ucumCode, domain=PhysicalConstant, range=Optional[Union[str, list[str]]])

slots.PhysicalConstant_exactConstant = Slot(uri=QUDT.exactConstant, name="PhysicalConstant_exactConstant", curie=QUDT.curie('exactConstant'),
                   model_uri=POKEMON.PhysicalConstant_exactConstant, domain=PhysicalConstant, range=Optional[Union[Union[bool, Bool], list[Union[bool, Bool]]]])

slots.PhysicalConstant_altSymbol = Slot(uri=QUDT.altSymbol, name="PhysicalConstant_altSymbol", curie=QUDT.curie('altSymbol'),
                   model_uri=POKEMON.PhysicalConstant_altSymbol, domain=PhysicalConstant, range=Optional[Union[str, list[str]]])

slots.PhysicalConstant_isoNormativeReference = Slot(uri=QUDT.isoNormativeReference, name="PhysicalConstant_isoNormativeReference", curie=QUDT.curie('isoNormativeReference'),
                   model_uri=POKEMON.PhysicalConstant_isoNormativeReference, domain=PhysicalConstant, range=Optional[Union[str, list[str]]])

slots.PhysicalConstant_latexSymbol = Slot(uri=QUDT.latexSymbol, name="PhysicalConstant_latexSymbol", curie=QUDT.curie('latexSymbol'),
                   model_uri=POKEMON.PhysicalConstant_latexSymbol, domain=PhysicalConstant, range=Optional[Union[str, list[str]]])

slots.PhysicalConstant_normativeReference = Slot(uri=QUDT.normativeReference, name="PhysicalConstant_normativeReference", curie=QUDT.curie('normativeReference'),
                   model_uri=POKEMON.PhysicalConstant_normativeReference, domain=PhysicalConstant, range=Optional[Union[str, list[str]]])

slots.PhysicalConstant_symbol = Slot(uri=QUDT.symbol, name="PhysicalConstant_symbol", curie=QUDT.curie('symbol'),
                   model_uri=POKEMON.PhysicalConstant_symbol, domain=PhysicalConstant, range=Optional[Union[str, list[str]]])

slots.PhysicalConstant_latexDefinition = Slot(uri=QUDT.latexDefinition, name="PhysicalConstant_latexDefinition", curie=QUDT.curie('latexDefinition'),
                   model_uri=POKEMON.PhysicalConstant_latexDefinition, domain=PhysicalConstant, range=Optional[Union[str, list[str]]])

slots.PhysicalConstant_mathMLdefinition = Slot(uri=QUDT.mathMLdefinition, name="PhysicalConstant_mathMLdefinition", curie=QUDT.curie('mathMLdefinition'),
                   model_uri=POKEMON.PhysicalConstant_mathMLdefinition, domain=PhysicalConstant, range=Optional[Union[str, list[str]]])

slots.Encoding_bits = Slot(uri=QUDT.bits, name="Encoding_bits", curie=QUDT.curie('bits'),
                   model_uri=POKEMON.Encoding_bits, domain=Encoding, range=Optional[Union[str, list[str]]])

slots.Encoding_bytes = Slot(uri=QUDT.bytes, name="Encoding_bytes", curie=QUDT.curie('bytes'),
                   model_uri=POKEMON.Encoding_bytes, domain=Encoding, range=Optional[Union[str, list[str]]])

slots.Enumeration_default = Slot(uri=QUDT.default, name="Enumeration_default", curie=QUDT.curie('default'),
                   model_uri=POKEMON.Enumeration_default, domain=Enumeration, range=Optional[Union[Union[str, EnumeratedValueId], list[Union[str, EnumeratedValueId]]]])

slots.Enumeration_element = Slot(uri=QUDT.element, name="Enumeration_element", curie=QUDT.curie('element'),
                   model_uri=POKEMON.Enumeration_element, domain=Enumeration, range=Union[Union[str, EnumeratedValueId], list[Union[str, EnumeratedValueId]]])

slots.Enumeration_abbreviation = Slot(uri=QUDT.abbreviation, name="Enumeration_abbreviation", curie=QUDT.curie('abbreviation'),
                   model_uri=POKEMON.Enumeration_abbreviation, domain=Enumeration, range=Optional[Union[str, list[str]]])

slots.SystemOfUnits_applicablePhysicalConstant = Slot(uri=QUDT.applicablePhysicalConstant, name="SystemOfUnits_applicablePhysicalConstant", curie=QUDT.curie('applicablePhysicalConstant'),
                   model_uri=POKEMON.SystemOfUnits_applicablePhysicalConstant, domain=SystemOfUnits, range=Optional[Union[Union[str, PhysicalConstantId], list[Union[str, PhysicalConstantId]]]])

slots.SystemOfUnits_hasAllowedUnit = Slot(uri=QUDT.hasAllowedUnit, name="SystemOfUnits_hasAllowedUnit", curie=QUDT.curie('hasAllowedUnit'),
                   model_uri=POKEMON.SystemOfUnits_hasAllowedUnit, domain=SystemOfUnits, range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]])

slots.SystemOfUnits_hasBaseUnit = Slot(uri=QUDT.hasBaseUnit, name="SystemOfUnits_hasBaseUnit", curie=QUDT.curie('hasBaseUnit'),
                   model_uri=POKEMON.SystemOfUnits_hasBaseUnit, domain=SystemOfUnits, range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]])

slots.SystemOfUnits_hasCoherentUnit = Slot(uri=QUDT.hasCoherentUnit, name="SystemOfUnits_hasCoherentUnit", curie=QUDT.curie('hasCoherentUnit'),
                   model_uri=POKEMON.SystemOfUnits_hasCoherentUnit, domain=SystemOfUnits, range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]])

slots.SystemOfUnits_hasDefinedUnit = Slot(uri=QUDT.hasDefinedUnit, name="SystemOfUnits_hasDefinedUnit", curie=QUDT.curie('hasDefinedUnit'),
                   model_uri=POKEMON.SystemOfUnits_hasDefinedUnit, domain=SystemOfUnits, range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]])

slots.SystemOfUnits_hasDerivedCoherentUnit = Slot(uri=QUDT.hasDerivedCoherentUnit, name="SystemOfUnits_hasDerivedCoherentUnit", curie=QUDT.curie('hasDerivedCoherentUnit'),
                   model_uri=POKEMON.SystemOfUnits_hasDerivedCoherentUnit, domain=SystemOfUnits, range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]])

slots.SystemOfUnits_hasDerivedUnit = Slot(uri=QUDT.hasDerivedUnit, name="SystemOfUnits_hasDerivedUnit", curie=QUDT.curie('hasDerivedUnit'),
                   model_uri=POKEMON.SystemOfUnits_hasDerivedUnit, domain=SystemOfUnits, range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]])

slots.SystemOfUnits_hasUnit = Slot(uri=QUDT.hasUnit, name="SystemOfUnits_hasUnit", curie=QUDT.curie('hasUnit'),
                   model_uri=POKEMON.SystemOfUnits_hasUnit, domain=SystemOfUnits, range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]])

slots.SystemOfUnits_prefix = Slot(uri=QUDT.prefix, name="SystemOfUnits_prefix", curie=QUDT.curie('prefix'),
                   model_uri=POKEMON.SystemOfUnits_prefix, domain=SystemOfUnits, range=Optional[Union[Union[str, PrefixId], list[Union[str, PrefixId]]]])

slots.Prefix_exactMatch = Slot(uri=QUDT.exactMatch, name="Prefix_exactMatch", curie=QUDT.curie('exactMatch'),
                   model_uri=POKEMON.Prefix_exactMatch, domain=Prefix, range=Optional[Union[Union[str, PrefixId], list[Union[str, PrefixId]]]])

slots.Prefix_ucumCode = Slot(uri=QUDT.ucumCode, name="Prefix_ucumCode", curie=QUDT.curie('ucumCode'),
                   model_uri=POKEMON.Prefix_ucumCode, domain=Prefix, range=Optional[Union[Union[str, UCUMcs-termId], list[Union[str, UCUMcs-termId]]]])

slots.Prefix_altSymbol = Slot(uri=QUDT.altSymbol, name="Prefix_altSymbol", curie=QUDT.curie('altSymbol'),
                   model_uri=POKEMON.Prefix_altSymbol, domain=Prefix, range=Optional[Union[str, list[str]]])

slots.Prefix_latexSymbol = Slot(uri=QUDT.latexSymbol, name="Prefix_latexSymbol", curie=QUDT.curie('latexSymbol'),
                   model_uri=POKEMON.Prefix_latexSymbol, domain=Prefix, range=Optional[Union[str, list[str]]])

slots.Prefix_symbol = Slot(uri=QUDT.symbol, name="Prefix_symbol", curie=QUDT.curie('symbol'),
                   model_uri=POKEMON.Prefix_symbol, domain=Prefix, range=Optional[Union[str, list[str]]])

slots.Prefix_prefixMultiplier = Slot(uri=QUDT.prefixMultiplier, name="Prefix_prefixMultiplier", curie=QUDT.curie('prefixMultiplier'),
                   model_uri=POKEMON.Prefix_prefixMultiplier, domain=Prefix, range=Optional[Union[str, list[str]]])

slots.AbstractQuantityKind_broader = Slot(uri=POKEMON.broader, name="AbstractQuantityKind_broader", curie=POKEMON.curie('broader'),
                   model_uri=POKEMON.AbstractQuantityKind_broader, domain=AbstractQuantityKind, range=Optional[Union[str, QuantityKindId]])

slots.AbstractQuantityKind_altSymbol = Slot(uri=QUDT.altSymbol, name="AbstractQuantityKind_altSymbol", curie=QUDT.curie('altSymbol'),
                   model_uri=POKEMON.AbstractQuantityKind_altSymbol, domain=AbstractQuantityKind, range=Optional[Union[str, list[str]]])

slots.AbstractQuantityKind_latexSymbol = Slot(uri=QUDT.latexSymbol, name="AbstractQuantityKind_latexSymbol", curie=QUDT.curie('latexSymbol'),
                   model_uri=POKEMON.AbstractQuantityKind_latexSymbol, domain=AbstractQuantityKind, range=Optional[Union[str, list[str]]])

slots.AbstractQuantityKind_symbol = Slot(uri=QUDT.symbol, name="AbstractQuantityKind_symbol", curie=QUDT.curie('symbol'),
                   model_uri=POKEMON.AbstractQuantityKind_symbol, domain=AbstractQuantityKind, range=Optional[Union[str, list[str]]])

slots.OrderedType_literal = Slot(uri=DTYPE.literal, name="OrderedType_literal", curie=DTYPE.curie('literal'),
                   model_uri=POKEMON.OrderedType_literal, domain=OrderedType, range=Optional[Union[str, list[str]]])

slots.EnumeratedValue_altSymbol = Slot(uri=QUDT.altSymbol, name="EnumeratedValue_altSymbol", curie=QUDT.curie('altSymbol'),
                   model_uri=POKEMON.EnumeratedValue_altSymbol, domain=EnumeratedValue, range=Optional[Union[str, list[str]]])

slots.EnumeratedValue_qudt_description = Slot(uri=DC.description, name="EnumeratedValue_qudt_description", curie=DC.curie('description'),
                   model_uri=POKEMON.EnumeratedValue_qudt_description, domain=EnumeratedValue, range=Optional[Union[str, list[str]]])

slots.EnumeratedValue_abbreviation = Slot(uri=QUDT.abbreviation, name="EnumeratedValue_abbreviation", curie=QUDT.curie('abbreviation'),
                   model_uri=POKEMON.EnumeratedValue_abbreviation, domain=EnumeratedValue, range=Optional[Union[str, list[str]]])

slots.EnumeratedValue_symbol = Slot(uri=QUDT.symbol, name="EnumeratedValue_symbol", curie=QUDT.curie('symbol'),
                   model_uri=POKEMON.EnumeratedValue_symbol, domain=EnumeratedValue, range=Optional[Union[str, list[str]]])

slots.Concept_hasRule = Slot(uri=QUDT.hasRule, name="Concept_hasRule", curie=QUDT.curie('hasRule'),
                   model_uri=POKEMON.Concept_hasRule, domain=Concept, range=Optional[Union[Union[str, RuleId], list[Union[str, RuleId]]]])

slots.Concept_isReplacedBy = Slot(uri=DCTERMS.isReplacedBy, name="Concept_isReplacedBy", curie=DCTERMS.curie('isReplacedBy'),
                   model_uri=POKEMON.Concept_isReplacedBy, domain=Concept, range=Optional[Union[str, list[str]]])

slots.Concept_qudt_description = Slot(uri=DC.description, name="Concept_qudt_description", curie=DC.curie('description'),
                   model_uri=POKEMON.Concept_qudt_description, domain=Concept, range=Optional[Union[str, list[str]]])

slots.Concept_abbreviation = Slot(uri=QUDT.abbreviation, name="Concept_abbreviation", curie=QUDT.curie('abbreviation'),
                   model_uri=POKEMON.Concept_abbreviation, domain=Concept, range=Optional[Union[str, list[str]]])

slots.Concept_deprecated = Slot(uri=QUDT.deprecated, name="Concept_deprecated", curie=QUDT.curie('deprecated'),
                   model_uri=POKEMON.Concept_deprecated, domain=Concept, range=Optional[Union[str, list[str]]])

slots.Concept_qudt_id = Slot(uri=QUDT.id, name="Concept_qudt_id", curie=QUDT.curie('id'),
                   model_uri=POKEMON.Concept_qudt_id, domain=Concept, range=Optional[Union[str, list[str]]])

slots.Concept_plainTextDescription = Slot(uri=QUDT.plainTextDescription, name="Concept_plainTextDescription", curie=QUDT.curie('plainTextDescription'),
                   model_uri=POKEMON.Concept_plainTextDescription, domain=Concept, range=Optional[Union[str, list[str]]])

slots.QuantityValue_hasUnit = Slot(uri=QUDT.hasUnit, name="QuantityValue_hasUnit", curie=QUDT.curie('hasUnit'),
                   model_uri=POKEMON.QuantityValue_hasUnit, domain=QuantityValue, range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]])

slots.DataEncoding_bitOrder = Slot(uri=QUDT.bitOrder, name="DataEncoding_bitOrder", curie=QUDT.curie('bitOrder'),
                   model_uri=POKEMON.DataEncoding_bitOrder, domain=DataEncoding, range=Optional[Union[Union[str, EndianTypeId], list[Union[str, EndianTypeId]]]])

slots.DataEncoding_encoding = Slot(uri=QUDT.encoding, name="DataEncoding_encoding", curie=QUDT.curie('encoding'),
                   model_uri=POKEMON.DataEncoding_encoding, domain=DataEncoding, range=Optional[Union[Union[str, EncodingId], list[Union[str, EncodingId]]]])

slots.DataEncoding_byteOrder = Slot(uri=QUDT.byteOrder, name="DataEncoding_byteOrder", curie=QUDT.curie('byteOrder'),
                   model_uri=POKEMON.DataEncoding_byteOrder, domain=DataEncoding, range=Optional[Union[Union[str, EndianTypeId], list[Union[str, EndianTypeId]]]])

slots.Unit_applicableSystem = Slot(uri=QUDT.applicableSystem, name="Unit_applicableSystem", curie=QUDT.curie('applicableSystem'),
                   model_uri=POKEMON.Unit_applicableSystem, domain=Unit, range=Optional[Union[Union[str, SystemOfUnitsId], list[Union[str, SystemOfUnitsId]]]])

slots.Unit_definedUnitOfSystem = Slot(uri=QUDT.definedUnitOfSystem, name="Unit_definedUnitOfSystem", curie=QUDT.curie('definedUnitOfSystem'),
                   model_uri=POKEMON.Unit_definedUnitOfSystem, domain=Unit, range=Optional[Union[Union[str, SystemOfUnitsId], list[Union[str, SystemOfUnitsId]]]])

slots.Unit_derivedCoherentUnitOfSystem = Slot(uri=QUDT.derivedCoherentUnitOfSystem, name="Unit_derivedCoherentUnitOfSystem", curie=QUDT.curie('derivedCoherentUnitOfSystem'),
                   model_uri=POKEMON.Unit_derivedCoherentUnitOfSystem, domain=Unit, range=Optional[Union[Union[str, SystemOfUnitsId], list[Union[str, SystemOfUnitsId]]]])

slots.Unit_derivedUnitOfSystem = Slot(uri=QUDT.derivedUnitOfSystem, name="Unit_derivedUnitOfSystem", curie=QUDT.curie('derivedUnitOfSystem'),
                   model_uri=POKEMON.Unit_derivedUnitOfSystem, domain=Unit, range=Optional[Union[Union[str, SystemOfUnitsId], list[Union[str, SystemOfUnitsId]]]])

slots.Unit_exactMatch = Slot(uri=QUDT.exactMatch, name="Unit_exactMatch", curie=QUDT.curie('exactMatch'),
                   model_uri=POKEMON.Unit_exactMatch, domain=Unit, range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]])

slots.Unit_hasDimensionVector = Slot(uri=QUDT.hasDimensionVector, name="Unit_hasDimensionVector", curie=QUDT.curie('hasDimensionVector'),
                   model_uri=POKEMON.Unit_hasDimensionVector, domain=Unit, range=Optional[Union[Union[str, QuantityKindDimensionVectorId], list[Union[str, QuantityKindDimensionVectorId]]]])

slots.Unit_hasFactorUnit = Slot(uri=QUDT.hasFactorUnit, name="Unit_hasFactorUnit", curie=QUDT.curie('hasFactorUnit'),
                   model_uri=POKEMON.Unit_hasFactorUnit, domain=Unit, range=Optional[Union[str, list[str]]])

slots.Unit_hasQuantityKind = Slot(uri=QUDT.hasQuantityKind, name="Unit_hasQuantityKind", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=POKEMON.Unit_hasQuantityKind, domain=Unit, range=Optional[Union[Union[str, QuantityKindId], list[Union[str, QuantityKindId]]]])

slots.Unit_iec61360Code = Slot(uri=QUDT.iec61360Code, name="Unit_iec61360Code", curie=QUDT.curie('iec61360Code'),
                   model_uri=POKEMON.Unit_iec61360Code, domain=Unit, range=Optional[Union[str, list[str]]])

slots.Unit_prefix = Slot(uri=QUDT.prefix, name="Unit_prefix", curie=QUDT.curie('prefix'),
                   model_uri=POKEMON.Unit_prefix, domain=Unit, range=Optional[Union[Union[str, PrefixId], list[Union[str, PrefixId]]]])

slots.Unit_qkdvDenominator = Slot(uri=QUDT.qkdvDenominator, name="Unit_qkdvDenominator", curie=QUDT.curie('qkdvDenominator'),
                   model_uri=POKEMON.Unit_qkdvDenominator, domain=Unit, range=Optional[Union[Union[str, QuantityKindDimensionVectorId], list[Union[str, QuantityKindDimensionVectorId]]]])

slots.Unit_qkdvNumerator = Slot(uri=QUDT.qkdvNumerator, name="Unit_qkdvNumerator", curie=QUDT.curie('qkdvNumerator'),
                   model_uri=POKEMON.Unit_qkdvNumerator, domain=Unit, range=Optional[Union[Union[str, QuantityKindDimensionVectorId], list[Union[str, QuantityKindDimensionVectorId]]]])

slots.Unit_scalingOf = Slot(uri=QUDT.scalingOf, name="Unit_scalingOf", curie=QUDT.curie('scalingOf'),
                   model_uri=POKEMON.Unit_scalingOf, domain=Unit, range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]])

slots.Unit_ucumCode = Slot(uri=QUDT.ucumCode, name="Unit_ucumCode", curie=QUDT.curie('ucumCode'),
                   model_uri=POKEMON.Unit_ucumCode, domain=Unit, range=Optional[Union[Union[str, UCUMcsId], list[Union[str, UCUMcsId]]]])

slots.Unit_udunitsCode = Slot(uri=QUDT.udunitsCode, name="Unit_udunitsCode", curie=QUDT.curie('udunitsCode'),
                   model_uri=POKEMON.Unit_udunitsCode, domain=Unit, range=Optional[Union[str, list[str]]])

slots.Unit_uneceCommonCode = Slot(uri=QUDT.uneceCommonCode, name="Unit_uneceCommonCode", curie=QUDT.curie('uneceCommonCode'),
                   model_uri=POKEMON.Unit_uneceCommonCode, domain=Unit, range=Optional[Union[str, list[str]]])

slots.Unit_altSymbol = Slot(uri=QUDT.altSymbol, name="Unit_altSymbol", curie=QUDT.curie('altSymbol'),
                   model_uri=POKEMON.Unit_altSymbol, domain=Unit, range=Optional[Union[str, list[str]]])

slots.Unit_latexDefinition = Slot(uri=QUDT.latexDefinition, name="Unit_latexDefinition", curie=QUDT.curie('latexDefinition'),
                   model_uri=POKEMON.Unit_latexDefinition, domain=Unit, range=Optional[Union[str, list[str]]])

slots.Unit_latexSymbol = Slot(uri=QUDT.latexSymbol, name="Unit_latexSymbol", curie=QUDT.curie('latexSymbol'),
                   model_uri=POKEMON.Unit_latexSymbol, domain=Unit, range=Optional[Union[str, list[str]]])

slots.Unit_siUnitsExpression = Slot(uri=QUDT.siUnitsExpression, name="Unit_siUnitsExpression", curie=QUDT.curie('siUnitsExpression'),
                   model_uri=POKEMON.Unit_siUnitsExpression, domain=Unit, range=Optional[Union[str, list[str]]])

slots.Unit_symbol = Slot(uri=QUDT.symbol, name="Unit_symbol", curie=QUDT.curie('symbol'),
                   model_uri=POKEMON.Unit_symbol, domain=Unit, range=Optional[Union[str, list[str]]])

slots.Unit_conversionMultiplier = Slot(uri=QUDT.conversionMultiplier, name="Unit_conversionMultiplier", curie=QUDT.curie('conversionMultiplier'),
                   model_uri=POKEMON.Unit_conversionMultiplier, domain=Unit, range=Optional[Union[str, list[str]]])

slots.Unit_conversionMultiplierSN = Slot(uri=QUDT.conversionMultiplierSN, name="Unit_conversionMultiplierSN", curie=QUDT.curie('conversionMultiplierSN'),
                   model_uri=POKEMON.Unit_conversionMultiplierSN, domain=Unit, range=Optional[Union[str, list[str]]])

slots.Unit_conversionOffset = Slot(uri=QUDT.conversionOffset, name="Unit_conversionOffset", curie=QUDT.curie('conversionOffset'),
                   model_uri=POKEMON.Unit_conversionOffset, domain=Unit, range=Optional[Union[str, list[str]]])

slots.Unit_conversionOffsetSN = Slot(uri=QUDT.conversionOffsetSN, name="Unit_conversionOffsetSN", curie=QUDT.curie('conversionOffsetSN'),
                   model_uri=POKEMON.Unit_conversionOffsetSN, domain=Unit, range=Optional[Union[str, list[str]]])

slots.Unit_factorUnitScalar = Slot(uri=QUDT.factorUnitScalar, name="Unit_factorUnitScalar", curie=QUDT.curie('factorUnitScalar'),
                   model_uri=POKEMON.Unit_factorUnitScalar, domain=Unit, range=Optional[Union[str, list[str]]])

slots.Unit_mathMLdefinition = Slot(uri=QUDT.mathMLdefinition, name="Unit_mathMLdefinition", curie=QUDT.curie('mathMLdefinition'),
                   model_uri=POKEMON.Unit_mathMLdefinition, domain=Unit, range=Optional[Union[str, list[str]]])

slots.Datatype_basis = Slot(uri=QUDT.basis, name="Datatype_basis", curie=QUDT.curie('basis'),
                   model_uri=POKEMON.Datatype_basis, domain=Datatype, range=Optional[Union[Union[str, DatatypeId], list[Union[str, DatatypeId]]]])

slots.Datatype_cardinality = Slot(uri=QUDT.cardinality, name="Datatype_cardinality", curie=QUDT.curie('cardinality'),
                   model_uri=POKEMON.Datatype_cardinality, domain=Datatype, range=Optional[Union[Union[str, CardinalityTypeId], list[Union[str, CardinalityTypeId]]]])

slots.Datatype_orderedType = Slot(uri=QUDT.orderedType, name="Datatype_orderedType", curie=QUDT.curie('orderedType'),
                   model_uri=POKEMON.Datatype_orderedType, domain=Datatype, range=Optional[Union[Union[str, OrderedTypeId], list[Union[str, OrderedTypeId]]]])

slots.Datatype_ansiSQLName = Slot(uri=QUDT.ansiSQLName, name="Datatype_ansiSQLName", curie=QUDT.curie('ansiSQLName'),
                   model_uri=POKEMON.Datatype_ansiSQLName, domain=Datatype, range=Optional[Union[str, list[str]]])

slots.Datatype_cName = Slot(uri=QUDT.cName, name="Datatype_cName", curie=QUDT.curie('cName'),
                   model_uri=POKEMON.Datatype_cName, domain=Datatype, range=Optional[Union[str, list[str]]])

slots.Datatype_oracleSQLName = Slot(uri=QUDT.oracleSQLName, name="Datatype_oracleSQLName", curie=QUDT.curie('oracleSQLName'),
                   model_uri=POKEMON.Datatype_oracleSQLName, domain=Datatype, range=Optional[Union[str, list[str]]])

slots.Datatype_protocolBuffersName = Slot(uri=QUDT.protocolBuffersName, name="Datatype_protocolBuffersName", curie=QUDT.curie('protocolBuffersName'),
                   model_uri=POKEMON.Datatype_protocolBuffersName, domain=Datatype, range=Optional[Union[str, list[str]]])

slots.Datatype_pythonName = Slot(uri=QUDT.pythonName, name="Datatype_pythonName", curie=QUDT.curie('pythonName'),
                   model_uri=POKEMON.Datatype_pythonName, domain=Datatype, range=Optional[Union[str, list[str]]])

slots.Datatype_vbName = Slot(uri=QUDT.vbName, name="Datatype_vbName", curie=QUDT.curie('vbName'),
                   model_uri=POKEMON.Datatype_vbName, domain=Datatype, range=Optional[Union[str, list[str]]])

slots.Datatype_bounded = Slot(uri=QUDT.bounded, name="Datatype_bounded", curie=QUDT.curie('bounded'),
                   model_uri=POKEMON.Datatype_bounded, domain=Datatype, range=Optional[Union[str, list[str]]])

slots.Datatype_qudt_id = Slot(uri=QUDT.id, name="Datatype_qudt_id", curie=QUDT.curie('id'),
                   model_uri=POKEMON.Datatype_qudt_id, domain=Datatype, range=Optional[Union[str, list[str]]])

slots.Datatype_javaName = Slot(uri=QUDT.javaName, name="Datatype_javaName", curie=QUDT.curie('javaName'),
                   model_uri=POKEMON.Datatype_javaName, domain=Datatype, range=Optional[Union[str, list[str]]])

slots.Datatype_jsName = Slot(uri=QUDT.jsName, name="Datatype_jsName", curie=QUDT.curie('jsName'),
                   model_uri=POKEMON.Datatype_jsName, domain=Datatype, range=Optional[Union[str, list[str]]])

slots.Datatype_matlabName = Slot(uri=QUDT.matlabName, name="Datatype_matlabName", curie=QUDT.curie('matlabName'),
                   model_uri=POKEMON.Datatype_matlabName, domain=Datatype, range=Optional[Union[str, list[str]]])

slots.Datatype_microsoftSQLServerName = Slot(uri=QUDT.microsoftSQLServerName, name="Datatype_microsoftSQLServerName", curie=QUDT.curie('microsoftSQLServerName'),
                   model_uri=POKEMON.Datatype_microsoftSQLServerName, domain=Datatype, range=Optional[Union[str, list[str]]])

slots.Datatype_mySQLName = Slot(uri=QUDT.mySQLName, name="Datatype_mySQLName", curie=QUDT.curie('mySQLName'),
                   model_uri=POKEMON.Datatype_mySQLName, domain=Datatype, range=Optional[Union[str, list[str]]])

slots.Datatype_odbcName = Slot(uri=QUDT.odbcName, name="Datatype_odbcName", curie=QUDT.curie('odbcName'),
                   model_uri=POKEMON.Datatype_odbcName, domain=Datatype, range=Optional[Union[str, list[str]]])

slots.Datatype_oleDBName = Slot(uri=QUDT.oleDBName, name="Datatype_oleDBName", curie=QUDT.curie('oleDBName'),
                   model_uri=POKEMON.Datatype_oleDBName, domain=Datatype, range=Optional[Union[str, list[str]]])

slots.Verifiable_isoNormativeReference = Slot(uri=QUDT.isoNormativeReference, name="Verifiable_isoNormativeReference", curie=QUDT.curie('isoNormativeReference'),
                   model_uri=POKEMON.Verifiable_isoNormativeReference, domain=Verifiable, range=Optional[Union[str, list[str]]])

slots.Verifiable_normativeReference = Slot(uri=QUDT.normativeReference, name="Verifiable_normativeReference", curie=QUDT.curie('normativeReference'),
                   model_uri=POKEMON.Verifiable_normativeReference, domain=Verifiable, range=Optional[Union[str, list[str]]])

slots.Verifiable_wikidataMatch = Slot(uri=QUDT.wikidataMatch, name="Verifiable_wikidataMatch", curie=QUDT.curie('wikidataMatch'),
                   model_uri=POKEMON.Verifiable_wikidataMatch, domain=Verifiable, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.Verifiable_dbpediaMatch = Slot(uri=QUDT.dbpediaMatch, name="Verifiable_dbpediaMatch", curie=QUDT.curie('dbpediaMatch'),
                   model_uri=POKEMON.Verifiable_dbpediaMatch, domain=Verifiable, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.QuantityKind_dimensionVectorForSI = Slot(uri=QUDT.dimensionVectorForSI, name="QuantityKind_dimensionVectorForSI", curie=QUDT.curie('dimensionVectorForSI'),
                   model_uri=POKEMON.QuantityKind_dimensionVectorForSI, domain=QuantityKind, range=Optional[Union[Union[str, QuantityKindDimensionVectorSIId], list[Union[str, QuantityKindDimensionVectorSIId]]]])

slots.QuantityKind_exactMatch = Slot(uri=QUDT.exactMatch, name="QuantityKind_exactMatch", curie=QUDT.curie('exactMatch'),
                   model_uri=POKEMON.QuantityKind_exactMatch, domain=QuantityKind, range=Optional[Union[Union[str, QuantityKindId], list[Union[str, QuantityKindId]]]])

slots.QuantityKind_hasDimensionVector = Slot(uri=QUDT.hasDimensionVector, name="QuantityKind_hasDimensionVector", curie=QUDT.curie('hasDimensionVector'),
                   model_uri=POKEMON.QuantityKind_hasDimensionVector, domain=QuantityKind, range=Optional[Union[Union[str, QuantityKindDimensionVectorId], list[Union[str, QuantityKindDimensionVectorId]]]])

slots.QuantityKind_iec61360Code = Slot(uri=QUDT.iec61360Code, name="QuantityKind_iec61360Code", curie=QUDT.curie('iec61360Code'),
                   model_uri=POKEMON.QuantityKind_iec61360Code, domain=QuantityKind, range=Optional[Union[str, list[str]]])

slots.QuantityKind_applicableCGSUnit = Slot(uri=QUDT.applicableCGSUnit, name="QuantityKind_applicableCGSUnit", curie=QUDT.curie('applicableCGSUnit'),
                   model_uri=POKEMON.QuantityKind_applicableCGSUnit, domain=QuantityKind, range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]])

slots.QuantityKind_applicableISOUnit = Slot(uri=QUDT.applicableISOUnit, name="QuantityKind_applicableISOUnit", curie=QUDT.curie('applicableISOUnit'),
                   model_uri=POKEMON.QuantityKind_applicableISOUnit, domain=QuantityKind, range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]])

slots.QuantityKind_applicableImperialUnit = Slot(uri=QUDT.applicableImperialUnit, name="QuantityKind_applicableImperialUnit", curie=QUDT.curie('applicableImperialUnit'),
                   model_uri=POKEMON.QuantityKind_applicableImperialUnit, domain=QuantityKind, range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]])

slots.QuantityKind_applicableSIUnit = Slot(uri=QUDT.applicableSIUnit, name="QuantityKind_applicableSIUnit", curie=QUDT.curie('applicableSIUnit'),
                   model_uri=POKEMON.QuantityKind_applicableSIUnit, domain=QuantityKind, range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]])

slots.QuantityKind_applicableUSCustomaryUnit = Slot(uri=QUDT.applicableUSCustomaryUnit, name="QuantityKind_applicableUSCustomaryUnit", curie=QUDT.curie('applicableUSCustomaryUnit'),
                   model_uri=POKEMON.QuantityKind_applicableUSCustomaryUnit, domain=QuantityKind, range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]])

slots.QuantityKind_applicableUnit = Slot(uri=QUDT.applicableUnit, name="QuantityKind_applicableUnit", curie=QUDT.curie('applicableUnit'),
                   model_uri=POKEMON.QuantityKind_applicableUnit, domain=QuantityKind, range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]])

slots.QuantityKind_qkdvDenominator = Slot(uri=QUDT.qkdvDenominator, name="QuantityKind_qkdvDenominator", curie=QUDT.curie('qkdvDenominator'),
                   model_uri=POKEMON.QuantityKind_qkdvDenominator, domain=QuantityKind, range=Optional[Union[Union[str, QuantityKindDimensionVectorId], list[Union[str, QuantityKindDimensionVectorId]]]])

slots.QuantityKind_qkdvNumerator = Slot(uri=QUDT.qkdvNumerator, name="QuantityKind_qkdvNumerator", curie=QUDT.curie('qkdvNumerator'),
                   model_uri=POKEMON.QuantityKind_qkdvNumerator, domain=QuantityKind, range=Optional[Union[Union[str, QuantityKindDimensionVectorId], list[Union[str, QuantityKindDimensionVectorId]]]])

slots.QuantityKind_latexDefinition = Slot(uri=QUDT.latexDefinition, name="QuantityKind_latexDefinition", curie=QUDT.curie('latexDefinition'),
                   model_uri=POKEMON.QuantityKind_latexDefinition, domain=QuantityKind, range=Optional[Union[str, list[str]]])

slots.QuantityKind_mathMLdefinition = Slot(uri=QUDT.mathMLdefinition, name="QuantityKind_mathMLdefinition", curie=QUDT.curie('mathMLdefinition'),
                   model_uri=POKEMON.QuantityKind_mathMLdefinition, domain=QuantityKind, range=Optional[Union[str, list[str]]])

slots.QuantityKindDimensionVector_hasReferenceQuantityKind = Slot(uri=QUDT.hasReferenceQuantityKind, name="QuantityKindDimensionVector_hasReferenceQuantityKind", curie=QUDT.curie('hasReferenceQuantityKind'),
                   model_uri=POKEMON.QuantityKindDimensionVector_hasReferenceQuantityKind, domain=QuantityKindDimensionVector, range=Optional[Union[Union[str, QuantityKindId], list[Union[str, QuantityKindId]]]])

slots.QuantityKindDimensionVector_latexSymbol = Slot(uri=QUDT.latexSymbol, name="QuantityKindDimensionVector_latexSymbol", curie=QUDT.curie('latexSymbol'),
                   model_uri=POKEMON.QuantityKindDimensionVector_latexSymbol, domain=QuantityKindDimensionVector, range=Optional[Union[str, list[str]]])

slots.QuantityKindDimensionVector_dimensionExponentForAmountOfSubstance = Slot(uri=QUDT.dimensionExponentForAmountOfSubstance, name="QuantityKindDimensionVector_dimensionExponentForAmountOfSubstance", curie=QUDT.curie('dimensionExponentForAmountOfSubstance'),
                   model_uri=POKEMON.QuantityKindDimensionVector_dimensionExponentForAmountOfSubstance, domain=QuantityKindDimensionVector, range=Union[str, list[str]])

slots.QuantityKindDimensionVector_dimensionExponentForElectricCurrent = Slot(uri=QUDT.dimensionExponentForElectricCurrent, name="QuantityKindDimensionVector_dimensionExponentForElectricCurrent", curie=QUDT.curie('dimensionExponentForElectricCurrent'),
                   model_uri=POKEMON.QuantityKindDimensionVector_dimensionExponentForElectricCurrent, domain=QuantityKindDimensionVector, range=Union[str, list[str]])

slots.QuantityKindDimensionVector_dimensionExponentForLength = Slot(uri=QUDT.dimensionExponentForLength, name="QuantityKindDimensionVector_dimensionExponentForLength", curie=QUDT.curie('dimensionExponentForLength'),
                   model_uri=POKEMON.QuantityKindDimensionVector_dimensionExponentForLength, domain=QuantityKindDimensionVector, range=Union[str, list[str]])

slots.QuantityKindDimensionVector_dimensionExponentForLuminousIntensity = Slot(uri=QUDT.dimensionExponentForLuminousIntensity, name="QuantityKindDimensionVector_dimensionExponentForLuminousIntensity", curie=QUDT.curie('dimensionExponentForLuminousIntensity'),
                   model_uri=POKEMON.QuantityKindDimensionVector_dimensionExponentForLuminousIntensity, domain=QuantityKindDimensionVector, range=Union[str, list[str]])

slots.QuantityKindDimensionVector_dimensionExponentForMass = Slot(uri=QUDT.dimensionExponentForMass, name="QuantityKindDimensionVector_dimensionExponentForMass", curie=QUDT.curie('dimensionExponentForMass'),
                   model_uri=POKEMON.QuantityKindDimensionVector_dimensionExponentForMass, domain=QuantityKindDimensionVector, range=Union[str, list[str]])

slots.QuantityKindDimensionVector_dimensionExponentForThermodynamicTemperature = Slot(uri=QUDT.dimensionExponentForThermodynamicTemperature, name="QuantityKindDimensionVector_dimensionExponentForThermodynamicTemperature", curie=QUDT.curie('dimensionExponentForThermodynamicTemperature'),
                   model_uri=POKEMON.QuantityKindDimensionVector_dimensionExponentForThermodynamicTemperature, domain=QuantityKindDimensionVector, range=Union[str, list[str]])

slots.QuantityKindDimensionVector_dimensionExponentForTime = Slot(uri=QUDT.dimensionExponentForTime, name="QuantityKindDimensionVector_dimensionExponentForTime", curie=QUDT.curie('dimensionExponentForTime'),
                   model_uri=POKEMON.QuantityKindDimensionVector_dimensionExponentForTime, domain=QuantityKindDimensionVector, range=Union[str, list[str]])

slots.QuantityKindDimensionVector_dimensionlessExponent = Slot(uri=QUDT.dimensionlessExponent, name="QuantityKindDimensionVector_dimensionlessExponent", curie=QUDT.curie('dimensionlessExponent'),
                   model_uri=POKEMON.QuantityKindDimensionVector_dimensionlessExponent, domain=QuantityKindDimensionVector, range=Union[str, list[str]])

slots.QuantityKindDimensionVector_latexDefinition = Slot(uri=QUDT.latexDefinition, name="QuantityKindDimensionVector_latexDefinition", curie=QUDT.curie('latexDefinition'),
                   model_uri=POKEMON.QuantityKindDimensionVector_latexDefinition, domain=QuantityKindDimensionVector, range=Optional[Union[str, list[str]]])

slots.Rule_ruleType = Slot(uri=QUDT.ruleType, name="Rule_ruleType", curie=QUDT.curie('ruleType'),
                   model_uri=POKEMON.Rule_ruleType, domain=Rule, range=Optional[Union[Union[str, RuleTypeId], list[Union[str, RuleTypeId]]]])

slots.Rule_rationale = Slot(uri=QUDT.rationale, name="Rule_rationale", curie=QUDT.curie('rationale'),
                   model_uri=POKEMON.Rule_rationale, domain=Rule, range=Optional[Union[str, list[str]]])
