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


linkml_meta = LinkMLMeta({'annotations': {'dcterms:description': {'tag': 'dcterms:description',
                                             'value': 'Ontology covering the '
                                                      'Pokemon world as it is '
                                                      'presented in games and '
                                                      'anime television series.'},
                     'dcterms:issued': {'tag': 'dcterms:issued',
                                        'value': '2019-07-27^^xsd:date'}},
     'classes': {'Ability': {'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                                              'value': 'Abilities '
                                                                       'were '
                                                                       'introduced '
                                                                       'in '
                                                                       'Generation '
                                                                       'III as an '
                                                                       'all new '
                                                                       'game '
                                                                       'mechanic. '
                                                                       'Each and '
                                                                       'every '
                                                                       'Pokemon '
                                                                       'has an '
                                                                       'ability, '
                                                                       'and can '
                                                                       'only have '
                                                                       'one at a '
                                                                       'time. Some '
                                                                       'abilities '
                                                                       'are '
                                                                       'exclusive '
                                                                       'to certain '
                                                                       'Pokemon '
                                                                       'and '
                                                                       'Evolution '
                                                                       'lines, '
                                                                       'while '
                                                                       'others are '
                                                                       'known by '
                                                                       'many '
                                                                       'Pokemon.'}},
                             'class_uri': 'pokemon:Ability',
                             'from_schema': 'https://pokemonkg.org/ontology',
                             'is_a': 'Thing',
                             'name': 'Ability',
                             'slots': ['effectDescription']},
                 'BattleItem': {'description': 'Battle items are items that can be '
                                               'used during battles.',
                                'from_schema': 'https://pokemonkg.org/ontology',
                                'is_a': 'Item',
                                'name': 'BattleItem'},
                 'Berry': {'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                                            'value': 'Berries are '
                                                                     'small, '
                                                                     'juicy, '
                                                                     'fleshy '
                                                                     'fruit. As in '
                                                                     'the real '
                                                                     'world, a '
                                                                     'large '
                                                                     'variety '
                                                                     'exists in '
                                                                     'the Pokémon '
                                                                     'world, with '
                                                                     'a large '
                                                                     'range of '
                                                                     'flavors, '
                                                                     'names, and '
                                                                     'effects. '
                                                                     'First found '
                                                                     'in the '
                                                                     'Generation '
                                                                     'II games, '
                                                                     'many Berries '
                                                                     'have since '
                                                                     'became '
                                                                     'critical '
                                                                     'help items '
                                                                     'in battle, '
                                                                     'where their '
                                                                     'various '
                                                                     'effects '
                                                                     'include HP '
                                                                     'and status '
                                                                     'condition '
                                                                     'restoration, '
                                                                     'stat '
                                                                     'enhancement, '
                                                                     'and even '
                                                                     'damage '
                                                                     'negation.'}},
                           'from_schema': 'https://pokemonkg.org/ontology',
                           'is_a': 'Food',
                           'name': 'Berry',
                           'slots': ['hasSize']},
                 'EggGroup': {'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                                               'value': 'Egg group '
                                                                        'is a '
                                                                        'category '
                                                                        'that '
                                                                        'determines '
                                                                        'which '
                                                                        'Pokemon '
                                                                        'are able '
                                                                        'to '
                                                                        'interbreed. '
                                                                        'The '
                                                                        'concept '
                                                                        'was '
                                                                        'introduced '
                                                                        'in '
                                                                        'Generation '
                                                                        'II, along '
                                                                        'with '
                                                                        'breeding. '
                                                                        'Similar '
                                                                        'to types, '
                                                                        'a Pokémon '
                                                                        'may '
                                                                        'belong to '
                                                                        'either '
                                                                        'one or '
                                                                        'two egg '
                                                                        'groups.'}},
                              'from_schema': 'https://pokemonkg.org/ontology',
                              'is_a': 'Thing',
                              'name': 'EggGroup'},
                 'Flavor': {'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                                             'value': 'Flavor is a '
                                                                      'special set '
                                                                      'of '
                                                                      'attributes '
                                                                      'that '
                                                                      'certain '
                                                                      'foods in '
                                                                      'the Pokémon '
                                                                      'world have. '
                                                                      'Most of the '
                                                                      'foods can '
                                                                      'have more '
                                                                      'than one '
                                                                      'flavor, and '
                                                                      'the flavor '
                                                                      'determines '
                                                                      'which '
                                                                      'Pokemon can '
                                                                      'eat them.'}},
                            'from_schema': 'https://pokemonkg.org/ontology',
                            'is_a': 'Thing',
                            'name': 'Flavor'},
                 'Food': {'from_schema': 'https://pokemonkg.org/ontology',
                          'is_a': 'Item',
                          'name': 'Food',
                          'slots': ['hasFlavor', 'firmness', 'smoothness']},
                 'Game': {'description': 'A game is a type of media that can be '
                                         'played by people.',
                          'from_schema': 'https://pokemonkg.org/ontology',
                          'is_a': 'Thing',
                          'name': 'Game'},
                 'Generation': {'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                                                 'value': 'Generations '
                                                                          'refers '
                                                                          'to the '
                                                                          'Pokemon '
                                                                          'game '
                                                                          'series. '
                                                                          'It is a '
                                                                          'group '
                                                                          'of '
                                                                          'games '
                                                                          'that '
                                                                          'were '
                                                                          'released '
                                                                          'at or '
                                                                          'around '
                                                                          'the '
                                                                          'same '
                                                                          'time. '
                                                                          'It also '
                                                                          'means '
                                                                          'that '
                                                                          'games '
                                                                          'in the '
                                                                          'same '
                                                                          'generation '
                                                                          'are '
                                                                          'compatible '
                                                                          'with '
                                                                          'the '
                                                                          'others, '
                                                                          'containing '
                                                                          'the '
                                                                          'same '
                                                                          'Pokemon '
                                                                          'and the '
                                                                          'number '
                                                                          'of '
                                                                          'moves '
                                                                          'there '
                                                                          'are to '
                                                                          'be '
                                                                          'learned.'}},
                                'from_schema': 'https://pokemonkg.org/ontology',
                                'is_a': 'Thing',
                                'name': 'Generation',
                                'slots': ['featuresSpecies']},
                 'Gym': {'description': 'A gym is a location that can be battled '
                                        'at.',
                         'from_schema': 'https://pokemonkg.org/ontology',
                         'is_a': 'Place',
                         'name': 'Gym'},
                 'GymLeader': {'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                                                'value': 'A gym '
                                                                         'leader '
                                                                         'is the '
                                                                         'highest '
                                                                         'ranking '
                                                                         'member '
                                                                         'and '
                                                                         'owner of '
                                                                         'an '
                                                                         'official '
                                                                         'Pokémon '
                                                                         'gym. Gym '
                                                                         'leaders '
                                                                         'use '
                                                                         'their '
                                                                         'gym and '
                                                                         'their '
                                                                         'Pokemon '
                                                                         'to test '
                                                                         'the '
                                                                         'skills '
                                                                         'of '
                                                                         'trainers '
                                                                         'that '
                                                                         'challenge '
                                                                         'them, '
                                                                         'and if '
                                                                         'said '
                                                                         'trainers '
                                                                         'win a '
                                                                         'battle, '
                                                                         'the gym '
                                                                         'leader '
                                                                         'will '
                                                                         'gift '
                                                                         'them a '
                                                                         'badge '
                                                                         "that's "
                                                                         'unique '
                                                                         'to that '
                                                                         'specific '
                                                                         'gym.'}},
                               'from_schema': 'https://pokemonkg.org/ontology',
                               'is_a': 'Trainer',
                               'name': 'GymLeader'},
                 'HM': {'description': 'Hidden Machine',
                        'from_schema': 'https://pokemonkg.org/ontology',
                        'is_a': 'Item',
                        'name': 'HM'},
                 'Habitat': {'description': 'A habitat is a type of environment '
                                            'that certain Pokemon belong to.',
                             'from_schema': 'https://pokemonkg.org/ontology',
                             'is_a': 'NamedThing',
                             'name': 'Habitat'},
                 'HoldItem': {'description': 'A hold item is an item that can be '
                                             'held by a Pokemon.',
                              'from_schema': 'https://pokemonkg.org/ontology',
                              'is_a': 'Item',
                              'name': 'HoldItem'},
                 'Item': {'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                                           'value': 'An item is an '
                                                                    'object in the '
                                                                    'Pokémon games '
                                                                    'which the '
                                                                    'player can '
                                                                    'pick up, keep '
                                                                    'in their Bag, '
                                                                    'and use in '
                                                                    'some manner. '
                                                                    'They have '
                                                                    'various uses, '
                                                                    'including '
                                                                    'healing, '
                                                                    'powering up, '
                                                                    'helping one '
                                                                    'to catch '
                                                                    'Pokémon, or '
                                                                    'to access a '
                                                                    'new area.'}},
                          'from_schema': 'https://pokemonkg.org/ontology',
                          'is_a': 'Thing',
                          'name': 'Item'},
                 'LearningByLevelingUp': {'description': 'A move that is learned '
                                                         'by leveling up.',
                                          'from_schema': 'https://pokemonkg.org/ontology',
                                          'is_a': 'MoveLearning',
                                          'name': 'LearningByLevelingUp'},
                 'LearningThroughBreeding': {'description': 'A move that is '
                                                            'learned by breeding.',
                                             'from_schema': 'https://pokemonkg.org/ontology',
                                             'is_a': 'MoveLearning',
                                             'name': 'LearningThroughBreeding'},
                 'Medicine': {'description': 'Medicine items can heal various '
                                             'afflictions of a Pokemon.',
                              'from_schema': 'https://pokemonkg.org/ontology',
                              'is_a': 'Item',
                              'name': 'Medicine'},
                 'Move': {'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                                           'value': 'A move is a '
                                                                    'special '
                                                                    'ability of a '
                                                                    'Pokemon.'}},
                          'class_uri': 'pokemon:Move',
                          'from_schema': 'https://pokemonkg.org/ontology',
                          'is_a': 'Thing',
                          'name': 'Move',
                          'slots': ['effectDescription', 'hasType']},
                 'MoveLearning': {'description': 'A move learning is a way that a '
                                                 'Pokemon can learn a move.',
                                  'from_schema': 'https://pokemonkg.org/ontology',
                                  'name': 'MoveLearning'},
                 'PhysicalMove': {'description': 'A physical move is a type of '
                                                 'move that can be used during '
                                                 'battles.',
                                  'from_schema': 'https://pokemonkg.org/ontology',
                                  'is_a': 'Move',
                                  'name': 'PhysicalMove'},
                 'Place': {'abstract': True,
                           'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                                            'value': 'Entities '
                                                                     'that have a '
                                                                     'somewhat '
                                                                     'fixed, '
                                                                     'physical '
                                                                     'extension.'}},
                           'from_schema': 'https://pokemonkg.org/ontology',
                           'is_a': 'Thing',
                           'name': 'Place'},
                 'Pokeball': {'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                                               'value': 'A Poké '
                                                                        'Ball is a '
                                                                        'type of '
                                                                        'item that '
                                                                        'is '
                                                                        'critical '
                                                                        'to a '
                                                                        "Trainer's "
                                                                        'quest, '
                                                                        'used for '
                                                                        'catching '
                                                                        'and '
                                                                        'storing '
                                                                        'Pokémon.'}},
                              'from_schema': 'https://pokemonkg.org/ontology',
                              'is_a': 'Item',
                              'name': 'Pokeball'},
                 'Pokedex': {'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                                              'value': 'The '
                                                                       'Pokedex is '
                                                                       'an '
                                                                       'electronic '
                                                                       'device '
                                                                       'designed '
                                                                       'to '
                                                                       'catalogue '
                                                                       'and '
                                                                       'provide '
                                                                       'information '
                                                                       'regarding '
                                                                       'the '
                                                                       'various '
                                                                       'species of '
                                                                       'Pokemon '
                                                                       'featured '
                                                                       'in the '
                                                                       'Pokemon '
                                                                       'video '
                                                                       'game, '
                                                                       'anime and '
                                                                       'manga '
                                                                       'series.'}},
                             'from_schema': 'https://pokemonkg.org/ontology',
                             'is_a': 'Thing',
                             'name': 'Pokedex'},
                 'PokedexEntry': {'description': 'A pokedex entry is a description '
                                                 'of a Pokemon.',
                                  'from_schema': 'https://pokemonkg.org/ontology',
                                  'is_a': 'NamedThing',
                                  'name': 'PokedexEntry'},
                 'Pokemon': {'annotations': {'rdfs:seeAlso': {'tag': 'rdfs:seeAlso',
                                                              'value': '<https://dbpedia.org/resource/Pokémon>'}},
                             'description': 'A Pokemon',
                             'from_schema': 'https://pokemonkg.org/ontology',
                             'name': 'Pokemon',
                             'union_of': ['Pokedex', 'Type']},
                 'Region': {'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                                             'value': 'Regions are '
                                                                      'areas in '
                                                                      'the Pokémon '
                                                                      'universe '
                                                                      'that are '
                                                                      'smaller '
                                                                      'parts of a '
                                                                      'nation.'}},
                            'from_schema': 'https://pokemonkg.org/ontology',
                            'is_a': 'Place',
                            'name': 'Region'},
                 'Shape': {'description': 'Shapes are categories that certain '
                                          'Pokemon belong to, which determine '
                                          'which Pokemon they can breed with.',
                           'from_schema': 'https://pokemonkg.org/ontology',
                           'is_a': 'NamedThing',
                           'name': 'Shape'},
                 'SpecialMove': {'description': 'A special move is a type of move '
                                                'that can be used during battles.',
                                 'from_schema': 'https://pokemonkg.org/ontology',
                                 'is_a': 'Move',
                                 'name': 'SpecialMove'},
                 'Species': {'class_uri': 'pokemon:Species',
                             'description': 'A species is a category of Pokemon '
                                            'that share common features.',
                             'from_schema': 'https://pokemonkg.org/ontology',
                             'is_a': 'NamedThing',
                             'name': 'Species',
                             'slots': ['hasColour',
                                       'mayHaveHiddenAbility',
                                       'mayHaveAbility',
                                       'isAbleToApply',
                                       'hasHeight',
                                       'hasWeight',
                                       'depiction',
                                       'inEggGroup',
                                       'hasType',
                                       'hasShape',
                                       'hasGenus',
                                       'hasCatchRate',
                                       'foundIn']},
                 'StatusMove': {'description': 'A status move is a type of move '
                                               'that can be used during battles.',
                                'from_schema': 'https://pokemonkg.org/ontology',
                                'is_a': 'Move',
                                'name': 'StatusMove'},
                 'TM': {'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                                         'value': 'A Technical '
                                                                  'Machine is an '
                                                                  'item that can '
                                                                  'be used to '
                                                                  'teach a Pokemon '
                                                                  'a move.'}},
                        'from_schema': 'https://pokemonkg.org/ontology',
                        'is_a': 'Item',
                        'mixins': ['MoveLearning'],
                        'name': 'TM'},
                 'Town': {'description': 'A town is a type of place that can be '
                                         'visited.',
                          'from_schema': 'https://pokemonkg.org/ontology',
                          'is_a': 'Place',
                          'name': 'Town'},
                 'Trainer': {'description': 'A trainer is a person who is able to '
                                            'catch Pokemon.',
                             'from_schema': 'https://pokemonkg.org/ontology',
                             'is_a': 'Person',
                             'name': 'Trainer'},
                 'Type': {'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                                           'value': 'All Pokemon '
                                                                    'creatures and '
                                                                    'their moves '
                                                                    'are assigned '
                                                                    'certain '
                                                                    'types. Each '
                                                                    'type has '
                                                                    'several '
                                                                    'strengths and '
                                                                    'weaknesses in '
                                                                    'both attack '
                                                                    'and '
                                                                    'defense.'}},
                          'class_uri': 'pokemon:Type',
                          'from_schema': 'https://pokemonkg.org/ontology',
                          'is_a': 'NamedThing',
                          'name': 'Type'}},
     'created_on': '2019-07-27T00:00:00',
     'default_prefix': 'pokemon',
     'default_range': 'string',
     'description': 'Ontology covering the Pokémon world as it is presented in '
                    'games and anime television series',
     'enums': {'HabitatEnum': {'from_schema': 'https://pokemonkg.org/ontology',
                               'implements': ['owl:NamedIndividual'],
                               'name': 'HabitatEnum',
                               'permissible_values': {'Cave': {'meaning': 'pokemon:Habitat_Cave',
                                                               'text': 'Cave'},
                                                      'Forest': {'meaning': 'pokemon:Habitat_Forest',
                                                                 'text': 'Forest'},
                                                      'Grassland': {'meaning': 'pokemon:Habitat_Grassland',
                                                                    'text': 'Grassland'}}}},
     'id': 'https://pokemonkg.org/ontology',
     'imports': ['linkml:types', './foaf', './dbpedia', './owl'],
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
     'slots': {'accuracy': {'domain': 'Move',
                            'from_schema': 'https://pokemonkg.org/ontology',
                            'name': 'accuracy',
                            'range': 'integer'},
               'basePower': {'domain': 'Move',
                             'from_schema': 'https://pokemonkg.org/ontology',
                             'name': 'basePower',
                             'range': 'integer'},
               'basePowerPoints': {'domain': 'Move',
                                   'from_schema': 'https://pokemonkg.org/ontology',
                                   'name': 'basePowerPoints',
                                   'range': 'integer'},
               'containsPlace': {'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                                                  'value': 'A '
                                                                           'place '
                                                                           'is '
                                                                           'contained '
                                                                           'to '
                                                                           'some '
                                                                           'extent '
                                                                           'in '
                                                                           'this '
                                                                           'place.'}},
                                 'asymmetric': True,
                                 'domain': 'Place',
                                 'from_schema': 'https://pokemonkg.org/ontology',
                                 'inverse': 'locatedIn',
                                 'multivalued': True,
                                 'name': 'containsPlace',
                                 'range': 'Place',
                                 'required': False,
                                 'slot_uri': 'pokemon:contains_place',
                                 'transitive': True},
               'describedInPokedex': {'description': "['A Pokedex entry is "
                                                     "described in a Pokedex']",
                                      'domain': 'Species',
                                      'from_schema': 'https://pokemonkg.org/ontology',
                                      'inverse': 'describesPokemon',
                                      'multivalued': True,
                                      'name': 'describedInPokedex',
                                      'range': 'PokedexEntry',
                                      'required': False,
                                      'slot_uri': 'pokemon:describedInPokedex'},
               'describesPokemon': {'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                                                     'value': 'A '
                                                                              'Pokemon '
                                                                              'that '
                                                                              'is '
                                                                              'described '
                                                                              'by '
                                                                              'this '
                                                                              'Pokedex '
                                                                              'entry.'}},
                                    'domain': 'PokedexEntry',
                                    'from_schema': 'https://pokemonkg.org/ontology',
                                    'multivalued': True,
                                    'name': 'describesPokemon',
                                    'range': 'Species',
                                    'required': False,
                                    'slot_uri': 'pokemon:describesPokemon'},
               'effectDescription': {'description': 'A description of the effect '
                                                    'of the entity',
                                     'domain_of': ['Ability', 'Move'],
                                     'from_schema': 'https://pokemonkg.org/ontology',
                                     'multivalued': True,
                                     'name': 'effectDescription',
                                     'range': 'string',
                                     'required': False,
                                     'slot_uri': 'pokemon:effectDescription'},
               'entryNumber': {'domain': 'PokedexEntry',
                               'from_schema': 'https://pokemonkg.org/ontology',
                               'name': 'entryNumber',
                               'range': 'integer'},
               'evolvesFrom': {'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                                                'value': 'This '
                                                                         'species '
                                                                         'evolves '
                                                                         'the '
                                                                         'other '
                                                                         'species.'}},
                               'domain': 'Species',
                               'from_schema': 'https://pokemonkg.org/ontology',
                               'inverse': 'evolvesTo',
                               'multivalued': False,
                               'name': 'evolvesFrom',
                               'range': 'Species',
                               'required': False,
                               'slot_uri': 'pokemon:evolvesFrom'},
               'evolvesTo': {'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                                              'value': 'A Pokemon '
                                                                       'evolves to '
                                                                       'another '
                                                                       'Pokemon.'}},
                             'domain': 'Species',
                             'from_schema': 'https://pokemonkg.org/ontology',
                             'inverse': 'evolvesFrom',
                             'multivalued': True,
                             'name': 'evolvesTo',
                             'range': 'Species',
                             'required': False,
                             'slot_uri': 'pokemon:evolvesTo'},
               'featuresSpecies': {'description': "['A Pokedex entry features a "
                                                  "species']",
                                   'domain_of': ['Generation'],
                                   'from_schema': 'https://pokemonkg.org/ontology',
                                   'multivalued': True,
                                   'name': 'featuresSpecies',
                                   'range': 'Species',
                                   'required': False,
                                   'slot_uri': 'pokemon:featuresSpecies'},
               'firmness': {'domain': 'Food',
                            'domain_of': ['Food'],
                            'from_schema': 'https://pokemonkg.org/ontology',
                            'name': 'firmness',
                            'range': 'integer'},
               'foundIn': {'description': 'A place is found in a location',
                           'domain': 'Species',
                           'domain_of': ['Species'],
                           'from_schema': 'https://pokemonkg.org/ontology',
                           'multivalued': True,
                           'name': 'foundIn',
                           'range': 'Habitat',
                           'required': False,
                           'slot_uri': 'pokemon:foundIn'},
               'hasCatchRate': {'domain': 'Species',
                                'domain_of': ['Species'],
                                'from_schema': 'https://pokemonkg.org/ontology',
                                'multivalued': False,
                                'name': 'hasCatchRate',
                                'range': 'integer',
                                'required': False,
                                'slot_uri': 'pokemon:hasCatchRate'},
               'hasColour': {'description': 'A Pokemon has a color',
                             'domain_of': ['Species'],
                             'from_schema': 'https://pokemonkg.org/ontology',
                             'multivalued': False,
                             'name': 'hasColour',
                             'range': 'Colour',
                             'required': False,
                             'slot_uri': 'pokemon:hasColour'},
               'hasFlavor': {'description': 'A Pokemon has a flavor',
                             'domain': 'Food',
                             'domain_of': ['Food'],
                             'from_schema': 'https://pokemonkg.org/ontology',
                             'multivalued': True,
                             'name': 'hasFlavor',
                             'range': 'Flavor',
                             'required': False,
                             'slot_uri': 'pokemon:hasFlavor'},
               'hasGenus': {'domain': 'Species',
                            'domain_of': ['Species'],
                            'from_schema': 'https://pokemonkg.org/ontology',
                            'name': 'hasGenus',
                            'range': 'string'},
               'hasHeight': {'domain': 'Species',
                             'domain_of': ['Species'],
                             'from_schema': 'https://pokemonkg.org/ontology',
                             'multivalued': False,
                             'name': 'hasHeight',
                             'required': False,
                             'slot_uri': 'pokemon:hasHeight'},
               'hasPokedexEntry': {'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                                                    'value': 'A '
                                                                             'Pokedex '
                                                                             'entry '
                                                                             'in '
                                                                             'which '
                                                                             'this '
                                                                             'Pokemon '
                                                                             'is '
                                                                             'described.'}},
                                   'domain': 'Pokedex',
                                   'from_schema': 'https://pokemonkg.org/ontology',
                                   'multivalued': True,
                                   'name': 'hasPokedexEntry',
                                   'range': 'PokedexEntry',
                                   'required': False,
                                   'slot_uri': 'pokemon:hasPokedexEntry'},
               'hasShape': {'description': 'The shape of a berry is a measure of '
                                           'how good it  is for making a Potion.',
                            'domain': 'Species',
                            'domain_of': ['Species'],
                            'from_schema': 'https://pokemonkg.org/ontology',
                            'multivalued': False,
                            'name': 'hasShape',
                            'range': 'Shape',
                            'required': False,
                            'slot_uri': 'pokemon:hasShape'},
               'hasSize': {'domain_of': ['Berry'],
                           'from_schema': 'https://pokemonkg.org/ontology',
                           'multivalued': False,
                           'name': 'hasSize',
                           'required': False,
                           'slot_uri': 'pokemon:hasSize'},
               'hasType': {'description': 'A Pokemon has a type',
                           'domain_of': ['Species', 'Move'],
                           'from_schema': 'https://pokemonkg.org/ontology',
                           'inlined': True,
                           'inlined_as_list': True,
                           'multivalued': True,
                           'name': 'hasType',
                           'range': 'Type',
                           'required': False,
                           'slot_uri': 'pokemon:hasType'},
               'hasWeight': {'domain': 'Species',
                             'domain_of': ['Species'],
                             'from_schema': 'https://pokemonkg.org/ontology',
                             'multivalued': False,
                             'name': 'hasWeight',
                             'required': False,
                             'slot_uri': 'pokemon:hasWeight'},
               'inEggGroup': {'domain': 'Species',
                              'domain_of': ['Species'],
                              'from_schema': 'https://pokemonkg.org/ontology',
                              'multivalued': True,
                              'name': 'inEggGroup',
                              'range': 'EggGroup',
                              'required': False,
                              'slot_uri': 'pokemon:inEggGroup'},
               'isAbleToApply': {'domain_of': ['Species'],
                                 'from_schema': 'https://pokemonkg.org/ontology',
                                 'multivalued': True,
                                 'name': 'isAbleToApply',
                                 'range': 'Move',
                                 'required': False,
                                 'slot_uri': 'pokemon:isAbleToApply'},
               'learnsMove': {'domain': 'MoveLearning',
                              'from_schema': 'https://pokemonkg.org/ontology',
                              'multivalued': True,
                              'name': 'learnsMove',
                              'range': 'Move',
                              'required': False,
                              'slot_uri': 'pokemon:learnsMove'},
               'locatedIn': {'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                                              'value': 'This place '
                                                                       'is located '
                                                                       'to some '
                                                                       'extent in '
                                                                       'another '
                                                                       'place.'}},
                             'asymmetric': True,
                             'domain': 'Place',
                             'from_schema': 'https://pokemonkg.org/ontology',
                             'multivalued': True,
                             'name': 'locatedIn',
                             'range': 'Place',
                             'required': False,
                             'slot_uri': 'pokemon:locatedIn',
                             'transitive': True},
               'maxPowerPoints': {'domain': 'Move',
                                  'from_schema': 'https://pokemonkg.org/ontology',
                                  'name': 'maxPowerPoints',
                                  'range': 'integer'},
               'mayHaveAbility': {'description': 'A Pokemon may have an ability',
                                  'domain': 'Species',
                                  'domain_of': ['Species'],
                                  'from_schema': 'https://pokemonkg.org/ontology',
                                  'multivalued': True,
                                  'name': 'mayHaveAbility',
                                  'range': 'Ability',
                                  'slot_uri': 'pokemon:mayHaveAbility'},
               'mayHaveHiddenAbility': {'domain': 'Species',
                                        'domain_of': ['Species'],
                                        'from_schema': 'https://pokemonkg.org/ontology',
                                        'multivalued': True,
                                        'name': 'mayHaveHiddenAbility',
                                        'range': 'Ability',
                                        'slot_uri': 'pokemon:mayHaveHiddenAbility',
                                        'subproperty_of': 'mayHaveAbility'},
               'minLevelToLearn': {'from_schema': 'https://pokemonkg.org/ontology',
                                   'name': 'minLevelToLearn',
                                   'range': 'integer'},
               'smoothness': {'domain': 'Food',
                              'domain_of': ['Food'],
                              'from_schema': 'https://pokemonkg.org/ontology',
                              'name': 'smoothness',
                              'range': 'integer'}},
     'source_file': '../../pokemon/src/linkml_pokemon/schema/linkml_pokemon.yaml',
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
         'description': 'An rdfs:Resource that defines name and description',
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'Thing',
         'slots': ['id', 'name', 'description']})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'Thing',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'Thing',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'Thing',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class NamedThing(Thing):
    """
    A Thing that requires a name
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'owl:NamedIndividual',
         'description': 'A Thing that requires a name',
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'is_a': 'Thing',
         'name': 'NamedThing',
         'slot_usage': {'name': {'name': 'name', 'required': True}}})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'NamedThing',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'NamedThing',
         'range': 'string',
         'required': True,
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'NamedThing',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class Person(NamedThing):
    """
    A person is a human being
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'foaf:Person',
         'description': 'A person is a human being',
         'from_schema': 'http://xmlns.com/foaf/0.1/',
         'is_a': 'NamedThing',
         'name': 'Person',
         'slots': ['depiction']})

    depiction: Optional[str] = Field(default=None, description="""A depiction of the person""", json_schema_extra = { "linkml_meta": {'alias': 'depiction',
         'description': 'A depiction of the person',
         'domain_of': ['Person', 'Species'],
         'from_schema': 'http://xmlns.com/foaf/0.1/',
         'name': 'depiction',
         'owner': 'Person',
         'range': 'string',
         'slot_uri': 'foaf:depiction'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'Person',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'Person',
         'range': 'string',
         'required': True,
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'Person',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class Colour(Thing):
    """
    Color or colour is the visual perceptual property corresponding in humans to the categories called red, yellow, blue and others.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dbpedia:Colour',
         'description': 'Color or colour is the visual perceptual property '
                        'corresponding in humans to the categories called red, yellow, '
                        'blue and others.',
         'from_schema': 'https://dbpedia.org/ontology/',
         'is_a': 'Thing',
         'name': 'Colour',
         'slots': ['black',
                   'cyanic',
                   'magenta',
                   'yellow',
                   'hue',
                   'saturation',
                   'value',
                   'red',
                   'green',
                   'blue',
                   'wavelength']})

    black: Optional[float] = Field(default=None, description="""Black component in CMYK color model""", json_schema_extra = { "linkml_meta": {'alias': 'black',
         'description': 'Black component in CMYK color model',
         'domain_of': ['Colour'],
         'from_schema': 'https://dbpedia.org/ontology/',
         'name': 'black',
         'owner': 'Colour',
         'range': 'float',
         'slot_uri': 'dbpedia:cmykCoordinateBlack'} })
    cyanic: Optional[float] = Field(default=None, description="""Cyan component in CMYK color model""", json_schema_extra = { "linkml_meta": {'alias': 'cyanic',
         'description': 'Cyan component in CMYK color model',
         'domain_of': ['Colour'],
         'from_schema': 'https://dbpedia.org/ontology/',
         'name': 'cyanic',
         'owner': 'Colour',
         'range': 'float',
         'slot_uri': 'dbpedia:cmykCoordinateCyanic'} })
    magenta: Optional[float] = Field(default=None, description="""Magenta component in CMYK color model""", json_schema_extra = { "linkml_meta": {'alias': 'magenta',
         'description': 'Magenta component in CMYK color model',
         'domain_of': ['Colour'],
         'from_schema': 'https://dbpedia.org/ontology/',
         'name': 'magenta',
         'owner': 'Colour',
         'range': 'float',
         'slot_uri': 'dbpedia:cmykCoordinateMagenta'} })
    yellow: Optional[float] = Field(default=None, description="""Yellow component in CMYK color model""", json_schema_extra = { "linkml_meta": {'alias': 'yellow',
         'description': 'Yellow component in CMYK color model',
         'domain_of': ['Colour'],
         'from_schema': 'https://dbpedia.org/ontology/',
         'name': 'yellow',
         'owner': 'Colour',
         'range': 'float',
         'slot_uri': 'dbpedia:cmykCoordinateYellow'} })
    hue: Optional[float] = Field(default=None, description="""Hue component in HSV color model""", json_schema_extra = { "linkml_meta": {'alias': 'hue',
         'description': 'Hue component in HSV color model',
         'domain_of': ['Colour'],
         'from_schema': 'https://dbpedia.org/ontology/',
         'name': 'hue',
         'owner': 'Colour',
         'range': 'float',
         'slot_uri': 'dbpedia:hsvCoordinateHue'} })
    saturation: Optional[float] = Field(default=None, description="""Saturation component in HSV color model""", json_schema_extra = { "linkml_meta": {'alias': 'saturation',
         'description': 'Saturation component in HSV color model',
         'domain_of': ['Colour'],
         'from_schema': 'https://dbpedia.org/ontology/',
         'name': 'saturation',
         'owner': 'Colour',
         'range': 'float',
         'slot_uri': 'dbpedia:hsvCoordinateSaturation'} })
    value: Optional[float] = Field(default=None, description="""Value/Lightness component in HSV color model""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'description': 'Value/Lightness component in HSV color model',
         'domain_of': ['Colour'],
         'from_schema': 'https://dbpedia.org/ontology/',
         'name': 'value',
         'owner': 'Colour',
         'range': 'float',
         'slot_uri': 'dbpedia:hsvCoordinateLightness'} })
    red: Optional[int] = Field(default=None, description="""Red component in RGB color model (0-255)""", json_schema_extra = { "linkml_meta": {'alias': 'red',
         'description': 'Red component in RGB color model (0-255)',
         'domain_of': ['Colour'],
         'from_schema': 'https://dbpedia.org/ontology/',
         'name': 'red',
         'owner': 'Colour',
         'range': 'integer',
         'slot_uri': 'dbpedia:rgbCoordinateRed'} })
    green: Optional[int] = Field(default=None, description="""Green component in RGB color model (0-255)""", json_schema_extra = { "linkml_meta": {'alias': 'green',
         'description': 'Green component in RGB color model (0-255)',
         'domain_of': ['Colour'],
         'from_schema': 'https://dbpedia.org/ontology/',
         'name': 'green',
         'owner': 'Colour',
         'range': 'integer',
         'slot_uri': 'dbpedia:rgbCoordinateGreen'} })
    blue: Optional[int] = Field(default=None, description="""Blue component in RGB color model (0-255)""", json_schema_extra = { "linkml_meta": {'alias': 'blue',
         'description': 'Blue component in RGB color model (0-255)',
         'domain_of': ['Colour'],
         'from_schema': 'https://dbpedia.org/ontology/',
         'name': 'blue',
         'owner': 'Colour',
         'range': 'integer',
         'slot_uri': 'dbpedia:rgbCoordinateBlue'} })
    wavelength: Optional[float] = Field(default=None, description="""The wavelength of the color in nanometers""", json_schema_extra = { "linkml_meta": {'alias': 'wavelength',
         'description': 'The wavelength of the color in nanometers',
         'domain_of': ['Colour'],
         'from_schema': 'https://dbpedia.org/ontology/',
         'name': 'wavelength',
         'owner': 'Colour',
         'range': 'float',
         'slot_uri': 'dbpedia:wavelength'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'Colour',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'Colour',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'Colour',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


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
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'Thing',
         'name': 'Ability',
         'slots': ['effectDescription']})

    effectDescription: Optional[list[str]] = Field(default=None, description="""A description of the effect of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'effectDescription',
         'description': 'A description of the effect of the entity',
         'domain_of': ['Ability', 'Move'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'multivalued': True,
         'name': 'effectDescription',
         'owner': 'Ability',
         'range': 'string',
         'required': False,
         'slot_uri': 'pokemon:effectDescription'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'Ability',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'Ability',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'Ability',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class EggGroup(Thing):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'Egg group is a category that '
                                                   'determines which Pokemon are able '
                                                   'to interbreed. The concept was '
                                                   'introduced in Generation II, along '
                                                   'with breeding. Similar to types, a '
                                                   'Pokémon may belong to either one '
                                                   'or two egg groups.'}},
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'Thing',
         'name': 'EggGroup'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'EggGroup',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'EggGroup',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'EggGroup',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class Flavor(Thing):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'Flavor is a special set of '
                                                   'attributes that certain foods in '
                                                   'the Pokémon world have. Most of '
                                                   'the foods can have more than one '
                                                   'flavor, and the flavor determines '
                                                   'which Pokemon can eat them.'}},
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'Thing',
         'name': 'Flavor'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'Flavor',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'Flavor',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'Flavor',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class Game(Thing):
    """
    A game is a type of media that can be played by people.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'A game is a type of media that can be played by people.',
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'Thing',
         'name': 'Game'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'Game',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'Game',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'Game',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


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
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'Thing',
         'name': 'Generation',
         'slots': ['featuresSpecies']})

    featuresSpecies: Optional[list[str]] = Field(default=None, description="""['A Pokedex entry features a species']""", json_schema_extra = { "linkml_meta": {'alias': 'featuresSpecies',
         'description': "['A Pokedex entry features a species']",
         'domain_of': ['Generation'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'multivalued': True,
         'name': 'featuresSpecies',
         'owner': 'Generation',
         'range': 'Species',
         'required': False,
         'slot_uri': 'pokemon:featuresSpecies'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'Generation',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'Generation',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'Generation',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class Habitat(NamedThing):
    """
    A habitat is a type of environment that certain Pokemon belong to.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'A habitat is a type of environment that certain Pokemon '
                        'belong to.',
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'NamedThing',
         'name': 'Habitat'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'Habitat',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'Habitat',
         'range': 'string',
         'required': True,
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'Habitat',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


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
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'Thing',
         'name': 'Item'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'Item',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'Item',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'Item',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class BattleItem(Item):
    """
    Battle items are items that can be used during battles.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'Battle items are items that can be used during battles.',
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'Item',
         'name': 'BattleItem'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'BattleItem',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'BattleItem',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'BattleItem',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class Food(Item):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'Item',
         'name': 'Food',
         'slots': ['hasFlavor', 'firmness', 'smoothness']})

    hasFlavor: Optional[list[str]] = Field(default=None, description="""A Pokemon has a flavor""", json_schema_extra = { "linkml_meta": {'alias': 'hasFlavor',
         'description': 'A Pokemon has a flavor',
         'domain': 'Food',
         'domain_of': ['Food'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'multivalued': True,
         'name': 'hasFlavor',
         'owner': 'Food',
         'range': 'Flavor',
         'required': False,
         'slot_uri': 'pokemon:hasFlavor'} })
    firmness: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'firmness',
         'domain': 'Food',
         'domain_of': ['Food'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'name': 'firmness',
         'owner': 'Food',
         'range': 'integer'} })
    smoothness: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'smoothness',
         'domain': 'Food',
         'domain_of': ['Food'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'name': 'smoothness',
         'owner': 'Food',
         'range': 'integer'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'Food',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'Food',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'Food',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


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
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'Food',
         'name': 'Berry',
         'slots': ['hasSize']})

    hasSize: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'hasSize',
         'domain_of': ['Berry'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'multivalued': False,
         'name': 'hasSize',
         'owner': 'Berry',
         'range': 'string',
         'required': False,
         'slot_uri': 'pokemon:hasSize'} })
    hasFlavor: Optional[list[str]] = Field(default=None, description="""A Pokemon has a flavor""", json_schema_extra = { "linkml_meta": {'alias': 'hasFlavor',
         'description': 'A Pokemon has a flavor',
         'domain': 'Food',
         'domain_of': ['Food'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'multivalued': True,
         'name': 'hasFlavor',
         'owner': 'Berry',
         'range': 'Flavor',
         'required': False,
         'slot_uri': 'pokemon:hasFlavor'} })
    firmness: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'firmness',
         'domain': 'Food',
         'domain_of': ['Food'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'name': 'firmness',
         'owner': 'Berry',
         'range': 'integer'} })
    smoothness: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'smoothness',
         'domain': 'Food',
         'domain_of': ['Food'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'name': 'smoothness',
         'owner': 'Berry',
         'range': 'integer'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'Berry',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'Berry',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'Berry',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class HM(Item):
    """
    Hidden Machine
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'Hidden Machine',
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'Item',
         'name': 'HM'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'HM',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'HM',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'HM',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class HoldItem(Item):
    """
    A hold item is an item that can be held by a Pokemon.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'A hold item is an item that can be held by a Pokemon.',
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'Item',
         'name': 'HoldItem'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'HoldItem',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'HoldItem',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'HoldItem',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class Pokedex(Thing):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'The Pokedex is an electronic '
                                                   'device designed to catalogue and '
                                                   'provide information regarding the '
                                                   'various species of Pokemon '
                                                   'featured in the Pokemon video '
                                                   'game, anime and manga series.'}},
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'Thing',
         'name': 'Pokedex'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'Pokedex',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'Pokedex',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'Pokedex',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class Pokemon(ConfiguredBaseModel):
    """
    A Pokemon
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:seeAlso': {'tag': 'rdfs:seeAlso',
                                          'value': '<https://dbpedia.org/resource/Pokémon>'}},
         'description': 'A Pokemon',
         'from_schema': 'https://pokemonkg.org/ontology',
         'name': 'Pokemon',
         'union_of': ['Pokedex', 'Type']})

    pass


class PokedexEntry(NamedThing):
    """
    A pokedex entry is a description of a Pokemon.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'A pokedex entry is a description of a Pokemon.',
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'NamedThing',
         'name': 'PokedexEntry'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'PokedexEntry',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'PokedexEntry',
         'range': 'string',
         'required': True,
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'PokedexEntry',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class Pokeball(Item):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'A Poké Ball is a type of item that '
                                                   "is critical to a Trainer's quest, "
                                                   'used for catching and storing '
                                                   'Pokémon.'}},
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'Item',
         'name': 'Pokeball'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'Pokeball',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'Pokeball',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'Pokeball',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class Place(Thing):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'Entities that have a somewhat '
                                                   'fixed, physical extension.'}},
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'Thing',
         'name': 'Place'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'Place',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'Place',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'Place',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class Gym(Place):
    """
    A gym is a location that can be battled at.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'A gym is a location that can be battled at.',
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'Place',
         'name': 'Gym'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'Gym',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'Gym',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'Gym',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class Shape(NamedThing):
    """
    Shapes are categories that certain Pokemon belong to, which determine which Pokemon they can breed with.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'Shapes are categories that certain Pokemon belong to, which '
                        'determine which Pokemon they can breed with.',
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'NamedThing',
         'name': 'Shape'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'Shape',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'Shape',
         'range': 'string',
         'required': True,
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'Shape',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class Region(Place):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'Regions are areas in the Pokémon '
                                                   'universe that are smaller parts of '
                                                   'a nation.'}},
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'Place',
         'name': 'Region'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'Region',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'Region',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'Region',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class Species(NamedThing):
    """
    A species is a category of Pokemon that share common features.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pokemon:Species',
         'description': 'A species is a category of Pokemon that share common '
                        'features.',
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'NamedThing',
         'name': 'Species',
         'slots': ['hasColour',
                   'mayHaveHiddenAbility',
                   'mayHaveAbility',
                   'isAbleToApply',
                   'hasHeight',
                   'hasWeight',
                   'depiction',
                   'inEggGroup',
                   'hasType',
                   'hasShape',
                   'hasGenus',
                   'hasCatchRate',
                   'foundIn']})

    hasColour: Optional[str] = Field(default=None, description="""A Pokemon has a color""", json_schema_extra = { "linkml_meta": {'alias': 'hasColour',
         'description': 'A Pokemon has a color',
         'domain_of': ['Species'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'multivalued': False,
         'name': 'hasColour',
         'owner': 'Species',
         'range': 'Colour',
         'required': False,
         'slot_uri': 'pokemon:hasColour'} })
    mayHaveHiddenAbility: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'mayHaveHiddenAbility',
         'domain': 'Species',
         'domain_of': ['Species'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'multivalued': True,
         'name': 'mayHaveHiddenAbility',
         'owner': 'Species',
         'range': 'Ability',
         'slot_uri': 'pokemon:mayHaveHiddenAbility',
         'subproperty_of': 'mayHaveAbility'} })
    mayHaveAbility: Optional[list[str]] = Field(default=None, description="""A Pokemon may have an ability""", json_schema_extra = { "linkml_meta": {'alias': 'mayHaveAbility',
         'description': 'A Pokemon may have an ability',
         'domain': 'Species',
         'domain_of': ['Species'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'multivalued': True,
         'name': 'mayHaveAbility',
         'owner': 'Species',
         'range': 'Ability',
         'slot_uri': 'pokemon:mayHaveAbility'} })
    isAbleToApply: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'isAbleToApply',
         'domain_of': ['Species'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'multivalued': True,
         'name': 'isAbleToApply',
         'owner': 'Species',
         'range': 'Move',
         'required': False,
         'slot_uri': 'pokemon:isAbleToApply'} })
    hasHeight: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'hasHeight',
         'domain': 'Species',
         'domain_of': ['Species'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'multivalued': False,
         'name': 'hasHeight',
         'owner': 'Species',
         'range': 'string',
         'required': False,
         'slot_uri': 'pokemon:hasHeight'} })
    hasWeight: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'hasWeight',
         'domain': 'Species',
         'domain_of': ['Species'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'multivalued': False,
         'name': 'hasWeight',
         'owner': 'Species',
         'range': 'string',
         'required': False,
         'slot_uri': 'pokemon:hasWeight'} })
    depiction: Optional[str] = Field(default=None, description="""A depiction of the person""", json_schema_extra = { "linkml_meta": {'alias': 'depiction',
         'description': 'A depiction of the person',
         'domain_of': ['Person', 'Species'],
         'from_schema': 'http://xmlns.com/foaf/0.1/',
         'name': 'depiction',
         'owner': 'Species',
         'range': 'string',
         'slot_uri': 'foaf:depiction'} })
    inEggGroup: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'inEggGroup',
         'domain': 'Species',
         'domain_of': ['Species'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'multivalued': True,
         'name': 'inEggGroup',
         'owner': 'Species',
         'range': 'EggGroup',
         'required': False,
         'slot_uri': 'pokemon:inEggGroup'} })
    hasType: Optional[list[Type]] = Field(default=None, description="""A Pokemon has a type""", json_schema_extra = { "linkml_meta": {'alias': 'hasType',
         'description': 'A Pokemon has a type',
         'domain_of': ['Species', 'Move'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'inlined_as_list': True,
         'multivalued': True,
         'name': 'hasType',
         'owner': 'Species',
         'range': 'Type',
         'required': False,
         'slot_uri': 'pokemon:hasType'} })
    hasShape: Optional[str] = Field(default=None, description="""The shape of a berry is a measure of how good it  is for making a Potion.""", json_schema_extra = { "linkml_meta": {'alias': 'hasShape',
         'description': 'The shape of a berry is a measure of how good it  is for '
                        'making a Potion.',
         'domain': 'Species',
         'domain_of': ['Species'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'multivalued': False,
         'name': 'hasShape',
         'owner': 'Species',
         'range': 'Shape',
         'required': False,
         'slot_uri': 'pokemon:hasShape'} })
    hasGenus: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'hasGenus',
         'domain': 'Species',
         'domain_of': ['Species'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'name': 'hasGenus',
         'owner': 'Species',
         'range': 'string'} })
    hasCatchRate: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'hasCatchRate',
         'domain': 'Species',
         'domain_of': ['Species'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'multivalued': False,
         'name': 'hasCatchRate',
         'owner': 'Species',
         'range': 'integer',
         'required': False,
         'slot_uri': 'pokemon:hasCatchRate'} })
    foundIn: Optional[list[str]] = Field(default=None, description="""A place is found in a location""", json_schema_extra = { "linkml_meta": {'alias': 'foundIn',
         'description': 'A place is found in a location',
         'domain': 'Species',
         'domain_of': ['Species'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'multivalued': True,
         'name': 'foundIn',
         'owner': 'Species',
         'range': 'Habitat',
         'required': False,
         'slot_uri': 'pokemon:foundIn'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'Species',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'Species',
         'range': 'string',
         'required': True,
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'Species',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class Move(Thing):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'A move is a special ability of a '
                                                   'Pokemon.'}},
         'class_uri': 'pokemon:Move',
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'Thing',
         'name': 'Move',
         'slots': ['effectDescription', 'hasType']})

    effectDescription: Optional[list[str]] = Field(default=None, description="""A description of the effect of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'effectDescription',
         'description': 'A description of the effect of the entity',
         'domain_of': ['Ability', 'Move'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'multivalued': True,
         'name': 'effectDescription',
         'owner': 'Move',
         'range': 'string',
         'required': False,
         'slot_uri': 'pokemon:effectDescription'} })
    hasType: Optional[list[Type]] = Field(default=None, description="""A Pokemon has a type""", json_schema_extra = { "linkml_meta": {'alias': 'hasType',
         'description': 'A Pokemon has a type',
         'domain_of': ['Species', 'Move'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'inlined': True,
         'inlined_as_list': True,
         'multivalued': True,
         'name': 'hasType',
         'owner': 'Move',
         'range': 'Type',
         'required': False,
         'slot_uri': 'pokemon:hasType'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'Move',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'Move',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'Move',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class MoveLearning(ConfiguredBaseModel):
    """
    A move learning is a way that a Pokemon can learn a move.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'A move learning is a way that a Pokemon can learn a move.',
         'from_schema': 'https://pokemonkg.org/ontology',
         'name': 'MoveLearning'})

    pass


class LearningByLevelingUp(MoveLearning):
    """
    A move that is learned by leveling up.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'A move that is learned by leveling up.',
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'MoveLearning',
         'name': 'LearningByLevelingUp'})

    pass


class LearningThroughBreeding(MoveLearning):
    """
    A move that is learned by breeding.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'A move that is learned by breeding.',
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'MoveLearning',
         'name': 'LearningThroughBreeding'})

    pass


class Medicine(Item):
    """
    Medicine items can heal various afflictions of a Pokemon.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'Medicine items can heal various afflictions of a Pokemon.',
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'Item',
         'name': 'Medicine'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'Medicine',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'Medicine',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'Medicine',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class SpecialMove(Move):
    """
    A special move is a type of move that can be used during battles.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'A special move is a type of move that can be used during '
                        'battles.',
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'Move',
         'name': 'SpecialMove'})

    effectDescription: Optional[list[str]] = Field(default=None, description="""A description of the effect of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'effectDescription',
         'description': 'A description of the effect of the entity',
         'domain_of': ['Ability', 'Move'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'multivalued': True,
         'name': 'effectDescription',
         'owner': 'SpecialMove',
         'range': 'string',
         'required': False,
         'slot_uri': 'pokemon:effectDescription'} })
    hasType: Optional[list[Type]] = Field(default=None, description="""A Pokemon has a type""", json_schema_extra = { "linkml_meta": {'alias': 'hasType',
         'description': 'A Pokemon has a type',
         'domain_of': ['Species', 'Move'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'inlined': True,
         'inlined_as_list': True,
         'multivalued': True,
         'name': 'hasType',
         'owner': 'SpecialMove',
         'range': 'Type',
         'required': False,
         'slot_uri': 'pokemon:hasType'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'SpecialMove',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'SpecialMove',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'SpecialMove',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class PhysicalMove(Move):
    """
    A physical move is a type of move that can be used during battles.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'A physical move is a type of move that can be used during '
                        'battles.',
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'Move',
         'name': 'PhysicalMove'})

    effectDescription: Optional[list[str]] = Field(default=None, description="""A description of the effect of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'effectDescription',
         'description': 'A description of the effect of the entity',
         'domain_of': ['Ability', 'Move'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'multivalued': True,
         'name': 'effectDescription',
         'owner': 'PhysicalMove',
         'range': 'string',
         'required': False,
         'slot_uri': 'pokemon:effectDescription'} })
    hasType: Optional[list[Type]] = Field(default=None, description="""A Pokemon has a type""", json_schema_extra = { "linkml_meta": {'alias': 'hasType',
         'description': 'A Pokemon has a type',
         'domain_of': ['Species', 'Move'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'inlined': True,
         'inlined_as_list': True,
         'multivalued': True,
         'name': 'hasType',
         'owner': 'PhysicalMove',
         'range': 'Type',
         'required': False,
         'slot_uri': 'pokemon:hasType'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'PhysicalMove',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'PhysicalMove',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'PhysicalMove',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class StatusMove(Move):
    """
    A status move is a type of move that can be used during battles.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'A status move is a type of move that can be used during '
                        'battles.',
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'Move',
         'name': 'StatusMove'})

    effectDescription: Optional[list[str]] = Field(default=None, description="""A description of the effect of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'effectDescription',
         'description': 'A description of the effect of the entity',
         'domain_of': ['Ability', 'Move'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'multivalued': True,
         'name': 'effectDescription',
         'owner': 'StatusMove',
         'range': 'string',
         'required': False,
         'slot_uri': 'pokemon:effectDescription'} })
    hasType: Optional[list[Type]] = Field(default=None, description="""A Pokemon has a type""", json_schema_extra = { "linkml_meta": {'alias': 'hasType',
         'description': 'A Pokemon has a type',
         'domain_of': ['Species', 'Move'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'inlined': True,
         'inlined_as_list': True,
         'multivalued': True,
         'name': 'hasType',
         'owner': 'StatusMove',
         'range': 'Type',
         'required': False,
         'slot_uri': 'pokemon:hasType'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'StatusMove',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'StatusMove',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'StatusMove',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class TM(MoveLearning, Item):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'A Technical Machine is an item '
                                                   'that can be used to teach a '
                                                   'Pokemon a move.'}},
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'Item',
         'mixins': ['MoveLearning'],
         'name': 'TM'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'TM',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'TM',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'TM',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class Town(Place):
    """
    A town is a type of place that can be visited.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'A town is a type of place that can be visited.',
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'Place',
         'name': 'Town'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'Town',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'Town',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'Town',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class Trainer(Person):
    """
    A trainer is a person who is able to catch Pokemon.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'A trainer is a person who is able to catch Pokemon.',
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'Person',
         'name': 'Trainer'})

    depiction: Optional[str] = Field(default=None, description="""A depiction of the person""", json_schema_extra = { "linkml_meta": {'alias': 'depiction',
         'description': 'A depiction of the person',
         'domain_of': ['Person', 'Species'],
         'from_schema': 'http://xmlns.com/foaf/0.1/',
         'name': 'depiction',
         'owner': 'Trainer',
         'range': 'string',
         'slot_uri': 'foaf:depiction'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'Trainer',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'Trainer',
         'range': 'string',
         'required': True,
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'Trainer',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


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
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'Trainer',
         'name': 'GymLeader'})

    depiction: Optional[str] = Field(default=None, description="""A depiction of the person""", json_schema_extra = { "linkml_meta": {'alias': 'depiction',
         'description': 'A depiction of the person',
         'domain_of': ['Person', 'Species'],
         'from_schema': 'http://xmlns.com/foaf/0.1/',
         'name': 'depiction',
         'owner': 'GymLeader',
         'range': 'string',
         'slot_uri': 'foaf:depiction'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'GymLeader',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'GymLeader',
         'range': 'string',
         'required': True,
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'GymLeader',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class Type(NamedThing):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'rdfs:comment': {'tag': 'rdfs:comment',
                                          'value': 'All Pokemon creatures and their '
                                                   'moves are assigned certain types. '
                                                   'Each type has several strengths '
                                                   'and weaknesses in both attack and '
                                                   'defense.'}},
         'class_uri': 'pokemon:Type',
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'NamedThing',
         'name': 'Type'})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'Type',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'Type',
         'range': 'string',
         'required': True,
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'Type',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Thing.model_rebuild()
NamedThing.model_rebuild()
Person.model_rebuild()
Colour.model_rebuild()
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

