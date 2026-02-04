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

    black: Optional[float] = Field(default=None, description="""Black component in CMYK color model""", json_schema_extra = { "linkml_meta": {'domain_of': ['Colour'], 'slot_uri': 'dbpedia:cmykCoordinateBlack'} })
    cyanic: Optional[float] = Field(default=None, description="""Cyan component in CMYK color model""", json_schema_extra = { "linkml_meta": {'domain_of': ['Colour'], 'slot_uri': 'dbpedia:cmykCoordinateCyanic'} })
    magenta: Optional[float] = Field(default=None, description="""Magenta component in CMYK color model""", json_schema_extra = { "linkml_meta": {'domain_of': ['Colour'], 'slot_uri': 'dbpedia:cmykCoordinateMagenta'} })
    yellow: Optional[float] = Field(default=None, description="""Yellow component in CMYK color model""", json_schema_extra = { "linkml_meta": {'domain_of': ['Colour'], 'slot_uri': 'dbpedia:cmykCoordinateYellow'} })
    hue: Optional[float] = Field(default=None, description="""Hue component in HSV color model""", json_schema_extra = { "linkml_meta": {'domain_of': ['Colour'], 'slot_uri': 'dbpedia:hsvCoordinateHue'} })
    saturation: Optional[float] = Field(default=None, description="""Saturation component in HSV color model""", json_schema_extra = { "linkml_meta": {'domain_of': ['Colour'], 'slot_uri': 'dbpedia:hsvCoordinateSaturation'} })
    value: Optional[float] = Field(default=None, description="""Value/Lightness component in HSV color model""", json_schema_extra = { "linkml_meta": {'domain_of': ['Colour'], 'slot_uri': 'dbpedia:hsvCoordinateLightness'} })
    red: Optional[int] = Field(default=None, description="""Red component in RGB color model (0-255)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Colour'], 'slot_uri': 'dbpedia:rgbCoordinateRed'} })
    green: Optional[int] = Field(default=None, description="""Green component in RGB color model (0-255)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Colour'], 'slot_uri': 'dbpedia:rgbCoordinateGreen'} })
    blue: Optional[int] = Field(default=None, description="""Blue component in RGB color model (0-255)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Colour'], 'slot_uri': 'dbpedia:rgbCoordinateBlue'} })
    wavelength: Optional[float] = Field(default=None, description="""The wavelength of the color in nanometers""", json_schema_extra = { "linkml_meta": {'domain_of': ['Colour'], 'slot_uri': 'dbpedia:wavelength'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Aspect(Thing):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Aspect',
         'comments': ['An aspect is an abstract type class that defines properties '
                      'that can be reused.^^rdf:HTML'],
         'from_schema': 'http://qudt.org/subset/qudt_subset'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Quantifiable(Aspect):
    """
    <p><em>Quantifiable</em> ascribes to some thing the capability of being measured, observed, or counted.</p>
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Quantifiable',
         'comments': ['<p><em>Quantifiable</em> ascribes to some thing the capability '
                      'of being measured, observed, or counted.</p>^^rdf:HTML'],
         'from_schema': 'http://qudt.org/subset/qudt_subset',
         'slot_usage': {'dataEncoding': {'multivalued': False,
                                         'name': 'dataEncoding',
                                         'range': 'DataEncoding'},
                        'datatype': {'multivalued': False,
                                     'name': 'datatype',
                                     'range': 'Datatype'},
                        'hasUnit': {'multivalued': False,
                                    'name': 'hasUnit',
                                    'range': 'Unit'},
                        'qudt_value': {'multivalued': False, 'name': 'qudt_value'},
                        'relativeStandardUncertainty': {'multivalued': False,
                                                        'name': 'relativeStandardUncertainty',
                                                        'range': 'double'},
                        'standardUncertainty': {'multivalued': False,
                                                'name': 'standardUncertainty',
                                                'range': 'decimal'},
                        'standardUncertaintySN': {'name': 'standardUncertaintySN',
                                                  'range': 'double'},
                        'valueSN': {'multivalued': False, 'name': 'valueSN'}}})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Concept(Thing):
    """
    The root class for all QUDT concepts.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Concept',
         'comments': ['The root class for all QUDT concepts.^^rdf:HTML'],
         'from_schema': 'http://qudt.org/subset/qudt_subset',
         'slot_usage': {'abbreviation': {'multivalued': False, 'name': 'abbreviation'},
                        'deprecated': {'multivalued': False, 'name': 'deprecated'},
                        'hasRule': {'name': 'hasRule', 'range': 'Rule'},
                        'isReplacedBy': {'multivalued': False, 'name': 'isReplacedBy'},
                        'plainTextDescription': {'multivalued': False,
                                                 'name': 'plainTextDescription'},
                        'qudt_description': {'multivalued': False,
                                             'name': 'qudt_description'},
                        'qudt_id': {'multivalued': False, 'name': 'qudt_id'}}})

    guidance: Optional[list[str]] = Field(default=None, description="""guidance""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    qudt_id: Optional[str] = Field(default=None, description="""The \"qudt:id\" is an identifier string that uniquely identifies a QUDT concept.  The identifier is constructed using a prefix. For example, units are coded using the pattern: \"UCCCENNNN\", where \"CCC\" is a numeric code or a category and \"NNNN\" is a digit string for a member element of that category. For scaled units there may be an addition field that has the format \"QNN\" where \"NN\" is a digit string representing an exponent power, and \"Q\" is a qualifier that indicates with the code \"P\" that the power is a positive decimal exponent, or the code \"N\" for a negative decimal exponent, or the code \"B\" for binary positive exponents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class SystemOfQuantityKinds(Concept):
    """
    A system of quantity kinds is a set of one or more quantity kinds together with a set of zero or more algebraic equations that define relationships between quantity kinds in the set. In the physical sciences, the equations relating quantity kinds are typically physical laws and definitional relations, and constants of proportionality. Examples include Newton’s First Law of Motion, Coulomb’s Law, and the definition of velocity as the instantaneous change in position.  In almost all cases, the system identifies a subset of base quantity kinds. The base set is chosen so that all other quantity kinds of interest can be derived from the base quantity kinds and the algebraic equations. If the unit system is explicitly associated with a quantity kind system, then the unit system must define at least one unit for each quantity kind.  From a scientific point of view, the division of quantities into base quantities and derived quantities is a matter of convention.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:SystemOfQuantityKinds',
         'comments': ['A system of quantity kinds is a set of one or more quantity '
                      'kinds together with a set of zero or more algebraic equations '
                      'that define relationships between quantity kinds in the set. In '
                      'the physical sciences, the equations relating quantity kinds '
                      'are typically physical laws and definitional relations, and '
                      'constants of proportionality. Examples include Newton’s First '
                      'Law of Motion, Coulomb’s Law, and the definition of velocity as '
                      'the instantaneous change in position.  In almost all cases, the '
                      'system identifies a subset of base quantity kinds. The base set '
                      'is chosen so that all other quantity kinds of interest can be '
                      'derived from the base quantity kinds and the algebraic '
                      'equations. If the unit system is explicitly associated with a '
                      'quantity kind system, then the unit system must define at least '
                      'one unit for each quantity kind.  From a scientific point of '
                      'view, the division of quantities into base quantities and '
                      'derived quantities is a matter of convention.^^rdf:HTML'],
         'from_schema': 'http://qudt.org/subset/qudt_subset',
         'slot_usage': {'baseDimensionEnumeration': {'multivalued': False,
                                                     'name': 'baseDimensionEnumeration',
                                                     'range': 'Enumeration'},
                        'hasBaseQuantityKind': {'name': 'hasBaseQuantityKind',
                                                'range': 'QuantityKind'},
                        'hasQuantityKind': {'name': 'hasQuantityKind',
                                            'range': 'QuantityKind',
                                            'required': False},
                        'hasUnitSystem': {'name': 'hasUnitSystem',
                                          'range': 'SystemOfUnits'},
                        'systemDerivedQuantityKind': {'name': 'systemDerivedQuantityKind',
                                                      'range': 'QuantityKind'}}})

    guidance: Optional[list[str]] = Field(default=None, description="""guidance""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    qudt_id: Optional[str] = Field(default=None, description="""The \"qudt:id\" is an identifier string that uniquely identifies a QUDT concept.  The identifier is constructed using a prefix. For example, units are coded using the pattern: \"UCCCENNNN\", where \"CCC\" is a numeric code or a category and \"NNNN\" is a digit string for a member element of that category. For scaled units there may be an addition field that has the format \"QNN\" where \"NN\" is a digit string representing an exponent power, and \"Q\" is a qualifier that indicates with the code \"P\" that the power is a positive decimal exponent, or the code \"N\" for a negative decimal exponent, or the code \"B\" for binary positive exponents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Quantity(Concept, Quantifiable):
    """
    <p class=\"lm-para\">A <b>quantity</b> is the measurement of an observable property of a particular object, event, or physical system.
      A quantity is always associated with the context of measurement (i.e. the thing measured, the measured value, the accuracy of measurement, etc.) whereas the
      underlying <b>quantity kind</b> is independent of any particular measurement. Thus, length is a quantity kind while the height of a rocket is a specific
      quantity of length; its magnitude that may be expressed in meters, feet, inches, etc. Examples of physical quantities include physical constants, such as
      the speed of light in a vacuum, Planck's constant, the electric permittivity of free space, and the fine structure constant. </p>
    <p class=\"lm-para\">In other words, quantities are quantifiable aspects of the world, such as the duration of a movie, the distance between two points,
    velocity of a car, the pressure of the atmosphere, and a person's weight; and units are used to describe their numerical measure.</p>
    <p class=\"lm-para\">Many <b>quantity kinds</b> are related to each other by various physical laws, and as a result, the associated units of some quantity
    kinds can be expressed as products (or ratios) of powers of other quantity kinds (e.g., momentum is mass times velocity and velocity is defined as distance
    divided by time). In this way, some quantities can be calculated from other measured quantities using their associations to the quantity kinds in these
    expressions. These quantity kind relationships are also discussed in dimensional analysis. Those that cannot be so expressed can be regarded
    as \"fundamental\" in this sense.</p>
    <p class=\"lm-para\">A quantity is distinguished from a \"quantity kind\" in that the former carries a value and the latter is a type specifier.</p>
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Quantity',
         'comments': ['<p class=\\"lm-para\\">A <b>quantity</b> is the measurement of '
                      'an observable property of a particular object, event, or '
                      'physical system.\n'
                      '  A quantity is always associated with the context of '
                      'measurement (i.e. the thing measured, the measured value, the '
                      'accuracy of measurement, etc.) whereas the\n'
                      '  underlying <b>quantity kind</b> is independent of any '
                      'particular measurement. Thus, length is a quantity kind while '
                      'the height of a rocket is a specific\n'
                      '  quantity of length; its magnitude that may be expressed in '
                      'meters, feet, inches, etc. Examples of physical quantities '
                      'include physical constants, such as\n'
                      "  the speed of light in a vacuum, Planck's constant, the "
                      'electric permittivity of free space, and the fine structure '
                      'constant. </p>\n'
                      '<p class=\\"lm-para\\">In other words, quantities are '
                      'quantifiable aspects of the world, such as the duration of a '
                      'movie, the distance between two points,\n'
                      'velocity of a car, the pressure of the atmosphere, and a '
                      "person's weight; and units are used to describe their numerical "
                      'measure.</p>\n'
                      '<p class=\\"lm-para\\">Many <b>quantity kinds</b> are related '
                      'to each other by various physical laws, and as a result, the '
                      'associated units of some quantity\n'
                      'kinds can be expressed as products (or ratios) of powers of '
                      'other quantity kinds (e.g., momentum is mass times velocity and '
                      'velocity is defined as distance\n'
                      'divided by time). In this way, some quantities can be '
                      'calculated from other measured quantities using their '
                      'associations to the quantity kinds in these\n'
                      'expressions. These quantity kind relationships are also '
                      'discussed in dimensional analysis. Those that cannot be so '
                      'expressed can be regarded\n'
                      'as \\"fundamental\\" in this sense.</p>\n'
                      '<p class=\\"lm-para\\">A quantity is distinguished from a '
                      '\\"quantity kind\\" in that the former carries a value and the '
                      'latter is a type specifier.</p>^^rdf:HTML'],
         'from_schema': 'http://qudt.org/subset/qudt_subset',
         'mixins': ['Concept'],
         'slot_usage': {'hasQuantityKind': {'name': 'hasQuantityKind',
                                            'range': 'QuantityKind',
                                            'required': False},
                        'isDeltaQuantity': {'name': 'isDeltaQuantity',
                                            'range': 'boolean'},
                        'quantityValue': {'name': 'quantityValue',
                                          'range': 'QuantityValue'}}})

    guidance: Optional[list[str]] = Field(default=None, description="""guidance""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    qudt_id: Optional[str] = Field(default=None, description="""The \"qudt:id\" is an identifier string that uniquely identifies a QUDT concept.  The identifier is constructed using a prefix. For example, units are coded using the pattern: \"UCCCENNNN\", where \"CCC\" is a numeric code or a category and \"NNNN\" is a digit string for a member element of that category. For scaled units there may be an addition field that has the format \"QNN\" where \"NN\" is a digit string representing an exponent power, and \"Q\" is a qualifier that indicates with the code \"P\" that the power is a positive decimal exponent, or the code \"N\" for a negative decimal exponent, or the code \"B\" for binary positive exponents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class PhysicalConstant(Quantity):
    """
    A physical constant is a physical quantity that is generally believed to be both universal in nature and constant in time. It can be contrasted with a mathematical constant, which is a fixed numerical value but does not directly involve any physical measurement. There are many physical constants in science, some of the most widely recognized being the speed of light in vacuum c, Newton's gravitational constant G, Planck's constant h, the electric permittivity of free space ε0, and the elementary charge e. Physical constants can take many dimensional forms, or may be dimensionless depending on the system of quantities and units used.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:PhysicalConstant',
         'comments': ['A physical constant is a physical quantity that is generally '
                      'believed to be both universal in nature and constant in time. '
                      'It can be contrasted with a mathematical constant, which is a '
                      'fixed numerical value but does not directly involve any '
                      'physical measurement. There are many physical constants in '
                      'science, some of the most widely recognized being the speed of '
                      "light in vacuum c, Newton's gravitational constant G, Planck's "
                      'constant h, the electric permittivity of free space ε0, and the '
                      'elementary charge e. Physical constants can take many '
                      'dimensional forms, or may be dimensionless depending on the '
                      'system of quantities and units used.^^rdf:HTML'],
         'from_schema': 'http://qudt.org/subset/qudt_subset',
         'slot_usage': {'altSymbol': {'name': 'altSymbol', 'required': False},
                        'applicableSystem': {'name': 'applicableSystem',
                                             'range': 'SystemOfUnits'},
                        'applicableUnit': {'name': 'applicableUnit', 'range': 'Unit'},
                        'exactConstant': {'name': 'exactConstant', 'range': 'boolean'},
                        'exactMatch': {'name': 'exactMatch',
                                       'range': 'PhysicalConstant'},
                        'hasDimensionVector': {'name': 'hasDimensionVector',
                                               'range': 'QuantityKindDimensionVector'},
                        'isoNormativeReference': {'name': 'isoNormativeReference',
                                                  'required': False},
                        'latexDefinition': {'multivalued': False,
                                            'name': 'latexDefinition'},
                        'latexSymbol': {'name': 'latexSymbol', 'required': False},
                        'mathMLdefinition': {'multivalued': False,
                                             'name': 'mathMLdefinition'},
                        'normativeReference': {'name': 'normativeReference',
                                               'required': False},
                        'symbol': {'name': 'symbol', 'required': False},
                        'ucumCode': {'name': 'ucumCode', 'required': False}}})

    guidance: Optional[list[str]] = Field(default=None, description="""guidance""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    qudt_id: Optional[str] = Field(default=None, description="""The \"qudt:id\" is an identifier string that uniquely identifies a QUDT concept.  The identifier is constructed using a prefix. For example, units are coded using the pattern: \"UCCCENNNN\", where \"CCC\" is a numeric code or a category and \"NNNN\" is a digit string for a member element of that category. For scaled units there may be an addition field that has the format \"QNN\" where \"NN\" is a digit string representing an exponent power, and \"Q\" is a qualifier that indicates with the code \"P\" that the power is a positive decimal exponent, or the code \"N\" for a negative decimal exponent, or the code \"B\" for binary positive exponents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Encoding(Concept):
    """
    An encoding is a rule or algorithm that is used to convert data from a native, or unspecified form into a specific form that satisfies the encoding rules. Examples of encodings include character encodings, such as UTF-8.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Encoding',
         'from_schema': 'http://qudt.org/subset/qudt_subset',
         'slot_usage': {'bits': {'multivalued': False, 'name': 'bits'},
                        'bytes': {'multivalued': False, 'name': 'bytes'}}})

    guidance: Optional[list[str]] = Field(default=None, description="""guidance""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    qudt_id: Optional[str] = Field(default=None, description="""The \"qudt:id\" is an identifier string that uniquely identifies a QUDT concept.  The identifier is constructed using a prefix. For example, units are coded using the pattern: \"UCCCENNNN\", where \"CCC\" is a numeric code or a category and \"NNNN\" is a digit string for a member element of that category. For scaled units there may be an addition field that has the format \"QNN\" where \"NN\" is a digit string representing an exponent power, and \"Q\" is a qualifier that indicates with the code \"P\" that the power is a positive decimal exponent, or the code \"N\" for a negative decimal exponent, or the code \"B\" for binary positive exponents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Enumeration(Concept):
    """
    <p>An enumeration is a set of literals from which a single value is selected. Each literal can have a tag as an integer within a standard encoding appropriate to the range of integer values. Consistency of enumeration types will allow them, and the enumerated values, to be referred to unambiguously either through symbolic name or encoding. Enumerated values are also controlled vocabularies and as such need to be standardized. Without this consistency enumeration literals can be stated differently and result in  data conflicts and misinterpretations.</p>

    <p>The tags are a set of positive whole numbers, not necessarily contiguous and having no numerical significance, each corresponding to the associated literal identifier. An order attribute can also be given on the enumeration elements. An enumeration can itself be a member of an enumeration. This allows enumerations to be enumerated in a selection. Enumerations are also subclasses of <em>Scalar Datatype</em>. This allows them to be used as the reference of a datatype specification.</p>
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Enumeration',
         'comments': ['<p>An enumeration is a set of literals from which a single '
                      'value is selected. Each literal can have a tag as an integer '
                      'within a standard encoding appropriate to the range of integer '
                      'values. Consistency of enumeration types will allow them, and '
                      'the enumerated values, to be referred to unambiguously either '
                      'through symbolic name or encoding. Enumerated values are also '
                      'controlled vocabularies and as such need to be standardized. '
                      'Without this consistency enumeration literals can be stated '
                      'differently and result in  data conflicts and '
                      'misinterpretations.</p>\n'
                      '\n'
                      '<p>The tags are a set of positive whole numbers, not '
                      'necessarily contiguous and having no numerical significance, '
                      'each corresponding to the associated literal identifier. An '
                      'order attribute can also be given on the enumeration elements. '
                      'An enumeration can itself be a member of an enumeration. This '
                      'allows enumerations to be enumerated in a selection. '
                      'Enumerations are also subclasses of <em>Scalar Datatype</em>. '
                      'This allows them to be used as the reference of a datatype '
                      'specification.</p>^^rdf:HTML'],
         'from_schema': 'http://qudt.org/subset/qudt_subset',
         'slot_usage': {'abbreviation': {'multivalued': False, 'name': 'abbreviation'},
                        'default': {'multivalued': False,
                                    'name': 'default',
                                    'range': 'EnumeratedValue'},
                        'element': {'name': 'element',
                                    'range': 'EnumeratedValue',
                                    'required': True}}})

    guidance: Optional[list[str]] = Field(default=None, description="""guidance""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    qudt_id: Optional[str] = Field(default=None, description="""The \"qudt:id\" is an identifier string that uniquely identifies a QUDT concept.  The identifier is constructed using a prefix. For example, units are coded using the pattern: \"UCCCENNNN\", where \"CCC\" is a numeric code or a category and \"NNNN\" is a digit string for a member element of that category. For scaled units there may be an addition field that has the format \"QNN\" where \"NN\" is a digit string representing an exponent power, and \"Q\" is a qualifier that indicates with the code \"P\" that the power is a positive decimal exponent, or the code \"N\" for a negative decimal exponent, or the code \"B\" for binary positive exponents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class AbstractQuantityKind(Concept):
    """
    Quantity Kind (abstract)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:AbstractQuantityKind',
         'from_schema': 'http://qudt.org/subset/qudt_subset',
         'slot_usage': {'altSymbol': {'name': 'altSymbol', 'required': False},
                        'broader': {'name': 'broader', 'range': 'QuantityKind'},
                        'latexSymbol': {'name': 'latexSymbol', 'required': False},
                        'symbol': {'multivalued': False, 'name': 'symbol'}}})

    guidance: Optional[list[str]] = Field(default=None, description="""guidance""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    qudt_id: Optional[str] = Field(default=None, description="""The \"qudt:id\" is an identifier string that uniquely identifies a QUDT concept.  The identifier is constructed using a prefix. For example, units are coded using the pattern: \"UCCCENNNN\", where \"CCC\" is a numeric code or a category and \"NNNN\" is a digit string for a member element of that category. For scaled units there may be an addition field that has the format \"QNN\" where \"NN\" is a digit string representing an exponent power, and \"Q\" is a qualifier that indicates with the code \"P\" that the power is a positive decimal exponent, or the code \"N\" for a negative decimal exponent, or the code \"B\" for binary positive exponents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class QuantityValue(Concept, Quantifiable):
    """
    A <i>Quantity Value</i> expresses the magnitude and kind of a quantity and is given by the product of a numerical value <code>n</code> and a unit of measure <code>U</code>. The number multiplying the unit is referred to as the numerical value of the quantity expressed in that unit. Refer to <a href=\"http://physics.nist.gov/Pubs/SP811/sec07.html\">NIST SP 811 section 7</a> for more on quantity values.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:QuantityValue',
         'comments': ['A <i>Quantity Value</i> expresses the magnitude and kind of a '
                      'quantity and is given by the product of a numerical value '
                      '<code>n</code> and a unit of measure <code>U</code>. The number '
                      'multiplying the unit is referred to as the numerical value of '
                      'the quantity expressed in that unit. Refer to <a '
                      'href=\\"http://physics.nist.gov/Pubs/SP811/sec07.html\\">NIST '
                      'SP 811 section 7</a> for more on quantity values.^^rdf:HTML'],
         'from_schema': 'http://qudt.org/subset/qudt_subset',
         'mixins': ['Concept'],
         'slot_usage': {'hasUnit': {'multivalued': False, 'name': 'hasUnit'}}})

    guidance: Optional[list[str]] = Field(default=None, description="""guidance""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    qudt_id: Optional[str] = Field(default=None, description="""The \"qudt:id\" is an identifier string that uniquely identifies a QUDT concept.  The identifier is constructed using a prefix. For example, units are coded using the pattern: \"UCCCENNNN\", where \"CCC\" is a numeric code or a category and \"NNNN\" is a digit string for a member element of that category. For scaled units there may be an addition field that has the format \"QNN\" where \"NN\" is a digit string representing an exponent power, and \"Q\" is a qualifier that indicates with the code \"P\" that the power is a positive decimal exponent, or the code \"N\" for a negative decimal exponent, or the code \"B\" for binary positive exponents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class DataEncoding(Aspect):
    """
    <p><em>Data Encoding</em> expresses the properties that specify how data is represented at the bit and byte level. These properties are applicable to describing raw data.</p>
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:DataEncoding',
         'comments': ['<p><em>Data Encoding</em> expresses the properties that specify '
                      'how data is represented at the bit and byte level. These '
                      'properties are applicable to describing raw '
                      'data.</p>^^rdf:HTML'],
         'from_schema': 'http://qudt.org/subset/qudt_subset',
         'slot_usage': {'bitOrder': {'multivalued': False,
                                     'name': 'bitOrder',
                                     'range': 'EndianType'},
                        'byteOrder': {'multivalued': False, 'name': 'byteOrder'},
                        'encoding': {'multivalued': False,
                                     'name': 'encoding',
                                     'range': 'Encoding'}}})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class UCUMcs(Thing):
    """
    Lexical pattern for the case-sensitive version of UCUM code
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Lexical pattern for the case-sensitive version of UCUM code'],
         'from_schema': 'http://qudt.org/subset/qudt_subset'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Datatype(Concept):
    """
    
       <p>A <em>Datatype</em> is a definition of the type of the \"value\" of a data item (for example, \"all integers between 0 and 10\"),
       and the allowable operations on those values; the meaning of the data; and the way values of that type can be stored.
      Some types are primitive - built-in to the language, with no visible internal structure.
      For example \"Boolean\"; others are composite - constructed from one or more other types (of either kind).
      For example lists, arrays, structures, unions.
      Some languages provide strong typing, others allow implicit type conversion and/or explicit type conversion.
      </p>
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'rdfs:Datatype',
         'from_schema': 'http://qudt.org/subset/qudt_subset',
         'slot_usage': {'ansiSQLName': {'multivalued': False, 'name': 'ansiSQLName'},
                        'basis': {'multivalued': False,
                                  'name': 'basis',
                                  'range': 'Datatype'},
                        'bounded': {'multivalued': False, 'name': 'bounded'},
                        'cName': {'multivalued': False, 'name': 'cName'},
                        'cardinality': {'multivalued': False,
                                        'name': 'cardinality',
                                        'range': 'CardinalityType'},
                        'javaName': {'multivalued': False, 'name': 'javaName'},
                        'jsName': {'multivalued': False, 'name': 'jsName'},
                        'matlabName': {'multivalued': False, 'name': 'matlabName'},
                        'microsoftSQLServerName': {'multivalued': False,
                                                   'name': 'microsoftSQLServerName'},
                        'mySQLName': {'multivalued': False, 'name': 'mySQLName'},
                        'odbcName': {'multivalued': False, 'name': 'odbcName'},
                        'oleDBName': {'multivalued': False, 'name': 'oleDBName'},
                        'oracleSQLName': {'multivalued': False,
                                          'name': 'oracleSQLName'},
                        'orderedType': {'multivalued': False,
                                        'name': 'orderedType',
                                        'range': 'OrderedType'},
                        'protocolBuffersName': {'multivalued': False,
                                                'name': 'protocolBuffersName'},
                        'pythonName': {'multivalued': False, 'name': 'pythonName'},
                        'qudt_id': {'multivalued': False, 'name': 'qudt_id'},
                        'vbName': {'multivalued': False, 'name': 'vbName'}}})

    guidance: Optional[list[str]] = Field(default=None, description="""guidance""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    qudt_id: Optional[str] = Field(default=None, description="""The \"qudt:id\" is an identifier string that uniquely identifies a QUDT concept.  The identifier is constructed using a prefix. For example, units are coded using the pattern: \"UCCCENNNN\", where \"CCC\" is a numeric code or a category and \"NNNN\" is a digit string for a member element of that category. For scaled units there may be an addition field that has the format \"QNN\" where \"NN\" is a digit string representing an exponent power, and \"Q\" is a qualifier that indicates with the code \"P\" that the power is a positive decimal exponent, or the code \"N\" for a negative decimal exponent, or the code \"B\" for binary positive exponents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Verifiable(Aspect):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Verifiable',
         'comments': ['An aspect class that holds properties that provide external '
                      'knowledge and specifications of a given resource.'],
         'from_schema': 'http://qudt.org/subset/qudt_subset',
         'slot_usage': {'dbpediaMatch': {'name': 'dbpediaMatch', 'required': False},
                        'isoNormativeReference': {'name': 'isoNormativeReference',
                                                  'required': False},
                        'normativeReference': {'name': 'normativeReference',
                                               'required': False},
                        'wikidataMatch': {'name': 'wikidataMatch', 'required': False}}})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class SystemOfUnits(Verifiable, Concept):
    """
    A system of units is a set of units which are chosen as the reference scales for some set of quantity kinds together with the definitions of each unit. Units may be defined by experimental observation or by proportion to another unit not included in the system. If the unit system is explicitly associated with a quantity kind system, then the unit system must define at least one unit for each quantity kind.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:SystemOfUnits',
         'comments': ['A system of units is a set of units which are chosen as the '
                      'reference scales for some set of quantity kinds together with '
                      'the definitions of each unit. Units may be defined by '
                      'experimental observation or by proportion to another unit not '
                      'included in the system. If the unit system is explicitly '
                      'associated with a quantity kind system, then the unit system '
                      'must define at least one unit for each quantity '
                      'kind.^^rdf:HTML'],
         'from_schema': 'http://qudt.org/subset/qudt_subset',
         'mixins': ['Concept'],
         'slot_usage': {'applicablePhysicalConstant': {'name': 'applicablePhysicalConstant',
                                                       'range': 'PhysicalConstant'},
                        'hasAllowedUnit': {'name': 'hasAllowedUnit', 'range': 'Unit'},
                        'hasBaseUnit': {'name': 'hasBaseUnit', 'range': 'Unit'},
                        'hasCoherentUnit': {'name': 'hasCoherentUnit', 'range': 'Unit'},
                        'hasDefinedUnit': {'name': 'hasDefinedUnit', 'range': 'Unit'},
                        'hasDerivedCoherentUnit': {'name': 'hasDerivedCoherentUnit',
                                                   'range': 'Unit'},
                        'hasDerivedUnit': {'name': 'hasDerivedUnit', 'range': 'Unit'},
                        'hasUnit': {'name': 'hasUnit', 'range': 'Unit'},
                        'prefix': {'name': 'prefix', 'range': 'Prefix'}}})

    guidance: Optional[list[str]] = Field(default=None, description="""guidance""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    qudt_id: Optional[str] = Field(default=None, description="""The \"qudt:id\" is an identifier string that uniquely identifies a QUDT concept.  The identifier is constructed using a prefix. For example, units are coded using the pattern: \"UCCCENNNN\", where \"CCC\" is a numeric code or a category and \"NNNN\" is a digit string for a member element of that category. For scaled units there may be an addition field that has the format \"QNN\" where \"NN\" is a digit string representing an exponent power, and \"Q\" is a qualifier that indicates with the code \"P\" that the power is a positive decimal exponent, or the code \"N\" for a negative decimal exponent, or the code \"B\" for binary positive exponents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Prefix(Verifiable, Concept):
    """
    Prefix
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Prefix',
         'from_schema': 'http://qudt.org/subset/qudt_subset',
         'mixins': ['Concept'],
         'slot_usage': {'altSymbol': {'name': 'altSymbol', 'required': False},
                        'exactMatch': {'name': 'exactMatch', 'range': 'Prefix'},
                        'latexSymbol': {'name': 'latexSymbol', 'required': False},
                        'prefixMultiplier': {'multivalued': False,
                                             'name': 'prefixMultiplier'},
                        'symbol': {'name': 'symbol', 'required': False},
                        'ucumCode': {'name': 'ucumCode', 'range': 'UCUMcs-term'}}})

    guidance: Optional[list[str]] = Field(default=None, description="""guidance""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    qudt_id: Optional[str] = Field(default=None, description="""The \"qudt:id\" is an identifier string that uniquely identifies a QUDT concept.  The identifier is constructed using a prefix. For example, units are coded using the pattern: \"UCCCENNNN\", where \"CCC\" is a numeric code or a category and \"NNNN\" is a digit string for a member element of that category. For scaled units there may be an addition field that has the format \"QNN\" where \"NN\" is a digit string representing an exponent power, and \"Q\" is a qualifier that indicates with the code \"P\" that the power is a positive decimal exponent, or the code \"N\" for a negative decimal exponent, or the code \"B\" for binary positive exponents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class EnumeratedValue(Verifiable, Concept):
    """
    <p>This class is for all enumerated and/or coded values.  For example, it contains the dimension objects that are the basis elements in some abstract vector space associated with a quantity kind system. Another use is for the base dimensions for quantity systems. Each quantity kind system that defines a base set has a corresponding ordered enumeration whose elements are the dimension objects for the base quantity kinds. The order of the dimensions in the enumeration determines the canonical order of the basis elements in the corresponding abstract vector space.</p>

    <p>An enumeration is a set of literals from which a single value is selected. Each literal can have a tag as an integer within a standard encoding appropriate to the range of integer values. Consistency of enumeration types will allow them, and the enumerated values, to be referred to unambiguously either through symbolic name or encoding. Enumerated values are also controlled vocabularies and as such need to be standardized. Without this consistency enumeration literals can be stated differently and result in  data conflicts and misinterpretations.</p>

    <p>The tags are a set of positive whole numbers, not necessarily contiguous and having no numerical significance, each corresponding to the associated literal identifier. An order attribute can also be given on the enumeration elements. An enumeration can itself be a member of an enumeration. This allows enumerations to be enumerated in a selection. Enumerations are also subclasses of Scalar Datatype. This allows them to be used as the reference of a datatype specification.</p>
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:EnumeratedValue',
         'from_schema': 'http://qudt.org/subset/qudt_subset',
         'mixins': ['Concept'],
         'slot_usage': {'abbreviation': {'multivalued': False, 'name': 'abbreviation'},
                        'altSymbol': {'name': 'altSymbol', 'required': False},
                        'qudt_description': {'multivalued': False,
                                             'name': 'qudt_description'},
                        'symbol': {'multivalued': False, 'name': 'symbol'}}})

    guidance: Optional[list[str]] = Field(default=None, description="""guidance""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    qudt_id: Optional[str] = Field(default=None, description="""The \"qudt:id\" is an identifier string that uniquely identifies a QUDT concept.  The identifier is constructed using a prefix. For example, units are coded using the pattern: \"UCCCENNNN\", where \"CCC\" is a numeric code or a category and \"NNNN\" is a digit string for a member element of that category. For scaled units there may be an addition field that has the format \"QNN\" where \"NN\" is a digit string representing an exponent power, and \"Q\" is a qualifier that indicates with the code \"P\" that the power is a positive decimal exponent, or the code \"N\" for a negative decimal exponent, or the code \"B\" for binary positive exponents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class EndianType(EnumeratedValue):
    """
    Endian Type
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:EndianType',
         'from_schema': 'http://qudt.org/subset/qudt_subset'})

    guidance: Optional[list[str]] = Field(default=None, description="""guidance""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    qudt_id: Optional[str] = Field(default=None, description="""The \"qudt:id\" is an identifier string that uniquely identifies a QUDT concept.  The identifier is constructed using a prefix. For example, units are coded using the pattern: \"UCCCENNNN\", where \"CCC\" is a numeric code or a category and \"NNNN\" is a digit string for a member element of that category. For scaled units there may be an addition field that has the format \"QNN\" where \"NN\" is a digit string representing an exponent power, and \"Q\" is a qualifier that indicates with the code \"P\" that the power is a positive decimal exponent, or the code \"N\" for a negative decimal exponent, or the code \"B\" for binary positive exponents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class RuleType(EnumeratedValue):
    """
    Rule Type
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:RuleType',
         'from_schema': 'http://qudt.org/subset/qudt_subset'})

    guidance: Optional[list[str]] = Field(default=None, description="""guidance""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    qudt_id: Optional[str] = Field(default=None, description="""The \"qudt:id\" is an identifier string that uniquely identifies a QUDT concept.  The identifier is constructed using a prefix. For example, units are coded using the pattern: \"UCCCENNNN\", where \"CCC\" is a numeric code or a category and \"NNNN\" is a digit string for a member element of that category. For scaled units there may be an addition field that has the format \"QNN\" where \"NN\" is a digit string representing an exponent power, and \"Q\" is a qualifier that indicates with the code \"P\" that the power is a positive decimal exponent, or the code \"N\" for a negative decimal exponent, or the code \"B\" for binary positive exponents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class CardinalityType(EnumeratedValue):
    """
    
      In mathematics, the cardinality of a set is a measure of the number of elements of the set.
      For example, the set $A = {2, 4, 6}$ contains 3 elements, and therefore $A$ has a cardinality of 3.
      There are two approaches to cardinality: one which compares sets directly using bijections and injections,
       and another which uses cardinal numbers.
      
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:CardinalityType',
         'from_schema': 'http://qudt.org/subset/qudt_subset',
         'slot_usage': {'literal': {'multivalued': False, 'name': 'literal'}}})

    guidance: Optional[list[str]] = Field(default=None, description="""guidance""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    qudt_id: Optional[str] = Field(default=None, description="""The \"qudt:id\" is an identifier string that uniquely identifies a QUDT concept.  The identifier is constructed using a prefix. For example, units are coded using the pattern: \"UCCCENNNN\", where \"CCC\" is a numeric code or a category and \"NNNN\" is a digit string for a member element of that category. For scaled units there may be an addition field that has the format \"QNN\" where \"NN\" is a digit string representing an exponent power, and \"Q\" is a qualifier that indicates with the code \"P\" that the power is a positive decimal exponent, or the code \"N\" for a negative decimal exponent, or the code \"B\" for binary positive exponents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class OrderedType(EnumeratedValue):
    """
    Describes how a data or information structure is ordered.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:OrderedType',
         'from_schema': 'http://qudt.org/subset/qudt_subset',
         'slot_usage': {'literal': {'multivalued': False, 'name': 'literal'}}})

    guidance: Optional[list[str]] = Field(default=None, description="""guidance""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    qudt_id: Optional[str] = Field(default=None, description="""The \"qudt:id\" is an identifier string that uniquely identifies a QUDT concept.  The identifier is constructed using a prefix. For example, units are coded using the pattern: \"UCCCENNNN\", where \"CCC\" is a numeric code or a category and \"NNNN\" is a digit string for a member element of that category. For scaled units there may be an addition field that has the format \"QNN\" where \"NN\" is a digit string representing an exponent power, and \"Q\" is a qualifier that indicates with the code \"P\" that the power is a positive decimal exponent, or the code \"N\" for a negative decimal exponent, or the code \"B\" for binary positive exponents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Unit(Verifiable, Concept):
    """
    
      A unit of measure, or unit, is a particular quantity value that has been chosen as a scale for measuring other quantities the same kind (more generally of equivalent dimension).
      For example, the meter is a quantity of length that has been rigorously defined and standardized by the BIPM (International Board of Weights and Measures).
      Any measurement of the length can be expressed as a number multiplied by the unit meter.
      More formally, the value of a physical quantity Q with respect to a unit (U) is expressed as the scalar multiple of a real number (n) and U, as  $Q = nU$.
      
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Unit',
         'from_schema': 'http://qudt.org/subset/qudt_subset',
         'mixins': ['Concept'],
         'slot_usage': {'altSymbol': {'name': 'altSymbol', 'required': False},
                        'applicableSystem': {'name': 'applicableSystem',
                                             'range': 'SystemOfUnits'},
                        'conversionMultiplier': {'multivalued': False,
                                                 'name': 'conversionMultiplier'},
                        'conversionMultiplierSN': {'multivalued': False,
                                                   'name': 'conversionMultiplierSN'},
                        'conversionOffset': {'multivalued': False,
                                             'name': 'conversionOffset'},
                        'conversionOffsetSN': {'multivalued': False,
                                               'name': 'conversionOffsetSN'},
                        'definedUnitOfSystem': {'name': 'definedUnitOfSystem',
                                                'range': 'SystemOfUnits'},
                        'derivedCoherentUnitOfSystem': {'name': 'derivedCoherentUnitOfSystem',
                                                        'range': 'SystemOfUnits'},
                        'derivedUnitOfSystem': {'name': 'derivedUnitOfSystem',
                                                'range': 'SystemOfUnits'},
                        'exactMatch': {'name': 'exactMatch', 'range': 'Unit'},
                        'factorUnitScalar': {'multivalued': False,
                                             'name': 'factorUnitScalar'},
                        'hasDimensionVector': {'multivalued': False,
                                               'name': 'hasDimensionVector',
                                               'range': 'QuantityKindDimensionVector'},
                        'hasFactorUnit': {'name': 'hasFactorUnit'},
                        'hasQuantityKind': {'name': 'hasQuantityKind',
                                            'range': 'QuantityKind'},
                        'iec61360Code': {'name': 'iec61360Code', 'range': 'string'},
                        'latexDefinition': {'name': 'latexDefinition',
                                            'required': False},
                        'latexSymbol': {'name': 'latexSymbol', 'required': False},
                        'mathMLdefinition': {'multivalued': False,
                                             'name': 'mathMLdefinition'},
                        'prefix': {'name': 'prefix', 'range': 'Prefix'},
                        'qkdvDenominator': {'multivalued': False,
                                            'name': 'qkdvDenominator',
                                            'range': 'QuantityKindDimensionVector'},
                        'qkdvNumerator': {'multivalued': False,
                                          'name': 'qkdvNumerator',
                                          'range': 'QuantityKindDimensionVector'},
                        'scalingOf': {'name': 'scalingOf', 'range': 'Unit'},
                        'siUnitsExpression': {'name': 'siUnitsExpression',
                                              'required': False},
                        'symbol': {'name': 'symbol', 'required': False},
                        'ucumCode': {'name': 'ucumCode', 'range': 'UCUMcs'},
                        'udunitsCode': {'name': 'udunitsCode', 'range': 'string'},
                        'uneceCommonCode': {'name': 'uneceCommonCode',
                                            'range': 'string'}}})

    hasReciprocalUnit: Optional[list[str]] = Field(default=None, description="""has reciprocal unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:hasReciprocalUnit'} })
    isUnitOfSystem: Optional[list[str]] = Field(default=None, description="""This property relates a unit of measure with a system of units that either a) defines the unit or b) allows the unit to be used within the system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:isUnitOfSystem'} })
    omUnit: Optional[list[str]] = Field(default=None, description="""om unit""", json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:omUnit'} })
    unitFor: Optional[list[str]] = Field(default=None, description="""unit for""", json_schema_extra = { "linkml_meta": {'domain_of': ['Unit'], 'slot_uri': 'qudt:unitFor'} })
    guidance: Optional[list[str]] = Field(default=None, description="""guidance""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    qudt_id: Optional[str] = Field(default=None, description="""The \"qudt:id\" is an identifier string that uniquely identifies a QUDT concept.  The identifier is constructed using a prefix. For example, units are coded using the pattern: \"UCCCENNNN\", where \"CCC\" is a numeric code or a category and \"NNNN\" is a digit string for a member element of that category. For scaled units there may be an addition field that has the format \"QNN\" where \"NN\" is a digit string representing an exponent power, and \"Q\" is a qualifier that indicates with the code \"P\" that the power is a positive decimal exponent, or the code \"N\" for a negative decimal exponent, or the code \"B\" for binary positive exponents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class QuantityKind(Verifiable, AbstractQuantityKind):
    """
    A <b>Quantity Kind</b> is any observable property that can be measured and quantified numerically. Familiar examples include physical properties such as length, mass, time, force, energy, power, electric charge, etc. Less familiar examples include currency, interest rate, price to earning ratio, and information capacity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:QuantityKind',
         'comments': ['A <b>Quantity Kind</b> is any observable property that can be  '
                      'measured and quantified numerically. Familiar examples include '
                      'physical properties such as length, mass, time, force, energy, '
                      'power, electric charge, etc. Less familiar examples include '
                      'currency, interest rate, price to earning ratio, and '
                      'information capacity.^^rdf:HTML'],
         'from_schema': 'http://qudt.org/subset/qudt_subset',
         'mixins': ['AbstractQuantityKind'],
         'slot_usage': {'applicableCGSUnit': {'name': 'applicableCGSUnit',
                                              'required': False},
                        'applicableISOUnit': {'name': 'applicableISOUnit',
                                              'required': False},
                        'applicableImperialUnit': {'name': 'applicableImperialUnit',
                                                   'required': False},
                        'applicableSIUnit': {'name': 'applicableSIUnit',
                                             'required': False},
                        'applicableUSCustomaryUnit': {'name': 'applicableUSCustomaryUnit',
                                                      'required': False},
                        'applicableUnit': {'name': 'applicableUnit', 'required': False},
                        'dimensionVectorForSI': {'multivalued': False,
                                                 'name': 'dimensionVectorForSI',
                                                 'range': 'QuantityKindDimensionVector_SI'},
                        'exactMatch': {'name': 'exactMatch', 'range': 'QuantityKind'},
                        'hasDimensionVector': {'name': 'hasDimensionVector',
                                               'range': 'QuantityKindDimensionVector'},
                        'iec61360Code': {'name': 'iec61360Code', 'range': 'string'},
                        'latexDefinition': {'multivalued': False,
                                            'name': 'latexDefinition'},
                        'mathMLdefinition': {'multivalued': False,
                                             'name': 'mathMLdefinition'},
                        'qkdvDenominator': {'multivalued': False,
                                            'name': 'qkdvDenominator'},
                        'qkdvNumerator': {'multivalued': False,
                                          'name': 'qkdvNumerator'}}})

    belongsToSystemOfQuantities: Optional[list[str]] = Field(default=None, description="""belongs to system of quantities""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantityKind'], 'slot_uri': 'qudt:belongsToSystemOfQuantities'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })
    guidance: Optional[list[str]] = Field(default=None, description="""guidance""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    qudt_id: Optional[str] = Field(default=None, description="""The \"qudt:id\" is an identifier string that uniquely identifies a QUDT concept.  The identifier is constructed using a prefix. For example, units are coded using the pattern: \"UCCCENNNN\", where \"CCC\" is a numeric code or a category and \"NNNN\" is a digit string for a member element of that category. For scaled units there may be an addition field that has the format \"QNN\" where \"NN\" is a digit string representing an exponent power, and \"Q\" is a qualifier that indicates with the code \"P\" that the power is a positive decimal exponent, or the code \"N\" for a negative decimal exponent, or the code \"B\" for binary positive exponents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })


class UCUMcs-term(Thing):
    """
    Lexical pattern for the terminal symbols in the case-sensitive version of UCUM code
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['Lexical pattern for the terminal symbols in the case-sensitive '
                      'version of UCUM code'],
         'from_schema': 'http://qudt.org/subset/qudt_subset'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class QuantityKindDimensionVector(Concept):
    """
    <p class=\"lm-para\">A  <em>Quantity Kind Dimension Vector</em> describes the dimensionality of a quantity kind in the context of a system of units. In the SI system of units, the dimensions of a quantity kind are expressed as a product of the basic physical dimensions mass ($M$), length ($L$), time ($T$) current ($I$), amount of substance ($N$), luminous intensity ($J$) and absolute temperature ($\theta$) as $dim \, Q = L^{\alpha} \, M^{\beta} \, T^{\gamma} \, I ^{\delta} \, \theta ^{\epsilon} \, N^{\eta} \, J ^{\nu}$.</p>

    <p class=\"lm-para\">The rational powers of the dimensional exponents, $\alpha, \, \beta, \, \gamma, \, \delta, \, \epsilon, \ , \eta, \, \nu$, are positive, negative, or zero.</p>

    <p class=\"lm-para\">For example, the dimension of the physical quantity kind $\it{speed}$ is $\ boxed{length/time}$, $L/T$ or $LT^{-1}$, and the dimension of the physical quantity kind force is $\boxed{mass \times acceleration}$ or $\boxed{mass \times (length/time)/time}$, $ML/T^2$ or $MLT^{-2}$ respectively.</p>
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:QuantityKindDimensionVector',
         'comments': ['<p class=\\"lm-para\\">A  <em>Quantity Kind Dimension '
                      'Vector</em> describes the dimensionality of a quantity kind in '
                      'the context of a system of units. In the SI system of units, '
                      'the dimensions of a quantity kind are expressed as a product of '
                      'the basic physical dimensions mass ($M$), length ($L$), time '
                      '($T$) current ($I$), amount of substance ($N$), luminous '
                      'intensity ($J$) and absolute temperature ($\\\\theta$) as $dim '
                      '\\\\, Q = L^{\\\\alpha} \\\\, M^{\\\\beta} \\\\, T^{\\\\gamma} '
                      '\\\\, I ^{\\\\delta} \\\\, \\\\theta ^{\\\\epsilon} \\\\ , '
                      'N^{\\\\eta} \\\\, J ^{\\\\nu}$.</p>\n'
                      '\n'
                      '<p class=\\"lm-para\\">The rational powers of the dimensional '
                      'exponents, $\\\\alpha, \\\\, \\\\beta, \\\\, \\\\gamma, \\\\, '
                      '\\\\delta, \\\\, \\\\epsilon, \\\\, \\\\eta, \\\\, \\\\nu$, are '
                      'positive, negative, or zero.</p>\n'
                      '\n'
                      '<p class=\\"lm-para\\">For example, the dimension of the '
                      'physical quantity kind $\\\\it{speed}$ is '
                      '$\\\\boxed{length/time}$, $L/T$ or $LT^{-1}$, and the dimension '
                      'of the physical quantity kind force is $\\\\boxed{mass '
                      '\\\\times acceleration}$ or $\\\\boxed{mass \\\\times '
                      '(length/time)/time}$, $ML/T^2$ or $MLT^{-2}$ '
                      'respectively.</p>^^rdf:HTML'],
         'from_schema': 'http://qudt.org/subset/qudt_subset',
         'slot_usage': {'dimensionExponentForAmountOfSubstance': {'multivalued': False,
                                                                  'name': 'dimensionExponentForAmountOfSubstance',
                                                                  'required': True},
                        'dimensionExponentForElectricCurrent': {'multivalued': False,
                                                                'name': 'dimensionExponentForElectricCurrent',
                                                                'required': True},
                        'dimensionExponentForLength': {'multivalued': False,
                                                       'name': 'dimensionExponentForLength',
                                                       'required': True},
                        'dimensionExponentForLuminousIntensity': {'multivalued': False,
                                                                  'name': 'dimensionExponentForLuminousIntensity',
                                                                  'required': True},
                        'dimensionExponentForMass': {'multivalued': False,
                                                     'name': 'dimensionExponentForMass',
                                                     'required': True},
                        'dimensionExponentForThermodynamicTemperature': {'multivalued': False,
                                                                         'name': 'dimensionExponentForThermodynamicTemperature',
                                                                         'required': True},
                        'dimensionExponentForTime': {'multivalued': False,
                                                     'name': 'dimensionExponentForTime',
                                                     'required': True},
                        'dimensionlessExponent': {'multivalued': False,
                                                  'name': 'dimensionlessExponent',
                                                  'required': True},
                        'hasReferenceQuantityKind': {'name': 'hasReferenceQuantityKind',
                                                     'range': 'QuantityKind'},
                        'latexDefinition': {'multivalued': False,
                                            'name': 'latexDefinition'},
                        'latexSymbol': {'name': 'latexSymbol', 'required': False}}})

    guidance: Optional[list[str]] = Field(default=None, description="""guidance""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    qudt_id: Optional[str] = Field(default=None, description="""The \"qudt:id\" is an identifier string that uniquely identifies a QUDT concept.  The identifier is constructed using a prefix. For example, units are coded using the pattern: \"UCCCENNNN\", where \"CCC\" is a numeric code or a category and \"NNNN\" is a digit string for a member element of that category. For scaled units there may be an addition field that has the format \"QNN\" where \"NN\" is a digit string representing an exponent power, and \"Q\" is a qualifier that indicates with the code \"P\" that the power is a positive decimal exponent, or the code \"N\" for a negative decimal exponent, or the code \"B\" for binary positive exponents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class QuantityKindDimensionVectorSI(QuantityKindDimensionVector):
    """
    Quantity Kind Dimension vector (SI)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:QuantityKindDimensionVector_SI',
         'from_schema': 'http://qudt.org/subset/qudt_subset'})

    guidance: Optional[list[str]] = Field(default=None, description="""guidance""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    qudt_id: Optional[str] = Field(default=None, description="""The \"qudt:id\" is an identifier string that uniquely identifies a QUDT concept.  The identifier is constructed using a prefix. For example, units are coded using the pattern: \"UCCCENNNN\", where \"CCC\" is a numeric code or a category and \"NNNN\" is a digit string for a member element of that category. For scaled units there may be an addition field that has the format \"QNN\" where \"NN\" is a digit string representing an exponent power, and \"Q\" is a qualifier that indicates with the code \"P\" that the power is a positive decimal exponent, or the code \"N\" for a negative decimal exponent, or the code \"B\" for binary positive exponents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Rule(Verifiable, Concept):
    """
    Rule
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Rule',
         'from_schema': 'http://qudt.org/subset/qudt_subset',
         'mixins': ['Concept'],
         'slot_usage': {'rationale': {'name': 'rationale', 'required': False},
                        'ruleType': {'name': 'ruleType', 'range': 'RuleType'}}})

    guidance: Optional[list[str]] = Field(default=None, description="""guidance""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:guidance'} })
    qudt_id: Optional[str] = Field(default=None, description="""The \"qudt:id\" is an identifier string that uniquely identifies a QUDT concept.  The identifier is constructed using a prefix. For example, units are coded using the pattern: \"UCCCENNNN\", where \"CCC\" is a numeric code or a category and \"NNNN\" is a digit string for a member element of that category. For scaled units there may be an addition field that has the format \"QNN\" where \"NN\" is a digit string representing an exponent power, and \"Q\" is a qualifier that indicates with the code \"P\" that the power is a positive decimal exponent, or the code \"N\" for a negative decimal exponent, or the code \"B\" for binary positive exponents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept'], 'slot_uri': 'qudt:id'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


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

    hasSize: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Berry'], 'slot_uri': 'pokemon:hasSize'} })
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
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing'], 'slot_uri': 'rdfs:comment'} })


class Pokeball(Item):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'A Poké Ball is a type of item that '
                                                   "is critical to a Trainer's quest, "
                                                   'used for catching and storing '
                                                   'Pokémon.'}},
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
Aspect.model_rebuild()
Quantifiable.model_rebuild()
Concept.model_rebuild()
SystemOfQuantityKinds.model_rebuild()
Quantity.model_rebuild()
PhysicalConstant.model_rebuild()
Encoding.model_rebuild()
Enumeration.model_rebuild()
AbstractQuantityKind.model_rebuild()
QuantityValue.model_rebuild()
DataEncoding.model_rebuild()
UCUMcs.model_rebuild()
Datatype.model_rebuild()
Verifiable.model_rebuild()
SystemOfUnits.model_rebuild()
Prefix.model_rebuild()
EnumeratedValue.model_rebuild()
EndianType.model_rebuild()
RuleType.model_rebuild()
CardinalityType.model_rebuild()
OrderedType.model_rebuild()
Unit.model_rebuild()
QuantityKind.model_rebuild()
UCUMcs-term.model_rebuild()
QuantityKindDimensionVector.model_rebuild()
QuantityKindDimensionVectorSI.model_rebuild()
Rule.model_rebuild()
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
