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
                                                      'Pokémon world as it is '
                                                      'presented in games and '
                                                      'anime television series.'},
                     'dcterms:issued': {'tag': 'dcterms:issued',
                                        'value': '2019-07-27^^xsd:date'}},
     'classes': {'Ability': {'class_uri': 'pokemon:Ability',
                             'description': 'Abilities were introduced in '
                                            'Generation III as an all new game '
                                            'mechanic. Each and every Pokémon has '
                                            'an ability, and can only have one at '
                                            'a time. Some abilities are exclusive '
                                            'to certain Pokémon and Evolution '
                                            'lines, while others are known by many '
                                            'Pokémon.',
                             'from_schema': 'https://pokemonkg.org/ontology',
                             'is_a': 'Thing',
                             'name': 'Ability',
                             'slots': ['effectDescription']},
                 'BattleItem': {'description': 'Battle items are items that can be '
                                               'used during battles.',
                                'from_schema': 'https://pokemonkg.org/ontology',
                                'is_a': 'Item',
                                'name': 'BattleItem'},
                 'Berry': {'description': 'Berries are small, juicy, fleshy fruit. '
                                          'As in the real world, a large variety '
                                          'exists in the Pokémon world, with a '
                                          'large range of flavors, names, and '
                                          'effects. First found in the Generation '
                                          'II games, many Berries have since '
                                          'became critical help items in battle, '
                                          'where their various effects include HP '
                                          'and status condition restoration, stat '
                                          'enhancement, and even damage negation.',
                           'from_schema': 'https://pokemonkg.org/ontology',
                           'is_a': 'Food',
                           'name': 'Berry',
                           'slots': ['hasSize']},
                 'EggGroup': {'description': 'Egg group is a category that '
                                             'determines which Pokémon are able to '
                                             'interbreed. The concept was '
                                             'introduced in Generation II, along '
                                             'with breeding. Similar to types, a '
                                             'Pokémon may belong to either one or '
                                             'two egg groups.',
                              'from_schema': 'https://pokemonkg.org/ontology',
                              'is_a': 'NamedIndividual',
                              'name': 'EggGroup'},
                 'Flavor': {'description': 'Flavor is a special set of attributes '
                                           'that certain foods in the Pokémon '
                                           'world have. Most of the foods can have '
                                           'more than one flavor, and the flavor '
                                           'determines which Pokémon can eat them.',
                            'from_schema': 'https://pokemonkg.org/ontology',
                            'is_a': 'NamedIndividual',
                            'name': 'Flavor'},
                 'Food': {'description': 'Food items are consumable items in the '
                                         'Pokémon world that can have flavors, '
                                         'firmness, and smoothness attributes.',
                          'from_schema': 'https://pokemonkg.org/ontology',
                          'is_a': 'Item',
                          'name': 'Food',
                          'slots': ['hasFlavor', 'firmness', 'smoothness']},
                 'Game': {'description': 'A game is a type of media that can be '
                                         'played by people.',
                          'from_schema': 'https://pokemonkg.org/ontology',
                          'is_a': 'Thing',
                          'name': 'Game'},
                 'Generation': {'description': 'Generations refers to the Pokémon '
                                               'game series. It is a group of '
                                               'games that were released at or '
                                               'around the same time. It also '
                                               'means that games in the same '
                                               'generation are compatible with the '
                                               'others, containing the same '
                                               'Pokémon and the number of moves '
                                               'there are to be learned.',
                                'from_schema': 'https://pokemonkg.org/ontology',
                                'is_a': 'Thing',
                                'name': 'Generation',
                                'slots': ['featuresSpecies']},
                 'Gym': {'description': 'A gym is a location that can be battled '
                                        'at.',
                         'from_schema': 'https://pokemonkg.org/ontology',
                         'is_a': 'Place',
                         'name': 'Gym'},
                 'GymLeader': {'description': 'A gym leader is the highest ranking '
                                              'member and owner of an official '
                                              'Pokémon gym. Gym leaders use their '
                                              'gym and their Pokémon to test the '
                                              'skills of trainers that challenge '
                                              'them, and if said trainers win a '
                                              'battle, the gym leader will gift '
                                              "them a badge that's unique to that "
                                              'specific gym.',
                               'from_schema': 'https://pokemonkg.org/ontology',
                               'is_a': 'Trainer',
                               'name': 'GymLeader'},
                 'HM': {'description': 'Hidden Machine',
                        'from_schema': 'https://pokemonkg.org/ontology',
                        'is_a': 'Item',
                        'name': 'HM'},
                 'Habitat': {'description': 'A habitat is a type of environment '
                                            'that certain Pokémon belong to.',
                             'from_schema': 'https://pokemonkg.org/ontology',
                             'is_a': 'NamedIndividual',
                             'name': 'Habitat'},
                 'HoldItem': {'description': 'A hold item is an item that can be '
                                             'held by a Pokémon.',
                              'from_schema': 'https://pokemonkg.org/ontology',
                              'is_a': 'Item',
                              'name': 'HoldItem'},
                 'Item': {'description': 'An item is an object in the Pokémon '
                                         'games which the player can pick up, keep '
                                         'in their Bag, and use in some manner. '
                                         'They have various uses, including '
                                         'healing, powering up, helping one to '
                                         'catch Pokémon, or to access a new area.',
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
                                             'afflictions of a Pokémon.',
                              'from_schema': 'https://pokemonkg.org/ontology',
                              'is_a': 'Item',
                              'name': 'Medicine'},
                 'Move': {'class_uri': 'pokemon:Move',
                          'description': 'A move is a special ability of a '
                                         'Pokémon.',
                          'from_schema': 'https://pokemonkg.org/ontology',
                          'is_a': 'Thing',
                          'name': 'Move',
                          'slots': ['effectDescription', 'hasType']},
                 'MoveLearning': {'description': 'A move learning is a way that a '
                                                 'Pokémon can learn a move.',
                                  'from_schema': 'https://pokemonkg.org/ontology',
                                  'name': 'MoveLearning'},
                 'PhysicalMove': {'description': 'A physical move is a type of '
                                                 'move that can be used during '
                                                 'battles.',
                                  'from_schema': 'https://pokemonkg.org/ontology',
                                  'is_a': 'Move',
                                  'name': 'PhysicalMove'},
                 'Place': {'abstract': True,
                           'description': 'Entities that have a somewhat fixed, '
                                          'physical extension.',
                           'from_schema': 'https://pokemonkg.org/ontology',
                           'is_a': 'Thing',
                           'name': 'Place'},
                 'Pokeball': {'class_uri': 'https://pokemonkg.org/ontology#Pok%C3%A9ball',
                              'description': 'A Poké Ball is a type of item that '
                                             "is critical to a Trainer's quest, "
                                             'used for catching and storing '
                                             'Pokémon.',
                              'from_schema': 'https://pokemonkg.org/ontology',
                              'is_a': 'Item',
                              'name': 'Pokeball'},
                 'Pokedex': {'class_uri': 'https://pokemonkg.org/ontology#Pok%C3%A9dex',
                             'description': 'The Pokédex is an electronic device '
                                            'designed to catalog and provide '
                                            'information regarding the various '
                                            'species of Pokémon featured in the '
                                            'Pokémon video game, anime and manga '
                                            'series.',
                             'from_schema': 'https://pokemonkg.org/ontology',
                             'is_a': 'Thing',
                             'name': 'Pokedex'},
                 'PokedexEntry': {'class_uri': 'https://pokemonkg.org/ontology#Pok%C3%A9dexEntry',
                                  'description': 'A Pokédex entry is a description '
                                                 'of a Pokémon.',
                                  'from_schema': 'https://pokemonkg.org/ontology',
                                  'is_a': 'Thing',
                                  'name': 'PokedexEntry'},
                 'Pokemon': {'annotations': {'rdfs:seeAlso': {'tag': 'rdfs:seeAlso',
                                                              'value': '<https://dbpedia.org/resource/Pokémon>'}},
                             'class_uri': 'https://pokemonkg.org/ontology#Pok%C3%A9mon',
                             'description': 'A Pokémon',
                             'from_schema': 'https://pokemonkg.org/ontology',
                             'name': 'Pokemon',
                             'union_of': ['Pokedex', 'Type']},
                 'Region': {'description': 'Regions are areas in the Pokémon '
                                           'universe that are smaller parts of a '
                                           'nation.',
                            'from_schema': 'https://pokemonkg.org/ontology',
                            'is_a': 'Place',
                            'name': 'Region'},
                 'Shape': {'description': 'Shapes are categories that certain '
                                          'Pokémon belong to, which determine '
                                          'which Pokémon they can breed with.',
                           'from_schema': 'https://pokemonkg.org/ontology',
                           'is_a': 'NamedIndividual',
                           'name': 'Shape'},
                 'SpecialMove': {'description': 'A special move is a type of move '
                                                'that can be used during battles.',
                                 'from_schema': 'https://pokemonkg.org/ontology',
                                 'is_a': 'Move',
                                 'name': 'SpecialMove'},
                 'Species': {'class_uri': 'pokemon:Species',
                             'description': 'A species is a category of Pokémon '
                                            'that share common features.',
                             'from_schema': 'https://pokemonkg.org/ontology',
                             'is_a': 'NamedIndividual',
                             'name': 'Species',
                             'slots': ['hasColor',
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
                                       'foundIn',
                                       'evolvesFrom',
                                       'evolvesTo']},
                 'StatusMove': {'description': 'A status move is a type of move '
                                               'that can be used during battles.',
                                'from_schema': 'https://pokemonkg.org/ontology',
                                'is_a': 'Move',
                                'name': 'StatusMove'},
                 'TM': {'description': 'A Technical Machine is an item that can be '
                                       'used to teach a Pokémon a move.',
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
                                            'catch Pokémon.',
                             'from_schema': 'https://pokemonkg.org/ontology',
                             'is_a': 'Person',
                             'name': 'Trainer'},
                 'Type': {'class_uri': 'pokemon:Type',
                          'description': 'All Pokémon creatures and their moves '
                                         'are assigned certain types. Each type '
                                         'has several strengths and weaknesses in '
                                         'both attack and defense.',
                          'from_schema': 'https://pokemonkg.org/ontology',
                          'is_a': 'NamedIndividual',
                          'name': 'Type'}},
     'created_on': '2019-07-27T00:00:00',
     'default_prefix': 'pokemon',
     'default_range': 'string',
     'description': 'Ontology covering the Pokémon world as it is presented in '
                    'games and anime television series',
     'enums': {'HabitatEnum': {'from_schema': 'https://pokemonkg.org/ontology',
                               'implements': ['owl:NamedIndividual'],
                               'name': 'HabitatEnum',
                               'permissible_values': {'Cave': {'description': 'A '
                                                                              'hollow '
                                                                              'underground '
                                                                              'area, '
                                                                              'typically '
                                                                              'formed '
                                                                              'in '
                                                                              'rocky '
                                                                              'or '
                                                                              'mountainous '
                                                                              'terrain.',
                                                               'meaning': 'pokemon:Habitat_Cave',
                                                               'text': 'Cave'},
                                                      'Forest': {'description': 'A '
                                                                                'dense '
                                                                                'area '
                                                                                'covered '
                                                                                'with '
                                                                                'trees '
                                                                                'and '
                                                                                'undergrowth.',
                                                                 'meaning': 'pokemon:Habitat_Forest',
                                                                 'text': 'Forest'},
                                                      'Grassland': {'description': 'An '
                                                                                   'open '
                                                                                   'area '
                                                                                   'of '
                                                                                   'land '
                                                                                   'covered '
                                                                                   'predominantly '
                                                                                   'with '
                                                                                   'grasses '
                                                                                   'and '
                                                                                   'low '
                                                                                   'vegetation.',
                                                                    'meaning': 'pokemon:Habitat_Grassland',
                                                                    'text': 'Grassland'},
                                                      'Mountain': {'description': 'A '
                                                                                  'large '
                                                                                  'elevated '
                                                                                  'landform '
                                                                                  'rising '
                                                                                  'steeply '
                                                                                  'above '
                                                                                  'the '
                                                                                  'surrounding '
                                                                                  'terrain.',
                                                                   'meaning': 'pokemon:Habitat_Mountain',
                                                                   'text': 'Mountain'},
                                                      'Rare': {'description': 'An '
                                                                              'uncommon '
                                                                              'or '
                                                                              'hard-to-reach '
                                                                              'environment '
                                                                              'with '
                                                                              'no '
                                                                              'single '
                                                                              'fixed '
                                                                              'location.',
                                                               'meaning': 'pokemon:Habitat_Rare',
                                                               'text': 'Rare'},
                                                      'Rough terrain': {'description': 'Harsh, '
                                                                                       'uneven '
                                                                                       'landscape '
                                                                                       'such '
                                                                                       'as '
                                                                                       'deserts, '
                                                                                       'volcanic '
                                                                                       'areas, '
                                                                                       'or '
                                                                                       'rocky '
                                                                                       'wastelands.',
                                                                        'meaning': 'pokemon:Habitat_RoughTerrain',
                                                                        'text': 'Rough '
                                                                                'terrain'},
                                                      'Sea': {'description': 'Open '
                                                                             'deep '
                                                                             'water '
                                                                             'far '
                                                                             'from '
                                                                             'shore, '
                                                                             'including '
                                                                             'oceans '
                                                                             'and '
                                                                             'large '
                                                                             'lakes.',
                                                              'meaning': 'pokemon:Habitat_Sea',
                                                              'text': 'Sea'},
                                                      'Urban': {'description': 'A '
                                                                               'densely '
                                                                               'developed '
                                                                               'area '
                                                                               'with '
                                                                               'buildings, '
                                                                               'roads, '
                                                                               'and '
                                                                               'other '
                                                                               'human-made '
                                                                               'structures.',
                                                                'meaning': 'pokemon:Habitat_Urban',
                                                                'text': 'Urban'},
                                                      "Water's edge": {'description': 'The '
                                                                                      'transitional '
                                                                                      'zone '
                                                                                      'where '
                                                                                      'land '
                                                                                      'meets '
                                                                                      'water, '
                                                                                      'including '
                                                                                      'shorelines, '
                                                                                      'riverbanks, '
                                                                                      'and '
                                                                                      'wetlands.',
                                                                       'meaning': 'pokemon:Habitat_WatersEdge',
                                                                       'text': "Water's "
                                                                               'edge'}}}},
     'id': 'https://pokemonkg.org/ontology',
     'imports': ['linkml:types', './foaf', './dbpedia', './owl', './qudt'],
     'license': 'MIT',
     'metamodel_version': '1.7.0',
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
                  'skos': {'prefix_prefix': 'skos',
                           'prefix_reference': 'http://www.w3.org/2004/02/skos/core#'},
                  'xml': {'prefix_prefix': 'xml',
                          'prefix_reference': 'http://www.w3.org/XML/1998/namespace'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['https://vladistan.github.io/linkml-pokemon'],
     'slots': {'accuracy': {'description': 'Chance of a move successfully hitting '
                                           'the target, as a percentage.',
                            'domain': 'Move',
                            'from_schema': 'https://pokemonkg.org/ontology',
                            'name': 'accuracy',
                            'range': 'integer'},
               'basePower': {'description': 'Base damage output of a move before '
                                            'applying type effectiveness and stat '
                                            'modifiers.',
                             'domain': 'Move',
                             'from_schema': 'https://pokemonkg.org/ontology',
                             'name': 'basePower',
                             'range': 'integer'},
               'basePowerPoints': {'description': 'Starting number of times a move '
                                                  'can be used before needing '
                                                  'restoration.',
                                   'domain': 'Move',
                                   'from_schema': 'https://pokemonkg.org/ontology',
                                   'name': 'basePowerPoints',
                                   'range': 'integer'},
               'containsPlace': {'asymmetric': True,
                                 'description': 'A place is contained to some '
                                                'extent in this place.',
                                 'domain': 'Place',
                                 'from_schema': 'https://pokemonkg.org/ontology',
                                 'inverse': 'locatedIn',
                                 'multivalued': True,
                                 'name': 'containsPlace',
                                 'range': 'Place',
                                 'required': False,
                                 'slot_uri': 'pokemon:contains_place',
                                 'transitive': True},
               'describedInPokedex': {'description': "['A Pokédex entry is "
                                                     "described in a Pokédex']",
                                      'domain': 'Species',
                                      'from_schema': 'https://pokemonkg.org/ontology',
                                      'inverse': 'describesPokemon',
                                      'multivalued': True,
                                      'name': 'describedInPokedex',
                                      'range': 'PokedexEntry',
                                      'required': False,
                                      'slot_uri': 'https://pokemonkg.org/ontology#describedInPok%C3%A9dex'},
               'describesPokemon': {'description': 'A Pokémon that is described by '
                                                   'this Pokédex entry.',
                                    'domain': 'PokedexEntry',
                                    'from_schema': 'https://pokemonkg.org/ontology',
                                    'multivalued': True,
                                    'name': 'describesPokemon',
                                    'range': 'Species',
                                    'required': False,
                                    'slot_uri': 'https://pokemonkg.org/ontology#describesPok%C3%A9mon'},
               'effectDescription': {'description': 'A description of the effect '
                                                    'of the entity',
                                     'domain_of': ['Ability', 'Move'],
                                     'from_schema': 'https://pokemonkg.org/ontology',
                                     'multivalued': True,
                                     'name': 'effectDescription',
                                     'range': 'string',
                                     'required': False,
                                     'slot_uri': 'pokemon:effectDescription'},
               'entryNumber': {'description': 'The unique number identifying this '
                                              'entry within a Pokédex.',
                               'domain': 'PokedexEntry',
                               'from_schema': 'https://pokemonkg.org/ontology',
                               'name': 'entryNumber',
                               'range': 'integer'},
               'evolvesFrom': {'description': 'This species evolves the other '
                                              'species.',
                               'domain': 'Species',
                               'domain_of': ['Species'],
                               'from_schema': 'https://pokemonkg.org/ontology',
                               'inlined': True,
                               'inverse': 'evolvesTo',
                               'multivalued': False,
                               'name': 'evolvesFrom',
                               'range': 'Species',
                               'required': False,
                               'slot_uri': 'pokemon:evolvesFrom'},
               'evolvesTo': {'description': 'A Pokémon evolves to another Pokémon.',
                             'domain': 'Species',
                             'domain_of': ['Species'],
                             'from_schema': 'https://pokemonkg.org/ontology',
                             'inlined': True,
                             'inlined_as_list': True,
                             'inverse': 'evolvesFrom',
                             'multivalued': True,
                             'name': 'evolvesTo',
                             'range': 'Species',
                             'required': False,
                             'slot_uri': 'pokemon:evolvesTo'},
               'featuresSpecies': {'description': "['A Pokédex entry features a "
                                                  "species']",
                                   'domain_of': ['Generation'],
                                   'from_schema': 'https://pokemonkg.org/ontology',
                                   'multivalued': True,
                                   'name': 'featuresSpecies',
                                   'range': 'Species',
                                   'required': False,
                                   'slot_uri': 'pokemon:featuresSpecies'},
               'firmness': {'description': 'How firm a berry or food item feels, '
                                           'affecting its use in Pokéblock or '
                                           'Poffin making.',
                            'domain': 'Food',
                            'domain_of': ['Food'],
                            'from_schema': 'https://pokemonkg.org/ontology',
                            'name': 'firmness',
                            'range': 'integer'},
               'foundIn': {'description': 'A place is found in a location',
                           'domain': 'Species',
                           'domain_of': ['Species'],
                           'from_schema': 'https://pokemonkg.org/ontology',
                           'inlined': True,
                           'inlined_as_list': True,
                           'multivalued': True,
                           'name': 'foundIn',
                           'range': 'Habitat',
                           'required': False,
                           'slot_uri': 'pokemon:foundIn'},
               'hasCatchRate': {'description': 'Determines how easy a Pokémon '
                                               'species is to catch, with higher '
                                               'values meaning easier capture.',
                                'domain': 'Species',
                                'domain_of': ['Species'],
                                'from_schema': 'https://pokemonkg.org/ontology',
                                'multivalued': False,
                                'name': 'hasCatchRate',
                                'range': 'integer',
                                'required': False,
                                'slot_uri': 'pokemon:hasCatchRate'},
               'hasColor': {'description': 'A Pokémon has a color',
                            'domain_of': ['Species'],
                            'from_schema': 'https://pokemonkg.org/ontology',
                            'inlined': True,
                            'multivalued': False,
                            'name': 'hasColor',
                            'range': 'Color',
                            'required': False,
                            'slot_uri': 'pokemon:hasColour'},
               'hasFlavor': {'description': 'A Pokémon has a flavor',
                             'domain': 'Food',
                             'domain_of': ['Food'],
                             'from_schema': 'https://pokemonkg.org/ontology',
                             'multivalued': True,
                             'name': 'hasFlavor',
                             'range': 'Flavor',
                             'required': False,
                             'slot_uri': 'pokemon:hasFlavor'},
               'hasGenus': {'description': 'The species category label shown in '
                                           'the Pokédex, such as "Seed Pokémon" '
                                           'for Bulbasaur.',
                            'domain': 'Species',
                            'domain_of': ['Species'],
                            'from_schema': 'https://pokemonkg.org/ontology',
                            'name': 'hasGenus',
                            'range': 'string'},
               'hasHeight': {'description': 'How tall a Pokémon species is, '
                                            'expressed as a quantity with unit.',
                             'domain': 'Species',
                             'domain_of': ['Species'],
                             'from_schema': 'https://pokemonkg.org/ontology',
                             'inlined': True,
                             'multivalued': False,
                             'name': 'hasHeight',
                             'range': 'Quantity',
                             'required': False,
                             'slot_uri': 'pokemon:hasHeight'},
               'hasPokedexEntry': {'description': 'A Pokédex entry in which this '
                                                  'Pokémon is described.',
                                   'domain': 'Pokedex',
                                   'from_schema': 'https://pokemonkg.org/ontology',
                                   'multivalued': True,
                                   'name': 'hasPokedexEntry',
                                   'range': 'PokedexEntry',
                                   'required': False,
                                   'slot_uri': 'https://pokemonkg.org/ontology#hasPok%C3%A9dexEntry'},
               'hasShape': {'description': 'The shape of a berry is a measure of '
                                           'how good it is for making a Potion.',
                            'domain': 'Species',
                            'domain_of': ['Species'],
                            'from_schema': 'https://pokemonkg.org/ontology',
                            'inlined': True,
                            'multivalued': False,
                            'name': 'hasShape',
                            'range': 'Shape',
                            'required': False,
                            'slot_uri': 'pokemon:hasShape'},
               'hasSize': {'description': 'The physical size of an entity, '
                                          'expressed as a quantity with unit.',
                           'domain_of': ['Berry'],
                           'from_schema': 'https://pokemonkg.org/ontology',
                           'inlined': True,
                           'multivalued': False,
                           'name': 'hasSize',
                           'range': 'Quantity',
                           'required': False,
                           'slot_uri': 'pokemon:hasSize'},
               'hasType': {'description': 'A Pokémon has a type',
                           'domain_of': ['Species', 'Move'],
                           'from_schema': 'https://pokemonkg.org/ontology',
                           'inlined': True,
                           'inlined_as_list': True,
                           'multivalued': True,
                           'name': 'hasType',
                           'range': 'Type',
                           'required': False,
                           'slot_uri': 'pokemon:hasType'},
               'hasWeight': {'description': 'How heavy a Pokémon species is, '
                                            'expressed as a quantity with unit.',
                             'domain': 'Species',
                             'domain_of': ['Species'],
                             'from_schema': 'https://pokemonkg.org/ontology',
                             'inlined': True,
                             'multivalued': False,
                             'name': 'hasWeight',
                             'range': 'Quantity',
                             'required': False,
                             'slot_uri': 'pokemon:hasWeight'},
               'inEggGroup': {'description': 'Which egg group a species belongs '
                                             'to, controlling which Pokémon can '
                                             'breed together.',
                              'domain': 'Species',
                              'domain_of': ['Species'],
                              'from_schema': 'https://pokemonkg.org/ontology',
                              'inlined': True,
                              'inlined_as_list': True,
                              'multivalued': True,
                              'name': 'inEggGroup',
                              'range': 'EggGroup',
                              'required': False,
                              'slot_uri': 'pokemon:inEggGroup'},
               'isAbleToApply': {'description': 'Moves that a Pokémon can use in '
                                                'battle or in the overworld.',
                                 'domain_of': ['Species'],
                                 'from_schema': 'https://pokemonkg.org/ontology',
                                 'inlined': True,
                                 'inlined_as_list': True,
                                 'multivalued': True,
                                 'name': 'isAbleToApply',
                                 'range': 'Move',
                                 'required': False,
                                 'slot_uri': 'pokemon:isAbleToApply'},
               'learnsMove': {'description': 'The move acquired through this '
                                             'particular learning method.',
                              'domain': 'MoveLearning',
                              'from_schema': 'https://pokemonkg.org/ontology',
                              'multivalued': True,
                              'name': 'learnsMove',
                              'range': 'Move',
                              'required': False,
                              'slot_uri': 'pokemon:learnsMove'},
               'locatedIn': {'asymmetric': True,
                             'description': 'This place is located to some extent '
                                            'in another place.',
                             'domain': 'Place',
                             'from_schema': 'https://pokemonkg.org/ontology',
                             'multivalued': True,
                             'name': 'locatedIn',
                             'range': 'Place',
                             'required': False,
                             'slot_uri': 'pokemon:locatedIn',
                             'transitive': True},
               'maxPowerPoints': {'description': 'Maximum times a move can be used '
                                                 'after PP-enhancing items are '
                                                 'applied.',
                                  'domain': 'Move',
                                  'from_schema': 'https://pokemonkg.org/ontology',
                                  'name': 'maxPowerPoints',
                                  'range': 'integer'},
               'mayHaveAbility': {'description': 'A Pokémon may have an ability',
                                  'domain': 'Species',
                                  'domain_of': ['Species'],
                                  'from_schema': 'https://pokemonkg.org/ontology',
                                  'inlined': True,
                                  'inlined_as_list': True,
                                  'multivalued': True,
                                  'name': 'mayHaveAbility',
                                  'range': 'Ability',
                                  'slot_uri': 'pokemon:mayHaveAbility'},
               'mayHaveHiddenAbility': {'description': 'A special ability only '
                                                       'obtainable through '
                                                       'specific encounters or '
                                                       'events, not through normal '
                                                       'gameplay.',
                                        'domain': 'Species',
                                        'domain_of': ['Species'],
                                        'from_schema': 'https://pokemonkg.org/ontology',
                                        'inlined': True,
                                        'inlined_as_list': True,
                                        'multivalued': True,
                                        'name': 'mayHaveHiddenAbility',
                                        'range': 'Ability',
                                        'slot_uri': 'pokemon:mayHaveHiddenAbility',
                                        'subproperty_of': 'mayHaveAbility'},
               'minLevelToLearn': {'description': 'The minimum level a Pokémon '
                                                  'needs to reach to learn this '
                                                  'move.',
                                   'from_schema': 'https://pokemonkg.org/ontology',
                                   'name': 'minLevelToLearn',
                                   'range': 'integer'},
               'smoothness': {'description': 'How smooth a berry or food item is, '
                                             'affecting its use in Pokéblock or '
                                             'Poffin making.',
                              'domain': 'Food',
                              'domain_of': ['Food'],
                              'from_schema': 'https://pokemonkg.org/ontology',
                              'name': 'smoothness',
                              'range': 'integer'}},
     'source_file': 'src/linkml_pokemon/schema/linkml_pokemon.yaml',
     'title': 'Pokémon Ontology'} )

class HabitatEnum(str, Enum):
    Cave = "Cave"
    """
    A hollow underground area, typically formed in rocky or mountainous terrain.
    """
    Forest = "Forest"
    """
    A dense area covered with trees and undergrowth.
    """
    Grassland = "Grassland"
    """
    An open area of land covered predominantly with grasses and low vegetation.
    """
    Mountain = "Mountain"
    """
    A large elevated landform rising steeply above the surrounding terrain.
    """
    Rare = "Rare"
    """
    An uncommon or hard-to-reach environment with no single fixed location.
    """
    Rough_terrain = "Rough terrain"
    """
    Harsh, uneven landscape such as deserts, volcanic areas, or rocky wastelands.
    """
    Sea = "Sea"
    """
    Open deep water far from shore, including oceans and large lakes.
    """
    Urban = "Urban"
    """
    A densely developed area with buildings, roads, and other human-made structures.
    """
    WaterAPOSTROPHEs_edge = "Water's edge"
    """
    The transitional zone where land meets water, including shorelines, riverbanks, and wetlands.
    """



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


class NamedIndividual(Thing):
    """
    A Thing that requires a name
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'owl:NamedIndividual',
         'description': 'A Thing that requires a name',
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'is_a': 'Thing',
         'name': 'NamedIndividual',
         'slot_usage': {'name': {'name': 'name', 'required': True}}})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'NamedIndividual',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'NamedIndividual',
         'range': 'string',
         'required': True,
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'NamedIndividual',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class Person(NamedIndividual):
    """
    A person is a human being
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'foaf:Person',
         'description': 'A person is a human being',
         'from_schema': 'http://xmlns.com/foaf/0.1/',
         'is_a': 'NamedIndividual',
         'name': 'Person',
         'slots': ['depiction']})

    depiction: Optional[list[Artwork]] = Field(default=None, description="""Visual artwork depicting this entity""", json_schema_extra = { "linkml_meta": {'alias': 'depiction',
         'description': 'Visual artwork depicting this entity',
         'domain_of': ['Person', 'Species'],
         'from_schema': 'http://xmlns.com/foaf/0.1/',
         'inlined_as_list': True,
         'inverse': 'depicts',
         'multivalued': True,
         'name': 'depiction',
         'owner': 'Person',
         'range': 'Artwork',
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


class Artwork(NamedIndividual):
    """
    A visual representation or artwork depicting an entity. In the Pokémon context, this includes official artwork, sprites, and other visual media.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'foaf:Image',
         'description': 'A visual representation or artwork depicting an entity. In '
                        'the Pokémon context, this includes official artwork, sprites, '
                        'and other visual media.',
         'from_schema': 'http://xmlns.com/foaf/0.1/',
         'is_a': 'NamedIndividual',
         'name': 'Artwork',
         'slots': ['depicts']})

    depicts: Optional[list[NamedIndividual]] = Field(default=None, description="""The entity depicted in this artwork""", json_schema_extra = { "linkml_meta": {'alias': 'depicts',
         'description': 'The entity depicted in this artwork',
         'domain_of': ['Artwork'],
         'from_schema': 'http://xmlns.com/foaf/0.1/',
         'inlined_as_list': True,
         'inverse': 'depiction',
         'multivalued': True,
         'name': 'depicts',
         'owner': 'Artwork',
         'range': 'NamedIndividual',
         'slot_uri': 'foaf:depicts'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'Artwork',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'Artwork',
         'range': 'string',
         'required': True,
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'Artwork',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class CmykColor(ConfiguredBaseModel):
    """
    CMYK color space coordinates (0-100).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'CMYK color space coordinates (0-100).',
         'from_schema': 'https://dbpedia.org/ontology/',
         'mixin': True,
         'name': 'CmykColor',
         'slots': ['cmykC', 'cmykM', 'cmykY', 'cmykK']})

    cmykC: Optional[int] = Field(default=None, description="""Cyan component in CMYK color model (0-100)""", json_schema_extra = { "linkml_meta": {'alias': 'cmykC',
         'description': 'Cyan component in CMYK color model (0-100)',
         'domain_of': ['CmykColor'],
         'from_schema': 'https://dbpedia.org/ontology/',
         'name': 'cmykC',
         'owner': 'CmykColor',
         'range': 'integer',
         'slot_uri': 'dbpedia:cmykCoordinateCyanic'} })
    cmykM: Optional[int] = Field(default=None, description="""Magenta component in CMYK color model (0-100)""", json_schema_extra = { "linkml_meta": {'alias': 'cmykM',
         'description': 'Magenta component in CMYK color model (0-100)',
         'domain_of': ['CmykColor'],
         'from_schema': 'https://dbpedia.org/ontology/',
         'name': 'cmykM',
         'owner': 'CmykColor',
         'range': 'integer',
         'slot_uri': 'dbpedia:cmykCoordinateMagenta'} })
    cmykY: Optional[int] = Field(default=None, description="""Yellow component in CMYK color model (0-100)""", json_schema_extra = { "linkml_meta": {'alias': 'cmykY',
         'description': 'Yellow component in CMYK color model (0-100)',
         'domain_of': ['CmykColor'],
         'from_schema': 'https://dbpedia.org/ontology/',
         'name': 'cmykY',
         'owner': 'CmykColor',
         'range': 'integer',
         'slot_uri': 'dbpedia:cmykCoordinateYellow'} })
    cmykK: Optional[int] = Field(default=None, description="""Black (K) component in CMYK color model (0-100)""", json_schema_extra = { "linkml_meta": {'alias': 'cmykK',
         'description': 'Black (K) component in CMYK color model (0-100)',
         'domain_of': ['CmykColor'],
         'from_schema': 'https://dbpedia.org/ontology/',
         'name': 'cmykK',
         'owner': 'CmykColor',
         'range': 'integer',
         'slot_uri': 'dbpedia:cmykCoordinateBlack'} })


class Color(CmykColor, Thing):
    """
    Color is the visual perceptual property corresponding in humans to the categories called red, yellow, blue and others.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'dbpedia:Colour',
         'description': 'Color is the visual perceptual property corresponding in '
                        'humans to the categories called red, yellow, blue and others.',
         'from_schema': 'https://dbpedia.org/ontology/',
         'is_a': 'Thing',
         'mixins': ['CmykColor'],
         'name': 'Color',
         'slots': ['wavelength',
                   'frequency',
                   'colorHexCode',
                   'connotation',
                   'thumbnail']})

    wavelength: Optional[float] = Field(default=None, description="""The wavelength of the color in meters (e.g., 4.5e-07 for blue)""", json_schema_extra = { "linkml_meta": {'alias': 'wavelength',
         'description': 'The wavelength of the color in meters (e.g., 4.5e-07 for '
                        'blue)',
         'domain_of': ['Color'],
         'from_schema': 'https://dbpedia.org/ontology/',
         'name': 'wavelength',
         'owner': 'Color',
         'range': 'float',
         'slot_uri': 'dbpedia:wavelength'} })
    frequency: Optional[float] = Field(default=None, description="""The frequency of the color in Hz""", json_schema_extra = { "linkml_meta": {'alias': 'frequency',
         'description': 'The frequency of the color in Hz',
         'domain_of': ['Color'],
         'from_schema': 'https://dbpedia.org/ontology/',
         'name': 'frequency',
         'owner': 'Color',
         'range': 'float',
         'slot_uri': 'dbpedia:frequency'} })
    colorHexCode: Optional[str] = Field(default=None, description="""Hexadecimal RGB color code (e.g., \"0000FF\" for blue)""", json_schema_extra = { "linkml_meta": {'alias': 'colorHexCode',
         'description': 'Hexadecimal RGB color code (e.g., "0000FF" for blue)',
         'domain_of': ['Color'],
         'from_schema': 'https://dbpedia.org/ontology/',
         'name': 'colorHexCode',
         'owner': 'Color',
         'range': 'string',
         'slot_uri': 'dbpedia:colourHexCode'} })
    connotation: Optional[list[str]] = Field(default=None, description="""Cultural or symbolic meanings associated with this color""", json_schema_extra = { "linkml_meta": {'alias': 'connotation',
         'description': 'Cultural or symbolic meanings associated with this color',
         'domain_of': ['Color'],
         'from_schema': 'https://dbpedia.org/ontology/',
         'inlined': False,
         'multivalued': True,
         'name': 'connotation',
         'owner': 'Color',
         'range': 'Connotation',
         'slot_uri': 'dbpedia:connotation'} })
    thumbnail: Optional[str] = Field(default=None, description="""URL to a representative image of this color""", json_schema_extra = { "linkml_meta": {'alias': 'thumbnail',
         'description': 'URL to a representative image of this color',
         'domain_of': ['Color'],
         'from_schema': 'https://dbpedia.org/ontology/',
         'name': 'thumbnail',
         'owner': 'Color',
         'range': 'uri',
         'slot_uri': 'dbpedia:thumbnail'} })
    cmykC: Optional[int] = Field(default=None, description="""Cyan component in CMYK color model (0-100)""", json_schema_extra = { "linkml_meta": {'alias': 'cmykC',
         'description': 'Cyan component in CMYK color model (0-100)',
         'domain_of': ['CmykColor'],
         'from_schema': 'https://dbpedia.org/ontology/',
         'name': 'cmykC',
         'owner': 'Color',
         'range': 'integer',
         'slot_uri': 'dbpedia:cmykCoordinateCyanic'} })
    cmykM: Optional[int] = Field(default=None, description="""Magenta component in CMYK color model (0-100)""", json_schema_extra = { "linkml_meta": {'alias': 'cmykM',
         'description': 'Magenta component in CMYK color model (0-100)',
         'domain_of': ['CmykColor'],
         'from_schema': 'https://dbpedia.org/ontology/',
         'name': 'cmykM',
         'owner': 'Color',
         'range': 'integer',
         'slot_uri': 'dbpedia:cmykCoordinateMagenta'} })
    cmykY: Optional[int] = Field(default=None, description="""Yellow component in CMYK color model (0-100)""", json_schema_extra = { "linkml_meta": {'alias': 'cmykY',
         'description': 'Yellow component in CMYK color model (0-100)',
         'domain_of': ['CmykColor'],
         'from_schema': 'https://dbpedia.org/ontology/',
         'name': 'cmykY',
         'owner': 'Color',
         'range': 'integer',
         'slot_uri': 'dbpedia:cmykCoordinateYellow'} })
    cmykK: Optional[int] = Field(default=None, description="""Black (K) component in CMYK color model (0-100)""", json_schema_extra = { "linkml_meta": {'alias': 'cmykK',
         'description': 'Black (K) component in CMYK color model (0-100)',
         'domain_of': ['CmykColor'],
         'from_schema': 'https://dbpedia.org/ontology/',
         'name': 'cmykK',
         'owner': 'Color',
         'range': 'integer',
         'slot_uri': 'dbpedia:cmykCoordinateBlack'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'Color',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'Color',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'Color',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class Connotation(Thing):
    """
    Cultural or symbolic meaning associated with a color. Imported from DBpedia as generic owl:Thing resources.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'owl:Thing',
         'description': 'Cultural or symbolic meaning associated with a color. '
                        'Imported from DBpedia as generic owl:Thing resources.',
         'from_schema': 'https://dbpedia.org/ontology/',
         'is_a': 'Thing',
         'name': 'Connotation',
         'slot_usage': {'name': {'name': 'name', 'required': True}}})

    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'Connotation',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: str = Field(default=..., description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'Connotation',
         'range': 'string',
         'required': True,
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'Connotation',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class Concept(Thing):
    """
    The root class for all QUDT concepts
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'qudt:Concept',
         'description': 'The root class for all QUDT concepts',
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'is_a': 'Thing',
         'name': 'Concept',
         'slots': ['abbreviation', 'deprecated', 'plainTextDescription']})

    abbreviation: Optional[str] = Field(default=None, description="""Short alphanumeric abbreviation for a unit""", json_schema_extra = { "linkml_meta": {'alias': 'abbreviation',
         'description': 'Short alphanumeric abbreviation for a unit',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'abbreviation',
         'owner': 'Concept',
         'range': 'string',
         'slot_uri': 'qudt:abbreviation'} })
    deprecated: Optional[bool] = Field(default=None, description="""Whether this entity is deprecated""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'description': 'Whether this entity is deprecated',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'deprecated',
         'owner': 'Concept',
         'range': 'boolean',
         'slot_uri': 'qudt:deprecated'} })
    plainTextDescription: Optional[str] = Field(default=None, description="""Plain text description""", json_schema_extra = { "linkml_meta": {'alias': 'plainTextDescription',
         'description': 'Plain text description',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'plainTextDescription',
         'owner': 'Concept',
         'range': 'string',
         'slot_uri': 'qudt:plainTextDescription'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'Concept',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'Concept',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'Concept',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class Aspect(ConfiguredBaseModel):
    """
    An abstract type class that defines properties that can be reused
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'qudt:Aspect',
         'description': 'An abstract type class that defines properties that can be '
                        'reused',
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'mixin': True,
         'name': 'Aspect'})

    pass


class Quantifiable(Aspect):
    """
    Ascribes to some thing the capability of being measured, observed, or counted
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Quantifiable',
         'description': 'Ascribes to some thing the capability of being measured, '
                        'observed, or counted',
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'is_a': 'Aspect',
         'mixin': True,
         'name': 'Quantifiable',
         'slots': ['hasUnit', 'standardUncertainty', 'relativeStandardUncertainty']})

    hasUnit: Optional[str] = Field(default=None, description="""Unit associated with a quantifiable entity""", json_schema_extra = { "linkml_meta": {'alias': 'hasUnit',
         'description': 'Unit associated with a quantifiable entity',
         'domain_of': ['Quantifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'hasUnit',
         'owner': 'Quantifiable',
         'range': 'Unit',
         'slot_uri': 'qudt:hasUnit'} })
    standardUncertainty: Optional[Decimal] = Field(default=None, description="""Standard uncertainty of the measurement""", json_schema_extra = { "linkml_meta": {'alias': 'standardUncertainty',
         'description': 'Standard uncertainty of the measurement',
         'domain_of': ['Quantifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'standardUncertainty',
         'owner': 'Quantifiable',
         'range': 'decimal',
         'slot_uri': 'qudt:standardUncertainty'} })
    relativeStandardUncertainty: Optional[float] = Field(default=None, description="""Relative standard uncertainty of the measurement""", json_schema_extra = { "linkml_meta": {'alias': 'relativeStandardUncertainty',
         'description': 'Relative standard uncertainty of the measurement',
         'domain_of': ['Quantifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'relativeStandardUncertainty',
         'owner': 'Quantifiable',
         'range': 'double',
         'slot_uri': 'qudt:relativeStandardUncertainty'} })


class Verifiable(Aspect):
    """
    Holds properties that provide external knowledge and specifications of a given resource
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Verifiable',
         'description': 'Holds properties that provide external knowledge and '
                        'specifications of a given resource',
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'is_a': 'Aspect',
         'mixin': True,
         'name': 'Verifiable',
         'slots': ['dbpediaMatch',
                   'wikidataMatch',
                   'informativeReference',
                   'isoNormativeReference',
                   'normativeReference']})

    dbpediaMatch: Optional[str] = Field(default=None, description="""DBpedia URI for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'dbpediaMatch',
         'description': 'DBpedia URI for this entity',
         'domain_of': ['Verifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dbpediaMatch',
         'owner': 'Verifiable',
         'range': 'uri',
         'slot_uri': 'qudt:dbpediaMatch'} })
    wikidataMatch: Optional[str] = Field(default=None, description="""Wikidata URI for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'wikidataMatch',
         'description': 'Wikidata URI for this entity',
         'domain_of': ['Verifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'wikidataMatch',
         'owner': 'Verifiable',
         'range': 'uri',
         'slot_uri': 'qudt:wikidataMatch'} })
    informativeReference: Optional[list[str]] = Field(default=None, description="""Informative reference URL""", json_schema_extra = { "linkml_meta": {'alias': 'informativeReference',
         'description': 'Informative reference URL',
         'domain_of': ['Verifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'multivalued': True,
         'name': 'informativeReference',
         'owner': 'Verifiable',
         'range': 'uri',
         'slot_uri': 'qudt:informativeReference'} })
    isoNormativeReference: Optional[list[str]] = Field(default=None, description="""ISO normative reference URI""", json_schema_extra = { "linkml_meta": {'alias': 'isoNormativeReference',
         'description': 'ISO normative reference URI',
         'domain_of': ['Verifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'multivalued': True,
         'name': 'isoNormativeReference',
         'owner': 'Verifiable',
         'range': 'uri',
         'slot_uri': 'qudt:isoNormativeReference'} })
    normativeReference: Optional[list[str]] = Field(default=None, description="""Normative reference URI""", json_schema_extra = { "linkml_meta": {'alias': 'normativeReference',
         'description': 'Normative reference URI',
         'domain_of': ['Verifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'multivalued': True,
         'name': 'normativeReference',
         'owner': 'Verifiable',
         'range': 'uri',
         'slot_uri': 'qudt:normativeReference'} })


class Quantity(Quantifiable, Concept):
    """
    A measured quantity with kind and value
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Quantity',
         'description': 'A measured quantity with kind and value',
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'is_a': 'Concept',
         'mixins': ['Quantifiable'],
         'name': 'Quantity',
         'slots': ['hasQuantityKind', 'quantityValue']})

    hasQuantityKind: Optional[list[QuantityKind]] = Field(default=None, description="""Associates a quantity with its kind (e.g., Height, Weight)""", json_schema_extra = { "linkml_meta": {'alias': 'hasQuantityKind',
         'description': 'Associates a quantity with its kind (e.g., Height, Weight)',
         'domain_of': ['Quantity', 'Unit'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'inlined_as_list': True,
         'multivalued': True,
         'name': 'hasQuantityKind',
         'owner': 'Quantity',
         'range': 'QuantityKind',
         'slot_uri': 'qudt:hasQuantityKind'} })
    quantityValue: Optional[list[QuantityValue]] = Field(default=None, description="""The value component of a quantity""", json_schema_extra = { "linkml_meta": {'alias': 'quantityValue',
         'description': 'The value component of a quantity',
         'domain_of': ['Quantity'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'inlined_as_list': True,
         'multivalued': True,
         'name': 'quantityValue',
         'owner': 'Quantity',
         'range': 'QuantityValue',
         'slot_uri': 'qudt:quantityValue'} })
    hasUnit: Optional[str] = Field(default=None, description="""Unit associated with a quantifiable entity""", json_schema_extra = { "linkml_meta": {'alias': 'hasUnit',
         'description': 'Unit associated with a quantifiable entity',
         'domain_of': ['Quantifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'hasUnit',
         'owner': 'Quantity',
         'range': 'Unit',
         'slot_uri': 'qudt:hasUnit'} })
    standardUncertainty: Optional[Decimal] = Field(default=None, description="""Standard uncertainty of the measurement""", json_schema_extra = { "linkml_meta": {'alias': 'standardUncertainty',
         'description': 'Standard uncertainty of the measurement',
         'domain_of': ['Quantifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'standardUncertainty',
         'owner': 'Quantity',
         'range': 'decimal',
         'slot_uri': 'qudt:standardUncertainty'} })
    relativeStandardUncertainty: Optional[float] = Field(default=None, description="""Relative standard uncertainty of the measurement""", json_schema_extra = { "linkml_meta": {'alias': 'relativeStandardUncertainty',
         'description': 'Relative standard uncertainty of the measurement',
         'domain_of': ['Quantifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'relativeStandardUncertainty',
         'owner': 'Quantity',
         'range': 'double',
         'slot_uri': 'qudt:relativeStandardUncertainty'} })
    abbreviation: Optional[str] = Field(default=None, description="""Short alphanumeric abbreviation for a unit""", json_schema_extra = { "linkml_meta": {'alias': 'abbreviation',
         'description': 'Short alphanumeric abbreviation for a unit',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'abbreviation',
         'owner': 'Quantity',
         'range': 'string',
         'slot_uri': 'qudt:abbreviation'} })
    deprecated: Optional[bool] = Field(default=None, description="""Whether this entity is deprecated""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'description': 'Whether this entity is deprecated',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'deprecated',
         'owner': 'Quantity',
         'range': 'boolean',
         'slot_uri': 'qudt:deprecated'} })
    plainTextDescription: Optional[str] = Field(default=None, description="""Plain text description""", json_schema_extra = { "linkml_meta": {'alias': 'plainTextDescription',
         'description': 'Plain text description',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'plainTextDescription',
         'owner': 'Quantity',
         'range': 'string',
         'slot_uri': 'qudt:plainTextDescription'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'Quantity',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'Quantity',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'Quantity',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class QuantityValue(Concept):
    """
    Numeric value with unit
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:QuantityValue',
         'description': 'Numeric value with unit',
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'is_a': 'Concept',
         'name': 'QuantityValue',
         'slots': ['numericValue', 'unit']})

    numericValue: Optional[float] = Field(default=None, description="""Numeric value of a quantity""", json_schema_extra = { "linkml_meta": {'alias': 'numericValue',
         'description': 'Numeric value of a quantity',
         'domain_of': ['QuantityValue'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'numericValue',
         'owner': 'QuantityValue',
         'range': 'double',
         'slot_uri': 'qudt:value'} })
    unit: Optional[Unit] = Field(default=None, description="""Unit of measurement""", json_schema_extra = { "linkml_meta": {'alias': 'unit',
         'description': 'Unit of measurement',
         'domain_of': ['QuantityValue'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'inlined': True,
         'name': 'unit',
         'owner': 'QuantityValue',
         'range': 'Unit',
         'slot_uri': 'qudt:unit'} })
    abbreviation: Optional[str] = Field(default=None, description="""Short alphanumeric abbreviation for a unit""", json_schema_extra = { "linkml_meta": {'alias': 'abbreviation',
         'description': 'Short alphanumeric abbreviation for a unit',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'abbreviation',
         'owner': 'QuantityValue',
         'range': 'string',
         'slot_uri': 'qudt:abbreviation'} })
    deprecated: Optional[bool] = Field(default=None, description="""Whether this entity is deprecated""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'description': 'Whether this entity is deprecated',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'deprecated',
         'owner': 'QuantityValue',
         'range': 'boolean',
         'slot_uri': 'qudt:deprecated'} })
    plainTextDescription: Optional[str] = Field(default=None, description="""Plain text description""", json_schema_extra = { "linkml_meta": {'alias': 'plainTextDescription',
         'description': 'Plain text description',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'plainTextDescription',
         'owner': 'QuantityValue',
         'range': 'string',
         'slot_uri': 'qudt:plainTextDescription'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'QuantityValue',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'QuantityValue',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'QuantityValue',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class AbstractQuantityKind(Concept):
    """
    Abstract base for quantity kinds, constraining symbol and broader
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'qudt:AbstractQuantityKind',
         'description': 'Abstract base for quantity kinds, constraining symbol and '
                        'broader',
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'is_a': 'Concept',
         'name': 'AbstractQuantityKind',
         'slots': ['symbol', 'broader']})

    symbol: Optional[str] = Field(default=None, description="""Symbol for a unit (e.g., \"m\" for meter)""", json_schema_extra = { "linkml_meta": {'alias': 'symbol',
         'description': 'Symbol for a unit (e.g., "m" for meter)',
         'domain_of': ['AbstractQuantityKind', 'Unit', 'Prefix'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'symbol',
         'owner': 'AbstractQuantityKind',
         'range': 'string',
         'slot_uri': 'qudt:symbol'} })
    broader: Optional[list[QuantityKind]] = Field(default=None, description="""Broader/parent quantity kind""", json_schema_extra = { "linkml_meta": {'alias': 'broader',
         'description': 'Broader/parent quantity kind',
         'domain_of': ['AbstractQuantityKind'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'inlined_as_list': True,
         'multivalued': True,
         'name': 'broader',
         'owner': 'AbstractQuantityKind',
         'range': 'QuantityKind',
         'slot_uri': 'skos:broader'} })
    abbreviation: Optional[str] = Field(default=None, description="""Short alphanumeric abbreviation for a unit""", json_schema_extra = { "linkml_meta": {'alias': 'abbreviation',
         'description': 'Short alphanumeric abbreviation for a unit',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'abbreviation',
         'owner': 'AbstractQuantityKind',
         'range': 'string',
         'slot_uri': 'qudt:abbreviation'} })
    deprecated: Optional[bool] = Field(default=None, description="""Whether this entity is deprecated""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'description': 'Whether this entity is deprecated',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'deprecated',
         'owner': 'AbstractQuantityKind',
         'range': 'boolean',
         'slot_uri': 'qudt:deprecated'} })
    plainTextDescription: Optional[str] = Field(default=None, description="""Plain text description""", json_schema_extra = { "linkml_meta": {'alias': 'plainTextDescription',
         'description': 'Plain text description',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'plainTextDescription',
         'owner': 'AbstractQuantityKind',
         'range': 'string',
         'slot_uri': 'qudt:plainTextDescription'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'AbstractQuantityKind',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'AbstractQuantityKind',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'AbstractQuantityKind',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class QuantityKind(AbstractQuantityKind, Verifiable):
    """
    Kind of quantity (e.g., Length, Mass, Height, Weight)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:QuantityKind',
         'description': 'Kind of quantity (e.g., Length, Mass, Height, Weight)',
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'is_a': 'AbstractQuantityKind',
         'mixins': ['Verifiable'],
         'name': 'QuantityKind',
         'slots': ['latexSymbol', 'hasDimensionVector', 'applicableUnit', 'exactMatch']})

    latexSymbol: Optional[str] = Field(default=None, description="""LaTeX representation of symbol""", json_schema_extra = { "linkml_meta": {'alias': 'latexSymbol',
         'description': 'LaTeX representation of symbol',
         'domain_of': ['QuantityKind', 'Unit', 'QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'latexSymbol',
         'owner': 'QuantityKind',
         'range': 'string',
         'slot_uri': 'qudt:latexSymbol'} })
    hasDimensionVector: Optional[str] = Field(default=None, description="""Dimension vector for a unit or quantity kind""", json_schema_extra = { "linkml_meta": {'alias': 'hasDimensionVector',
         'description': 'Dimension vector for a unit or quantity kind',
         'domain_of': ['QuantityKind', 'Unit'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'hasDimensionVector',
         'owner': 'QuantityKind',
         'range': 'QuantityKindDimensionVector',
         'slot_uri': 'qudt:hasDimensionVector'} })
    applicableUnit: Optional[list[str]] = Field(default=None, description="""Units applicable to a quantity kind""", json_schema_extra = { "linkml_meta": {'alias': 'applicableUnit',
         'description': 'Units applicable to a quantity kind',
         'domain_of': ['QuantityKind'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'multivalued': True,
         'name': 'applicableUnit',
         'owner': 'QuantityKind',
         'range': 'Unit',
         'slot_uri': 'qudt:applicableUnit'} })
    exactMatch: Optional[list[str]] = Field(default=None, description="""Equivalent quantity kind or unit""", json_schema_extra = { "linkml_meta": {'alias': 'exactMatch',
         'description': 'Equivalent quantity kind or unit',
         'domain_of': ['QuantityKind', 'Prefix'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'multivalued': True,
         'name': 'exactMatch',
         'owner': 'QuantityKind',
         'range': 'string',
         'slot_uri': 'skos:exactMatch'} })
    dbpediaMatch: Optional[str] = Field(default=None, description="""DBpedia URI for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'dbpediaMatch',
         'description': 'DBpedia URI for this entity',
         'domain_of': ['Verifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dbpediaMatch',
         'owner': 'QuantityKind',
         'range': 'uri',
         'slot_uri': 'qudt:dbpediaMatch'} })
    wikidataMatch: Optional[str] = Field(default=None, description="""Wikidata URI for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'wikidataMatch',
         'description': 'Wikidata URI for this entity',
         'domain_of': ['Verifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'wikidataMatch',
         'owner': 'QuantityKind',
         'range': 'uri',
         'slot_uri': 'qudt:wikidataMatch'} })
    informativeReference: Optional[list[str]] = Field(default=None, description="""Informative reference URL""", json_schema_extra = { "linkml_meta": {'alias': 'informativeReference',
         'description': 'Informative reference URL',
         'domain_of': ['Verifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'multivalued': True,
         'name': 'informativeReference',
         'owner': 'QuantityKind',
         'range': 'uri',
         'slot_uri': 'qudt:informativeReference'} })
    isoNormativeReference: Optional[list[str]] = Field(default=None, description="""ISO normative reference URI""", json_schema_extra = { "linkml_meta": {'alias': 'isoNormativeReference',
         'description': 'ISO normative reference URI',
         'domain_of': ['Verifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'multivalued': True,
         'name': 'isoNormativeReference',
         'owner': 'QuantityKind',
         'range': 'uri',
         'slot_uri': 'qudt:isoNormativeReference'} })
    normativeReference: Optional[list[str]] = Field(default=None, description="""Normative reference URI""", json_schema_extra = { "linkml_meta": {'alias': 'normativeReference',
         'description': 'Normative reference URI',
         'domain_of': ['Verifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'multivalued': True,
         'name': 'normativeReference',
         'owner': 'QuantityKind',
         'range': 'uri',
         'slot_uri': 'qudt:normativeReference'} })
    symbol: Optional[str] = Field(default=None, description="""Symbol for a unit (e.g., \"m\" for meter)""", json_schema_extra = { "linkml_meta": {'alias': 'symbol',
         'description': 'Symbol for a unit (e.g., "m" for meter)',
         'domain_of': ['AbstractQuantityKind', 'Unit', 'Prefix'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'symbol',
         'owner': 'QuantityKind',
         'range': 'string',
         'slot_uri': 'qudt:symbol'} })
    broader: Optional[list[QuantityKind]] = Field(default=None, description="""Broader/parent quantity kind""", json_schema_extra = { "linkml_meta": {'alias': 'broader',
         'description': 'Broader/parent quantity kind',
         'domain_of': ['AbstractQuantityKind'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'inlined': True,
         'inlined_as_list': True,
         'multivalued': True,
         'name': 'broader',
         'owner': 'QuantityKind',
         'range': 'QuantityKind',
         'slot_uri': 'skos:broader'} })
    abbreviation: Optional[str] = Field(default=None, description="""Short alphanumeric abbreviation for a unit""", json_schema_extra = { "linkml_meta": {'alias': 'abbreviation',
         'description': 'Short alphanumeric abbreviation for a unit',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'abbreviation',
         'owner': 'QuantityKind',
         'range': 'string',
         'slot_uri': 'qudt:abbreviation'} })
    deprecated: Optional[bool] = Field(default=None, description="""Whether this entity is deprecated""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'description': 'Whether this entity is deprecated',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'deprecated',
         'owner': 'QuantityKind',
         'range': 'boolean',
         'slot_uri': 'qudt:deprecated'} })
    plainTextDescription: Optional[str] = Field(default=None, description="""Plain text description""", json_schema_extra = { "linkml_meta": {'alias': 'plainTextDescription',
         'description': 'Plain text description',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'plainTextDescription',
         'owner': 'QuantityKind',
         'range': 'string',
         'slot_uri': 'qudt:plainTextDescription'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'QuantityKind',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'QuantityKind',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'QuantityKind',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class Unit(Verifiable, Concept):
    """
    Unit of measurement
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Unit',
         'description': 'Unit of measurement',
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'is_a': 'Concept',
         'mixins': ['Verifiable'],
         'name': 'Unit',
         'slots': ['symbol',
                   'latexSymbol',
                   'conversionMultiplier',
                   'conversionOffset',
                   'hasDimensionVector',
                   'hasQuantityKind',
                   'isUnitOfSystem',
                   'applicableSystem',
                   'prefix',
                   'scalingOf',
                   'ucumCode']})

    symbol: Optional[str] = Field(default=None, description="""Symbol for a unit (e.g., \"m\" for meter)""", json_schema_extra = { "linkml_meta": {'alias': 'symbol',
         'description': 'Symbol for a unit (e.g., "m" for meter)',
         'domain_of': ['AbstractQuantityKind', 'Unit', 'Prefix'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'symbol',
         'owner': 'Unit',
         'range': 'string',
         'slot_uri': 'qudt:symbol'} })
    latexSymbol: Optional[str] = Field(default=None, description="""LaTeX representation of symbol""", json_schema_extra = { "linkml_meta": {'alias': 'latexSymbol',
         'description': 'LaTeX representation of symbol',
         'domain_of': ['QuantityKind', 'Unit', 'QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'latexSymbol',
         'owner': 'Unit',
         'range': 'string',
         'slot_uri': 'qudt:latexSymbol'} })
    conversionMultiplier: Optional[float] = Field(default=None, description="""Multiplier to convert to base unit""", json_schema_extra = { "linkml_meta": {'alias': 'conversionMultiplier',
         'description': 'Multiplier to convert to base unit',
         'domain_of': ['Unit'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'conversionMultiplier',
         'owner': 'Unit',
         'range': 'double',
         'slot_uri': 'qudt:conversionMultiplier'} })
    conversionOffset: Optional[float] = Field(default=None, description="""Offset to convert to base unit""", json_schema_extra = { "linkml_meta": {'alias': 'conversionOffset',
         'description': 'Offset to convert to base unit',
         'domain_of': ['Unit'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'conversionOffset',
         'owner': 'Unit',
         'range': 'double',
         'slot_uri': 'qudt:conversionOffset'} })
    hasDimensionVector: Optional[str] = Field(default=None, description="""Dimension vector for a unit or quantity kind""", json_schema_extra = { "linkml_meta": {'alias': 'hasDimensionVector',
         'description': 'Dimension vector for a unit or quantity kind',
         'domain_of': ['QuantityKind', 'Unit'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'hasDimensionVector',
         'owner': 'Unit',
         'range': 'QuantityKindDimensionVector',
         'slot_uri': 'qudt:hasDimensionVector'} })
    hasQuantityKind: Optional[list[QuantityKind]] = Field(default=None, description="""Associates a quantity with its kind (e.g., Height, Weight)""", json_schema_extra = { "linkml_meta": {'alias': 'hasQuantityKind',
         'description': 'Associates a quantity with its kind (e.g., Height, Weight)',
         'domain_of': ['Quantity', 'Unit'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'inlined': True,
         'inlined_as_list': True,
         'multivalued': True,
         'name': 'hasQuantityKind',
         'owner': 'Unit',
         'range': 'QuantityKind',
         'slot_uri': 'qudt:hasQuantityKind'} })
    isUnitOfSystem: Optional[list[str]] = Field(default=None, description="""System of units this unit belongs to""", json_schema_extra = { "linkml_meta": {'alias': 'isUnitOfSystem',
         'description': 'System of units this unit belongs to',
         'domain_of': ['Unit'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'multivalued': True,
         'name': 'isUnitOfSystem',
         'owner': 'Unit',
         'range': 'SystemOfUnits',
         'slot_uri': 'qudt:isUnitOfSystem'} })
    applicableSystem: Optional[list[str]] = Field(default=None, description="""Systems where this unit is applicable""", json_schema_extra = { "linkml_meta": {'alias': 'applicableSystem',
         'description': 'Systems where this unit is applicable',
         'domain_of': ['Unit'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'multivalued': True,
         'name': 'applicableSystem',
         'owner': 'Unit',
         'range': 'SystemOfUnits',
         'slot_uri': 'qudt:applicableSystem'} })
    prefix: Optional[str] = Field(default=None, description="""Prefix for a unit (e.g., Kilo, Milli)""", json_schema_extra = { "linkml_meta": {'alias': 'prefix',
         'description': 'Prefix for a unit (e.g., Kilo, Milli)',
         'domain_of': ['Unit', 'SystemOfUnits'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'prefix',
         'owner': 'Unit',
         'range': 'Prefix',
         'slot_uri': 'qudt:prefix'} })
    scalingOf: Optional[str] = Field(default=None, description="""Base unit this unit is a scaling of""", json_schema_extra = { "linkml_meta": {'alias': 'scalingOf',
         'description': 'Base unit this unit is a scaling of',
         'domain_of': ['Unit'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'scalingOf',
         'owner': 'Unit',
         'range': 'Unit',
         'slot_uri': 'qudt:scalingOf'} })
    ucumCode: Optional[str] = Field(default=None, description="""UCUM code for the unit""", json_schema_extra = { "linkml_meta": {'alias': 'ucumCode',
         'description': 'UCUM code for the unit',
         'domain_of': ['Unit', 'Prefix'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'ucumCode',
         'owner': 'Unit',
         'range': 'string',
         'slot_uri': 'qudt:ucumCode'} })
    dbpediaMatch: Optional[str] = Field(default=None, description="""DBpedia URI for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'dbpediaMatch',
         'description': 'DBpedia URI for this entity',
         'domain_of': ['Verifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dbpediaMatch',
         'owner': 'Unit',
         'range': 'uri',
         'slot_uri': 'qudt:dbpediaMatch'} })
    wikidataMatch: Optional[str] = Field(default=None, description="""Wikidata URI for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'wikidataMatch',
         'description': 'Wikidata URI for this entity',
         'domain_of': ['Verifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'wikidataMatch',
         'owner': 'Unit',
         'range': 'uri',
         'slot_uri': 'qudt:wikidataMatch'} })
    informativeReference: Optional[list[str]] = Field(default=None, description="""Informative reference URL""", json_schema_extra = { "linkml_meta": {'alias': 'informativeReference',
         'description': 'Informative reference URL',
         'domain_of': ['Verifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'multivalued': True,
         'name': 'informativeReference',
         'owner': 'Unit',
         'range': 'uri',
         'slot_uri': 'qudt:informativeReference'} })
    isoNormativeReference: Optional[list[str]] = Field(default=None, description="""ISO normative reference URI""", json_schema_extra = { "linkml_meta": {'alias': 'isoNormativeReference',
         'description': 'ISO normative reference URI',
         'domain_of': ['Verifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'multivalued': True,
         'name': 'isoNormativeReference',
         'owner': 'Unit',
         'range': 'uri',
         'slot_uri': 'qudt:isoNormativeReference'} })
    normativeReference: Optional[list[str]] = Field(default=None, description="""Normative reference URI""", json_schema_extra = { "linkml_meta": {'alias': 'normativeReference',
         'description': 'Normative reference URI',
         'domain_of': ['Verifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'multivalued': True,
         'name': 'normativeReference',
         'owner': 'Unit',
         'range': 'uri',
         'slot_uri': 'qudt:normativeReference'} })
    abbreviation: Optional[str] = Field(default=None, description="""Short alphanumeric abbreviation for a unit""", json_schema_extra = { "linkml_meta": {'alias': 'abbreviation',
         'description': 'Short alphanumeric abbreviation for a unit',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'abbreviation',
         'owner': 'Unit',
         'range': 'string',
         'slot_uri': 'qudt:abbreviation'} })
    deprecated: Optional[bool] = Field(default=None, description="""Whether this entity is deprecated""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'description': 'Whether this entity is deprecated',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'deprecated',
         'owner': 'Unit',
         'range': 'boolean',
         'slot_uri': 'qudt:deprecated'} })
    plainTextDescription: Optional[str] = Field(default=None, description="""Plain text description""", json_schema_extra = { "linkml_meta": {'alias': 'plainTextDescription',
         'description': 'Plain text description',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'plainTextDescription',
         'owner': 'Unit',
         'range': 'string',
         'slot_uri': 'qudt:plainTextDescription'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'Unit',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'Unit',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'Unit',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class DerivedUnit(Unit):
    """
    Unit derived from base units (e.g., KiloM)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:DerivedUnit',
         'description': 'Unit derived from base units (e.g., KiloM)',
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'is_a': 'Unit',
         'name': 'DerivedUnit'})

    symbol: Optional[str] = Field(default=None, description="""Symbol for a unit (e.g., \"m\" for meter)""", json_schema_extra = { "linkml_meta": {'alias': 'symbol',
         'description': 'Symbol for a unit (e.g., "m" for meter)',
         'domain_of': ['AbstractQuantityKind', 'Unit', 'Prefix'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'symbol',
         'owner': 'DerivedUnit',
         'range': 'string',
         'slot_uri': 'qudt:symbol'} })
    latexSymbol: Optional[str] = Field(default=None, description="""LaTeX representation of symbol""", json_schema_extra = { "linkml_meta": {'alias': 'latexSymbol',
         'description': 'LaTeX representation of symbol',
         'domain_of': ['QuantityKind', 'Unit', 'QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'latexSymbol',
         'owner': 'DerivedUnit',
         'range': 'string',
         'slot_uri': 'qudt:latexSymbol'} })
    conversionMultiplier: Optional[float] = Field(default=None, description="""Multiplier to convert to base unit""", json_schema_extra = { "linkml_meta": {'alias': 'conversionMultiplier',
         'description': 'Multiplier to convert to base unit',
         'domain_of': ['Unit'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'conversionMultiplier',
         'owner': 'DerivedUnit',
         'range': 'double',
         'slot_uri': 'qudt:conversionMultiplier'} })
    conversionOffset: Optional[float] = Field(default=None, description="""Offset to convert to base unit""", json_schema_extra = { "linkml_meta": {'alias': 'conversionOffset',
         'description': 'Offset to convert to base unit',
         'domain_of': ['Unit'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'conversionOffset',
         'owner': 'DerivedUnit',
         'range': 'double',
         'slot_uri': 'qudt:conversionOffset'} })
    hasDimensionVector: Optional[str] = Field(default=None, description="""Dimension vector for a unit or quantity kind""", json_schema_extra = { "linkml_meta": {'alias': 'hasDimensionVector',
         'description': 'Dimension vector for a unit or quantity kind',
         'domain_of': ['QuantityKind', 'Unit'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'hasDimensionVector',
         'owner': 'DerivedUnit',
         'range': 'QuantityKindDimensionVector',
         'slot_uri': 'qudt:hasDimensionVector'} })
    hasQuantityKind: Optional[list[QuantityKind]] = Field(default=None, description="""Associates a quantity with its kind (e.g., Height, Weight)""", json_schema_extra = { "linkml_meta": {'alias': 'hasQuantityKind',
         'description': 'Associates a quantity with its kind (e.g., Height, Weight)',
         'domain_of': ['Quantity', 'Unit'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'inlined': True,
         'inlined_as_list': True,
         'multivalued': True,
         'name': 'hasQuantityKind',
         'owner': 'DerivedUnit',
         'range': 'QuantityKind',
         'slot_uri': 'qudt:hasQuantityKind'} })
    isUnitOfSystem: Optional[list[str]] = Field(default=None, description="""System of units this unit belongs to""", json_schema_extra = { "linkml_meta": {'alias': 'isUnitOfSystem',
         'description': 'System of units this unit belongs to',
         'domain_of': ['Unit'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'multivalued': True,
         'name': 'isUnitOfSystem',
         'owner': 'DerivedUnit',
         'range': 'SystemOfUnits',
         'slot_uri': 'qudt:isUnitOfSystem'} })
    applicableSystem: Optional[list[str]] = Field(default=None, description="""Systems where this unit is applicable""", json_schema_extra = { "linkml_meta": {'alias': 'applicableSystem',
         'description': 'Systems where this unit is applicable',
         'domain_of': ['Unit'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'multivalued': True,
         'name': 'applicableSystem',
         'owner': 'DerivedUnit',
         'range': 'SystemOfUnits',
         'slot_uri': 'qudt:applicableSystem'} })
    prefix: Optional[str] = Field(default=None, description="""Prefix for a unit (e.g., Kilo, Milli)""", json_schema_extra = { "linkml_meta": {'alias': 'prefix',
         'description': 'Prefix for a unit (e.g., Kilo, Milli)',
         'domain_of': ['Unit', 'SystemOfUnits'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'prefix',
         'owner': 'DerivedUnit',
         'range': 'Prefix',
         'slot_uri': 'qudt:prefix'} })
    scalingOf: Optional[str] = Field(default=None, description="""Base unit this unit is a scaling of""", json_schema_extra = { "linkml_meta": {'alias': 'scalingOf',
         'description': 'Base unit this unit is a scaling of',
         'domain_of': ['Unit'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'scalingOf',
         'owner': 'DerivedUnit',
         'range': 'Unit',
         'slot_uri': 'qudt:scalingOf'} })
    ucumCode: Optional[str] = Field(default=None, description="""UCUM code for the unit""", json_schema_extra = { "linkml_meta": {'alias': 'ucumCode',
         'description': 'UCUM code for the unit',
         'domain_of': ['Unit', 'Prefix'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'ucumCode',
         'owner': 'DerivedUnit',
         'range': 'string',
         'slot_uri': 'qudt:ucumCode'} })
    dbpediaMatch: Optional[str] = Field(default=None, description="""DBpedia URI for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'dbpediaMatch',
         'description': 'DBpedia URI for this entity',
         'domain_of': ['Verifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dbpediaMatch',
         'owner': 'DerivedUnit',
         'range': 'uri',
         'slot_uri': 'qudt:dbpediaMatch'} })
    wikidataMatch: Optional[str] = Field(default=None, description="""Wikidata URI for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'wikidataMatch',
         'description': 'Wikidata URI for this entity',
         'domain_of': ['Verifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'wikidataMatch',
         'owner': 'DerivedUnit',
         'range': 'uri',
         'slot_uri': 'qudt:wikidataMatch'} })
    informativeReference: Optional[list[str]] = Field(default=None, description="""Informative reference URL""", json_schema_extra = { "linkml_meta": {'alias': 'informativeReference',
         'description': 'Informative reference URL',
         'domain_of': ['Verifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'multivalued': True,
         'name': 'informativeReference',
         'owner': 'DerivedUnit',
         'range': 'uri',
         'slot_uri': 'qudt:informativeReference'} })
    isoNormativeReference: Optional[list[str]] = Field(default=None, description="""ISO normative reference URI""", json_schema_extra = { "linkml_meta": {'alias': 'isoNormativeReference',
         'description': 'ISO normative reference URI',
         'domain_of': ['Verifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'multivalued': True,
         'name': 'isoNormativeReference',
         'owner': 'DerivedUnit',
         'range': 'uri',
         'slot_uri': 'qudt:isoNormativeReference'} })
    normativeReference: Optional[list[str]] = Field(default=None, description="""Normative reference URI""", json_schema_extra = { "linkml_meta": {'alias': 'normativeReference',
         'description': 'Normative reference URI',
         'domain_of': ['Verifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'multivalued': True,
         'name': 'normativeReference',
         'owner': 'DerivedUnit',
         'range': 'uri',
         'slot_uri': 'qudt:normativeReference'} })
    abbreviation: Optional[str] = Field(default=None, description="""Short alphanumeric abbreviation for a unit""", json_schema_extra = { "linkml_meta": {'alias': 'abbreviation',
         'description': 'Short alphanumeric abbreviation for a unit',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'abbreviation',
         'owner': 'DerivedUnit',
         'range': 'string',
         'slot_uri': 'qudt:abbreviation'} })
    deprecated: Optional[bool] = Field(default=None, description="""Whether this entity is deprecated""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'description': 'Whether this entity is deprecated',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'deprecated',
         'owner': 'DerivedUnit',
         'range': 'boolean',
         'slot_uri': 'qudt:deprecated'} })
    plainTextDescription: Optional[str] = Field(default=None, description="""Plain text description""", json_schema_extra = { "linkml_meta": {'alias': 'plainTextDescription',
         'description': 'Plain text description',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'plainTextDescription',
         'owner': 'DerivedUnit',
         'range': 'string',
         'slot_uri': 'qudt:plainTextDescription'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'DerivedUnit',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'DerivedUnit',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'DerivedUnit',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class SystemOfUnits(Concept):
    """
    A coherent system of units (e.g., SI, CGS)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:SystemOfUnits',
         'description': 'A coherent system of units (e.g., SI, CGS)',
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'is_a': 'Concept',
         'name': 'SystemOfUnits',
         'slots': ['hasBaseUnit', 'prefix']})

    hasBaseUnit: Optional[list[str]] = Field(default=None, description="""Base units defined by this system""", json_schema_extra = { "linkml_meta": {'alias': 'hasBaseUnit',
         'description': 'Base units defined by this system',
         'domain_of': ['SystemOfUnits'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'multivalued': True,
         'name': 'hasBaseUnit',
         'owner': 'SystemOfUnits',
         'range': 'Unit',
         'slot_uri': 'qudt:hasBaseUnit'} })
    prefix: Optional[str] = Field(default=None, description="""Prefix for a unit (e.g., Kilo, Milli)""", json_schema_extra = { "linkml_meta": {'alias': 'prefix',
         'description': 'Prefix for a unit (e.g., Kilo, Milli)',
         'domain_of': ['Unit', 'SystemOfUnits'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'prefix',
         'owner': 'SystemOfUnits',
         'range': 'Prefix',
         'slot_uri': 'qudt:prefix'} })
    abbreviation: Optional[str] = Field(default=None, description="""Short alphanumeric abbreviation for a unit""", json_schema_extra = { "linkml_meta": {'alias': 'abbreviation',
         'description': 'Short alphanumeric abbreviation for a unit',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'abbreviation',
         'owner': 'SystemOfUnits',
         'range': 'string',
         'slot_uri': 'qudt:abbreviation'} })
    deprecated: Optional[bool] = Field(default=None, description="""Whether this entity is deprecated""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'description': 'Whether this entity is deprecated',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'deprecated',
         'owner': 'SystemOfUnits',
         'range': 'boolean',
         'slot_uri': 'qudt:deprecated'} })
    plainTextDescription: Optional[str] = Field(default=None, description="""Plain text description""", json_schema_extra = { "linkml_meta": {'alias': 'plainTextDescription',
         'description': 'Plain text description',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'plainTextDescription',
         'owner': 'SystemOfUnits',
         'range': 'string',
         'slot_uri': 'qudt:plainTextDescription'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'SystemOfUnits',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'SystemOfUnits',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'SystemOfUnits',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class QuantityKindDimensionVector(Concept):
    """
    Dimension vector expressing quantity in base dimensions
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:QuantityKindDimensionVector',
         'description': 'Dimension vector expressing quantity in base dimensions',
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'is_a': 'Concept',
         'name': 'QuantityKindDimensionVector',
         'slots': ['latexSymbol',
                   'dimensionExponentForLength',
                   'dimensionExponentForMass',
                   'dimensionExponentForTime',
                   'dimensionExponentForElectricCurrent',
                   'dimensionExponentForThermodynamicTemperature',
                   'dimensionExponentForAmountOfSubstance',
                   'dimensionExponentForLuminousIntensity',
                   'dimensionlessExponent']})

    latexSymbol: Optional[str] = Field(default=None, description="""LaTeX representation of symbol""", json_schema_extra = { "linkml_meta": {'alias': 'latexSymbol',
         'description': 'LaTeX representation of symbol',
         'domain_of': ['QuantityKind', 'Unit', 'QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'latexSymbol',
         'owner': 'QuantityKindDimensionVector',
         'range': 'string',
         'slot_uri': 'qudt:latexSymbol'} })
    dimensionExponentForLength: Optional[int] = Field(default=None, description="""Exponent for length dimension (L)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForLength',
         'description': 'Exponent for length dimension (L)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForLength',
         'owner': 'QuantityKindDimensionVector',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForLength'} })
    dimensionExponentForMass: Optional[int] = Field(default=None, description="""Exponent for mass dimension (M)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForMass',
         'description': 'Exponent for mass dimension (M)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForMass',
         'owner': 'QuantityKindDimensionVector',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForMass'} })
    dimensionExponentForTime: Optional[int] = Field(default=None, description="""Exponent for time dimension (T)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForTime',
         'description': 'Exponent for time dimension (T)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForTime',
         'owner': 'QuantityKindDimensionVector',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForTime'} })
    dimensionExponentForElectricCurrent: Optional[int] = Field(default=None, description="""Exponent for electric current dimension (I)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForElectricCurrent',
         'description': 'Exponent for electric current dimension (I)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForElectricCurrent',
         'owner': 'QuantityKindDimensionVector',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForElectricCurrent'} })
    dimensionExponentForThermodynamicTemperature: Optional[int] = Field(default=None, description="""Exponent for temperature dimension (Θ)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForThermodynamicTemperature',
         'description': 'Exponent for temperature dimension (Θ)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForThermodynamicTemperature',
         'owner': 'QuantityKindDimensionVector',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForThermodynamicTemperature'} })
    dimensionExponentForAmountOfSubstance: Optional[int] = Field(default=None, description="""Exponent for amount of substance dimension (N)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForAmountOfSubstance',
         'description': 'Exponent for amount of substance dimension (N)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForAmountOfSubstance',
         'owner': 'QuantityKindDimensionVector',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForAmountOfSubstance'} })
    dimensionExponentForLuminousIntensity: Optional[int] = Field(default=None, description="""Exponent for luminous intensity dimension (J)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForLuminousIntensity',
         'description': 'Exponent for luminous intensity dimension (J)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForLuminousIntensity',
         'owner': 'QuantityKindDimensionVector',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForLuminousIntensity'} })
    dimensionlessExponent: Optional[int] = Field(default=None, description="""Dimensionless exponent""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionlessExponent',
         'description': 'Dimensionless exponent',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionlessExponent',
         'owner': 'QuantityKindDimensionVector',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionlessExponent'} })
    abbreviation: Optional[str] = Field(default=None, description="""Short alphanumeric abbreviation for a unit""", json_schema_extra = { "linkml_meta": {'alias': 'abbreviation',
         'description': 'Short alphanumeric abbreviation for a unit',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'abbreviation',
         'owner': 'QuantityKindDimensionVector',
         'range': 'string',
         'slot_uri': 'qudt:abbreviation'} })
    deprecated: Optional[bool] = Field(default=None, description="""Whether this entity is deprecated""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'description': 'Whether this entity is deprecated',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'deprecated',
         'owner': 'QuantityKindDimensionVector',
         'range': 'boolean',
         'slot_uri': 'qudt:deprecated'} })
    plainTextDescription: Optional[str] = Field(default=None, description="""Plain text description""", json_schema_extra = { "linkml_meta": {'alias': 'plainTextDescription',
         'description': 'Plain text description',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'plainTextDescription',
         'owner': 'QuantityKindDimensionVector',
         'range': 'string',
         'slot_uri': 'qudt:plainTextDescription'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'QuantityKindDimensionVector',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'QuantityKindDimensionVector',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'QuantityKindDimensionVector',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class QuantityKindDimensionVectorSI(QuantityKindDimensionVector):
    """
    SI dimension vector
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:QuantityKindDimensionVector_SI',
         'description': 'SI dimension vector',
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'is_a': 'QuantityKindDimensionVector',
         'name': 'QuantityKindDimensionVector_SI'})

    latexSymbol: Optional[str] = Field(default=None, description="""LaTeX representation of symbol""", json_schema_extra = { "linkml_meta": {'alias': 'latexSymbol',
         'description': 'LaTeX representation of symbol',
         'domain_of': ['QuantityKind', 'Unit', 'QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'latexSymbol',
         'owner': 'QuantityKindDimensionVector_SI',
         'range': 'string',
         'slot_uri': 'qudt:latexSymbol'} })
    dimensionExponentForLength: Optional[int] = Field(default=None, description="""Exponent for length dimension (L)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForLength',
         'description': 'Exponent for length dimension (L)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForLength',
         'owner': 'QuantityKindDimensionVector_SI',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForLength'} })
    dimensionExponentForMass: Optional[int] = Field(default=None, description="""Exponent for mass dimension (M)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForMass',
         'description': 'Exponent for mass dimension (M)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForMass',
         'owner': 'QuantityKindDimensionVector_SI',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForMass'} })
    dimensionExponentForTime: Optional[int] = Field(default=None, description="""Exponent for time dimension (T)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForTime',
         'description': 'Exponent for time dimension (T)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForTime',
         'owner': 'QuantityKindDimensionVector_SI',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForTime'} })
    dimensionExponentForElectricCurrent: Optional[int] = Field(default=None, description="""Exponent for electric current dimension (I)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForElectricCurrent',
         'description': 'Exponent for electric current dimension (I)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForElectricCurrent',
         'owner': 'QuantityKindDimensionVector_SI',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForElectricCurrent'} })
    dimensionExponentForThermodynamicTemperature: Optional[int] = Field(default=None, description="""Exponent for temperature dimension (Θ)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForThermodynamicTemperature',
         'description': 'Exponent for temperature dimension (Θ)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForThermodynamicTemperature',
         'owner': 'QuantityKindDimensionVector_SI',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForThermodynamicTemperature'} })
    dimensionExponentForAmountOfSubstance: Optional[int] = Field(default=None, description="""Exponent for amount of substance dimension (N)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForAmountOfSubstance',
         'description': 'Exponent for amount of substance dimension (N)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForAmountOfSubstance',
         'owner': 'QuantityKindDimensionVector_SI',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForAmountOfSubstance'} })
    dimensionExponentForLuminousIntensity: Optional[int] = Field(default=None, description="""Exponent for luminous intensity dimension (J)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForLuminousIntensity',
         'description': 'Exponent for luminous intensity dimension (J)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForLuminousIntensity',
         'owner': 'QuantityKindDimensionVector_SI',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForLuminousIntensity'} })
    dimensionlessExponent: Optional[int] = Field(default=None, description="""Dimensionless exponent""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionlessExponent',
         'description': 'Dimensionless exponent',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionlessExponent',
         'owner': 'QuantityKindDimensionVector_SI',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionlessExponent'} })
    abbreviation: Optional[str] = Field(default=None, description="""Short alphanumeric abbreviation for a unit""", json_schema_extra = { "linkml_meta": {'alias': 'abbreviation',
         'description': 'Short alphanumeric abbreviation for a unit',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'abbreviation',
         'owner': 'QuantityKindDimensionVector_SI',
         'range': 'string',
         'slot_uri': 'qudt:abbreviation'} })
    deprecated: Optional[bool] = Field(default=None, description="""Whether this entity is deprecated""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'description': 'Whether this entity is deprecated',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'deprecated',
         'owner': 'QuantityKindDimensionVector_SI',
         'range': 'boolean',
         'slot_uri': 'qudt:deprecated'} })
    plainTextDescription: Optional[str] = Field(default=None, description="""Plain text description""", json_schema_extra = { "linkml_meta": {'alias': 'plainTextDescription',
         'description': 'Plain text description',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'plainTextDescription',
         'owner': 'QuantityKindDimensionVector_SI',
         'range': 'string',
         'slot_uri': 'qudt:plainTextDescription'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'QuantityKindDimensionVector_SI',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'QuantityKindDimensionVector_SI',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'QuantityKindDimensionVector_SI',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class QuantityKindDimensionVectorCGS(QuantityKindDimensionVector):
    """
    CGS dimension vector
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:QuantityKindDimensionVector_CGS',
         'description': 'CGS dimension vector',
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'is_a': 'QuantityKindDimensionVector',
         'name': 'QuantityKindDimensionVector_CGS'})

    latexSymbol: Optional[str] = Field(default=None, description="""LaTeX representation of symbol""", json_schema_extra = { "linkml_meta": {'alias': 'latexSymbol',
         'description': 'LaTeX representation of symbol',
         'domain_of': ['QuantityKind', 'Unit', 'QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'latexSymbol',
         'owner': 'QuantityKindDimensionVector_CGS',
         'range': 'string',
         'slot_uri': 'qudt:latexSymbol'} })
    dimensionExponentForLength: Optional[int] = Field(default=None, description="""Exponent for length dimension (L)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForLength',
         'description': 'Exponent for length dimension (L)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForLength',
         'owner': 'QuantityKindDimensionVector_CGS',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForLength'} })
    dimensionExponentForMass: Optional[int] = Field(default=None, description="""Exponent for mass dimension (M)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForMass',
         'description': 'Exponent for mass dimension (M)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForMass',
         'owner': 'QuantityKindDimensionVector_CGS',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForMass'} })
    dimensionExponentForTime: Optional[int] = Field(default=None, description="""Exponent for time dimension (T)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForTime',
         'description': 'Exponent for time dimension (T)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForTime',
         'owner': 'QuantityKindDimensionVector_CGS',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForTime'} })
    dimensionExponentForElectricCurrent: Optional[int] = Field(default=None, description="""Exponent for electric current dimension (I)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForElectricCurrent',
         'description': 'Exponent for electric current dimension (I)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForElectricCurrent',
         'owner': 'QuantityKindDimensionVector_CGS',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForElectricCurrent'} })
    dimensionExponentForThermodynamicTemperature: Optional[int] = Field(default=None, description="""Exponent for temperature dimension (Θ)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForThermodynamicTemperature',
         'description': 'Exponent for temperature dimension (Θ)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForThermodynamicTemperature',
         'owner': 'QuantityKindDimensionVector_CGS',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForThermodynamicTemperature'} })
    dimensionExponentForAmountOfSubstance: Optional[int] = Field(default=None, description="""Exponent for amount of substance dimension (N)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForAmountOfSubstance',
         'description': 'Exponent for amount of substance dimension (N)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForAmountOfSubstance',
         'owner': 'QuantityKindDimensionVector_CGS',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForAmountOfSubstance'} })
    dimensionExponentForLuminousIntensity: Optional[int] = Field(default=None, description="""Exponent for luminous intensity dimension (J)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForLuminousIntensity',
         'description': 'Exponent for luminous intensity dimension (J)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForLuminousIntensity',
         'owner': 'QuantityKindDimensionVector_CGS',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForLuminousIntensity'} })
    dimensionlessExponent: Optional[int] = Field(default=None, description="""Dimensionless exponent""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionlessExponent',
         'description': 'Dimensionless exponent',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionlessExponent',
         'owner': 'QuantityKindDimensionVector_CGS',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionlessExponent'} })
    abbreviation: Optional[str] = Field(default=None, description="""Short alphanumeric abbreviation for a unit""", json_schema_extra = { "linkml_meta": {'alias': 'abbreviation',
         'description': 'Short alphanumeric abbreviation for a unit',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'abbreviation',
         'owner': 'QuantityKindDimensionVector_CGS',
         'range': 'string',
         'slot_uri': 'qudt:abbreviation'} })
    deprecated: Optional[bool] = Field(default=None, description="""Whether this entity is deprecated""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'description': 'Whether this entity is deprecated',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'deprecated',
         'owner': 'QuantityKindDimensionVector_CGS',
         'range': 'boolean',
         'slot_uri': 'qudt:deprecated'} })
    plainTextDescription: Optional[str] = Field(default=None, description="""Plain text description""", json_schema_extra = { "linkml_meta": {'alias': 'plainTextDescription',
         'description': 'Plain text description',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'plainTextDescription',
         'owner': 'QuantityKindDimensionVector_CGS',
         'range': 'string',
         'slot_uri': 'qudt:plainTextDescription'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'QuantityKindDimensionVector_CGS',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'QuantityKindDimensionVector_CGS',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'QuantityKindDimensionVector_CGS',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class QuantityKindDimensionVectorImperial(QuantityKindDimensionVector):
    """
    Imperial dimension vector
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:QuantityKindDimensionVector_Imperial',
         'description': 'Imperial dimension vector',
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'is_a': 'QuantityKindDimensionVector',
         'name': 'QuantityKindDimensionVector_Imperial'})

    latexSymbol: Optional[str] = Field(default=None, description="""LaTeX representation of symbol""", json_schema_extra = { "linkml_meta": {'alias': 'latexSymbol',
         'description': 'LaTeX representation of symbol',
         'domain_of': ['QuantityKind', 'Unit', 'QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'latexSymbol',
         'owner': 'QuantityKindDimensionVector_Imperial',
         'range': 'string',
         'slot_uri': 'qudt:latexSymbol'} })
    dimensionExponentForLength: Optional[int] = Field(default=None, description="""Exponent for length dimension (L)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForLength',
         'description': 'Exponent for length dimension (L)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForLength',
         'owner': 'QuantityKindDimensionVector_Imperial',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForLength'} })
    dimensionExponentForMass: Optional[int] = Field(default=None, description="""Exponent for mass dimension (M)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForMass',
         'description': 'Exponent for mass dimension (M)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForMass',
         'owner': 'QuantityKindDimensionVector_Imperial',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForMass'} })
    dimensionExponentForTime: Optional[int] = Field(default=None, description="""Exponent for time dimension (T)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForTime',
         'description': 'Exponent for time dimension (T)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForTime',
         'owner': 'QuantityKindDimensionVector_Imperial',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForTime'} })
    dimensionExponentForElectricCurrent: Optional[int] = Field(default=None, description="""Exponent for electric current dimension (I)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForElectricCurrent',
         'description': 'Exponent for electric current dimension (I)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForElectricCurrent',
         'owner': 'QuantityKindDimensionVector_Imperial',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForElectricCurrent'} })
    dimensionExponentForThermodynamicTemperature: Optional[int] = Field(default=None, description="""Exponent for temperature dimension (Θ)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForThermodynamicTemperature',
         'description': 'Exponent for temperature dimension (Θ)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForThermodynamicTemperature',
         'owner': 'QuantityKindDimensionVector_Imperial',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForThermodynamicTemperature'} })
    dimensionExponentForAmountOfSubstance: Optional[int] = Field(default=None, description="""Exponent for amount of substance dimension (N)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForAmountOfSubstance',
         'description': 'Exponent for amount of substance dimension (N)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForAmountOfSubstance',
         'owner': 'QuantityKindDimensionVector_Imperial',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForAmountOfSubstance'} })
    dimensionExponentForLuminousIntensity: Optional[int] = Field(default=None, description="""Exponent for luminous intensity dimension (J)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForLuminousIntensity',
         'description': 'Exponent for luminous intensity dimension (J)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForLuminousIntensity',
         'owner': 'QuantityKindDimensionVector_Imperial',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForLuminousIntensity'} })
    dimensionlessExponent: Optional[int] = Field(default=None, description="""Dimensionless exponent""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionlessExponent',
         'description': 'Dimensionless exponent',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionlessExponent',
         'owner': 'QuantityKindDimensionVector_Imperial',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionlessExponent'} })
    abbreviation: Optional[str] = Field(default=None, description="""Short alphanumeric abbreviation for a unit""", json_schema_extra = { "linkml_meta": {'alias': 'abbreviation',
         'description': 'Short alphanumeric abbreviation for a unit',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'abbreviation',
         'owner': 'QuantityKindDimensionVector_Imperial',
         'range': 'string',
         'slot_uri': 'qudt:abbreviation'} })
    deprecated: Optional[bool] = Field(default=None, description="""Whether this entity is deprecated""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'description': 'Whether this entity is deprecated',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'deprecated',
         'owner': 'QuantityKindDimensionVector_Imperial',
         'range': 'boolean',
         'slot_uri': 'qudt:deprecated'} })
    plainTextDescription: Optional[str] = Field(default=None, description="""Plain text description""", json_schema_extra = { "linkml_meta": {'alias': 'plainTextDescription',
         'description': 'Plain text description',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'plainTextDescription',
         'owner': 'QuantityKindDimensionVector_Imperial',
         'range': 'string',
         'slot_uri': 'qudt:plainTextDescription'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'QuantityKindDimensionVector_Imperial',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'QuantityKindDimensionVector_Imperial',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'QuantityKindDimensionVector_Imperial',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class QuantityKindDimensionVectorISO(QuantityKindDimensionVector):
    """
    ISO dimension vector
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:QuantityKindDimensionVector_ISO',
         'description': 'ISO dimension vector',
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'is_a': 'QuantityKindDimensionVector',
         'name': 'QuantityKindDimensionVector_ISO'})

    latexSymbol: Optional[str] = Field(default=None, description="""LaTeX representation of symbol""", json_schema_extra = { "linkml_meta": {'alias': 'latexSymbol',
         'description': 'LaTeX representation of symbol',
         'domain_of': ['QuantityKind', 'Unit', 'QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'latexSymbol',
         'owner': 'QuantityKindDimensionVector_ISO',
         'range': 'string',
         'slot_uri': 'qudt:latexSymbol'} })
    dimensionExponentForLength: Optional[int] = Field(default=None, description="""Exponent for length dimension (L)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForLength',
         'description': 'Exponent for length dimension (L)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForLength',
         'owner': 'QuantityKindDimensionVector_ISO',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForLength'} })
    dimensionExponentForMass: Optional[int] = Field(default=None, description="""Exponent for mass dimension (M)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForMass',
         'description': 'Exponent for mass dimension (M)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForMass',
         'owner': 'QuantityKindDimensionVector_ISO',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForMass'} })
    dimensionExponentForTime: Optional[int] = Field(default=None, description="""Exponent for time dimension (T)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForTime',
         'description': 'Exponent for time dimension (T)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForTime',
         'owner': 'QuantityKindDimensionVector_ISO',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForTime'} })
    dimensionExponentForElectricCurrent: Optional[int] = Field(default=None, description="""Exponent for electric current dimension (I)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForElectricCurrent',
         'description': 'Exponent for electric current dimension (I)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForElectricCurrent',
         'owner': 'QuantityKindDimensionVector_ISO',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForElectricCurrent'} })
    dimensionExponentForThermodynamicTemperature: Optional[int] = Field(default=None, description="""Exponent for temperature dimension (Θ)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForThermodynamicTemperature',
         'description': 'Exponent for temperature dimension (Θ)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForThermodynamicTemperature',
         'owner': 'QuantityKindDimensionVector_ISO',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForThermodynamicTemperature'} })
    dimensionExponentForAmountOfSubstance: Optional[int] = Field(default=None, description="""Exponent for amount of substance dimension (N)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForAmountOfSubstance',
         'description': 'Exponent for amount of substance dimension (N)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForAmountOfSubstance',
         'owner': 'QuantityKindDimensionVector_ISO',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForAmountOfSubstance'} })
    dimensionExponentForLuminousIntensity: Optional[int] = Field(default=None, description="""Exponent for luminous intensity dimension (J)""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionExponentForLuminousIntensity',
         'description': 'Exponent for luminous intensity dimension (J)',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionExponentForLuminousIntensity',
         'owner': 'QuantityKindDimensionVector_ISO',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionExponentForLuminousIntensity'} })
    dimensionlessExponent: Optional[int] = Field(default=None, description="""Dimensionless exponent""", json_schema_extra = { "linkml_meta": {'alias': 'dimensionlessExponent',
         'description': 'Dimensionless exponent',
         'domain_of': ['QuantityKindDimensionVector'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dimensionlessExponent',
         'owner': 'QuantityKindDimensionVector_ISO',
         'range': 'integer',
         'slot_uri': 'qudt:dimensionlessExponent'} })
    abbreviation: Optional[str] = Field(default=None, description="""Short alphanumeric abbreviation for a unit""", json_schema_extra = { "linkml_meta": {'alias': 'abbreviation',
         'description': 'Short alphanumeric abbreviation for a unit',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'abbreviation',
         'owner': 'QuantityKindDimensionVector_ISO',
         'range': 'string',
         'slot_uri': 'qudt:abbreviation'} })
    deprecated: Optional[bool] = Field(default=None, description="""Whether this entity is deprecated""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'description': 'Whether this entity is deprecated',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'deprecated',
         'owner': 'QuantityKindDimensionVector_ISO',
         'range': 'boolean',
         'slot_uri': 'qudt:deprecated'} })
    plainTextDescription: Optional[str] = Field(default=None, description="""Plain text description""", json_schema_extra = { "linkml_meta": {'alias': 'plainTextDescription',
         'description': 'Plain text description',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'plainTextDescription',
         'owner': 'QuantityKindDimensionVector_ISO',
         'range': 'string',
         'slot_uri': 'qudt:plainTextDescription'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'QuantityKindDimensionVector_ISO',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'QuantityKindDimensionVector_ISO',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'QuantityKindDimensionVector_ISO',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class Prefix(Verifiable, Concept):
    """
    Unit prefix (e.g., Kilo, Milli)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Prefix',
         'description': 'Unit prefix (e.g., Kilo, Milli)',
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'is_a': 'Concept',
         'mixins': ['Verifiable'],
         'name': 'Prefix',
         'slots': ['symbol', 'prefixMultiplier', 'ucumCode', 'exactMatch']})

    symbol: Optional[str] = Field(default=None, description="""Symbol for a unit (e.g., \"m\" for meter)""", json_schema_extra = { "linkml_meta": {'alias': 'symbol',
         'description': 'Symbol for a unit (e.g., "m" for meter)',
         'domain_of': ['AbstractQuantityKind', 'Unit', 'Prefix'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'symbol',
         'owner': 'Prefix',
         'range': 'string',
         'slot_uri': 'qudt:symbol'} })
    prefixMultiplier: Optional[float] = Field(default=None, description="""Numeric multiplier for the prefix (e.g., 1000 for Kilo)""", json_schema_extra = { "linkml_meta": {'alias': 'prefixMultiplier',
         'description': 'Numeric multiplier for the prefix (e.g., 1000 for Kilo)',
         'domain_of': ['Prefix'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'prefixMultiplier',
         'owner': 'Prefix',
         'range': 'double',
         'slot_uri': 'qudt:prefixMultiplier'} })
    ucumCode: Optional[str] = Field(default=None, description="""UCUM code for the unit""", json_schema_extra = { "linkml_meta": {'alias': 'ucumCode',
         'description': 'UCUM code for the unit',
         'domain_of': ['Unit', 'Prefix'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'ucumCode',
         'owner': 'Prefix',
         'range': 'string',
         'slot_uri': 'qudt:ucumCode'} })
    exactMatch: Optional[list[str]] = Field(default=None, description="""Equivalent quantity kind or unit""", json_schema_extra = { "linkml_meta": {'alias': 'exactMatch',
         'description': 'Equivalent quantity kind or unit',
         'domain_of': ['QuantityKind', 'Prefix'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'multivalued': True,
         'name': 'exactMatch',
         'owner': 'Prefix',
         'range': 'string',
         'slot_uri': 'skos:exactMatch'} })
    dbpediaMatch: Optional[str] = Field(default=None, description="""DBpedia URI for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'dbpediaMatch',
         'description': 'DBpedia URI for this entity',
         'domain_of': ['Verifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dbpediaMatch',
         'owner': 'Prefix',
         'range': 'uri',
         'slot_uri': 'qudt:dbpediaMatch'} })
    wikidataMatch: Optional[str] = Field(default=None, description="""Wikidata URI for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'wikidataMatch',
         'description': 'Wikidata URI for this entity',
         'domain_of': ['Verifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'wikidataMatch',
         'owner': 'Prefix',
         'range': 'uri',
         'slot_uri': 'qudt:wikidataMatch'} })
    informativeReference: Optional[list[str]] = Field(default=None, description="""Informative reference URL""", json_schema_extra = { "linkml_meta": {'alias': 'informativeReference',
         'description': 'Informative reference URL',
         'domain_of': ['Verifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'multivalued': True,
         'name': 'informativeReference',
         'owner': 'Prefix',
         'range': 'uri',
         'slot_uri': 'qudt:informativeReference'} })
    isoNormativeReference: Optional[list[str]] = Field(default=None, description="""ISO normative reference URI""", json_schema_extra = { "linkml_meta": {'alias': 'isoNormativeReference',
         'description': 'ISO normative reference URI',
         'domain_of': ['Verifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'multivalued': True,
         'name': 'isoNormativeReference',
         'owner': 'Prefix',
         'range': 'uri',
         'slot_uri': 'qudt:isoNormativeReference'} })
    normativeReference: Optional[list[str]] = Field(default=None, description="""Normative reference URI""", json_schema_extra = { "linkml_meta": {'alias': 'normativeReference',
         'description': 'Normative reference URI',
         'domain_of': ['Verifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'multivalued': True,
         'name': 'normativeReference',
         'owner': 'Prefix',
         'range': 'uri',
         'slot_uri': 'qudt:normativeReference'} })
    abbreviation: Optional[str] = Field(default=None, description="""Short alphanumeric abbreviation for a unit""", json_schema_extra = { "linkml_meta": {'alias': 'abbreviation',
         'description': 'Short alphanumeric abbreviation for a unit',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'abbreviation',
         'owner': 'Prefix',
         'range': 'string',
         'slot_uri': 'qudt:abbreviation'} })
    deprecated: Optional[bool] = Field(default=None, description="""Whether this entity is deprecated""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'description': 'Whether this entity is deprecated',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'deprecated',
         'owner': 'Prefix',
         'range': 'boolean',
         'slot_uri': 'qudt:deprecated'} })
    plainTextDescription: Optional[str] = Field(default=None, description="""Plain text description""", json_schema_extra = { "linkml_meta": {'alias': 'plainTextDescription',
         'description': 'Plain text description',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'plainTextDescription',
         'owner': 'Prefix',
         'range': 'string',
         'slot_uri': 'qudt:plainTextDescription'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'Prefix',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'Prefix',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'Prefix',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class DecimalPrefix(Prefix):
    """
    Decimal prefix (powers of 10)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:DecimalPrefix',
         'description': 'Decimal prefix (powers of 10)',
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'is_a': 'Prefix',
         'name': 'DecimalPrefix'})

    symbol: Optional[str] = Field(default=None, description="""Symbol for a unit (e.g., \"m\" for meter)""", json_schema_extra = { "linkml_meta": {'alias': 'symbol',
         'description': 'Symbol for a unit (e.g., "m" for meter)',
         'domain_of': ['AbstractQuantityKind', 'Unit', 'Prefix'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'symbol',
         'owner': 'DecimalPrefix',
         'range': 'string',
         'slot_uri': 'qudt:symbol'} })
    prefixMultiplier: Optional[float] = Field(default=None, description="""Numeric multiplier for the prefix (e.g., 1000 for Kilo)""", json_schema_extra = { "linkml_meta": {'alias': 'prefixMultiplier',
         'description': 'Numeric multiplier for the prefix (e.g., 1000 for Kilo)',
         'domain_of': ['Prefix'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'prefixMultiplier',
         'owner': 'DecimalPrefix',
         'range': 'double',
         'slot_uri': 'qudt:prefixMultiplier'} })
    ucumCode: Optional[str] = Field(default=None, description="""UCUM code for the unit""", json_schema_extra = { "linkml_meta": {'alias': 'ucumCode',
         'description': 'UCUM code for the unit',
         'domain_of': ['Unit', 'Prefix'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'ucumCode',
         'owner': 'DecimalPrefix',
         'range': 'string',
         'slot_uri': 'qudt:ucumCode'} })
    exactMatch: Optional[list[str]] = Field(default=None, description="""Equivalent quantity kind or unit""", json_schema_extra = { "linkml_meta": {'alias': 'exactMatch',
         'description': 'Equivalent quantity kind or unit',
         'domain_of': ['QuantityKind', 'Prefix'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'multivalued': True,
         'name': 'exactMatch',
         'owner': 'DecimalPrefix',
         'range': 'string',
         'slot_uri': 'skos:exactMatch'} })
    dbpediaMatch: Optional[str] = Field(default=None, description="""DBpedia URI for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'dbpediaMatch',
         'description': 'DBpedia URI for this entity',
         'domain_of': ['Verifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'dbpediaMatch',
         'owner': 'DecimalPrefix',
         'range': 'uri',
         'slot_uri': 'qudt:dbpediaMatch'} })
    wikidataMatch: Optional[str] = Field(default=None, description="""Wikidata URI for this entity""", json_schema_extra = { "linkml_meta": {'alias': 'wikidataMatch',
         'description': 'Wikidata URI for this entity',
         'domain_of': ['Verifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'wikidataMatch',
         'owner': 'DecimalPrefix',
         'range': 'uri',
         'slot_uri': 'qudt:wikidataMatch'} })
    informativeReference: Optional[list[str]] = Field(default=None, description="""Informative reference URL""", json_schema_extra = { "linkml_meta": {'alias': 'informativeReference',
         'description': 'Informative reference URL',
         'domain_of': ['Verifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'multivalued': True,
         'name': 'informativeReference',
         'owner': 'DecimalPrefix',
         'range': 'uri',
         'slot_uri': 'qudt:informativeReference'} })
    isoNormativeReference: Optional[list[str]] = Field(default=None, description="""ISO normative reference URI""", json_schema_extra = { "linkml_meta": {'alias': 'isoNormativeReference',
         'description': 'ISO normative reference URI',
         'domain_of': ['Verifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'multivalued': True,
         'name': 'isoNormativeReference',
         'owner': 'DecimalPrefix',
         'range': 'uri',
         'slot_uri': 'qudt:isoNormativeReference'} })
    normativeReference: Optional[list[str]] = Field(default=None, description="""Normative reference URI""", json_schema_extra = { "linkml_meta": {'alias': 'normativeReference',
         'description': 'Normative reference URI',
         'domain_of': ['Verifiable'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'multivalued': True,
         'name': 'normativeReference',
         'owner': 'DecimalPrefix',
         'range': 'uri',
         'slot_uri': 'qudt:normativeReference'} })
    abbreviation: Optional[str] = Field(default=None, description="""Short alphanumeric abbreviation for a unit""", json_schema_extra = { "linkml_meta": {'alias': 'abbreviation',
         'description': 'Short alphanumeric abbreviation for a unit',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'abbreviation',
         'owner': 'DecimalPrefix',
         'range': 'string',
         'slot_uri': 'qudt:abbreviation'} })
    deprecated: Optional[bool] = Field(default=None, description="""Whether this entity is deprecated""", json_schema_extra = { "linkml_meta": {'alias': 'deprecated',
         'description': 'Whether this entity is deprecated',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'deprecated',
         'owner': 'DecimalPrefix',
         'range': 'boolean',
         'slot_uri': 'qudt:deprecated'} })
    plainTextDescription: Optional[str] = Field(default=None, description="""Plain text description""", json_schema_extra = { "linkml_meta": {'alias': 'plainTextDescription',
         'description': 'Plain text description',
         'domain_of': ['Concept'],
         'from_schema': 'https://pokemonkg.org/schema/qudt',
         'name': 'plainTextDescription',
         'owner': 'DecimalPrefix',
         'range': 'string',
         'slot_uri': 'qudt:plainTextDescription'} })
    id: str = Field(default=..., description="""A unique identifier""", json_schema_extra = { "linkml_meta": {'alias': 'id',
         'description': 'A unique identifier',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'identifier': True,
         'name': 'id',
         'owner': 'DecimalPrefix',
         'range': 'uri',
         'required': True,
         'slot_uri': 'linkml_common:identifier'} })
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'DecimalPrefix',
         'range': 'string',
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'DecimalPrefix',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class Ability(Thing):
    """
    Abilities were introduced in Generation III as an all new game mechanic. Each and every Pokémon has an ability, and can only have one at a time. Some abilities are exclusive to certain Pokémon and Evolution lines, while others are known by many Pokémon.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pokemon:Ability',
         'description': 'Abilities were introduced in Generation III as an all new '
                        'game mechanic. Each and every Pokémon has an ability, and can '
                        'only have one at a time. Some abilities are exclusive to '
                        'certain Pokémon and Evolution lines, while others are known '
                        'by many Pokémon.',
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


class EggGroup(NamedIndividual):
    """
    Egg group is a category that determines which Pokémon are able to interbreed. The concept was introduced in Generation II, along with breeding. Similar to types, a Pokémon may belong to either one or two egg groups.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'Egg group is a category that determines which Pokémon are '
                        'able to interbreed. The concept was introduced in Generation '
                        'II, along with breeding. Similar to types, a Pokémon may '
                        'belong to either one or two egg groups.',
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'NamedIndividual',
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
    name: str = Field(default=..., description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'EggGroup',
         'range': 'string',
         'required': True,
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""A description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description',
         'description': 'A description of the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'description',
         'owner': 'EggGroup',
         'range': 'string',
         'slot_uri': 'rdfs:comment'} })


class Flavor(NamedIndividual):
    """
    Flavor is a special set of attributes that certain foods in the Pokémon world have. Most of the foods can have more than one flavor, and the flavor determines which Pokémon can eat them.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'Flavor is a special set of attributes that certain foods in '
                        'the Pokémon world have. Most of the foods can have more than '
                        'one flavor, and the flavor determines which Pokémon can eat '
                        'them.',
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'NamedIndividual',
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
    name: str = Field(default=..., description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'Flavor',
         'range': 'string',
         'required': True,
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
    """
    Generations refers to the Pokémon game series. It is a group of games that were released at or around the same time. It also means that games in the same generation are compatible with the others, containing the same Pokémon and the number of moves there are to be learned.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'Generations refers to the Pokémon game series. It is a group '
                        'of games that were released at or around the same time. It '
                        'also means that games in the same generation are compatible '
                        'with the others, containing the same Pokémon and the number '
                        'of moves there are to be learned.',
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'Thing',
         'name': 'Generation',
         'slots': ['featuresSpecies']})

    featuresSpecies: Optional[list[str]] = Field(default=None, description="""['A Pokédex entry features a species']""", json_schema_extra = { "linkml_meta": {'alias': 'featuresSpecies',
         'description': "['A Pokédex entry features a species']",
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


class Habitat(NamedIndividual):
    """
    A habitat is a type of environment that certain Pokémon belong to.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'A habitat is a type of environment that certain Pokémon '
                        'belong to.',
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'NamedIndividual',
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
    """
    An item is an object in the Pokémon games which the player can pick up, keep in their Bag, and use in some manner. They have various uses, including healing, powering up, helping one to catch Pokémon, or to access a new area.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'An item is an object in the Pokémon games which the player '
                        'can pick up, keep in their Bag, and use in some manner. They '
                        'have various uses, including healing, powering up, helping '
                        'one to catch Pokémon, or to access a new area.',
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
    """
    Food items are consumable items in the Pokémon world that can have flavors, firmness, and smoothness attributes.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'Food items are consumable items in the Pokémon world that can '
                        'have flavors, firmness, and smoothness attributes.',
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'Item',
         'name': 'Food',
         'slots': ['hasFlavor', 'firmness', 'smoothness']})

    hasFlavor: Optional[list[str]] = Field(default=None, description="""A Pokémon has a flavor""", json_schema_extra = { "linkml_meta": {'alias': 'hasFlavor',
         'description': 'A Pokémon has a flavor',
         'domain': 'Food',
         'domain_of': ['Food'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'multivalued': True,
         'name': 'hasFlavor',
         'owner': 'Food',
         'range': 'Flavor',
         'required': False,
         'slot_uri': 'pokemon:hasFlavor'} })
    firmness: Optional[int] = Field(default=None, description="""How firm a berry or food item feels, affecting its use in Pokéblock or Poffin making.""", json_schema_extra = { "linkml_meta": {'alias': 'firmness',
         'description': 'How firm a berry or food item feels, affecting its use in '
                        'Pokéblock or Poffin making.',
         'domain': 'Food',
         'domain_of': ['Food'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'name': 'firmness',
         'owner': 'Food',
         'range': 'integer'} })
    smoothness: Optional[int] = Field(default=None, description="""How smooth a berry or food item is, affecting its use in Pokéblock or Poffin making.""", json_schema_extra = { "linkml_meta": {'alias': 'smoothness',
         'description': 'How smooth a berry or food item is, affecting its use in '
                        'Pokéblock or Poffin making.',
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
    """
    Berries are small, juicy, fleshy fruit. As in the real world, a large variety exists in the Pokémon world, with a large range of flavors, names, and effects. First found in the Generation II games, many Berries have since became critical help items in battle, where their various effects include HP and status condition restoration, stat enhancement, and even damage negation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'Berries are small, juicy, fleshy fruit. As in the real world, '
                        'a large variety exists in the Pokémon world, with a large '
                        'range of flavors, names, and effects. First found in the '
                        'Generation II games, many Berries have since became critical '
                        'help items in battle, where their various effects include HP '
                        'and status condition restoration, stat enhancement, and even '
                        'damage negation.',
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'Food',
         'name': 'Berry',
         'slots': ['hasSize']})

    hasSize: Optional[Quantity] = Field(default=None, description="""The physical size of an entity, expressed as a quantity with unit.""", json_schema_extra = { "linkml_meta": {'alias': 'hasSize',
         'description': 'The physical size of an entity, expressed as a quantity with '
                        'unit.',
         'domain_of': ['Berry'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'inlined': True,
         'multivalued': False,
         'name': 'hasSize',
         'owner': 'Berry',
         'range': 'Quantity',
         'required': False,
         'slot_uri': 'pokemon:hasSize'} })
    hasFlavor: Optional[list[str]] = Field(default=None, description="""A Pokémon has a flavor""", json_schema_extra = { "linkml_meta": {'alias': 'hasFlavor',
         'description': 'A Pokémon has a flavor',
         'domain': 'Food',
         'domain_of': ['Food'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'multivalued': True,
         'name': 'hasFlavor',
         'owner': 'Berry',
         'range': 'Flavor',
         'required': False,
         'slot_uri': 'pokemon:hasFlavor'} })
    firmness: Optional[int] = Field(default=None, description="""How firm a berry or food item feels, affecting its use in Pokéblock or Poffin making.""", json_schema_extra = { "linkml_meta": {'alias': 'firmness',
         'description': 'How firm a berry or food item feels, affecting its use in '
                        'Pokéblock or Poffin making.',
         'domain': 'Food',
         'domain_of': ['Food'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'name': 'firmness',
         'owner': 'Berry',
         'range': 'integer'} })
    smoothness: Optional[int] = Field(default=None, description="""How smooth a berry or food item is, affecting its use in Pokéblock or Poffin making.""", json_schema_extra = { "linkml_meta": {'alias': 'smoothness',
         'description': 'How smooth a berry or food item is, affecting its use in '
                        'Pokéblock or Poffin making.',
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
    A hold item is an item that can be held by a Pokémon.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'A hold item is an item that can be held by a Pokémon.',
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
    """
    The Pokédex is an electronic device designed to catalog and provide information regarding the various species of Pokémon featured in the Pokémon video game, anime and manga series.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'https://pokemonkg.org/ontology#Pok%C3%A9dex',
         'description': 'The Pokédex is an electronic device designed to catalog and '
                        'provide information regarding the various species of Pokémon '
                        'featured in the Pokémon video game, anime and manga series.',
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


# A Pokémon
Pokemon = Union["Pokedex", "Type"]


class PokedexEntry(Thing):
    """
    A Pokédex entry is a description of a Pokémon.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'https://pokemonkg.org/ontology#Pok%C3%A9dexEntry',
         'description': 'A Pokédex entry is a description of a Pokémon.',
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'Thing',
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
    name: Optional[str] = Field(default=None, description="""Human-readable label for the entity""", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'description': 'Human-readable label for the entity',
         'domain_of': ['Thing'],
         'from_schema': 'http://www.w3.org/2002/07/owl',
         'name': 'name',
         'owner': 'PokedexEntry',
         'range': 'string',
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
    """
    A Poké Ball is a type of item that is critical to a Trainer's quest, used for catching and storing Pokémon.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'https://pokemonkg.org/ontology#Pok%C3%A9ball',
         'description': "A Poké Ball is a type of item that is critical to a Trainer's "
                        'quest, used for catching and storing Pokémon.',
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
    """
    Entities that have a somewhat fixed, physical extension.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'description': 'Entities that have a somewhat fixed, physical extension.',
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


class Shape(NamedIndividual):
    """
    Shapes are categories that certain Pokémon belong to, which determine which Pokémon they can breed with.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'Shapes are categories that certain Pokémon belong to, which '
                        'determine which Pokémon they can breed with.',
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'NamedIndividual',
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
    """
    Regions are areas in the Pokémon universe that are smaller parts of a nation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'Regions are areas in the Pokémon universe that are smaller '
                        'parts of a nation.',
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


class Species(NamedIndividual):
    """
    A species is a category of Pokémon that share common features.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pokemon:Species',
         'description': 'A species is a category of Pokémon that share common '
                        'features.',
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'NamedIndividual',
         'name': 'Species',
         'slots': ['hasColor',
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
                   'foundIn',
                   'evolvesFrom',
                   'evolvesTo']})

    hasColor: Optional[Color] = Field(default=None, description="""A Pokémon has a color""", json_schema_extra = { "linkml_meta": {'alias': 'hasColor',
         'description': 'A Pokémon has a color',
         'domain_of': ['Species'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'inlined': True,
         'multivalued': False,
         'name': 'hasColor',
         'owner': 'Species',
         'range': 'Color',
         'required': False,
         'slot_uri': 'pokemon:hasColour'} })
    mayHaveHiddenAbility: Optional[list[Ability]] = Field(default=None, description="""A special ability only obtainable through specific encounters or events, not through normal gameplay.""", json_schema_extra = { "linkml_meta": {'alias': 'mayHaveHiddenAbility',
         'description': 'A special ability only obtainable through specific encounters '
                        'or events, not through normal gameplay.',
         'domain': 'Species',
         'domain_of': ['Species'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'inlined_as_list': True,
         'multivalued': True,
         'name': 'mayHaveHiddenAbility',
         'owner': 'Species',
         'range': 'Ability',
         'slot_uri': 'pokemon:mayHaveHiddenAbility',
         'subproperty_of': 'mayHaveAbility'} })
    mayHaveAbility: Optional[list[Ability]] = Field(default=None, description="""A Pokémon may have an ability""", json_schema_extra = { "linkml_meta": {'alias': 'mayHaveAbility',
         'description': 'A Pokémon may have an ability',
         'domain': 'Species',
         'domain_of': ['Species'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'inlined_as_list': True,
         'multivalued': True,
         'name': 'mayHaveAbility',
         'owner': 'Species',
         'range': 'Ability',
         'slot_uri': 'pokemon:mayHaveAbility'} })
    isAbleToApply: Optional[list[Move]] = Field(default=None, description="""Moves that a Pokémon can use in battle or in the overworld.""", json_schema_extra = { "linkml_meta": {'alias': 'isAbleToApply',
         'description': 'Moves that a Pokémon can use in battle or in the overworld.',
         'domain_of': ['Species'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'inlined_as_list': True,
         'multivalued': True,
         'name': 'isAbleToApply',
         'owner': 'Species',
         'range': 'Move',
         'required': False,
         'slot_uri': 'pokemon:isAbleToApply'} })
    hasHeight: Optional[Quantity] = Field(default=None, description="""How tall a Pokémon species is, expressed as a quantity with unit.""", json_schema_extra = { "linkml_meta": {'alias': 'hasHeight',
         'description': 'How tall a Pokémon species is, expressed as a quantity with '
                        'unit.',
         'domain': 'Species',
         'domain_of': ['Species'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'inlined': True,
         'multivalued': False,
         'name': 'hasHeight',
         'owner': 'Species',
         'range': 'Quantity',
         'required': False,
         'slot_uri': 'pokemon:hasHeight'} })
    hasWeight: Optional[Quantity] = Field(default=None, description="""How heavy a Pokémon species is, expressed as a quantity with unit.""", json_schema_extra = { "linkml_meta": {'alias': 'hasWeight',
         'description': 'How heavy a Pokémon species is, expressed as a quantity with '
                        'unit.',
         'domain': 'Species',
         'domain_of': ['Species'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'inlined': True,
         'multivalued': False,
         'name': 'hasWeight',
         'owner': 'Species',
         'range': 'Quantity',
         'required': False,
         'slot_uri': 'pokemon:hasWeight'} })
    depiction: Optional[list[Artwork]] = Field(default=None, description="""Visual artwork depicting this entity""", json_schema_extra = { "linkml_meta": {'alias': 'depiction',
         'description': 'Visual artwork depicting this entity',
         'domain_of': ['Person', 'Species'],
         'from_schema': 'http://xmlns.com/foaf/0.1/',
         'inlined': True,
         'inlined_as_list': True,
         'inverse': 'depicts',
         'multivalued': True,
         'name': 'depiction',
         'owner': 'Species',
         'range': 'Artwork',
         'slot_uri': 'foaf:depiction'} })
    inEggGroup: Optional[list[EggGroup]] = Field(default=None, description="""Which egg group a species belongs to, controlling which Pokémon can breed together.""", json_schema_extra = { "linkml_meta": {'alias': 'inEggGroup',
         'description': 'Which egg group a species belongs to, controlling which '
                        'Pokémon can breed together.',
         'domain': 'Species',
         'domain_of': ['Species'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'inlined_as_list': True,
         'multivalued': True,
         'name': 'inEggGroup',
         'owner': 'Species',
         'range': 'EggGroup',
         'required': False,
         'slot_uri': 'pokemon:inEggGroup'} })
    hasType: Optional[list[Type]] = Field(default=None, description="""A Pokémon has a type""", json_schema_extra = { "linkml_meta": {'alias': 'hasType',
         'description': 'A Pokémon has a type',
         'domain_of': ['Species', 'Move'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'inlined_as_list': True,
         'multivalued': True,
         'name': 'hasType',
         'owner': 'Species',
         'range': 'Type',
         'required': False,
         'slot_uri': 'pokemon:hasType'} })
    hasShape: Optional[Shape] = Field(default=None, description="""The shape of a berry is a measure of how good it is for making a Potion.""", json_schema_extra = { "linkml_meta": {'alias': 'hasShape',
         'description': 'The shape of a berry is a measure of how good it is for '
                        'making a Potion.',
         'domain': 'Species',
         'domain_of': ['Species'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'inlined': True,
         'multivalued': False,
         'name': 'hasShape',
         'owner': 'Species',
         'range': 'Shape',
         'required': False,
         'slot_uri': 'pokemon:hasShape'} })
    hasGenus: Optional[str] = Field(default=None, description="""The species category label shown in the Pokédex, such as \"Seed Pokémon\" for Bulbasaur.""", json_schema_extra = { "linkml_meta": {'alias': 'hasGenus',
         'description': 'The species category label shown in the Pokédex, such as '
                        '"Seed Pokémon" for Bulbasaur.',
         'domain': 'Species',
         'domain_of': ['Species'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'name': 'hasGenus',
         'owner': 'Species',
         'range': 'string'} })
    hasCatchRate: Optional[int] = Field(default=None, description="""Determines how easy a Pokémon species is to catch, with higher values meaning easier capture.""", json_schema_extra = { "linkml_meta": {'alias': 'hasCatchRate',
         'description': 'Determines how easy a Pokémon species is to catch, with '
                        'higher values meaning easier capture.',
         'domain': 'Species',
         'domain_of': ['Species'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'multivalued': False,
         'name': 'hasCatchRate',
         'owner': 'Species',
         'range': 'integer',
         'required': False,
         'slot_uri': 'pokemon:hasCatchRate'} })
    foundIn: Optional[list[Habitat]] = Field(default=None, description="""A place is found in a location""", json_schema_extra = { "linkml_meta": {'alias': 'foundIn',
         'description': 'A place is found in a location',
         'domain': 'Species',
         'domain_of': ['Species'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'inlined_as_list': True,
         'multivalued': True,
         'name': 'foundIn',
         'owner': 'Species',
         'range': 'Habitat',
         'required': False,
         'slot_uri': 'pokemon:foundIn'} })
    evolvesFrom: Optional[Species] = Field(default=None, description="""This species evolves the other species.""", json_schema_extra = { "linkml_meta": {'alias': 'evolvesFrom',
         'description': 'This species evolves the other species.',
         'domain': 'Species',
         'domain_of': ['Species'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'inlined': True,
         'inverse': 'evolvesTo',
         'multivalued': False,
         'name': 'evolvesFrom',
         'owner': 'Species',
         'range': 'Species',
         'required': False,
         'slot_uri': 'pokemon:evolvesFrom'} })
    evolvesTo: Optional[list[Species]] = Field(default=None, description="""A Pokémon evolves to another Pokémon.""", json_schema_extra = { "linkml_meta": {'alias': 'evolvesTo',
         'description': 'A Pokémon evolves to another Pokémon.',
         'domain': 'Species',
         'domain_of': ['Species'],
         'from_schema': 'https://pokemonkg.org/ontology',
         'inlined_as_list': True,
         'inverse': 'evolvesFrom',
         'multivalued': True,
         'name': 'evolvesTo',
         'owner': 'Species',
         'range': 'Species',
         'required': False,
         'slot_uri': 'pokemon:evolvesTo'} })
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
    """
    A move is a special ability of a Pokémon.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pokemon:Move',
         'description': 'A move is a special ability of a Pokémon.',
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
    hasType: Optional[list[Type]] = Field(default=None, description="""A Pokémon has a type""", json_schema_extra = { "linkml_meta": {'alias': 'hasType',
         'description': 'A Pokémon has a type',
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
    A move learning is a way that a Pokémon can learn a move.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'A move learning is a way that a Pokémon can learn a move.',
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
    Medicine items can heal various afflictions of a Pokémon.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'Medicine items can heal various afflictions of a Pokémon.',
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
    hasType: Optional[list[Type]] = Field(default=None, description="""A Pokémon has a type""", json_schema_extra = { "linkml_meta": {'alias': 'hasType',
         'description': 'A Pokémon has a type',
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
    hasType: Optional[list[Type]] = Field(default=None, description="""A Pokémon has a type""", json_schema_extra = { "linkml_meta": {'alias': 'hasType',
         'description': 'A Pokémon has a type',
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
    hasType: Optional[list[Type]] = Field(default=None, description="""A Pokémon has a type""", json_schema_extra = { "linkml_meta": {'alias': 'hasType',
         'description': 'A Pokémon has a type',
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
    """
    A Technical Machine is an item that can be used to teach a Pokémon a move.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'A Technical Machine is an item that can be used to teach a '
                        'Pokémon a move.',
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
    A trainer is a person who is able to catch Pokémon.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'A trainer is a person who is able to catch Pokémon.',
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'Person',
         'name': 'Trainer'})

    depiction: Optional[list[Artwork]] = Field(default=None, description="""Visual artwork depicting this entity""", json_schema_extra = { "linkml_meta": {'alias': 'depiction',
         'description': 'Visual artwork depicting this entity',
         'domain_of': ['Person', 'Species'],
         'from_schema': 'http://xmlns.com/foaf/0.1/',
         'inlined': True,
         'inlined_as_list': True,
         'inverse': 'depicts',
         'multivalued': True,
         'name': 'depiction',
         'owner': 'Trainer',
         'range': 'Artwork',
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
    """
    A gym leader is the highest ranking member and owner of an official Pokémon gym. Gym leaders use their gym and their Pokémon to test the skills of trainers that challenge them, and if said trainers win a battle, the gym leader will gift them a badge that's unique to that specific gym.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'description': 'A gym leader is the highest ranking member and owner of an '
                        'official Pokémon gym. Gym leaders use their gym and their '
                        'Pokémon to test the skills of trainers that challenge them, '
                        'and if said trainers win a battle, the gym leader will gift '
                        "them a badge that's unique to that specific gym.",
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'Trainer',
         'name': 'GymLeader'})

    depiction: Optional[list[Artwork]] = Field(default=None, description="""Visual artwork depicting this entity""", json_schema_extra = { "linkml_meta": {'alias': 'depiction',
         'description': 'Visual artwork depicting this entity',
         'domain_of': ['Person', 'Species'],
         'from_schema': 'http://xmlns.com/foaf/0.1/',
         'inlined': True,
         'inlined_as_list': True,
         'inverse': 'depicts',
         'multivalued': True,
         'name': 'depiction',
         'owner': 'GymLeader',
         'range': 'Artwork',
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


class Type(NamedIndividual):
    """
    All Pokémon creatures and their moves are assigned certain types. Each type has several strengths and weaknesses in both attack and defense.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'pokemon:Type',
         'description': 'All Pokémon creatures and their moves are assigned certain '
                        'types. Each type has several strengths and weaknesses in both '
                        'attack and defense.',
         'from_schema': 'https://pokemonkg.org/ontology',
         'is_a': 'NamedIndividual',
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
NamedIndividual.model_rebuild()
Person.model_rebuild()
Artwork.model_rebuild()
CmykColor.model_rebuild()
Color.model_rebuild()
Connotation.model_rebuild()
Concept.model_rebuild()
Aspect.model_rebuild()
Quantifiable.model_rebuild()
Verifiable.model_rebuild()
Quantity.model_rebuild()
QuantityValue.model_rebuild()
AbstractQuantityKind.model_rebuild()
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
