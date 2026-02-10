# About

## Project Background

The Pokemon LinkML Model adapts the [Pokemon Knowledge Graph Ontology](https://pokemonkg.org/) into a [LinkML](https://linkml.io/) schema. The original ontology was created in 2019 to provide a structured, semantic representation of the Pokemon universe sourced from Bulbapedia and PokeAPI.

LinkML adds a practical modeling layer on top of the ontology, enabling code generation, data validation, and multi-format serialization from a single YAML schema definition.

## Schema Architecture

### Main Schema

The core schema (`linkml_pokemon.yaml`) defines all Pokemon-domain classes and relationships. It uses the `pokemon:` prefix namespace (`https://pokemonkg.org/ontology#`) to stay aligned with the upstream ontology URIs.

### Imported Schemas

The model composes several external vocabularies to reuse established standards rather than reinvent them:

| Import | Namespace | Purpose |
| --- | --- | --- |
| [**FOAF**](http://xmlns.com/foaf/spec/) | `http://xmlns.com/foaf/0.1/` | Person and agent modeling (Trainers, Gym Leaders) |
| [**DBpedia**](https://dbpedia.org/ontology/) | `http://dbpedia.org/ontology/` | Color definitions, real-world concept references |
| [**OWL**](https://www.w3.org/TR/owl2-overview/) | `http://www.w3.org/2002/07/owl#` | Named individuals, thing hierarchy |
| [**QUDT**](https://qudt.org/) | `http://qudt.org/schema/qudt/` | Units of measurement for height, weight, and size quantities |
| [**LinkML types**](https://linkml.io/linkml-model/docs/types/) | `https://w3id.org/linkml/` | Built-in type definitions (string, integer, boolean, etc.) |

### Class Hierarchy

The schema follows a layered inheritance structure:

```
Thing (name, description)
  +-- NamedIndividual (requires name)
  |     +-- Species
  |     +-- Type
  |     +-- EggGroup, Habitat, Shape, Flavor
  +-- Move
  |     +-- SpecialMove, PhysicalMove, StatusMove
  +-- Item
  |     +-- Pokeball, HoldItem, Medicine, HM, TM
  |     +-- Food
  |           +-- Berry
  +-- Generation, Game
  +-- Place (abstract)
  |     +-- Region, Town, Gym
  +-- Pokedex, PokedexEntry
Person (from FOAF)
  +-- Trainer
        +-- GymLeader
```

## Knowledge Graph

The schema is backed by a live Pokemon Knowledge Graph containing data from multiple sources:

| Dataset | Source | Content |
| --- | --- | --- |
| **Bulbapedia** | `pokemonkg.org/dataset/bulbapedia` | Species, moves, abilities, types, evolution data |
| **PokeAPI** | `pokemon.outofbits.com/dataset/pokeapi-co` | Berries, items, game metadata |

The knowledge graph contains approximately 900 species, 770+ moves, 18 types, and 300+ abilities, all represented as RDF triples queryable via SPARQL.

## Generated Artifacts

From the single YAML schema, the following artifacts are generated:

| Artifact | Format | Use Case |
| --- | --- | --- |
| Pydantic models | Python | Type-safe data access, validation, serialization |
| JSON Schema | JSON | Data validation in any language |
| OWL ontology | Turtle RDF | Semantic web reasoning and integration |
| SHACL shapes | Turtle RDF | RDF data validation |
| TypeScript types | TypeScript | Web application development |
| SQL DDL | SQL | Relational database schema |
| JSON-LD context | JSON-LD | Linked data interoperability |
| ShEx | ShEx | RDF shape constraints |
| Protobuf | Proto3 | Efficient binary serialization |

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

## License

This project is licensed under the MIT License.
