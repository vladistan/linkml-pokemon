# Auto generated from linkml_pokemon.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-02-09T19:07:01
# Schema: linkml-pokemon
#
# id: https://pokemonkg.org/ontology
# description: Ontology covering the Pokémon world as it is presented in games and anime television series
# license: MIT

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from jsonasobj2 import as_dict
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.metamodelcore import empty_dict, empty_list
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import YAMLRoot
from rdflib import URIRef

from linkml_runtime.linkml_model.types import Decimal
from linkml_runtime.utils.metamodelcore import Bool, Decimal, URI

metamodel_version = "1.7.0"
version = None

# Namespaces
PATO = CurieNamespace("PATO", "http://purl.obolibrary.org/obo/PATO_")
DBPEDIA = CurieNamespace("dbpedia", "http://dbpedia.org/ontology/")
EXAMPLE = CurieNamespace("example", "https://example.org/")
FOAF = CurieNamespace("foaf", "http://xmlns.com/foaf/0.1/")
LINKML = CurieNamespace("linkml", "https://w3id.org/linkml/")
LINKML_COMMON = CurieNamespace("linkml_common", "https://w3id.org/linkml/common/")
LINKML_POKEMON = CurieNamespace(
    "linkml_pokemon", "https://w3id.org/vladistan/linkml-pokemon/"
)
OWL = CurieNamespace("owl", "http://www.w3.org/2002/07/owl#")
POKEMON = CurieNamespace("pokemon", "https://pokemonkg.org/ontology#")
QUDT = CurieNamespace("qudt", "http://qudt.org/schema/qudt/")
RDF = CurieNamespace("rdf", "http://www.w3.org/1999/02/22-rdf-syntax-ns#")
RDFS = CurieNamespace("rdfs", "http://www.w3.org/2000/01/rdf-schema#")
SCHEMA = CurieNamespace("schema", "http://schema.org/")
XML = CurieNamespace("xml", "http://www.w3.org/XML/1998/namespace")
XSD = CurieNamespace("xsd", "http://www.w3.org/2001/XMLSchema#")
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


class ColorId(ThingId):
    pass


class ConnotationId(ThingId):
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


class ConceptId(ThingId):
    pass


class QuantityId(ConceptId):
    pass


class QuantityValueId(ConceptId):
    pass


class AbstractQuantityKindId(ConceptId):
    pass


class QuantityKindId(AbstractQuantityKindId):
    pass


class UnitId(ConceptId):
    pass


class DerivedUnitId(UnitId):
    pass


class SystemOfUnitsId(ConceptId):
    pass


class QuantityKindDimensionVectorId(ConceptId):
    pass


class QuantityKindDimensionVectorSIId(QuantityKindDimensionVectorId):
    pass


class QuantityKindDimensionVectorCGSId(QuantityKindDimensionVectorId):
    pass


class QuantityKindDimensionVectorImperialId(QuantityKindDimensionVectorId):
    pass


class QuantityKindDimensionVectorISOId(QuantityKindDimensionVectorId):
    pass


class PrefixId(ConceptId):
    pass


class DecimalPrefixId(PrefixId):
    pass


class Pokemon(YAMLRoot):
    """
    A Pokémon
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Pok%C3%A9mon"]
    class_class_curie: ClassVar[str] = "pokemon:Pok%C3%A9mon"
    class_name: ClassVar[str] = "Pokemon"
    class_model_uri: ClassVar[URIRef] = POKEMON.Pokemon


class MoveLearning(YAMLRoot):
    """
    A move learning is a way that a Pokémon can learn a move.
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
class CmykColor(YAMLRoot):
    """
    CMYK color space coordinates (0-100).
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://dbpedia.org/ontology/CmykColor")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CmykColor"
    class_model_uri: ClassVar[URIRef] = POKEMON.CmykColor

    cmykC: Optional[int] = None
    cmykM: Optional[int] = None
    cmykY: Optional[int] = None
    cmykK: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.cmykC is not None and not isinstance(self.cmykC, int):
            self.cmykC = int(self.cmykC)

        if self.cmykM is not None and not isinstance(self.cmykM, int):
            self.cmykM = int(self.cmykM)

        if self.cmykY is not None and not isinstance(self.cmykY, int):
            self.cmykY = int(self.cmykY)

        if self.cmykK is not None and not isinstance(self.cmykK, int):
            self.cmykK = int(self.cmykK)

        super().__post_init__(**kwargs)


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
    """
    Abilities were introduced in Generation III as an all new game mechanic. Each and every Pokémon has an ability,
    and can only have one at a time. Some abilities are exclusive to certain Pokémon and Evolution lines, while others
    are known by many Pokémon.
    """

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
            self.effectDescription = (
                [self.effectDescription] if self.effectDescription is not None else []
            )
        self.effectDescription = [
            v if isinstance(v, str) else str(v) for v in self.effectDescription
        ]

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
    """
    Generations refers to the Pokémon game series. It is a group of games that were released at or around the same
    time. It also means that games in the same generation are compatible with the others, containing the same Pokémon
    and the number of moves there are to be learned.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Generation"]
    class_class_curie: ClassVar[str] = "pokemon:Generation"
    class_name: ClassVar[str] = "Generation"
    class_model_uri: ClassVar[URIRef] = POKEMON.Generation

    id: Union[str, GenerationId] = None
    featuresSpecies: Optional[
        Union[Union[str, SpeciesId], list[Union[str, SpeciesId]]]
    ] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GenerationId):
            self.id = GenerationId(self.id)

        if not isinstance(self.featuresSpecies, list):
            self.featuresSpecies = (
                [self.featuresSpecies] if self.featuresSpecies is not None else []
            )
        self.featuresSpecies = [
            v if isinstance(v, SpeciesId) else SpeciesId(v)
            for v in self.featuresSpecies
        ]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Item(Thing):
    """
    An item is an object in the Pokémon games which the player can pick up, keep in their Bag, and use in some manner.
    They have various uses, including healing, powering up, helping one to catch Pokémon, or to access a new area.
    """

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
    """
    Food items are consumable items in the Pokémon world that can have flavors, firmness, and smoothness attributes.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Food"]
    class_class_curie: ClassVar[str] = "pokemon:Food"
    class_name: ClassVar[str] = "Food"
    class_model_uri: ClassVar[URIRef] = POKEMON.Food

    id: Union[str, FoodId] = None
    hasFlavor: Optional[Union[Union[str, FlavorId], list[Union[str, FlavorId]]]] = (
        empty_list()
    )
    firmness: Optional[int] = None
    smoothness: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FoodId):
            self.id = FoodId(self.id)

        if not isinstance(self.hasFlavor, list):
            self.hasFlavor = [self.hasFlavor] if self.hasFlavor is not None else []
        self.hasFlavor = [
            v if isinstance(v, FlavorId) else FlavorId(v) for v in self.hasFlavor
        ]

        if self.firmness is not None and not isinstance(self.firmness, int):
            self.firmness = int(self.firmness)

        if self.smoothness is not None and not isinstance(self.smoothness, int):
            self.smoothness = int(self.smoothness)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Berry(Food):
    """
    Berries are small, juicy, fleshy fruit. As in the real world, a large variety exists in the Pokémon world, with a
    large range of flavors, names, and effects. First found in the Generation II games, many Berries have since became
    critical help items in battle, where their various effects include HP and status condition restoration, stat
    enhancement, and even damage negation.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Berry"]
    class_class_curie: ClassVar[str] = "pokemon:Berry"
    class_name: ClassVar[str] = "Berry"
    class_model_uri: ClassVar[URIRef] = POKEMON.Berry

    id: Union[str, BerryId] = None
    hasSize: Optional[Union[dict, "Quantity"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BerryId):
            self.id = BerryId(self.id)

        if self.hasSize is not None and not isinstance(self.hasSize, Quantity):
            self.hasSize = Quantity(**as_dict(self.hasSize))

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
    A hold item is an item that can be held by a Pokémon.
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
    """
    The Pokédex is an electronic device designed to catalog and provide information regarding the various species of
    Pokémon featured in the Pokémon video game, anime and manga series.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Pok%C3%A9dex"]
    class_class_curie: ClassVar[str] = "pokemon:Pok%C3%A9dex"
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
    A Pokédex entry is a description of a Pokémon.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Pok%C3%A9dexEntry"]
    class_class_curie: ClassVar[str] = "pokemon:Pok%C3%A9dexEntry"
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
    """
    A Poké Ball is a type of item that is critical to a Trainer's quest, used for catching and storing Pokémon.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Pok%C3%A9ball"]
    class_class_curie: ClassVar[str] = "pokemon:Pok%C3%A9ball"
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
    """
    Entities that have a somewhat fixed, physical extension.
    """

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
    """
    Regions are areas in the Pokémon universe that are smaller parts of a nation.
    """

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
    """
    A move is a special ability of a Pokémon.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Move"]
    class_class_curie: ClassVar[str] = "pokemon:Move"
    class_name: ClassVar[str] = "Move"
    class_model_uri: ClassVar[URIRef] = POKEMON.Move

    id: Union[str, MoveId] = None
    effectDescription: Optional[Union[str, list[str]]] = empty_list()
    hasType: Optional[
        Union[dict[Union[str, TypeId], Union[dict, "Type"]], list[Union[dict, "Type"]]]
    ] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MoveId):
            self.id = MoveId(self.id)

        if not isinstance(self.effectDescription, list):
            self.effectDescription = (
                [self.effectDescription] if self.effectDescription is not None else []
            )
        self.effectDescription = [
            v if isinstance(v, str) else str(v) for v in self.effectDescription
        ]

        self._normalize_inlined_as_list(
            slot_name="hasType", slot_type=Type, key_name="id", keyed=True
        )

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Medicine(Item):
    """
    Medicine items can heal various afflictions of a Pokémon.
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
    """
    A Technical Machine is an item that can be used to teach a Pokémon a move.
    """

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
class Color(Thing):
    """
    Color is the visual perceptual property corresponding in humans to the categories called red, yellow, blue and
    others.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DBPEDIA["Colour"]
    class_class_curie: ClassVar[str] = "dbpedia:Colour"
    class_name: ClassVar[str] = "Color"
    class_model_uri: ClassVar[URIRef] = POKEMON.Color

    id: Union[str, ColorId] = None
    wavelength: Optional[float] = None
    frequency: Optional[float] = None
    colorHexCode: Optional[str] = None
    connotation: Optional[
        Union[Union[str, ConnotationId], list[Union[str, ConnotationId]]]
    ] = empty_list()
    thumbnail: Optional[Union[str, URI]] = None
    cmykC: Optional[int] = None
    cmykM: Optional[int] = None
    cmykY: Optional[int] = None
    cmykK: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ColorId):
            self.id = ColorId(self.id)

        if self.wavelength is not None and not isinstance(self.wavelength, float):
            self.wavelength = float(self.wavelength)

        if self.frequency is not None and not isinstance(self.frequency, float):
            self.frequency = float(self.frequency)

        if self.colorHexCode is not None and not isinstance(self.colorHexCode, str):
            self.colorHexCode = str(self.colorHexCode)

        if not isinstance(self.connotation, list):
            self.connotation = (
                [self.connotation] if self.connotation is not None else []
            )
        self.connotation = [
            v if isinstance(v, ConnotationId) else ConnotationId(v)
            for v in self.connotation
        ]

        if self.thumbnail is not None and not isinstance(self.thumbnail, URI):
            self.thumbnail = URI(self.thumbnail)

        if self.cmykC is not None and not isinstance(self.cmykC, int):
            self.cmykC = int(self.cmykC)

        if self.cmykM is not None and not isinstance(self.cmykM, int):
            self.cmykM = int(self.cmykM)

        if self.cmykY is not None and not isinstance(self.cmykY, int):
            self.cmykY = int(self.cmykY)

        if self.cmykK is not None and not isinstance(self.cmykK, int):
            self.cmykK = int(self.cmykK)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Connotation(Thing):
    """
    Cultural or symbolic meaning associated with a color. Imported from DBpedia as generic owl:Thing resources.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL["Thing"]
    class_class_curie: ClassVar[str] = "owl:Thing"
    class_name: ClassVar[str] = "Connotation"
    class_model_uri: ClassVar[URIRef] = POKEMON.Connotation

    id: Union[str, ConnotationId] = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConnotationId):
            self.id = ConnotationId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

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
    """
    Egg group is a category that determines which Pokémon are able to interbreed. The concept was introduced in
    Generation II, along with breeding. Similar to types, a Pokémon may belong to either one or two egg groups.
    """

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
    """
    Flavor is a special set of attributes that certain foods in the Pokémon world have. Most of the foods can have
    more than one flavor, and the flavor determines which Pokémon can eat them.
    """

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
    A habitat is a type of environment that certain Pokémon belong to.
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
    Shapes are categories that certain Pokémon belong to, which determine which Pokémon they can breed with.
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
    A species is a category of Pokémon that share common features.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = POKEMON["Species"]
    class_class_curie: ClassVar[str] = "pokemon:Species"
    class_name: ClassVar[str] = "Species"
    class_model_uri: ClassVar[URIRef] = POKEMON.Species

    id: Union[str, SpeciesId] = None
    name: str = None
    hasColor: Optional[Union[str, ColorId]] = None
    mayHaveHiddenAbility: Optional[
        Union[Union[str, AbilityId], list[Union[str, AbilityId]]]
    ] = empty_list()
    mayHaveAbility: Optional[
        Union[Union[str, AbilityId], list[Union[str, AbilityId]]]
    ] = empty_list()
    isAbleToApply: Optional[Union[Union[str, MoveId], list[Union[str, MoveId]]]] = (
        empty_list()
    )
    hasHeight: Optional[Union[dict, "Quantity"]] = None
    hasWeight: Optional[Union[dict, "Quantity"]] = None
    depiction: Optional[str] = None
    inEggGroup: Optional[
        Union[Union[str, EggGroupId], list[Union[str, EggGroupId]]]
    ] = empty_list()
    hasType: Optional[
        Union[dict[Union[str, TypeId], Union[dict, "Type"]], list[Union[dict, "Type"]]]
    ] = empty_dict()
    hasShape: Optional[Union[str, ShapeId]] = None
    hasGenus: Optional[str] = None
    hasCatchRate: Optional[int] = None
    foundIn: Optional[Union[Union[str, HabitatId], list[Union[str, HabitatId]]]] = (
        empty_list()
    )

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpeciesId):
            self.id = SpeciesId(self.id)

        if self.hasColor is not None and not isinstance(self.hasColor, ColorId):
            self.hasColor = ColorId(self.hasColor)

        if not isinstance(self.mayHaveHiddenAbility, list):
            self.mayHaveHiddenAbility = (
                [self.mayHaveHiddenAbility]
                if self.mayHaveHiddenAbility is not None
                else []
            )
        self.mayHaveHiddenAbility = [
            v if isinstance(v, AbilityId) else AbilityId(v)
            for v in self.mayHaveHiddenAbility
        ]

        if not isinstance(self.mayHaveAbility, list):
            self.mayHaveAbility = (
                [self.mayHaveAbility] if self.mayHaveAbility is not None else []
            )
        self.mayHaveAbility = [
            v if isinstance(v, AbilityId) else AbilityId(v) for v in self.mayHaveAbility
        ]

        if not isinstance(self.isAbleToApply, list):
            self.isAbleToApply = (
                [self.isAbleToApply] if self.isAbleToApply is not None else []
            )
        self.isAbleToApply = [
            v if isinstance(v, MoveId) else MoveId(v) for v in self.isAbleToApply
        ]

        if self.hasHeight is not None and not isinstance(self.hasHeight, Quantity):
            self.hasHeight = Quantity(**as_dict(self.hasHeight))

        if self.hasWeight is not None and not isinstance(self.hasWeight, Quantity):
            self.hasWeight = Quantity(**as_dict(self.hasWeight))

        if self.depiction is not None and not isinstance(self.depiction, str):
            self.depiction = str(self.depiction)

        if not isinstance(self.inEggGroup, list):
            self.inEggGroup = [self.inEggGroup] if self.inEggGroup is not None else []
        self.inEggGroup = [
            v if isinstance(v, EggGroupId) else EggGroupId(v) for v in self.inEggGroup
        ]

        self._normalize_inlined_as_list(
            slot_name="hasType", slot_type=Type, key_name="id", keyed=True
        )

        if self.hasShape is not None and not isinstance(self.hasShape, ShapeId):
            self.hasShape = ShapeId(self.hasShape)

        if self.hasGenus is not None and not isinstance(self.hasGenus, str):
            self.hasGenus = str(self.hasGenus)

        if self.hasCatchRate is not None and not isinstance(self.hasCatchRate, int):
            self.hasCatchRate = int(self.hasCatchRate)

        if not isinstance(self.foundIn, list):
            self.foundIn = [self.foundIn] if self.foundIn is not None else []
        self.foundIn = [
            v if isinstance(v, HabitatId) else HabitatId(v) for v in self.foundIn
        ]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Type(NamedIndividual):
    """
    All Pokémon creatures and their moves are assigned certain types. Each type has several strengths and weaknesses
    in both attack and defense.
    """

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
    A trainer is a person who is able to catch Pokémon.
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
    """
    A gym leader is the highest ranking member and owner of an official Pokémon gym. Gym leaders use their gym and
    their Pokémon to test the skills of trainers that challenge them, and if said trainers win a battle, the gym
    leader will gift them a badge that's unique to that specific gym.
    """

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
class Concept(Thing):
    """
    The root class for all QUDT concepts
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Concept"]
    class_class_curie: ClassVar[str] = "qudt:Concept"
    class_name: ClassVar[str] = "Concept"
    class_model_uri: ClassVar[URIRef] = POKEMON.Concept

    id: Union[str, ConceptId] = None
    abbreviation: Optional[str] = None
    deprecated: Optional[Union[bool, Bool]] = None
    plainTextDescription: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.abbreviation is not None and not isinstance(self.abbreviation, str):
            self.abbreviation = str(self.abbreviation)

        if self.deprecated is not None and not isinstance(self.deprecated, Bool):
            self.deprecated = Bool(self.deprecated)

        if self.plainTextDescription is not None and not isinstance(
            self.plainTextDescription, str
        ):
            self.plainTextDescription = str(self.plainTextDescription)

        super().__post_init__(**kwargs)


class Aspect(YAMLRoot):
    """
    An abstract type class that defines properties that can be reused
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Aspect"]
    class_class_curie: ClassVar[str] = "qudt:Aspect"
    class_name: ClassVar[str] = "Aspect"
    class_model_uri: ClassVar[URIRef] = POKEMON.Aspect


@dataclass(repr=False)
class Quantifiable(Aspect):
    """
    Ascribes to some thing the capability of being measured, observed, or counted
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantifiable"]
    class_class_curie: ClassVar[str] = "qudt:Quantifiable"
    class_name: ClassVar[str] = "Quantifiable"
    class_model_uri: ClassVar[URIRef] = POKEMON.Quantifiable

    hasUnit: Optional[Union[str, UnitId]] = None
    standardUncertainty: Optional[Decimal] = None
    relativeStandardUncertainty: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.hasUnit is not None and not isinstance(self.hasUnit, UnitId):
            self.hasUnit = UnitId(self.hasUnit)

        if self.standardUncertainty is not None and not isinstance(
            self.standardUncertainty, Decimal
        ):
            self.standardUncertainty = Decimal(self.standardUncertainty)

        if self.relativeStandardUncertainty is not None and not isinstance(
            self.relativeStandardUncertainty, float
        ):
            self.relativeStandardUncertainty = float(self.relativeStandardUncertainty)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Verifiable(Aspect):
    """
    Holds properties that provide external knowledge and specifications of a given resource
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Verifiable"]
    class_class_curie: ClassVar[str] = "qudt:Verifiable"
    class_name: ClassVar[str] = "Verifiable"
    class_model_uri: ClassVar[URIRef] = POKEMON.Verifiable

    dbpediaMatch: Optional[Union[str, URI]] = None
    wikidataMatch: Optional[Union[str, URI]] = None
    informativeReference: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = (
        empty_list()
    )
    isoNormativeReference: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = (
        empty_list()
    )
    normativeReference: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = (
        empty_list()
    )

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.dbpediaMatch is not None and not isinstance(self.dbpediaMatch, URI):
            self.dbpediaMatch = URI(self.dbpediaMatch)

        if self.wikidataMatch is not None and not isinstance(self.wikidataMatch, URI):
            self.wikidataMatch = URI(self.wikidataMatch)

        if not isinstance(self.informativeReference, list):
            self.informativeReference = (
                [self.informativeReference]
                if self.informativeReference is not None
                else []
            )
        self.informativeReference = [
            v if isinstance(v, URI) else URI(v) for v in self.informativeReference
        ]

        if not isinstance(self.isoNormativeReference, list):
            self.isoNormativeReference = (
                [self.isoNormativeReference]
                if self.isoNormativeReference is not None
                else []
            )
        self.isoNormativeReference = [
            v if isinstance(v, URI) else URI(v) for v in self.isoNormativeReference
        ]

        if not isinstance(self.normativeReference, list):
            self.normativeReference = (
                [self.normativeReference] if self.normativeReference is not None else []
            )
        self.normativeReference = [
            v if isinstance(v, URI) else URI(v) for v in self.normativeReference
        ]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Quantity(Concept):
    """
    A measured quantity with kind and value
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "Quantity"
    class_model_uri: ClassVar[URIRef] = POKEMON.Quantity

    id: Union[str, QuantityId] = None
    hasQuantityKind: Optional[
        Union[Union[str, QuantityKindId], list[Union[str, QuantityKindId]]]
    ] = empty_list()
    quantityValue: Optional[
        Union[Union[str, QuantityValueId], list[Union[str, QuantityValueId]]]
    ] = empty_list()
    hasUnit: Optional[Union[str, UnitId]] = None
    standardUncertainty: Optional[Decimal] = None
    relativeStandardUncertainty: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, QuantityId):
            self.id = QuantityId(self.id)

        if not isinstance(self.hasQuantityKind, list):
            self.hasQuantityKind = (
                [self.hasQuantityKind] if self.hasQuantityKind is not None else []
            )
        self.hasQuantityKind = [
            v if isinstance(v, QuantityKindId) else QuantityKindId(v)
            for v in self.hasQuantityKind
        ]

        if not isinstance(self.quantityValue, list):
            self.quantityValue = (
                [self.quantityValue] if self.quantityValue is not None else []
            )
        self.quantityValue = [
            v if isinstance(v, QuantityValueId) else QuantityValueId(v)
            for v in self.quantityValue
        ]

        if self.hasUnit is not None and not isinstance(self.hasUnit, UnitId):
            self.hasUnit = UnitId(self.hasUnit)

        if self.standardUncertainty is not None and not isinstance(
            self.standardUncertainty, Decimal
        ):
            self.standardUncertainty = Decimal(self.standardUncertainty)

        if self.relativeStandardUncertainty is not None and not isinstance(
            self.relativeStandardUncertainty, float
        ):
            self.relativeStandardUncertainty = float(self.relativeStandardUncertainty)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantityValue(Concept):
    """
    Numeric value with unit
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["QuantityValue"]
    class_class_curie: ClassVar[str] = "qudt:QuantityValue"
    class_name: ClassVar[str] = "QuantityValue"
    class_model_uri: ClassVar[URIRef] = POKEMON.QuantityValue

    id: Union[str, QuantityValueId] = None
    numericValue: Optional[float] = None
    unit: Optional[Union[str, UnitId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, QuantityValueId):
            self.id = QuantityValueId(self.id)

        if self.numericValue is not None and not isinstance(self.numericValue, float):
            self.numericValue = float(self.numericValue)

        if self.unit is not None and not isinstance(self.unit, UnitId):
            self.unit = UnitId(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AbstractQuantityKind(Concept):
    """
    Abstract base for quantity kinds, constraining symbol and broader
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["AbstractQuantityKind"]
    class_class_curie: ClassVar[str] = "qudt:AbstractQuantityKind"
    class_name: ClassVar[str] = "AbstractQuantityKind"
    class_model_uri: ClassVar[URIRef] = POKEMON.AbstractQuantityKind

    id: Union[str, AbstractQuantityKindId] = None
    symbol: Optional[str] = None
    broader: Optional[
        Union[Union[str, QuantityKindId], list[Union[str, QuantityKindId]]]
    ] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.symbol is not None and not isinstance(self.symbol, str):
            self.symbol = str(self.symbol)

        if not isinstance(self.broader, list):
            self.broader = [self.broader] if self.broader is not None else []
        self.broader = [
            v if isinstance(v, QuantityKindId) else QuantityKindId(v)
            for v in self.broader
        ]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantityKind(AbstractQuantityKind):
    """
    Kind of quantity (e.g., Length, Mass, Height, Weight)
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["QuantityKind"]
    class_class_curie: ClassVar[str] = "qudt:QuantityKind"
    class_name: ClassVar[str] = "QuantityKind"
    class_model_uri: ClassVar[URIRef] = POKEMON.QuantityKind

    id: Union[str, QuantityKindId] = None
    latexSymbol: Optional[str] = None
    hasDimensionVector: Optional[Union[str, QuantityKindDimensionVectorId]] = None
    applicableUnit: Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]] = (
        empty_list()
    )
    exactMatch: Optional[Union[str, list[str]]] = empty_list()
    dbpediaMatch: Optional[Union[str, URI]] = None
    wikidataMatch: Optional[Union[str, URI]] = None
    informativeReference: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = (
        empty_list()
    )
    isoNormativeReference: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = (
        empty_list()
    )
    normativeReference: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = (
        empty_list()
    )

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, QuantityKindId):
            self.id = QuantityKindId(self.id)

        if self.latexSymbol is not None and not isinstance(self.latexSymbol, str):
            self.latexSymbol = str(self.latexSymbol)

        if self.hasDimensionVector is not None and not isinstance(
            self.hasDimensionVector, QuantityKindDimensionVectorId
        ):
            self.hasDimensionVector = QuantityKindDimensionVectorId(
                self.hasDimensionVector
            )

        if not isinstance(self.applicableUnit, list):
            self.applicableUnit = (
                [self.applicableUnit] if self.applicableUnit is not None else []
            )
        self.applicableUnit = [
            v if isinstance(v, UnitId) else UnitId(v) for v in self.applicableUnit
        ]

        if not isinstance(self.exactMatch, list):
            self.exactMatch = [self.exactMatch] if self.exactMatch is not None else []
        self.exactMatch = [v if isinstance(v, str) else str(v) for v in self.exactMatch]

        if self.dbpediaMatch is not None and not isinstance(self.dbpediaMatch, URI):
            self.dbpediaMatch = URI(self.dbpediaMatch)

        if self.wikidataMatch is not None and not isinstance(self.wikidataMatch, URI):
            self.wikidataMatch = URI(self.wikidataMatch)

        if not isinstance(self.informativeReference, list):
            self.informativeReference = (
                [self.informativeReference]
                if self.informativeReference is not None
                else []
            )
        self.informativeReference = [
            v if isinstance(v, URI) else URI(v) for v in self.informativeReference
        ]

        if not isinstance(self.isoNormativeReference, list):
            self.isoNormativeReference = (
                [self.isoNormativeReference]
                if self.isoNormativeReference is not None
                else []
            )
        self.isoNormativeReference = [
            v if isinstance(v, URI) else URI(v) for v in self.isoNormativeReference
        ]

        if not isinstance(self.normativeReference, list):
            self.normativeReference = (
                [self.normativeReference] if self.normativeReference is not None else []
            )
        self.normativeReference = [
            v if isinstance(v, URI) else URI(v) for v in self.normativeReference
        ]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Unit(Concept):
    """
    Unit of measurement
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Unit"]
    class_class_curie: ClassVar[str] = "qudt:Unit"
    class_name: ClassVar[str] = "Unit"
    class_model_uri: ClassVar[URIRef] = POKEMON.Unit

    id: Union[str, UnitId] = None
    symbol: Optional[str] = None
    latexSymbol: Optional[str] = None
    conversionMultiplier: Optional[float] = None
    conversionOffset: Optional[float] = None
    hasDimensionVector: Optional[Union[str, QuantityKindDimensionVectorId]] = None
    hasQuantityKind: Optional[
        Union[Union[str, QuantityKindId], list[Union[str, QuantityKindId]]]
    ] = empty_list()
    isUnitOfSystem: Optional[
        Union[Union[str, SystemOfUnitsId], list[Union[str, SystemOfUnitsId]]]
    ] = empty_list()
    applicableSystem: Optional[
        Union[Union[str, SystemOfUnitsId], list[Union[str, SystemOfUnitsId]]]
    ] = empty_list()
    prefix: Optional[Union[str, PrefixId]] = None
    scalingOf: Optional[Union[str, UnitId]] = None
    ucumCode: Optional[str] = None
    dbpediaMatch: Optional[Union[str, URI]] = None
    wikidataMatch: Optional[Union[str, URI]] = None
    informativeReference: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = (
        empty_list()
    )
    isoNormativeReference: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = (
        empty_list()
    )
    normativeReference: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = (
        empty_list()
    )

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UnitId):
            self.id = UnitId(self.id)

        if self.symbol is not None and not isinstance(self.symbol, str):
            self.symbol = str(self.symbol)

        if self.latexSymbol is not None and not isinstance(self.latexSymbol, str):
            self.latexSymbol = str(self.latexSymbol)

        if self.conversionMultiplier is not None and not isinstance(
            self.conversionMultiplier, float
        ):
            self.conversionMultiplier = float(self.conversionMultiplier)

        if self.conversionOffset is not None and not isinstance(
            self.conversionOffset, float
        ):
            self.conversionOffset = float(self.conversionOffset)

        if self.hasDimensionVector is not None and not isinstance(
            self.hasDimensionVector, QuantityKindDimensionVectorId
        ):
            self.hasDimensionVector = QuantityKindDimensionVectorId(
                self.hasDimensionVector
            )

        if not isinstance(self.hasQuantityKind, list):
            self.hasQuantityKind = (
                [self.hasQuantityKind] if self.hasQuantityKind is not None else []
            )
        self.hasQuantityKind = [
            v if isinstance(v, QuantityKindId) else QuantityKindId(v)
            for v in self.hasQuantityKind
        ]

        if not isinstance(self.isUnitOfSystem, list):
            self.isUnitOfSystem = (
                [self.isUnitOfSystem] if self.isUnitOfSystem is not None else []
            )
        self.isUnitOfSystem = [
            v if isinstance(v, SystemOfUnitsId) else SystemOfUnitsId(v)
            for v in self.isUnitOfSystem
        ]

        if not isinstance(self.applicableSystem, list):
            self.applicableSystem = (
                [self.applicableSystem] if self.applicableSystem is not None else []
            )
        self.applicableSystem = [
            v if isinstance(v, SystemOfUnitsId) else SystemOfUnitsId(v)
            for v in self.applicableSystem
        ]

        if self.prefix is not None and not isinstance(self.prefix, PrefixId):
            self.prefix = PrefixId(self.prefix)

        if self.scalingOf is not None and not isinstance(self.scalingOf, UnitId):
            self.scalingOf = UnitId(self.scalingOf)

        if self.ucumCode is not None and not isinstance(self.ucumCode, str):
            self.ucumCode = str(self.ucumCode)

        if self.dbpediaMatch is not None and not isinstance(self.dbpediaMatch, URI):
            self.dbpediaMatch = URI(self.dbpediaMatch)

        if self.wikidataMatch is not None and not isinstance(self.wikidataMatch, URI):
            self.wikidataMatch = URI(self.wikidataMatch)

        if not isinstance(self.informativeReference, list):
            self.informativeReference = (
                [self.informativeReference]
                if self.informativeReference is not None
                else []
            )
        self.informativeReference = [
            v if isinstance(v, URI) else URI(v) for v in self.informativeReference
        ]

        if not isinstance(self.isoNormativeReference, list):
            self.isoNormativeReference = (
                [self.isoNormativeReference]
                if self.isoNormativeReference is not None
                else []
            )
        self.isoNormativeReference = [
            v if isinstance(v, URI) else URI(v) for v in self.isoNormativeReference
        ]

        if not isinstance(self.normativeReference, list):
            self.normativeReference = (
                [self.normativeReference] if self.normativeReference is not None else []
            )
        self.normativeReference = [
            v if isinstance(v, URI) else URI(v) for v in self.normativeReference
        ]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DerivedUnit(Unit):
    """
    Unit derived from base units (e.g., KiloM)
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["DerivedUnit"]
    class_class_curie: ClassVar[str] = "qudt:DerivedUnit"
    class_name: ClassVar[str] = "DerivedUnit"
    class_model_uri: ClassVar[URIRef] = POKEMON.DerivedUnit

    id: Union[str, DerivedUnitId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DerivedUnitId):
            self.id = DerivedUnitId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SystemOfUnits(Concept):
    """
    A coherent system of units (e.g., SI, CGS)
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["SystemOfUnits"]
    class_class_curie: ClassVar[str] = "qudt:SystemOfUnits"
    class_name: ClassVar[str] = "SystemOfUnits"
    class_model_uri: ClassVar[URIRef] = POKEMON.SystemOfUnits

    id: Union[str, SystemOfUnitsId] = None
    hasBaseUnit: Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]] = (
        empty_list()
    )
    prefix: Optional[Union[str, PrefixId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SystemOfUnitsId):
            self.id = SystemOfUnitsId(self.id)

        if not isinstance(self.hasBaseUnit, list):
            self.hasBaseUnit = (
                [self.hasBaseUnit] if self.hasBaseUnit is not None else []
            )
        self.hasBaseUnit = [
            v if isinstance(v, UnitId) else UnitId(v) for v in self.hasBaseUnit
        ]

        if self.prefix is not None and not isinstance(self.prefix, PrefixId):
            self.prefix = PrefixId(self.prefix)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantityKindDimensionVector(Concept):
    """
    Dimension vector expressing quantity in base dimensions
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["QuantityKindDimensionVector"]
    class_class_curie: ClassVar[str] = "qudt:QuantityKindDimensionVector"
    class_name: ClassVar[str] = "QuantityKindDimensionVector"
    class_model_uri: ClassVar[URIRef] = POKEMON.QuantityKindDimensionVector

    id: Union[str, QuantityKindDimensionVectorId] = None
    latexSymbol: Optional[str] = None
    dimensionExponentForLength: Optional[int] = None
    dimensionExponentForMass: Optional[int] = None
    dimensionExponentForTime: Optional[int] = None
    dimensionExponentForElectricCurrent: Optional[int] = None
    dimensionExponentForThermodynamicTemperature: Optional[int] = None
    dimensionExponentForAmountOfSubstance: Optional[int] = None
    dimensionExponentForLuminousIntensity: Optional[int] = None
    dimensionlessExponent: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, QuantityKindDimensionVectorId):
            self.id = QuantityKindDimensionVectorId(self.id)

        if self.latexSymbol is not None and not isinstance(self.latexSymbol, str):
            self.latexSymbol = str(self.latexSymbol)

        if self.dimensionExponentForLength is not None and not isinstance(
            self.dimensionExponentForLength, int
        ):
            self.dimensionExponentForLength = int(self.dimensionExponentForLength)

        if self.dimensionExponentForMass is not None and not isinstance(
            self.dimensionExponentForMass, int
        ):
            self.dimensionExponentForMass = int(self.dimensionExponentForMass)

        if self.dimensionExponentForTime is not None and not isinstance(
            self.dimensionExponentForTime, int
        ):
            self.dimensionExponentForTime = int(self.dimensionExponentForTime)

        if self.dimensionExponentForElectricCurrent is not None and not isinstance(
            self.dimensionExponentForElectricCurrent, int
        ):
            self.dimensionExponentForElectricCurrent = int(
                self.dimensionExponentForElectricCurrent
            )

        if (
            self.dimensionExponentForThermodynamicTemperature is not None
            and not isinstance(self.dimensionExponentForThermodynamicTemperature, int)
        ):
            self.dimensionExponentForThermodynamicTemperature = int(
                self.dimensionExponentForThermodynamicTemperature
            )

        if self.dimensionExponentForAmountOfSubstance is not None and not isinstance(
            self.dimensionExponentForAmountOfSubstance, int
        ):
            self.dimensionExponentForAmountOfSubstance = int(
                self.dimensionExponentForAmountOfSubstance
            )

        if self.dimensionExponentForLuminousIntensity is not None and not isinstance(
            self.dimensionExponentForLuminousIntensity, int
        ):
            self.dimensionExponentForLuminousIntensity = int(
                self.dimensionExponentForLuminousIntensity
            )

        if self.dimensionlessExponent is not None and not isinstance(
            self.dimensionlessExponent, int
        ):
            self.dimensionlessExponent = int(self.dimensionlessExponent)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantityKindDimensionVectorSI(QuantityKindDimensionVector):
    """
    SI dimension vector
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["QuantityKindDimensionVector_SI"]
    class_class_curie: ClassVar[str] = "qudt:QuantityKindDimensionVector_SI"
    class_name: ClassVar[str] = "QuantityKindDimensionVector_SI"
    class_model_uri: ClassVar[URIRef] = POKEMON.QuantityKindDimensionVectorSI

    id: Union[str, QuantityKindDimensionVectorSIId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, QuantityKindDimensionVectorSIId):
            self.id = QuantityKindDimensionVectorSIId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantityKindDimensionVectorCGS(QuantityKindDimensionVector):
    """
    CGS dimension vector
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["QuantityKindDimensionVector_CGS"]
    class_class_curie: ClassVar[str] = "qudt:QuantityKindDimensionVector_CGS"
    class_name: ClassVar[str] = "QuantityKindDimensionVector_CGS"
    class_model_uri: ClassVar[URIRef] = POKEMON.QuantityKindDimensionVectorCGS

    id: Union[str, QuantityKindDimensionVectorCGSId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, QuantityKindDimensionVectorCGSId):
            self.id = QuantityKindDimensionVectorCGSId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantityKindDimensionVectorImperial(QuantityKindDimensionVector):
    """
    Imperial dimension vector
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["QuantityKindDimensionVector_Imperial"]
    class_class_curie: ClassVar[str] = "qudt:QuantityKindDimensionVector_Imperial"
    class_name: ClassVar[str] = "QuantityKindDimensionVector_Imperial"
    class_model_uri: ClassVar[URIRef] = POKEMON.QuantityKindDimensionVectorImperial

    id: Union[str, QuantityKindDimensionVectorImperialId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, QuantityKindDimensionVectorImperialId):
            self.id = QuantityKindDimensionVectorImperialId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantityKindDimensionVectorISO(QuantityKindDimensionVector):
    """
    ISO dimension vector
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["QuantityKindDimensionVector_ISO"]
    class_class_curie: ClassVar[str] = "qudt:QuantityKindDimensionVector_ISO"
    class_name: ClassVar[str] = "QuantityKindDimensionVector_ISO"
    class_model_uri: ClassVar[URIRef] = POKEMON.QuantityKindDimensionVectorISO

    id: Union[str, QuantityKindDimensionVectorISOId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, QuantityKindDimensionVectorISOId):
            self.id = QuantityKindDimensionVectorISOId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Prefix(Concept):
    """
    Unit prefix (e.g., Kilo, Milli)
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Prefix"]
    class_class_curie: ClassVar[str] = "qudt:Prefix"
    class_name: ClassVar[str] = "Prefix"
    class_model_uri: ClassVar[URIRef] = POKEMON.Prefix

    id: Union[str, PrefixId] = None
    symbol: Optional[str] = None
    prefixMultiplier: Optional[float] = None
    ucumCode: Optional[str] = None
    exactMatch: Optional[Union[str, list[str]]] = empty_list()
    dbpediaMatch: Optional[Union[str, URI]] = None
    wikidataMatch: Optional[Union[str, URI]] = None
    informativeReference: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = (
        empty_list()
    )
    isoNormativeReference: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = (
        empty_list()
    )
    normativeReference: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = (
        empty_list()
    )

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrefixId):
            self.id = PrefixId(self.id)

        if self.symbol is not None and not isinstance(self.symbol, str):
            self.symbol = str(self.symbol)

        if self.prefixMultiplier is not None and not isinstance(
            self.prefixMultiplier, float
        ):
            self.prefixMultiplier = float(self.prefixMultiplier)

        if self.ucumCode is not None and not isinstance(self.ucumCode, str):
            self.ucumCode = str(self.ucumCode)

        if not isinstance(self.exactMatch, list):
            self.exactMatch = [self.exactMatch] if self.exactMatch is not None else []
        self.exactMatch = [v if isinstance(v, str) else str(v) for v in self.exactMatch]

        if self.dbpediaMatch is not None and not isinstance(self.dbpediaMatch, URI):
            self.dbpediaMatch = URI(self.dbpediaMatch)

        if self.wikidataMatch is not None and not isinstance(self.wikidataMatch, URI):
            self.wikidataMatch = URI(self.wikidataMatch)

        if not isinstance(self.informativeReference, list):
            self.informativeReference = (
                [self.informativeReference]
                if self.informativeReference is not None
                else []
            )
        self.informativeReference = [
            v if isinstance(v, URI) else URI(v) for v in self.informativeReference
        ]

        if not isinstance(self.isoNormativeReference, list):
            self.isoNormativeReference = (
                [self.isoNormativeReference]
                if self.isoNormativeReference is not None
                else []
            )
        self.isoNormativeReference = [
            v if isinstance(v, URI) else URI(v) for v in self.isoNormativeReference
        ]

        if not isinstance(self.normativeReference, list):
            self.normativeReference = (
                [self.normativeReference] if self.normativeReference is not None else []
            )
        self.normativeReference = [
            v if isinstance(v, URI) else URI(v) for v in self.normativeReference
        ]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DecimalPrefix(Prefix):
    """
    Decimal prefix (powers of 10)
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["DecimalPrefix"]
    class_class_curie: ClassVar[str] = "qudt:DecimalPrefix"
    class_name: ClassVar[str] = "DecimalPrefix"
    class_model_uri: ClassVar[URIRef] = POKEMON.DecimalPrefix

    id: Union[str, DecimalPrefixId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DecimalPrefixId):
            self.id = DecimalPrefixId(self.id)

        super().__post_init__(**kwargs)


# Enumerations
class HabitatEnum(EnumDefinitionImpl):
    Cave = PermissibleValue(text="Cave", meaning=POKEMON["Habitat_Cave"])
    Forest = PermissibleValue(text="Forest", meaning=POKEMON["Habitat_Forest"])
    Grassland = PermissibleValue(text="Grassland", meaning=POKEMON["Habitat_Grassland"])

    _defn = EnumDefinition(
        name="HabitatEnum",
    )


# Slots
class slots:
    pass


slots.effectDescription = Slot(
    uri=POKEMON.effectDescription,
    name="effectDescription",
    curie=POKEMON.curie("effectDescription"),
    model_uri=POKEMON.effectDescription,
    domain=None,
    range=Optional[Union[str, list[str]]],
)

slots.containsPlace = Slot(
    uri=POKEMON.contains_place,
    name="containsPlace",
    curie=POKEMON.curie("contains_place"),
    model_uri=POKEMON.containsPlace,
    domain=Place,
    range=Optional[Union[Union[str, PlaceId], list[Union[str, PlaceId]]]],
)

slots.describedInPokedex = Slot(
    uri=POKEMON["describedInPok%C3%A9dex"],
    name="describedInPokedex",
    curie=POKEMON.curie("describedInPok%C3%A9dex"),
    model_uri=POKEMON.describedInPokedex,
    domain=Species,
    range=Optional[Union[Union[str, PokedexEntryId], list[Union[str, PokedexEntryId]]]],
)

slots.describesPokemon = Slot(
    uri=POKEMON["describesPok%C3%A9mon"],
    name="describesPokemon",
    curie=POKEMON.curie("describesPok%C3%A9mon"),
    model_uri=POKEMON.describesPokemon,
    domain=PokedexEntry,
    range=Optional[Union[Union[str, SpeciesId], list[Union[str, SpeciesId]]]],
)

slots.featuresSpecies = Slot(
    uri=POKEMON.featuresSpecies,
    name="featuresSpecies",
    curie=POKEMON.curie("featuresSpecies"),
    model_uri=POKEMON.featuresSpecies,
    domain=None,
    range=Optional[Union[Union[str, SpeciesId], list[Union[str, SpeciesId]]]],
)

slots.hasPokedexEntry = Slot(
    uri=POKEMON["hasPok%C3%A9dexEntry"],
    name="hasPokedexEntry",
    curie=POKEMON.curie("hasPok%C3%A9dexEntry"),
    model_uri=POKEMON.hasPokedexEntry,
    domain=Pokedex,
    range=Optional[Union[Union[str, PokedexEntryId], list[Union[str, PokedexEntryId]]]],
)

slots.evolvesFrom = Slot(
    uri=POKEMON.evolvesFrom,
    name="evolvesFrom",
    curie=POKEMON.curie("evolvesFrom"),
    model_uri=POKEMON.evolvesFrom,
    domain=Species,
    range=Optional[Union[str, SpeciesId]],
)

slots.evolvesTo = Slot(
    uri=POKEMON.evolvesTo,
    name="evolvesTo",
    curie=POKEMON.curie("evolvesTo"),
    model_uri=POKEMON.evolvesTo,
    domain=Species,
    range=Optional[Union[Union[str, SpeciesId], list[Union[str, SpeciesId]]]],
)

slots.foundIn = Slot(
    uri=POKEMON.foundIn,
    name="foundIn",
    curie=POKEMON.curie("foundIn"),
    model_uri=POKEMON.foundIn,
    domain=Species,
    range=Optional[Union[Union[str, HabitatId], list[Union[str, HabitatId]]]],
)

slots.hasColor = Slot(
    uri=POKEMON.hasColour,
    name="hasColor",
    curie=POKEMON.curie("hasColour"),
    model_uri=POKEMON.hasColor,
    domain=None,
    range=Optional[Union[str, ColorId]],
)

slots.hasFlavor = Slot(
    uri=POKEMON.hasFlavor,
    name="hasFlavor",
    curie=POKEMON.curie("hasFlavor"),
    model_uri=POKEMON.hasFlavor,
    domain=Food,
    range=Optional[Union[Union[str, FlavorId], list[Union[str, FlavorId]]]],
)

slots.hasType = Slot(
    uri=POKEMON.hasType,
    name="hasType",
    curie=POKEMON.curie("hasType"),
    model_uri=POKEMON.hasType,
    domain=None,
    range=Optional[
        Union[dict[Union[str, TypeId], Union[dict, Type]], list[Union[dict, Type]]]
    ],
)

slots.hasSize = Slot(
    uri=POKEMON.hasSize,
    name="hasSize",
    curie=POKEMON.curie("hasSize"),
    model_uri=POKEMON.hasSize,
    domain=None,
    range=Optional[Union[dict, Quantity]],
)

slots.hasHeight = Slot(
    uri=POKEMON.hasHeight,
    name="hasHeight",
    curie=POKEMON.curie("hasHeight"),
    model_uri=POKEMON.hasHeight,
    domain=Species,
    range=Optional[Union[dict, "Quantity"]],
)

slots.hasWeight = Slot(
    uri=POKEMON.hasWeight,
    name="hasWeight",
    curie=POKEMON.curie("hasWeight"),
    model_uri=POKEMON.hasWeight,
    domain=Species,
    range=Optional[Union[dict, "Quantity"]],
)

slots.hasCatchRate = Slot(
    uri=POKEMON.hasCatchRate,
    name="hasCatchRate",
    curie=POKEMON.curie("hasCatchRate"),
    model_uri=POKEMON.hasCatchRate,
    domain=Species,
    range=Optional[int],
)

slots.hasShape = Slot(
    uri=POKEMON.hasShape,
    name="hasShape",
    curie=POKEMON.curie("hasShape"),
    model_uri=POKEMON.hasShape,
    domain=Species,
    range=Optional[Union[str, ShapeId]],
)

slots.learnsMove = Slot(
    uri=POKEMON.learnsMove,
    name="learnsMove",
    curie=POKEMON.curie("learnsMove"),
    model_uri=POKEMON.learnsMove,
    domain=MoveLearning,
    range=Optional[Union[Union[str, MoveId], list[Union[str, MoveId]]]],
)

slots.locatedIn = Slot(
    uri=POKEMON.locatedIn,
    name="locatedIn",
    curie=POKEMON.curie("locatedIn"),
    model_uri=POKEMON.locatedIn,
    domain=Place,
    range=Optional[Union[Union[str, PlaceId], list[Union[str, PlaceId]]]],
)

slots.inEggGroup = Slot(
    uri=POKEMON.inEggGroup,
    name="inEggGroup",
    curie=POKEMON.curie("inEggGroup"),
    model_uri=POKEMON.inEggGroup,
    domain=Species,
    range=Optional[Union[Union[str, EggGroupId], list[Union[str, EggGroupId]]]],
)

slots.mayHaveAbility = Slot(
    uri=POKEMON.mayHaveAbility,
    name="mayHaveAbility",
    curie=POKEMON.curie("mayHaveAbility"),
    model_uri=POKEMON.mayHaveAbility,
    domain=Species,
    range=Optional[Union[Union[str, AbilityId], list[Union[str, AbilityId]]]],
)

slots.mayHaveHiddenAbility = Slot(
    uri=POKEMON.mayHaveHiddenAbility,
    name="mayHaveHiddenAbility",
    curie=POKEMON.curie("mayHaveHiddenAbility"),
    model_uri=POKEMON.mayHaveHiddenAbility,
    domain=Species,
    range=Optional[Union[Union[str, AbilityId], list[Union[str, AbilityId]]]],
)

slots.isAbleToApply = Slot(
    uri=POKEMON.isAbleToApply,
    name="isAbleToApply",
    curie=POKEMON.curie("isAbleToApply"),
    model_uri=POKEMON.isAbleToApply,
    domain=None,
    range=Optional[Union[Union[str, MoveId], list[Union[str, MoveId]]]],
)

slots.firmness = Slot(
    uri=POKEMON.firmness,
    name="firmness",
    curie=POKEMON.curie("firmness"),
    model_uri=POKEMON.firmness,
    domain=Food,
    range=Optional[int],
)

slots.accuracy = Slot(
    uri=POKEMON.accuracy,
    name="accuracy",
    curie=POKEMON.curie("accuracy"),
    model_uri=POKEMON.accuracy,
    domain=Move,
    range=Optional[int],
)

slots.basePower = Slot(
    uri=POKEMON.basePower,
    name="basePower",
    curie=POKEMON.curie("basePower"),
    model_uri=POKEMON.basePower,
    domain=Move,
    range=Optional[int],
)

slots.basePowerPoints = Slot(
    uri=POKEMON.basePowerPoints,
    name="basePowerPoints",
    curie=POKEMON.curie("basePowerPoints"),
    model_uri=POKEMON.basePowerPoints,
    domain=Move,
    range=Optional[int],
)

slots.entryNumber = Slot(
    uri=POKEMON.entryNumber,
    name="entryNumber",
    curie=POKEMON.curie("entryNumber"),
    model_uri=POKEMON.entryNumber,
    domain=PokedexEntry,
    range=Optional[int],
)

slots.hasGenus = Slot(
    uri=POKEMON.hasGenus,
    name="hasGenus",
    curie=POKEMON.curie("hasGenus"),
    model_uri=POKEMON.hasGenus,
    domain=Species,
    range=Optional[str],
)

slots.maxPowerPoints = Slot(
    uri=POKEMON.maxPowerPoints,
    name="maxPowerPoints",
    curie=POKEMON.curie("maxPowerPoints"),
    model_uri=POKEMON.maxPowerPoints,
    domain=Move,
    range=Optional[int],
)

slots.minLevelToLearn = Slot(
    uri=POKEMON.minLevelToLearn,
    name="minLevelToLearn",
    curie=POKEMON.curie("minLevelToLearn"),
    model_uri=POKEMON.minLevelToLearn,
    domain=None,
    range=Optional[int],
)

slots.smoothness = Slot(
    uri=POKEMON.smoothness,
    name="smoothness",
    curie=POKEMON.curie("smoothness"),
    model_uri=POKEMON.smoothness,
    domain=Food,
    range=Optional[int],
)

slots.depiction = Slot(
    uri=FOAF.depiction,
    name="depiction",
    curie=FOAF.curie("depiction"),
    model_uri=POKEMON.depiction,
    domain=None,
    range=Optional[str],
)

slots.cmykC = Slot(
    uri=DBPEDIA.cmykCoordinateCyanic,
    name="cmykC",
    curie=DBPEDIA.curie("cmykCoordinateCyanic"),
    model_uri=POKEMON.cmykC,
    domain=None,
    range=Optional[int],
)

slots.cmykM = Slot(
    uri=DBPEDIA.cmykCoordinateMagenta,
    name="cmykM",
    curie=DBPEDIA.curie("cmykCoordinateMagenta"),
    model_uri=POKEMON.cmykM,
    domain=None,
    range=Optional[int],
)

slots.cmykY = Slot(
    uri=DBPEDIA.cmykCoordinateYellow,
    name="cmykY",
    curie=DBPEDIA.curie("cmykCoordinateYellow"),
    model_uri=POKEMON.cmykY,
    domain=None,
    range=Optional[int],
)

slots.cmykK = Slot(
    uri=DBPEDIA.cmykCoordinateBlack,
    name="cmykK",
    curie=DBPEDIA.curie("cmykCoordinateBlack"),
    model_uri=POKEMON.cmykK,
    domain=None,
    range=Optional[int],
)

slots.wavelength = Slot(
    uri=DBPEDIA.wavelength,
    name="wavelength",
    curie=DBPEDIA.curie("wavelength"),
    model_uri=POKEMON.wavelength,
    domain=None,
    range=Optional[float],
)

slots.frequency = Slot(
    uri=DBPEDIA.frequency,
    name="frequency",
    curie=DBPEDIA.curie("frequency"),
    model_uri=POKEMON.frequency,
    domain=None,
    range=Optional[float],
)

slots.colorHexCode = Slot(
    uri=DBPEDIA.colourHexCode,
    name="colorHexCode",
    curie=DBPEDIA.curie("colourHexCode"),
    model_uri=POKEMON.colorHexCode,
    domain=None,
    range=Optional[str],
)

slots.connotation = Slot(
    uri=DBPEDIA.connotation,
    name="connotation",
    curie=DBPEDIA.curie("connotation"),
    model_uri=POKEMON.connotation,
    domain=None,
    range=Optional[Union[Union[str, ConnotationId], list[Union[str, ConnotationId]]]],
)

slots.thumbnail = Slot(
    uri=DBPEDIA.thumbnail,
    name="thumbnail",
    curie=DBPEDIA.curie("thumbnail"),
    model_uri=POKEMON.thumbnail,
    domain=None,
    range=Optional[Union[str, URI]],
)

slots.id = Slot(
    uri=LINKML_COMMON.identifier,
    name="id",
    curie=LINKML_COMMON.curie("identifier"),
    model_uri=POKEMON.id,
    domain=None,
    range=URIRef,
)

slots.name = Slot(
    uri=RDFS.label,
    name="name",
    curie=RDFS.curie("label"),
    model_uri=POKEMON.name,
    domain=None,
    range=Optional[str],
)

slots.description = Slot(
    uri=RDFS.comment,
    name="description",
    curie=RDFS.curie("comment"),
    model_uri=POKEMON.description,
    domain=None,
    range=Optional[str],
)

slots.hasQuantityKind = Slot(
    uri=QUDT.hasQuantityKind,
    name="hasQuantityKind",
    curie=QUDT.curie("hasQuantityKind"),
    model_uri=POKEMON.hasQuantityKind,
    domain=None,
    range=Optional[Union[Union[str, QuantityKindId], list[Union[str, QuantityKindId]]]],
)

slots.quantityValue = Slot(
    uri=QUDT.quantityValue,
    name="quantityValue",
    curie=QUDT.curie("quantityValue"),
    model_uri=POKEMON.quantityValue,
    domain=None,
    range=Optional[
        Union[Union[str, QuantityValueId], list[Union[str, QuantityValueId]]]
    ],
)

slots.numericValue = Slot(
    uri=QUDT.value,
    name="numericValue",
    curie=QUDT.curie("value"),
    model_uri=POKEMON.numericValue,
    domain=None,
    range=Optional[float],
)

slots.unit = Slot(
    uri=QUDT.unit,
    name="unit",
    curie=QUDT.curie("unit"),
    model_uri=POKEMON.unit,
    domain=None,
    range=Optional[Union[str, UnitId]],
)

slots.symbol = Slot(
    uri=QUDT.symbol,
    name="symbol",
    curie=QUDT.curie("symbol"),
    model_uri=POKEMON.symbol,
    domain=None,
    range=Optional[str],
)

slots.abbreviation = Slot(
    uri=QUDT.abbreviation,
    name="abbreviation",
    curie=QUDT.curie("abbreviation"),
    model_uri=POKEMON.abbreviation,
    domain=None,
    range=Optional[str],
)

slots.conversionMultiplier = Slot(
    uri=QUDT.conversionMultiplier,
    name="conversionMultiplier",
    curie=QUDT.curie("conversionMultiplier"),
    model_uri=POKEMON.conversionMultiplier,
    domain=None,
    range=Optional[float],
)

slots.conversionOffset = Slot(
    uri=QUDT.conversionOffset,
    name="conversionOffset",
    curie=QUDT.curie("conversionOffset"),
    model_uri=POKEMON.conversionOffset,
    domain=None,
    range=Optional[float],
)

slots.hasDimensionVector = Slot(
    uri=QUDT.hasDimensionVector,
    name="hasDimensionVector",
    curie=QUDT.curie("hasDimensionVector"),
    model_uri=POKEMON.hasDimensionVector,
    domain=None,
    range=Optional[Union[str, QuantityKindDimensionVectorId]],
)

slots.isUnitOfSystem = Slot(
    uri=QUDT.isUnitOfSystem,
    name="isUnitOfSystem",
    curie=QUDT.curie("isUnitOfSystem"),
    model_uri=POKEMON.isUnitOfSystem,
    domain=None,
    range=Optional[
        Union[Union[str, SystemOfUnitsId], list[Union[str, SystemOfUnitsId]]]
    ],
)

slots.applicableSystem = Slot(
    uri=QUDT.applicableSystem,
    name="applicableSystem",
    curie=QUDT.curie("applicableSystem"),
    model_uri=POKEMON.applicableSystem,
    domain=None,
    range=Optional[
        Union[Union[str, SystemOfUnitsId], list[Union[str, SystemOfUnitsId]]]
    ],
)

slots.applicableUnit = Slot(
    uri=QUDT.applicableUnit,
    name="applicableUnit",
    curie=QUDT.curie("applicableUnit"),
    model_uri=POKEMON.applicableUnit,
    domain=None,
    range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]],
)

slots.prefix = Slot(
    uri=QUDT.prefix,
    name="prefix",
    curie=QUDT.curie("prefix"),
    model_uri=POKEMON.prefix,
    domain=None,
    range=Optional[Union[str, PrefixId]],
)

slots.scalingOf = Slot(
    uri=QUDT.scalingOf,
    name="scalingOf",
    curie=QUDT.curie("scalingOf"),
    model_uri=POKEMON.scalingOf,
    domain=None,
    range=Optional[Union[str, UnitId]],
)

slots.ucumCode = Slot(
    uri=QUDT.ucumCode,
    name="ucumCode",
    curie=QUDT.curie("ucumCode"),
    model_uri=POKEMON.ucumCode,
    domain=None,
    range=Optional[str],
)

slots.latexSymbol = Slot(
    uri=QUDT.latexSymbol,
    name="latexSymbol",
    curie=QUDT.curie("latexSymbol"),
    model_uri=POKEMON.latexSymbol,
    domain=None,
    range=Optional[str],
)

slots.broader = Slot(
    uri=QUDT.broader,
    name="broader",
    curie=QUDT.curie("broader"),
    model_uri=POKEMON.broader,
    domain=None,
    range=Optional[Union[Union[str, QuantityKindId], list[Union[str, QuantityKindId]]]],
)

slots.exactMatch = Slot(
    uri=QUDT.exactMatch,
    name="exactMatch",
    curie=QUDT.curie("exactMatch"),
    model_uri=POKEMON.exactMatch,
    domain=None,
    range=Optional[Union[str, list[str]]],
)

slots.deprecated = Slot(
    uri=QUDT.deprecated,
    name="deprecated",
    curie=QUDT.curie("deprecated"),
    model_uri=POKEMON.deprecated,
    domain=None,
    range=Optional[Union[bool, Bool]],
)

slots.dimensionExponentForLength = Slot(
    uri=QUDT.dimensionExponentForLength,
    name="dimensionExponentForLength",
    curie=QUDT.curie("dimensionExponentForLength"),
    model_uri=POKEMON.dimensionExponentForLength,
    domain=None,
    range=Optional[int],
)

slots.dimensionExponentForMass = Slot(
    uri=QUDT.dimensionExponentForMass,
    name="dimensionExponentForMass",
    curie=QUDT.curie("dimensionExponentForMass"),
    model_uri=POKEMON.dimensionExponentForMass,
    domain=None,
    range=Optional[int],
)

slots.dimensionExponentForTime = Slot(
    uri=QUDT.dimensionExponentForTime,
    name="dimensionExponentForTime",
    curie=QUDT.curie("dimensionExponentForTime"),
    model_uri=POKEMON.dimensionExponentForTime,
    domain=None,
    range=Optional[int],
)

slots.dimensionExponentForElectricCurrent = Slot(
    uri=QUDT.dimensionExponentForElectricCurrent,
    name="dimensionExponentForElectricCurrent",
    curie=QUDT.curie("dimensionExponentForElectricCurrent"),
    model_uri=POKEMON.dimensionExponentForElectricCurrent,
    domain=None,
    range=Optional[int],
)

slots.dimensionExponentForThermodynamicTemperature = Slot(
    uri=QUDT.dimensionExponentForThermodynamicTemperature,
    name="dimensionExponentForThermodynamicTemperature",
    curie=QUDT.curie("dimensionExponentForThermodynamicTemperature"),
    model_uri=POKEMON.dimensionExponentForThermodynamicTemperature,
    domain=None,
    range=Optional[int],
)

slots.dimensionExponentForAmountOfSubstance = Slot(
    uri=QUDT.dimensionExponentForAmountOfSubstance,
    name="dimensionExponentForAmountOfSubstance",
    curie=QUDT.curie("dimensionExponentForAmountOfSubstance"),
    model_uri=POKEMON.dimensionExponentForAmountOfSubstance,
    domain=None,
    range=Optional[int],
)

slots.dimensionExponentForLuminousIntensity = Slot(
    uri=QUDT.dimensionExponentForLuminousIntensity,
    name="dimensionExponentForLuminousIntensity",
    curie=QUDT.curie("dimensionExponentForLuminousIntensity"),
    model_uri=POKEMON.dimensionExponentForLuminousIntensity,
    domain=None,
    range=Optional[int],
)

slots.dimensionlessExponent = Slot(
    uri=QUDT.dimensionlessExponent,
    name="dimensionlessExponent",
    curie=QUDT.curie("dimensionlessExponent"),
    model_uri=POKEMON.dimensionlessExponent,
    domain=None,
    range=Optional[int],
)

slots.hasBaseUnit = Slot(
    uri=QUDT.hasBaseUnit,
    name="hasBaseUnit",
    curie=QUDT.curie("hasBaseUnit"),
    model_uri=POKEMON.hasBaseUnit,
    domain=None,
    range=Optional[Union[Union[str, UnitId], list[Union[str, UnitId]]]],
)

slots.prefixMultiplier = Slot(
    uri=QUDT.prefixMultiplier,
    name="prefixMultiplier",
    curie=QUDT.curie("prefixMultiplier"),
    model_uri=POKEMON.prefixMultiplier,
    domain=None,
    range=Optional[float],
)

slots.hasUnit = Slot(
    uri=QUDT.hasUnit,
    name="hasUnit",
    curie=QUDT.curie("hasUnit"),
    model_uri=POKEMON.hasUnit,
    domain=None,
    range=Optional[Union[str, UnitId]],
)

slots.standardUncertainty = Slot(
    uri=QUDT.standardUncertainty,
    name="standardUncertainty",
    curie=QUDT.curie("standardUncertainty"),
    model_uri=POKEMON.standardUncertainty,
    domain=None,
    range=Optional[Decimal],
)

slots.relativeStandardUncertainty = Slot(
    uri=QUDT.relativeStandardUncertainty,
    name="relativeStandardUncertainty",
    curie=QUDT.curie("relativeStandardUncertainty"),
    model_uri=POKEMON.relativeStandardUncertainty,
    domain=None,
    range=Optional[float],
)

slots.wikidataMatch = Slot(
    uri=QUDT.wikidataMatch,
    name="wikidataMatch",
    curie=QUDT.curie("wikidataMatch"),
    model_uri=POKEMON.wikidataMatch,
    domain=None,
    range=Optional[Union[str, URI]],
)

slots.isoNormativeReference = Slot(
    uri=QUDT.isoNormativeReference,
    name="isoNormativeReference",
    curie=QUDT.curie("isoNormativeReference"),
    model_uri=POKEMON.isoNormativeReference,
    domain=None,
    range=Optional[Union[Union[str, URI], list[Union[str, URI]]]],
)

slots.normativeReference = Slot(
    uri=QUDT.normativeReference,
    name="normativeReference",
    curie=QUDT.curie("normativeReference"),
    model_uri=POKEMON.normativeReference,
    domain=None,
    range=Optional[Union[Union[str, URI], list[Union[str, URI]]]],
)

slots.dbpediaMatch = Slot(
    uri=QUDT.dbpediaMatch,
    name="dbpediaMatch",
    curie=QUDT.curie("dbpediaMatch"),
    model_uri=POKEMON.dbpediaMatch,
    domain=None,
    range=Optional[Union[str, URI]],
)

slots.informativeReference = Slot(
    uri=QUDT.informativeReference,
    name="informativeReference",
    curie=QUDT.curie("informativeReference"),
    model_uri=POKEMON.informativeReference,
    domain=None,
    range=Optional[Union[Union[str, URI], list[Union[str, URI]]]],
)

slots.plainTextDescription = Slot(
    uri=QUDT.plainTextDescription,
    name="plainTextDescription",
    curie=QUDT.curie("plainTextDescription"),
    model_uri=POKEMON.plainTextDescription,
    domain=None,
    range=Optional[str],
)

slots.Connotation_name = Slot(
    uri=RDFS.label,
    name="Connotation_name",
    curie=RDFS.curie("label"),
    model_uri=POKEMON.Connotation_name,
    domain=Connotation,
    range=str,
)

slots.NamedIndividual_name = Slot(
    uri=RDFS.label,
    name="NamedIndividual_name",
    curie=RDFS.curie("label"),
    model_uri=POKEMON.NamedIndividual_name,
    domain=NamedIndividual,
    range=str,
)
