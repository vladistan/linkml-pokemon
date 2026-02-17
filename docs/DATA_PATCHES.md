# Pokemon Knowledge Graph Data Patches

This document describes the SPARQL UPDATE queries needed to fix data issues in the Pokemon Knowledge Graph.

## Overview

| Patch | Description | Affected Count | Graph |
|-------|-------------|----------------|-------|
| 1 | Fix weight units (KiloM → KiloGM) | 898 | bulbapedia |
| 2 | Add rdf:type to QuantityValue nodes | ~1,796 | bulbapedia |
| 3 | Fix berry size quantityKind (Height → Diameter) | 64 | pokeapi-co |

## Patch 1: Fix Weight Units

#### Problem
Pokemon weight values incorrectly use `unit:KiloM` (Kilometer) instead of `unit:KiloGM` (Kilogram).

#### Verification Query
```sparql
PREFIX qudt: <http://qudt.org/schema/qudt/>
PREFIX pkmn: <https://pokemonkg.org/ontology#>
PREFIX unit: <http://qudt.org/vocab/unit/>

SELECT (COUNT(*) as ?count) WHERE {
  GRAPH <https://pokemonkg.org/dataset/bulbapedia> {
    ?pokemon pkmn:hasWeight ?qty .
    ?qty qudt:quantityValue ?qv .
    ?qv qudt:unit unit:KiloM .
  }
}
```

#### Fix Query
```sparql
PREFIX qudt: <http://qudt.org/schema/qudt/>
PREFIX pkmn: <https://pokemonkg.org/ontology#>
PREFIX unit: <http://qudt.org/vocab/unit/>

DELETE {
  GRAPH <https://pokemonkg.org/dataset/bulbapedia> {
    ?qv qudt:unit unit:KiloM .
  }
}
INSERT {
  GRAPH <https://pokemonkg.org/dataset/bulbapedia> {
    ?qv qudt:unit unit:KiloGM .
  }
}
WHERE {
  GRAPH <https://pokemonkg.org/dataset/bulbapedia> {
    ?pokemon pkmn:hasWeight ?qty .
    ?qty qudt:quantityValue ?qv .
    ?qv qudt:unit unit:KiloM .
  }
}
```

#### Post-Fix Verification
```sparql
PREFIX qudt: <http://qudt.org/schema/qudt/>
PREFIX pkmn: <https://pokemonkg.org/ontology#>
PREFIX unit: <http://qudt.org/vocab/unit/>

SELECT ?unit (COUNT(*) as ?count) WHERE {
  GRAPH <https://pokemonkg.org/dataset/bulbapedia> {
    ?pokemon pkmn:hasWeight ?qty .
    ?qty qudt:quantityValue ?qv .
    ?qv qudt:unit ?unit .
  }
}
GROUP BY ?unit
```

Expected result: All weights should use `unit:KiloGM`.

#### Rollback Query
```sparql
PREFIX qudt: <http://qudt.org/schema/qudt/>
PREFIX pkmn: <https://pokemonkg.org/ontology#>
PREFIX unit: <http://qudt.org/vocab/unit/>

DELETE {
  GRAPH <https://pokemonkg.org/dataset/bulbapedia> {
    ?qv qudt:unit unit:KiloGM .
  }
}
INSERT {
  GRAPH <https://pokemonkg.org/dataset/bulbapedia> {
    ?qv qudt:unit unit:KiloM .
  }
}
WHERE {
  GRAPH <https://pokemonkg.org/dataset/bulbapedia> {
    ?pokemon pkmn:hasWeight ?qty .
    ?qty qudt:quantityValue ?qv .
    ?qv qudt:unit unit:KiloGM .
  }
}
```

---

## Patch 2: Add QuantityValue Types

#### Problem
QuantityValue instances (height/weight values) have no explicit `rdf:type`. They should be typed as `qudt:QuantityValue` for proper ORM materialization.

#### Verification Query
```sparql
PREFIX qudt: <http://qudt.org/schema/qudt/>

SELECT (COUNT(*) as ?untyped) WHERE {
  GRAPH <https://pokemonkg.org/dataset/bulbapedia> {
    ?qty qudt:quantityValue ?qv .
    ?qv qudt:value ?val .
    FILTER NOT EXISTS { ?qv a qudt:QuantityValue }
  }
}
```

#### Fix Query
```sparql
PREFIX qudt: <http://qudt.org/schema/qudt/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

INSERT {
  GRAPH <https://pokemonkg.org/dataset/bulbapedia> {
    ?qv rdf:type qudt:QuantityValue .
  }
}
WHERE {
  GRAPH <https://pokemonkg.org/dataset/bulbapedia> {
    ?qty qudt:quantityValue ?qv .
    ?qv qudt:value ?val .
    FILTER NOT EXISTS { ?qv a qudt:QuantityValue }
  }
}
```

#### Post-Fix Verification
```sparql
PREFIX qudt: <http://qudt.org/schema/qudt/>

SELECT (COUNT(*) as ?typed) WHERE {
  GRAPH <https://pokemonkg.org/dataset/bulbapedia> {
    ?qv a qudt:QuantityValue .
  }
}
```

Expected result: ~1,796 QuantityValue instances (898 heights + 898 weights).

#### Rollback Query
```sparql
PREFIX qudt: <http://qudt.org/schema/qudt/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

DELETE {
  GRAPH <https://pokemonkg.org/dataset/bulbapedia> {
    ?qv rdf:type qudt:QuantityValue .
  }
}
WHERE {
  GRAPH <https://pokemonkg.org/dataset/bulbapedia> {
    ?qv a qudt:QuantityValue .
    ?qv qudt:value ?val .
  }
}
```

---

## Patch 3: Fix Berry Size QuantityKind

#### Problem
Berry size values use `quantitykind:Height` which is semantically incorrect. Berries are roughly spherical objects, so their size should be expressed as `quantitykind:Diameter` (or alternatively `quantitykind:Length` for a general linear dimension).

All 64 berries consistently use Height, suggesting a deliberate but incorrect mapping decision during ETL from PokeAPI.

#### Verification Query
```sparql
PREFIX qudt: <http://qudt.org/schema/qudt/>
PREFIX pkmn: <https://pokemonkg.org/ontology#>
PREFIX qk: <http://qudt.org/vocab/quantitykind/>

SELECT ?quantityKind (COUNT(DISTINCT ?berry) as ?count) WHERE {
  GRAPH <http://pokemon.outofbits.com/dataset/pokeapi-co> {
    ?berry a pkmn:Berry ;
           pkmn:hasSize ?sizeQuantity .
    ?sizeQuantity qudt:hasQuantityKind ?quantityKind .
  }
}
GROUP BY ?quantityKind
```

Expected result before fix: All 64 berries use `quantitykind:Height`.

#### Fix Query
```sparql
PREFIX qudt: <http://qudt.org/schema/qudt/>
PREFIX pkmn: <https://pokemonkg.org/ontology#>
PREFIX qk: <http://qudt.org/vocab/quantitykind/>

DELETE {
  GRAPH <http://pokemon.outofbits.com/dataset/pokeapi-co> {
    ?sizeQuantity qudt:hasQuantityKind qk:Height .
  }
}
INSERT {
  GRAPH <http://pokemon.outofbits.com/dataset/pokeapi-co> {
    ?sizeQuantity qudt:hasQuantityKind qk:Diameter .
  }
}
WHERE {
  GRAPH <http://pokemon.outofbits.com/dataset/pokeapi-co> {
    ?berry a pkmn:Berry ;
           pkmn:hasSize ?sizeQuantity .
    ?sizeQuantity qudt:hasQuantityKind qk:Height .
  }
}
```

#### Post-Fix Verification
```sparql
PREFIX qudt: <http://qudt.org/schema/qudt/>
PREFIX pkmn: <https://pokemonkg.org/ontology#>
PREFIX qk: <http://qudt.org/vocab/quantitykind/>

SELECT ?quantityKind (COUNT(DISTINCT ?berry) as ?count) WHERE {
  GRAPH <http://pokemon.outofbits.com/dataset/pokeapi-co> {
    ?berry a pkmn:Berry ;
           pkmn:hasSize ?sizeQuantity .
    ?sizeQuantity qudt:hasQuantityKind ?quantityKind .
  }
}
GROUP BY ?quantityKind
```

Expected result: All 64 berries should use `quantitykind:Diameter`.

#### Rollback Query
```sparql
PREFIX qudt: <http://qudt.org/schema/qudt/>
PREFIX pkmn: <https://pokemonkg.org/ontology#>
PREFIX qk: <http://qudt.org/vocab/quantitykind/>

DELETE {
  GRAPH <http://pokemon.outofbits.com/dataset/pokeapi-co> {
    ?sizeQuantity qudt:hasQuantityKind qk:Diameter .
  }
}
INSERT {
  GRAPH <http://pokemon.outofbits.com/dataset/pokeapi-co> {
    ?sizeQuantity qudt:hasQuantityKind qk:Height .
  }
}
WHERE {
  GRAPH <http://pokemon.outofbits.com/dataset/pokeapi-co> {
    ?berry a pkmn:Berry ;
           pkmn:hasSize ?sizeQuantity .
    ?sizeQuantity qudt:hasQuantityKind qk:Diameter .
  }
}
```

---

## Execution Instructions

Using [sparql-cli](https://github.com/vladistan/sparql-cli) with the `supply` profile:

```bash
sparql -P supply update -f patch1.sparql
sparql -P supply update -f patch2.sparql
sparql -P supply update -f patch3.sparql
```

Verify each patch after execution using the post-fix verification queries above.
