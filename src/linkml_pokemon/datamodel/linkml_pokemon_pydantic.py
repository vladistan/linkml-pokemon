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
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.7.0"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





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


linkml_meta = LinkMLMeta({'annotations': {'dcterms:description': {'tag': 'dcterms:description',
                                             'value': 'Ontology covering the '
                                                      'Pokemon world as it is '
                                                      'presented in games and '
                                                      'anime television series.'},
                     'dcterms:issued': {'tag': 'dcterms:issued',
                                        'value': '2019-07-27^^xsd:date'}},
     'created_on': '2019-07-27T00:00:00',
     'default_prefix': 'pokemon',
     'default_range': 'string',
     'description': 'Ontology covering the Pokémon world as it is presented in '
                    'games and anime television series',
     'id': 'https://pokemonkg.org/ontology',
     'imports': ['linkml:types', './foaf', './dbpedia', './owl', './qudt'],
     'license': 'MIT',
     'name': 'linkml-pokemon',
     'prefixes': {'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'dbpedia': {'prefix_prefix': 'dbpedia',
                              'prefix_reference': 'http://dbpedia.org/ontology/'},
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
                  'qudt': {'prefix_prefix': 'qudt',
                           'prefix_reference': 'http://qudt.org/schema/qudt/'},
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
     'title': 'Pokemon Ontology'} )

class HabitatEnum(str, Enum):
    Cave = "Cave"
    Forest = "Forest"
    Grassland = "Grassland"



class Thing(ConfiguredBaseModel):
    """
    An rdfs:Resource that defines name and description
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'owl:Thing',
         'from_schema': 'http://www.w3.org/2002/07/owl'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class NamedIndividual(Thing):
    """
    A Thing that requires a name
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'owl:NamedIndividual',
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'slot_usage': {'name': {'name': 'name', 'required': True}}})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Person(NamedIndividual):
    """
    A person is a human being
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'foaf:Person', 'from_schema': 'http://xmlns.com/foaf/0.1/'})

    depiction: Optional[str] = Field(default=None, description="""A depiction of the person""", json_schema_extra = { "linkml_meta": {'domain_of': ['Person', 'Species'], 'slot_uri': 'foaf:depiction'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Colour(Thing):
    """
    Color or colour is the visual perceptual property corresponding in humans to the categories called red, yellow, blue and others.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dbpedia:Colour', 'from_schema': 'https://dbpedia.org/ontology/'})

    cyanic: Optional[int] = Field(default=None, description="""Cyan component in CMYK color model (0-100)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Colour'], 'slot_uri': 'dbpedia:cmykCoordinateCyanic'} })
    magenta: Optional[int] = Field(default=None, description="""Magenta component in CMYK color model (0-100)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Colour'], 'slot_uri': 'dbpedia:cmykCoordinateMagenta'} })
    colourYellow: Optional[int] = Field(default=None, description="""Yellow component in CMYK color model (0-100)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Colour'], 'slot_uri': 'dbpedia:cmykCoordinateYellow'} })
    black: Optional[int] = Field(default=None, description="""Black (K) component in CMYK color model (0-100)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Colour'], 'slot_uri': 'dbpedia:cmykCoordinateBlack'} })
    wavelength: Optional[float] = Field(default=None, description="""The wavelength of the color in meters (e.g., 4.5e-07 for blue)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Colour'], 'slot_uri': 'dbpedia:wavelength'} })
    frequency: Optional[float] = Field(default=None, description="""The frequency of the color in Hz""", json_schema_extra = { "linkml_meta": {'domain_of': ['Colour'], 'slot_uri': 'dbpedia:frequency'} })
    colourHexCode: Optional[str] = Field(default=None, description="""Hexadecimal RGB color code (e.g., \"0000FF\" for blue)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Colour'], 'slot_uri': 'dbpedia:colourHexCode'} })
    connotation: Optional[list[str]] = Field(default=None, description="""Cultural or symbolic meanings associated with this colour""", json_schema_extra = { "linkml_meta": {'domain_of': ['Colour'], 'slot_uri': 'dbpedia:connotation'} })
    thumbnail: Optional[str] = Field(default=None, description="""URL to a representative image of this colour""", json_schema_extra = { "linkml_meta": {'domain_of': ['Colour'], 'slot_uri': 'dbpedia:thumbnail'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Connotation(Thing):
    """
    Cultural or symbolic meaning associated with a colour. Imported from DBpedia as generic owl:Thing resources.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'owl:Thing',
         'from_schema': 'https://dbpedia.org/ontology/',
         'slot_usage': {'name': {'name': 'name', 'required': True}}})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Quantity(ConfiguredBaseModel):
    """
    A measured quantity with kind and value
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Quantity',
         'from_schema': 'https://pokemonkg.org/schema/qudt'})

    hasQuantityKind: Optional[list[QuantityKind]] = Field(default=None, description="""Associates a quantity with its kind (e.g., Height, Weight)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity', 'Unit'], 'slot_uri': 'qudt:hasQuantityKind'} })
    quantityValue: Optional[list[QuantityValue]] = Field(default=None, description="""The value component of a quantity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity'], 'slot_uri': 'qudt:quantityValue'} })
    plainTextDescription: Optional[str] = Field(default=None, description="""Plain text description""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity',
                       'QuantityValue',
                       'QuantityKind',
                       'Unit',
                       'SystemOfUnits',
                       'QuantityKindDimensionVector',
                       'Prefix'],
         'slot_uri': 'qudt:plainTextDescription'} })
    deprecated: Optional[bool] = Field(default=None, description="""Whether this entity is deprecated""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity',
                       'QuantityValue',
                       'QuantityKind',
                       'Unit',
                       'SystemOfUnits',
                       'QuantityKindDimensionVector',
                       'Prefix'],
         'slot_uri': 'qudt:deprecated'} })


class QuantityValue(ConfiguredBaseModel):
    """
    Numeric value with unit
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:QuantityValue',
         'from_schema': 'https://pokemonkg.org/schema/qudt'})

    numericValue: Optional[float] = Field(default=None, description="""Numeric value of a quantity""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityValue'], 'slot_uri': 'qudt:value'} })
    unit: Optional[Unit] = Field(default=None, description="""Unit of measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityValue'], 'slot_uri': 'qudt:unit'} })
    plainTextDescription: Optional[str] = Field(default=None, description="""Plain text description""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity',
                       'QuantityValue',
                       'QuantityKind',
                       'Unit',
                       'SystemOfUnits',
                       'QuantityKindDimensionVector',
                       'Prefix'],
         'slot_uri': 'qudt:plainTextDescription'} })
    deprecated: Optional[bool] = Field(default=None, description="""Whether this entity is deprecated""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity',
                       'QuantityValue',
                       'QuantityKind',
                       'Unit',
                       'SystemOfUnits',
                       'QuantityKindDimensionVector',
                       'Prefix'],
         'slot_uri': 'qudt:deprecated'} })


class QuantityKind(ConfiguredBaseModel):
    """
    Kind of quantity (e.g., Length, Mass, Height, Weight)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:QuantityKind',
         'from_schema': 'https://pokemonkg.org/schema/qudt'})

    symbol: Optional[str] = Field(default=None, description="""Symbol for a unit (e.g., \"m\" for meter)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit', 'Prefix'], 'slot_uri': 'qudt:symbol'} })
    latexSymbol: Optional[str] = Field(default=None, description="""LaTeX representation of symbol""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit', 'QuantityKindDimensionVector'],
         'slot_uri': 'qudt:latexSymbol'} })
    abbreviation: Optional[str] = Field(default=None, description="""Short alphanumeric abbreviation for a unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit', 'SystemOfUnits'],
         'slot_uri': 'qudt:abbreviation'} })
    hasDimensionVector: Optional[QuantityKindDimensionVector] = Field(default=None, description="""Dimension vector for a unit or quantity kind""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit'], 'slot_uri': 'qudt:hasDimensionVector'} })
    applicableUnit: Optional[list[Unit]] = Field(default=None, description="""Units applicable to a quantity kind""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind'], 'slot_uri': 'qudt:applicableUnit'} })
    broader: Optional[list[QuantityKind]] = Field(default=None, description="""Broader/parent quantity kind""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind'], 'slot_uri': 'qudt:broader'} })
    exactMatch: Optional[list[str]] = Field(default=None, description="""Equivalent quantity kind or unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Prefix'], 'slot_uri': 'qudt:exactMatch'} })
    deprecated: Optional[bool] = Field(default=None, description="""Whether this entity is deprecated""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity',
                       'QuantityValue',
                       'QuantityKind',
                       'Unit',
                       'SystemOfUnits',
                       'QuantityKindDimensionVector',
                       'Prefix'],
         'slot_uri': 'qudt:deprecated'} })
    dbpediaMatch: Optional[str] = Field(default=None, description="""DBpedia URI for this entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit', 'SystemOfUnits', 'Prefix'],
         'slot_uri': 'qudt:dbpediaMatch'} })
    informativeReference: Optional[list[str]] = Field(default=None, description="""Informative reference URL""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit', 'SystemOfUnits', 'Prefix'],
         'slot_uri': 'qudt:informativeReference'} })
    plainTextDescription: Optional[str] = Field(default=None, description="""Plain text description""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity',
                       'QuantityValue',
                       'QuantityKind',
                       'Unit',
                       'SystemOfUnits',
                       'QuantityKindDimensionVector',
                       'Prefix'],
         'slot_uri': 'qudt:plainTextDescription'} })


class Unit(ConfiguredBaseModel):
    """
    Unit of measurement
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Unit', 'from_schema': 'https://pokemonkg.org/schema/qudt'})

    symbol: Optional[str] = Field(default=None, description="""Symbol for a unit (e.g., \"m\" for meter)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit', 'Prefix'], 'slot_uri': 'qudt:symbol'} })
    latexSymbol: Optional[str] = Field(default=None, description="""LaTeX representation of symbol""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit', 'QuantityKindDimensionVector'],
         'slot_uri': 'qudt:latexSymbol'} })
    abbreviation: Optional[str] = Field(default=None, description="""Short alphanumeric abbreviation for a unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit', 'SystemOfUnits'],
         'slot_uri': 'qudt:abbreviation'} })
    conversionMultiplier: Optional[float] = Field(default=None, description="""Multiplier to convert to base unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:conversionMultiplier'} })
    conversionOffset: Optional[float] = Field(default=None, description="""Offset to convert to base unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:conversionOffset'} })
    hasDimensionVector: Optional[QuantityKindDimensionVector] = Field(default=None, description="""Dimension vector for a unit or quantity kind""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit'], 'slot_uri': 'qudt:hasDimensionVector'} })
    hasQuantityKind: Optional[list[QuantityKind]] = Field(default=None, description="""Associates a quantity with its kind (e.g., Height, Weight)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity', 'Unit'], 'slot_uri': 'qudt:hasQuantityKind'} })
    isUnitOfSystem: Optional[list[SystemOfUnits]] = Field(default=None, description="""System of units this unit belongs to""", json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:isUnitOfSystem'} })
    applicableSystem: Optional[list[SystemOfUnits]] = Field(default=None, description="""Systems where this unit is applicable""", json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:applicableSystem'} })
    prefix: Optional[Prefix] = Field(default=None, description="""Prefix for a unit (e.g., Kilo, Milli)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Unit', 'SystemOfUnits'], 'slot_uri': 'qudt:prefix'} })
    scalingOf: Optional[Unit] = Field(default=None, description="""Base unit this unit is a scaling of""", json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:scalingOf'} })
    ucumCode: Optional[str] = Field(default=None, description="""UCUM code for the unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['Unit', 'Prefix'], 'slot_uri': 'qudt:ucumCode'} })
    dbpediaMatch: Optional[str] = Field(default=None, description="""DBpedia URI for this entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit', 'SystemOfUnits', 'Prefix'],
         'slot_uri': 'qudt:dbpediaMatch'} })
    informativeReference: Optional[list[str]] = Field(default=None, description="""Informative reference URL""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit', 'SystemOfUnits', 'Prefix'],
         'slot_uri': 'qudt:informativeReference'} })
    plainTextDescription: Optional[str] = Field(default=None, description="""Plain text description""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity',
                       'QuantityValue',
                       'QuantityKind',
                       'Unit',
                       'SystemOfUnits',
                       'QuantityKindDimensionVector',
                       'Prefix'],
         'slot_uri': 'qudt:plainTextDescription'} })
    deprecated: Optional[bool] = Field(default=None, description="""Whether this entity is deprecated""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity',
                       'QuantityValue',
                       'QuantityKind',
                       'Unit',
                       'SystemOfUnits',
                       'QuantityKindDimensionVector',
                       'Prefix'],
         'slot_uri': 'qudt:deprecated'} })


class DerivedUnit(Unit):
    """
    Unit derived from base units (e.g., KiloM)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:DerivedUnit',
         'from_schema': 'https://pokemonkg.org/schema/qudt'})

    symbol: Optional[str] = Field(default=None, description="""Symbol for a unit (e.g., \"m\" for meter)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit', 'Prefix'], 'slot_uri': 'qudt:symbol'} })
    latexSymbol: Optional[str] = Field(default=None, description="""LaTeX representation of symbol""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit', 'QuantityKindDimensionVector'],
         'slot_uri': 'qudt:latexSymbol'} })
    abbreviation: Optional[str] = Field(default=None, description="""Short alphanumeric abbreviation for a unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit', 'SystemOfUnits'],
         'slot_uri': 'qudt:abbreviation'} })
    conversionMultiplier: Optional[float] = Field(default=None, description="""Multiplier to convert to base unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:conversionMultiplier'} })
    conversionOffset: Optional[float] = Field(default=None, description="""Offset to convert to base unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:conversionOffset'} })
    hasDimensionVector: Optional[QuantityKindDimensionVector] = Field(default=None, description="""Dimension vector for a unit or quantity kind""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit'], 'slot_uri': 'qudt:hasDimensionVector'} })
    hasQuantityKind: Optional[list[QuantityKind]] = Field(default=None, description="""Associates a quantity with its kind (e.g., Height, Weight)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity', 'Unit'], 'slot_uri': 'qudt:hasQuantityKind'} })
    isUnitOfSystem: Optional[list[SystemOfUnits]] = Field(default=None, description="""System of units this unit belongs to""", json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:isUnitOfSystem'} })
    applicableSystem: Optional[list[SystemOfUnits]] = Field(default=None, description="""Systems where this unit is applicable""", json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:applicableSystem'} })
    prefix: Optional[Prefix] = Field(default=None, description="""Prefix for a unit (e.g., Kilo, Milli)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Unit', 'SystemOfUnits'], 'slot_uri': 'qudt:prefix'} })
    scalingOf: Optional[Unit] = Field(default=None, description="""Base unit this unit is a scaling of""", json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:scalingOf'} })
    ucumCode: Optional[str] = Field(default=None, description="""UCUM code for the unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['Unit', 'Prefix'], 'slot_uri': 'qudt:ucumCode'} })
    dbpediaMatch: Optional[str] = Field(default=None, description="""DBpedia URI for this entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit', 'SystemOfUnits', 'Prefix'],
         'slot_uri': 'qudt:dbpediaMatch'} })
    informativeReference: Optional[list[str]] = Field(default=None, description="""Informative reference URL""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit', 'SystemOfUnits', 'Prefix'],
         'slot_uri': 'qudt:informativeReference'} })
    plainTextDescription: Optional[str] = Field(default=None, description="""Plain text description""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity',
                       'QuantityValue',
                       'QuantityKind',
                       'Unit',
                       'SystemOfUnits',
                       'QuantityKindDimensionVector',
                       'Prefix'],
         'slot_uri': 'qudt:plainTextDescription'} })
    deprecated: Optional[bool] = Field(default=None, description="""Whether this entity is deprecated""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity',
                       'QuantityValue',
                       'QuantityKind',
                       'Unit',
                       'SystemOfUnits',
                       'QuantityKindDimensionVector',
                       'Prefix'],
         'slot_uri': 'qudt:deprecated'} })


class SystemOfUnits(ConfiguredBaseModel):
    """
    A coherent system of units (e.g., SI, CGS)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:SystemOfUnits',
         'from_schema': 'https://pokemonkg.org/schema/qudt'})

    abbreviation: Optional[str] = Field(default=None, description="""Short alphanumeric abbreviation for a unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit', 'SystemOfUnits'],
         'slot_uri': 'qudt:abbreviation'} })
    hasBaseUnit: Optional[list[Unit]] = Field(default=None, description="""Base units defined by this system""", json_schema_extra = { "linkml_meta": {'domain_of': ['SystemOfUnits'], 'slot_uri': 'qudt:hasBaseUnit'} })
    prefix: Optional[Prefix] = Field(default=None, description="""Prefix for a unit (e.g., Kilo, Milli)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Unit', 'SystemOfUnits'], 'slot_uri': 'qudt:prefix'} })
    dbpediaMatch: Optional[str] = Field(default=None, description="""DBpedia URI for this entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit', 'SystemOfUnits', 'Prefix'],
         'slot_uri': 'qudt:dbpediaMatch'} })
    informativeReference: Optional[list[str]] = Field(default=None, description="""Informative reference URL""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit', 'SystemOfUnits', 'Prefix'],
         'slot_uri': 'qudt:informativeReference'} })
    plainTextDescription: Optional[str] = Field(default=None, description="""Plain text description""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity',
                       'QuantityValue',
                       'QuantityKind',
                       'Unit',
                       'SystemOfUnits',
                       'QuantityKindDimensionVector',
                       'Prefix'],
         'slot_uri': 'qudt:plainTextDescription'} })
    deprecated: Optional[bool] = Field(default=None, description="""Whether this entity is deprecated""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity',
                       'QuantityValue',
                       'QuantityKind',
                       'Unit',
                       'SystemOfUnits',
                       'QuantityKindDimensionVector',
                       'Prefix'],
         'slot_uri': 'qudt:deprecated'} })


class QuantityKindDimensionVector(ConfiguredBaseModel):
    """
    Dimension vector expressing quantity in base dimensions
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:QuantityKindDimensionVector',
         'from_schema': 'https://pokemonkg.org/schema/qudt'})

    latexSymbol: Optional[str] = Field(default=None, description="""LaTeX representation of symbol""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit', 'QuantityKindDimensionVector'],
         'slot_uri': 'qudt:latexSymbol'} })
    dimensionExponentForLength: Optional[int] = Field(default=None, description="""Exponent for length dimension (L)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForLength'} })
    dimensionExponentForMass: Optional[int] = Field(default=None, description="""Exponent for mass dimension (M)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForMass'} })
    dimensionExponentForTime: Optional[int] = Field(default=None, description="""Exponent for time dimension (T)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForTime'} })
    dimensionExponentForElectricCurrent: Optional[int] = Field(default=None, description="""Exponent for electric current dimension (I)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForElectricCurrent'} })
    dimensionExponentForThermodynamicTemperature: Optional[int] = Field(default=None, description="""Exponent for temperature dimension (Θ)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForThermodynamicTemperature'} })
    dimensionExponentForAmountOfSubstance: Optional[int] = Field(default=None, description="""Exponent for amount of substance dimension (N)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForAmountOfSubstance'} })
    dimensionExponentForLuminousIntensity: Optional[int] = Field(default=None, description="""Exponent for luminous intensity dimension (J)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForLuminousIntensity'} })
    dimensionlessExponent: Optional[int] = Field(default=None, description="""Dimensionless exponent""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionlessExponent'} })
    plainTextDescription: Optional[str] = Field(default=None, description="""Plain text description""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity',
                       'QuantityValue',
                       'QuantityKind',
                       'Unit',
                       'SystemOfUnits',
                       'QuantityKindDimensionVector',
                       'Prefix'],
         'slot_uri': 'qudt:plainTextDescription'} })
    deprecated: Optional[bool] = Field(default=None, description="""Whether this entity is deprecated""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity',
                       'QuantityValue',
                       'QuantityKind',
                       'Unit',
                       'SystemOfUnits',
                       'QuantityKindDimensionVector',
                       'Prefix'],
         'slot_uri': 'qudt:deprecated'} })


class QuantityKindDimensionVectorSI(QuantityKindDimensionVector):
    """
    SI dimension vector
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:QuantityKindDimensionVector_SI',
         'from_schema': 'https://pokemonkg.org/schema/qudt'})

    latexSymbol: Optional[str] = Field(default=None, description="""LaTeX representation of symbol""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit', 'QuantityKindDimensionVector'],
         'slot_uri': 'qudt:latexSymbol'} })
    dimensionExponentForLength: Optional[int] = Field(default=None, description="""Exponent for length dimension (L)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForLength'} })
    dimensionExponentForMass: Optional[int] = Field(default=None, description="""Exponent for mass dimension (M)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForMass'} })
    dimensionExponentForTime: Optional[int] = Field(default=None, description="""Exponent for time dimension (T)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForTime'} })
    dimensionExponentForElectricCurrent: Optional[int] = Field(default=None, description="""Exponent for electric current dimension (I)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForElectricCurrent'} })
    dimensionExponentForThermodynamicTemperature: Optional[int] = Field(default=None, description="""Exponent for temperature dimension (Θ)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForThermodynamicTemperature'} })
    dimensionExponentForAmountOfSubstance: Optional[int] = Field(default=None, description="""Exponent for amount of substance dimension (N)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForAmountOfSubstance'} })
    dimensionExponentForLuminousIntensity: Optional[int] = Field(default=None, description="""Exponent for luminous intensity dimension (J)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForLuminousIntensity'} })
    dimensionlessExponent: Optional[int] = Field(default=None, description="""Dimensionless exponent""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionlessExponent'} })
    plainTextDescription: Optional[str] = Field(default=None, description="""Plain text description""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity',
                       'QuantityValue',
                       'QuantityKind',
                       'Unit',
                       'SystemOfUnits',
                       'QuantityKindDimensionVector',
                       'Prefix'],
         'slot_uri': 'qudt:plainTextDescription'} })
    deprecated: Optional[bool] = Field(default=None, description="""Whether this entity is deprecated""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity',
                       'QuantityValue',
                       'QuantityKind',
                       'Unit',
                       'SystemOfUnits',
                       'QuantityKindDimensionVector',
                       'Prefix'],
         'slot_uri': 'qudt:deprecated'} })


class QuantityKindDimensionVectorCGS(QuantityKindDimensionVector):
    """
    CGS dimension vector
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:QuantityKindDimensionVector_CGS',
         'from_schema': 'https://pokemonkg.org/schema/qudt'})

    latexSymbol: Optional[str] = Field(default=None, description="""LaTeX representation of symbol""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit', 'QuantityKindDimensionVector'],
         'slot_uri': 'qudt:latexSymbol'} })
    dimensionExponentForLength: Optional[int] = Field(default=None, description="""Exponent for length dimension (L)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForLength'} })
    dimensionExponentForMass: Optional[int] = Field(default=None, description="""Exponent for mass dimension (M)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForMass'} })
    dimensionExponentForTime: Optional[int] = Field(default=None, description="""Exponent for time dimension (T)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForTime'} })
    dimensionExponentForElectricCurrent: Optional[int] = Field(default=None, description="""Exponent for electric current dimension (I)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForElectricCurrent'} })
    dimensionExponentForThermodynamicTemperature: Optional[int] = Field(default=None, description="""Exponent for temperature dimension (Θ)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForThermodynamicTemperature'} })
    dimensionExponentForAmountOfSubstance: Optional[int] = Field(default=None, description="""Exponent for amount of substance dimension (N)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForAmountOfSubstance'} })
    dimensionExponentForLuminousIntensity: Optional[int] = Field(default=None, description="""Exponent for luminous intensity dimension (J)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForLuminousIntensity'} })
    dimensionlessExponent: Optional[int] = Field(default=None, description="""Dimensionless exponent""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionlessExponent'} })
    plainTextDescription: Optional[str] = Field(default=None, description="""Plain text description""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity',
                       'QuantityValue',
                       'QuantityKind',
                       'Unit',
                       'SystemOfUnits',
                       'QuantityKindDimensionVector',
                       'Prefix'],
         'slot_uri': 'qudt:plainTextDescription'} })
    deprecated: Optional[bool] = Field(default=None, description="""Whether this entity is deprecated""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity',
                       'QuantityValue',
                       'QuantityKind',
                       'Unit',
                       'SystemOfUnits',
                       'QuantityKindDimensionVector',
                       'Prefix'],
         'slot_uri': 'qudt:deprecated'} })


class QuantityKindDimensionVectorImperial(QuantityKindDimensionVector):
    """
    Imperial dimension vector
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:QuantityKindDimensionVector_Imperial',
         'from_schema': 'https://pokemonkg.org/schema/qudt'})

    latexSymbol: Optional[str] = Field(default=None, description="""LaTeX representation of symbol""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit', 'QuantityKindDimensionVector'],
         'slot_uri': 'qudt:latexSymbol'} })
    dimensionExponentForLength: Optional[int] = Field(default=None, description="""Exponent for length dimension (L)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForLength'} })
    dimensionExponentForMass: Optional[int] = Field(default=None, description="""Exponent for mass dimension (M)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForMass'} })
    dimensionExponentForTime: Optional[int] = Field(default=None, description="""Exponent for time dimension (T)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForTime'} })
    dimensionExponentForElectricCurrent: Optional[int] = Field(default=None, description="""Exponent for electric current dimension (I)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForElectricCurrent'} })
    dimensionExponentForThermodynamicTemperature: Optional[int] = Field(default=None, description="""Exponent for temperature dimension (Θ)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForThermodynamicTemperature'} })
    dimensionExponentForAmountOfSubstance: Optional[int] = Field(default=None, description="""Exponent for amount of substance dimension (N)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForAmountOfSubstance'} })
    dimensionExponentForLuminousIntensity: Optional[int] = Field(default=None, description="""Exponent for luminous intensity dimension (J)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForLuminousIntensity'} })
    dimensionlessExponent: Optional[int] = Field(default=None, description="""Dimensionless exponent""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionlessExponent'} })
    plainTextDescription: Optional[str] = Field(default=None, description="""Plain text description""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity',
                       'QuantityValue',
                       'QuantityKind',
                       'Unit',
                       'SystemOfUnits',
                       'QuantityKindDimensionVector',
                       'Prefix'],
         'slot_uri': 'qudt:plainTextDescription'} })
    deprecated: Optional[bool] = Field(default=None, description="""Whether this entity is deprecated""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity',
                       'QuantityValue',
                       'QuantityKind',
                       'Unit',
                       'SystemOfUnits',
                       'QuantityKindDimensionVector',
                       'Prefix'],
         'slot_uri': 'qudt:deprecated'} })


class QuantityKindDimensionVectorISO(QuantityKindDimensionVector):
    """
    ISO dimension vector
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:QuantityKindDimensionVector_ISO',
         'from_schema': 'https://pokemonkg.org/schema/qudt'})

    latexSymbol: Optional[str] = Field(default=None, description="""LaTeX representation of symbol""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit', 'QuantityKindDimensionVector'],
         'slot_uri': 'qudt:latexSymbol'} })
    dimensionExponentForLength: Optional[int] = Field(default=None, description="""Exponent for length dimension (L)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForLength'} })
    dimensionExponentForMass: Optional[int] = Field(default=None, description="""Exponent for mass dimension (M)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForMass'} })
    dimensionExponentForTime: Optional[int] = Field(default=None, description="""Exponent for time dimension (T)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForTime'} })
    dimensionExponentForElectricCurrent: Optional[int] = Field(default=None, description="""Exponent for electric current dimension (I)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForElectricCurrent'} })
    dimensionExponentForThermodynamicTemperature: Optional[int] = Field(default=None, description="""Exponent for temperature dimension (Θ)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForThermodynamicTemperature'} })
    dimensionExponentForAmountOfSubstance: Optional[int] = Field(default=None, description="""Exponent for amount of substance dimension (N)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForAmountOfSubstance'} })
    dimensionExponentForLuminousIntensity: Optional[int] = Field(default=None, description="""Exponent for luminous intensity dimension (J)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionExponentForLuminousIntensity'} })
    dimensionlessExponent: Optional[int] = Field(default=None, description="""Dimensionless exponent""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKindDimensionVector'],
         'slot_uri': 'qudt:dimensionlessExponent'} })
    plainTextDescription: Optional[str] = Field(default=None, description="""Plain text description""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity',
                       'QuantityValue',
                       'QuantityKind',
                       'Unit',
                       'SystemOfUnits',
                       'QuantityKindDimensionVector',
                       'Prefix'],
         'slot_uri': 'qudt:plainTextDescription'} })
    deprecated: Optional[bool] = Field(default=None, description="""Whether this entity is deprecated""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity',
                       'QuantityValue',
                       'QuantityKind',
                       'Unit',
                       'SystemOfUnits',
                       'QuantityKindDimensionVector',
                       'Prefix'],
         'slot_uri': 'qudt:deprecated'} })


class Prefix(ConfiguredBaseModel):
    """
    Unit prefix (e.g., Kilo, Milli)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Prefix', 'from_schema': 'https://pokemonkg.org/schema/qudt'})

    symbol: Optional[str] = Field(default=None, description="""Symbol for a unit (e.g., \"m\" for meter)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit', 'Prefix'], 'slot_uri': 'qudt:symbol'} })
    prefixMultiplier: Optional[float] = Field(default=None, description="""Numeric multiplier for the prefix (e.g., 1000 for Kilo)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Prefix'], 'slot_uri': 'qudt:prefixMultiplier'} })
    ucumCode: Optional[str] = Field(default=None, description="""UCUM code for the unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['Unit', 'Prefix'], 'slot_uri': 'qudt:ucumCode'} })
    exactMatch: Optional[list[str]] = Field(default=None, description="""Equivalent quantity kind or unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Prefix'], 'slot_uri': 'qudt:exactMatch'} })
    dbpediaMatch: Optional[str] = Field(default=None, description="""DBpedia URI for this entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit', 'SystemOfUnits', 'Prefix'],
         'slot_uri': 'qudt:dbpediaMatch'} })
    informativeReference: Optional[list[str]] = Field(default=None, description="""Informative reference URL""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit', 'SystemOfUnits', 'Prefix'],
         'slot_uri': 'qudt:informativeReference'} })
    plainTextDescription: Optional[str] = Field(default=None, description="""Plain text description""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity',
                       'QuantityValue',
                       'QuantityKind',
                       'Unit',
                       'SystemOfUnits',
                       'QuantityKindDimensionVector',
                       'Prefix'],
         'slot_uri': 'qudt:plainTextDescription'} })
    deprecated: Optional[bool] = Field(default=None, description="""Whether this entity is deprecated""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity',
                       'QuantityValue',
                       'QuantityKind',
                       'Unit',
                       'SystemOfUnits',
                       'QuantityKindDimensionVector',
                       'Prefix'],
         'slot_uri': 'qudt:deprecated'} })


class DecimalPrefix(Prefix):
    """
    Decimal prefix (powers of 10)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:DecimalPrefix',
         'from_schema': 'https://pokemonkg.org/schema/qudt'})

    symbol: Optional[str] = Field(default=None, description="""Symbol for a unit (e.g., \"m\" for meter)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit', 'Prefix'], 'slot_uri': 'qudt:symbol'} })
    prefixMultiplier: Optional[float] = Field(default=None, description="""Numeric multiplier for the prefix (e.g., 1000 for Kilo)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Prefix'], 'slot_uri': 'qudt:prefixMultiplier'} })
    ucumCode: Optional[str] = Field(default=None, description="""UCUM code for the unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['Unit', 'Prefix'], 'slot_uri': 'qudt:ucumCode'} })
    exactMatch: Optional[list[str]] = Field(default=None, description="""Equivalent quantity kind or unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Prefix'], 'slot_uri': 'qudt:exactMatch'} })
    dbpediaMatch: Optional[str] = Field(default=None, description="""DBpedia URI for this entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit', 'SystemOfUnits', 'Prefix'],
         'slot_uri': 'qudt:dbpediaMatch'} })
    informativeReference: Optional[list[str]] = Field(default=None, description="""Informative reference URL""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit', 'SystemOfUnits', 'Prefix'],
         'slot_uri': 'qudt:informativeReference'} })
    plainTextDescription: Optional[str] = Field(default=None, description="""Plain text description""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity',
                       'QuantityValue',
                       'QuantityKind',
                       'Unit',
                       'SystemOfUnits',
                       'QuantityKindDimensionVector',
                       'Prefix'],
         'slot_uri': 'qudt:plainTextDescription'} })
    deprecated: Optional[bool] = Field(default=None, description="""Whether this entity is deprecated""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity',
                       'QuantityValue',
                       'QuantityKind',
                       'Unit',
                       'SystemOfUnits',
                       'QuantityKindDimensionVector',
                       'Prefix'],
         'slot_uri': 'qudt:deprecated'} })


class BinaryPrefix(Prefix):
    """
    Binary prefix (powers of 1024)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:BinaryPrefix',
         'from_schema': 'https://pokemonkg.org/schema/qudt'})

    symbol: Optional[str] = Field(default=None, description="""Symbol for a unit (e.g., \"m\" for meter)""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit', 'Prefix'], 'slot_uri': 'qudt:symbol'} })
    prefixMultiplier: Optional[float] = Field(default=None, description="""Numeric multiplier for the prefix (e.g., 1000 for Kilo)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Prefix'], 'slot_uri': 'qudt:prefixMultiplier'} })
    ucumCode: Optional[str] = Field(default=None, description="""UCUM code for the unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['Unit', 'Prefix'], 'slot_uri': 'qudt:ucumCode'} })
    exactMatch: Optional[list[str]] = Field(default=None, description="""Equivalent quantity kind or unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Prefix'], 'slot_uri': 'qudt:exactMatch'} })
    dbpediaMatch: Optional[str] = Field(default=None, description="""DBpedia URI for this entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit', 'SystemOfUnits', 'Prefix'],
         'slot_uri': 'qudt:dbpediaMatch'} })
    informativeReference: Optional[list[str]] = Field(default=None, description="""Informative reference URL""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind', 'Unit', 'SystemOfUnits', 'Prefix'],
         'slot_uri': 'qudt:informativeReference'} })
    plainTextDescription: Optional[str] = Field(default=None, description="""Plain text description""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity',
                       'QuantityValue',
                       'QuantityKind',
                       'Unit',
                       'SystemOfUnits',
                       'QuantityKindDimensionVector',
                       'Prefix'],
         'slot_uri': 'qudt:plainTextDescription'} })
    deprecated: Optional[bool] = Field(default=None, description="""Whether this entity is deprecated""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity',
                       'QuantityValue',
                       'QuantityKind',
                       'Unit',
                       'SystemOfUnits',
                       'QuantityKindDimensionVector',
                       'Prefix'],
         'slot_uri': 'qudt:deprecated'} })


class Ability(Thing):
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

    effectDescription: Optional[list[str]] = Field(default=None, description="""A description of the effect of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Ability', 'Move'], 'slot_uri': 'pokemon:effectDescription'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class EggGroup(NamedIndividual):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'Egg group is a category that '
                                                   'determines which Pokemon are able '
                                                   'to interbreed. The concept was '
                                                   'introduced in Generation II, along '
                                                   'with breeding. Similar to types, a '
                                                   'Pokémon may belong to either one '
                                                   'or two egg groups.'}},
         'from_schema': 'https://pokemonkg.org/ontology'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Flavor(NamedIndividual):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'Flavor is a special set of '
                                                   'attributes that certain foods in '
                                                   'the Pokémon world have. Most of '
                                                   'the foods can have more than one '
                                                   'flavor, and the flavor determines '
                                                   'which Pokemon can eat them.'}},
         'from_schema': 'https://pokemonkg.org/ontology'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Game(Thing):
    """
    A game is a type of media that can be played by people.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Generation(Thing):
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

    featuresSpecies: Optional[list[str]] = Field(default=None, description="""['A Pokedex entry features a species']""", json_schema_extra = { "linkml_meta": {'domain_of': ['Generation'], 'slot_uri': 'pokemon:featuresSpecies'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Habitat(NamedIndividual):
    """
    A habitat is a type of environment that certain Pokemon belong to.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Item(Thing):
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

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class BattleItem(Item):
    """
    Battle items are items that can be used during battles.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Food(Item):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    hasFlavor: Optional[list[str]] = Field(default=None, description="""A Pokemon has a flavor""", json_schema_extra = { "linkml_meta": {'domain': 'Food', 'domain_of': ['Food'], 'slot_uri': 'pokemon:hasFlavor'} })
    firmness: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain': 'Food', 'domain_of': ['Food']} })
    smoothness: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain': 'Food', 'domain_of': ['Food']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


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

    hasSize: Optional[Quantity] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Berry'], 'slot_uri': 'pokemon:hasSize'} })
    hasFlavor: Optional[list[str]] = Field(default=None, description="""A Pokemon has a flavor""", json_schema_extra = { "linkml_meta": {'domain': 'Food', 'domain_of': ['Food'], 'slot_uri': 'pokemon:hasFlavor'} })
    firmness: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain': 'Food', 'domain_of': ['Food']} })
    smoothness: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain': 'Food', 'domain_of': ['Food']} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class HM(Item):
    """
    Hidden Machine
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class HoldItem(Item):
    """
    A hold item is an item that can be held by a Pokemon.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Pokedex(Thing):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'The Pokedex is an electronic '
                                                   'device designed to catalogue and '
                                                   'provide information regarding the '
                                                   'various species of Pokemon '
                                                   'featured in the Pokemon video '
                                                   'game, anime and manga series.'}},
         'class_uri': 'https://pokemonkg.org/ontology#Pok%C3%A9dex',
         'from_schema': 'https://pokemonkg.org/ontology'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


# A Pokemon
Pokemon = Union["Pokedex", "Type"]


class PokedexEntry(Thing):
    """
    A pokedex entry is a description of a Pokemon.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'https://pokemonkg.org/ontology#Pok%C3%A9dexEntry',
         'from_schema': 'https://pokemonkg.org/ontology'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Pokeball(Item):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'A Poké Ball is a type of item that '
                                                   "is critical to a Trainer's quest, "
                                                   'used for catching and storing '
                                                   'Pokémon.'}},
         'class_uri': 'https://pokemonkg.org/ontology#Pok%C3%A9ball',
         'from_schema': 'https://pokemonkg.org/ontology'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Place(Thing):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'Entities that have a somewhat '
                                                   'fixed, physical extension.'}},
         'from_schema': 'https://pokemonkg.org/ontology'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Gym(Place):
    """
    A gym is a location that can be battled at.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Shape(NamedIndividual):
    """
    Shapes are categories that certain Pokemon belong to, which determine which Pokemon they can breed with.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Region(Place):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'Regions are areas in the Pokémon '
                                                   'universe that are smaller parts of '
                                                   'a nation.'}},
         'from_schema': 'https://pokemonkg.org/ontology'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Species(NamedIndividual):
    """
    A species is a category of Pokemon that share common features.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pokemon:Species',
         'from_schema': 'https://pokemonkg.org/ontology'})

    hasColour: Optional[str] = Field(default=None, description="""A Pokemon has a color""", json_schema_extra = { "linkml_meta": {'domain_of': ['Species'], 'slot_uri': 'pokemon:hasColour'} })
    mayHaveHiddenAbility: Optional[list[Literal["mayHaveAbility"]]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain': 'Species',
         'domain_of': ['Species'],
         'slot_uri': 'pokemon:mayHaveHiddenAbility',
         'subproperty_of': 'mayHaveAbility'} })
    mayHaveAbility: Optional[list[str]] = Field(default=None, description="""A Pokemon may have an ability""", json_schema_extra = { "linkml_meta": {'domain': 'Species',
         'domain_of': ['Species'],
         'slot_uri': 'pokemon:mayHaveAbility'} })
    isAbleToApply: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Species'], 'slot_uri': 'pokemon:isAbleToApply'} })
    hasHeight: Optional[Quantity] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain': 'Species', 'domain_of': ['Species'], 'slot_uri': 'pokemon:hasHeight'} })
    hasWeight: Optional[Quantity] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain': 'Species', 'domain_of': ['Species'], 'slot_uri': 'pokemon:hasWeight'} })
    depiction: Optional[str] = Field(default=None, description="""A depiction of the person""", json_schema_extra = { "linkml_meta": {'domain_of': ['Person', 'Species'], 'slot_uri': 'foaf:depiction'} })
    inEggGroup: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain': 'Species',
         'domain_of': ['Species'],
         'slot_uri': 'pokemon:inEggGroup'} })
    hasType: Optional[list[Type]] = Field(default=None, description="""A Pokemon has a type""", json_schema_extra = { "linkml_meta": {'domain_of': ['Species', 'Move'], 'slot_uri': 'pokemon:hasType'} })
    hasShape: Optional[str] = Field(default=None, description="""The shape of a berry is a measure of how good it  is for making a Potion.""", json_schema_extra = { "linkml_meta": {'domain': 'Species', 'domain_of': ['Species'], 'slot_uri': 'pokemon:hasShape'} })
    hasGenus: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain': 'Species', 'domain_of': ['Species']} })
    hasCatchRate: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain': 'Species',
         'domain_of': ['Species'],
         'slot_uri': 'pokemon:hasCatchRate'} })
    foundIn: Optional[list[str]] = Field(default=None, description="""A place is found in a location""", json_schema_extra = { "linkml_meta": {'domain': 'Species', 'domain_of': ['Species'], 'slot_uri': 'pokemon:foundIn'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Move(Thing):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'A move is a special ability of a '
                                                   'Pokemon.'}},
         'class_uri': 'pokemon:Move',
         'from_schema': 'https://pokemonkg.org/ontology'})

    effectDescription: Optional[list[str]] = Field(default=None, description="""A description of the effect of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Ability', 'Move'], 'slot_uri': 'pokemon:effectDescription'} })
    hasType: Optional[list[Type]] = Field(default=None, description="""A Pokemon has a type""", json_schema_extra = { "linkml_meta": {'domain_of': ['Species', 'Move'], 'slot_uri': 'pokemon:hasType'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


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

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class SpecialMove(Move):
    """
    A special move is a type of move that can be used during battles.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    effectDescription: Optional[list[str]] = Field(default=None, description="""A description of the effect of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Ability', 'Move'], 'slot_uri': 'pokemon:effectDescription'} })
    hasType: Optional[list[Type]] = Field(default=None, description="""A Pokemon has a type""", json_schema_extra = { "linkml_meta": {'domain_of': ['Species', 'Move'], 'slot_uri': 'pokemon:hasType'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class PhysicalMove(Move):
    """
    A physical move is a type of move that can be used during battles.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    effectDescription: Optional[list[str]] = Field(default=None, description="""A description of the effect of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Ability', 'Move'], 'slot_uri': 'pokemon:effectDescription'} })
    hasType: Optional[list[Type]] = Field(default=None, description="""A Pokemon has a type""", json_schema_extra = { "linkml_meta": {'domain_of': ['Species', 'Move'], 'slot_uri': 'pokemon:hasType'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class StatusMove(Move):
    """
    A status move is a type of move that can be used during battles.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    effectDescription: Optional[list[str]] = Field(default=None, description="""A description of the effect of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Ability', 'Move'], 'slot_uri': 'pokemon:effectDescription'} })
    hasType: Optional[list[Type]] = Field(default=None, description="""A Pokemon has a type""", json_schema_extra = { "linkml_meta": {'domain_of': ['Species', 'Move'], 'slot_uri': 'pokemon:hasType'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class TM(MoveLearning, Item):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'A Technical Machine is an item '
                                                   'that can be used to teach a '
                                                   'Pokemon a move.'}},
         'from_schema': 'https://pokemonkg.org/ontology',
         'mixins': ['MoveLearning']})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Town(Place):
    """
    A town is a type of place that can be visited.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Trainer(Person):
    """
    A trainer is a person who is able to catch Pokemon.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    depiction: Optional[str] = Field(default=None, description="""A depiction of the person""", json_schema_extra = { "linkml_meta": {'domain_of': ['Person', 'Species'], 'slot_uri': 'foaf:depiction'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class GymLeader(Trainer):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'A gym leader is the highest '
                                                   'ranking member and owner of an '
                                                   'official Pokémon gym. Gym leaders '
                                                   'use their gym and their Pokemon to '
                                                   'test the skills of trainers that '
                                                   'challenge them, and if said '
                                                   'trainers win a battle, the gym '
                                                   'leader will gift them a badge '
                                                   "that's unique to that specific "
                                                   'gym.'}},
         'from_schema': 'https://pokemonkg.org/ontology'})

    depiction: Optional[str] = Field(default=None, description="""A depiction of the person""", json_schema_extra = { "linkml_meta": {'domain_of': ['Person', 'Species'], 'slot_uri': 'foaf:depiction'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Type(NamedIndividual):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'All Pokemon creatures and their '
                                                   'moves are assigned certain types. '
                                                   'Each type has several strengths '
                                                   'and weaknesses in both attack and '
                                                   'defense.'}},
         'class_uri': 'pokemon:Type',
         'from_schema': 'https://pokemonkg.org/ontology'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Thing.model_rebuild()
NamedIndividual.model_rebuild()
Person.model_rebuild()
Colour.model_rebuild()
Connotation.model_rebuild()
Quantity.model_rebuild()
QuantityValue.model_rebuild()
QuantityKind.model_rebuild()
Unit.model_rebuild()
DerivedUnit.model_rebuild()
SystemOfUnits.model_rebuild()
QuantityKindDimensionVector.model_rebuild()
QuantityKindDimensionVectorSI.model_rebuild()
QuantityKindDimensionVectorCGS.model_rebuild()
QuantityKindDimensionVectorImperial.model_rebuild()
QuantityKindDimensionVectorISO.model_rebuild()
Prefix.model_rebuild()
DecimalPrefix.model_rebuild()
BinaryPrefix.model_rebuild()
Ability.model_rebuild()
EggGroup.model_rebuild()
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
