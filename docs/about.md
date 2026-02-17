# About

## Project Background

The Pokemon LinkML Model adapts the [Pokemon Knowledge Graph](https://pokemonkg.org/) ontology into a [LinkML](https://linkml.io/) schema. The original ontology was created in 2019 by [Kevin Haller](mailto:contact@kevinhaller.dev) to provide a structured, semantic representation of the Pokemon universe, with data sourced from community platforms including Bulbapedia, PokeWiki, PokeAPI, and PokemonDB.

This project serves three purposes: as an educational resource for learning LinkML and knowledge graph technologies, as a test bed for LinkML tooling development, and as a playground for AI agent development with rich ontology-backed data.

## Knowledge Graph

The [Pokemon Knowledge Graph](https://pokemonkg.org/) (PokemonKG) by Kevin Haller provides a comprehensive RDF dataset covering the Pokemon universe. This project adapts the original OWL ontology into [LinkML](https://linkml.io/) (Linked Data Modeling Language), a schema language that enables code generation, data validation, and multi-format serialization from a single YAML definition.

The knowledge graph contains data from multiple sources:

| Dataset | Source | Content |
| --- | --- | --- |
| **Bulbapedia** | `pokemonkg.org/dataset/bulbapedia` | Species, moves, abilities, types, evolution data |
| **PokeAPI** | `pokemon.outofbits.com/dataset/pokeapi-co` | Berries, items, game metadata |

In total, the graph holds over 100,000 RDF triples covering approximately 900 species, 770+ moves, 18 types, and 300+ abilities, all queryable via SPARQL.

The LinkML adaptation preserves the original ontology's URI namespace (`https://pokemonkg.org/ontology#`) ensuring compatibility with the upstream knowledge graph while adding features like type-safe code generation, built-in validation, and multi-format artifact output.

## Interoperability

The schema imports and builds on several established external ontologies and vocabularies:

| Ontology | Namespace | Role in this Schema |
| --- | --- | --- |
| [FOAF](http://xmlns.com/foaf/spec/) (Friend of a Friend) | `http://xmlns.com/foaf/0.1/` | Person modeling for Trainers and Gym Leaders. Provides the `Person` base class with properties like `name` and `depiction`. |
| [DBpedia](https://dbpedia.org/ontology/) | `http://dbpedia.org/ontology/` | Real-world concept references. Used for color definitions (e.g., `dbpedia:Yellow`) and connotations linking Pokemon concepts to encyclopedia entries. |
| [OWL](https://www.w3.org/TR/owl2-overview/) (Web Ontology Language) | `http://www.w3.org/2002/07/owl#` | Provides `Thing` as the root class and `NamedIndividual` for enumerated instances like Types, Habitats, and Egg Groups. |
| [QUDT](https://vladistan.github.io/linkml-qudt/) (Quantities, Units, Dimensions, Types) | `http://qudt.org/schema/qudt/` | Units of measurement for physical attributes. Pokemon height uses meters, weight uses kilograms, and berry size uses diameter, all expressed as QUDT Quantity values with proper units and quantity kinds. |
| [LinkML types](https://linkml.io/linkml-model/docs/types/) | `https://w3id.org/linkml/` | Built-in primitive type definitions (string, integer, boolean, uri, etc.) that form the base range types for slots. |

## Technology Stack

| Component | Technology |
| --- | --- |
| Schema language | [LinkML](https://linkml.io/) |
| Package management | [uv](https://docs.astral.sh/uv/) |
| Task runner | [just](https://just.systems/) |
| Documentation | [MkDocs](https://www.mkdocs.org/) with [Material](https://squidfundamentals.com/mkdocs-material/) theme |
| Diagrams | [Kroki](https://kroki.io/) (Mermaid rendering) |
| Code generation | LinkML generators (`gen-pydantic`, `gen-owl`, `gen-json-schema`, etc.) |
| Data dictionary | `gen-markdown-datadict` with SVG class/ERD diagrams |

## Disclaimer

This is an independent open source project and is not affiliated with, endorsed by, or connected to [The Pokemon Company](https://www.pokemon.com/) or [Nintendo](https://www.nintendo.com/) in any way. Pokemon and all related names, characters, and imagery are trademarks of The Pokemon Company and Nintendo, the original creators of the Pokemon world. This project is intended solely for educational and research purposes.

## License

This project is licensed under the MIT License.
