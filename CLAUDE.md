# CLAUDE.md

## Project Overview

Pokemon ontology built with LinkML. Adapts the Pokemon Knowledge Graph Ontology to LinkML format with classes for Pokemon, Species, Moves, Abilities, Types, Places, and Trainers.

## Schema

- **Main schema**: `src/linkml_pokemon/schema/linkml_pokemon.yaml` (source of truth)
- **Imported schemas**: `foaf.yaml`, `dbpedia.yaml`, `owl.yaml`, `qudt.yaml`
- **Generated models**: `src/linkml_pokemon/datamodel/` (never edit — regenerated from schema)
- **Generated artifacts**: `project/` (JSON Schema, OWL, TypeScript, etc.)

## Development

**Requires**: Python 3.12-3.14, `uv`, `just`

```bash
just install          # Install dependencies
just gen-project      # Generate all artifacts from schema
just gen-python       # Generate Python models only
just test             # Run all tests (regenerates first)
just lint             # Lint schema with linkml-lint
just serve-datadict   # Serve data dictionary locally (port 6420, with Mermaid diagrams)
just deploy           # Deploy docs to GitHub Pages (mkdocs gh-deploy)
just clean            # Remove generated files
```

### Workflow

1. Edit schema YAML in `src/linkml_pokemon/schema/`
2. `just gen-project` to regenerate artifacts
3. `just test` to validate
4. `just serve-datadict` to preview documentation

### Testing

- `tests/test_data.py` — Validates example YAML data against generated Python classes using `yaml_loader`
- `tests/test_semantics.py` — Semantic validation (stub)
- Example data: `src/data/examples/*.yaml`

## Workspace Dependencies

Part of the LinkML workspace with editable installs via `[tool.uv.sources]`:

```toml
linkml-runtime = { path = "../linkml-runtime", editable = true }
linkml = { path = "../linkml", editable = true }
```

- `linkml-runtime` — Runtime dependency (loaders, SchemaView)
- `linkml` — Dev dependency only (generators, linter)

## Knowledge Graph

The Pokemon KG data lives in a Stardog Cloud triplestore. Query it using the `sparql` CLI with the **`supply`** profile:

```bash
sparql -P supply classes               # List classes
sparql -P supply graphs                # List named graphs
sparql -P supply objects pokemon:Species  # List Pokemon species
```

- **SPARQL profile**: `supply`
- **SPARQL queries**: `sparql/` directory (`.rq` files for DBpedia extraction)
- **Data patches**: `docs/DATA_PATCHES.md` (SPARQL UPDATE patches for data quality fixes)

When working with this project's data, always use `sparql -P supply` to query the graph.

## Tools

- **Build**: `hatchling` with `hatch-vcs` versioning
- **Task runner**: `justfile` (not Make)
- **SPARQL**: `sparql` CLI with `supply` profile for KG queries
- **Diagrams**: Mermaid via Kroki server (`kroki_server` variable in justfile)
- **Docs**: mkdocs for site generation
- **Notebooks**: marimo for interactive exploration
- **DevContainer**: Python 3.13 with uv, just, pre-commit, gh CLI
