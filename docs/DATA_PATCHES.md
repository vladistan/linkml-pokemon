# Pokemon Knowledge Graph Data Patches

This document describes the SPARQL UPDATE queries needed to fix data issues in the Pokemon Knowledge Graph.

## Overview

| Patch | Description | Affected Count | Graph |
|-------|-------------|----------------|-------|
| 1 | Fix weight units (KiloM → KiloGM) | 898 | bulbapedia |
| 2 | Add rdf:type to QuantityValue nodes | ~1,796 | bulbapedia |
| 3 | Fix berry size quantityKind (Height → Diameter) | 64 | pokeapi-co |
| 4 | Fix hasShape URIs (colon → underscore) | 14 | pokeapi-co, bulbapedia |
| 5 | Fix foundIn/Habitat URIs (colon → underscore) | 8 | pokeapi-co |
| 6 | Fix inEggGroup URIs (colon → underscore) | 15 | pokeapi-co, bulbapedia |
| 7 | Add rdfs:label to Berry instances | 64 | pokeapi-co |
| 8 | Add rdf:type to QuantityValue nodes (pokeapi-co) | 64 | pokeapi-co |
| 9 | Add rdfs:label to Shape instances | 14 | default |
| 10 | Rename PokeType_Water → PokéType_Water | 6 triples | default |

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

## Patch 4: Fix Shape URIs

#### Problem
Species reference shapes via `hasShape` using colon-separated URIs (e.g., `Shape:Upright`) but the actual Shape instances use underscore URIs (`Shape_Upright`). This means all 14 `hasShape` references are dangling — they point to URIs with no corresponding `rdf:type` declaration.

The mismatch exists in two named graphs: `pokeapi-co` and `bulbapedia`.

#### Verification Query
```sparql
PREFIX pkmn: <https://pokemonkg.org/ontology#>

SELECT DISTINCT ?shape WHERE {
  GRAPH ?g { ?s pkmn:hasShape ?shape }
  FILTER(CONTAINS(STR(?shape), "Shape:"))
}
ORDER BY ?shape
```

Expected result before fix: 14 URIs with colon separator (`Shape:Armor`, `Shape:Arms`, etc.).

#### Fix Query
```sparql
PREFIX pkmn: <https://pokemonkg.org/ontology#>

DELETE {
  GRAPH ?g { ?s pkmn:hasShape ?oldShape }
}
INSERT {
  GRAPH ?g { ?s pkmn:hasShape ?newShape }
}
WHERE {
  VALUES ?g {
    <http://pokemon.outofbits.com/dataset/pokeapi-co>
    <https://pokemonkg.org/dataset/bulbapedia>
  }
  GRAPH ?g { ?s pkmn:hasShape ?oldShape }
  FILTER(CONTAINS(STR(?oldShape), "Shape:"))
  BIND(IRI(REPLACE(STR(?oldShape), "Shape:", "Shape_")) AS ?newShape)
}
```

#### Post-Fix Verification
```sparql
PREFIX pkmn: <https://pokemonkg.org/ontology#>

SELECT DISTINCT ?shape WHERE {
  ?s pkmn:hasShape ?shape .
  ?shape a pkmn:Shape .
}
ORDER BY ?shape
```

Expected result: 14 Shape URIs with underscore separator, all resolving to actual Shape instances.

#### Rollback Query
```sparql
PREFIX pkmn: <https://pokemonkg.org/ontology#>

DELETE {
  GRAPH ?g { ?s pkmn:hasShape ?oldShape }
}
INSERT {
  GRAPH ?g { ?s pkmn:hasShape ?newShape }
}
WHERE {
  VALUES ?g {
    <http://pokemon.outofbits.com/dataset/pokeapi-co>
    <https://pokemonkg.org/dataset/bulbapedia>
  }
  GRAPH ?g { ?s pkmn:hasShape ?oldShape }
  FILTER(CONTAINS(STR(?oldShape), "Shape_"))
  BIND(IRI(REPLACE(STR(?oldShape), "Shape_", "Shape:")) AS ?newShape)
}
```

---

## Patch 5: Fix Habitat URIs

#### Problem
Species reference habitats via `foundIn` using colon-separated URIs (e.g., `Habitat:Cave`) but the actual Habitat instances use underscore URIs (`Habitat_Cave`). All 8 referenced habitats are dangling references.

The mismatch exists only in the `pokeapi-co` graph. Note: `Habitat_Rare` exists as a declared instance but has no Species references.

#### Verification Query
```sparql
PREFIX pkmn: <https://pokemonkg.org/ontology#>

SELECT DISTINCT ?habitat WHERE {
  GRAPH ?g { ?s pkmn:foundIn ?habitat }
  FILTER(CONTAINS(STR(?habitat), "Habitat:"))
}
ORDER BY ?habitat
```

Expected result before fix: 8 URIs with colon separator (`Habitat:Cave`, `Habitat:Forest`, etc.).

#### Fix Query
```sparql
PREFIX pkmn: <https://pokemonkg.org/ontology#>

DELETE {
  GRAPH <http://pokemon.outofbits.com/dataset/pokeapi-co> {
    ?s pkmn:foundIn ?oldHabitat
  }
}
INSERT {
  GRAPH <http://pokemon.outofbits.com/dataset/pokeapi-co> {
    ?s pkmn:foundIn ?newHabitat
  }
}
WHERE {
  GRAPH <http://pokemon.outofbits.com/dataset/pokeapi-co> {
    ?s pkmn:foundIn ?oldHabitat
  }
  FILTER(CONTAINS(STR(?oldHabitat), "Habitat:"))
  BIND(IRI(REPLACE(STR(?oldHabitat), "Habitat:", "Habitat_")) AS ?newHabitat)
}
```

#### Post-Fix Verification
```sparql
PREFIX pkmn: <https://pokemonkg.org/ontology#>

SELECT DISTINCT ?habitat WHERE {
  ?s pkmn:foundIn ?habitat .
  ?habitat a pkmn:Habitat .
}
ORDER BY ?habitat
```

Expected result: 8 Habitat URIs with underscore separator, all resolving to actual Habitat instances.

#### Rollback Query
```sparql
PREFIX pkmn: <https://pokemonkg.org/ontology#>

DELETE {
  GRAPH <http://pokemon.outofbits.com/dataset/pokeapi-co> {
    ?s pkmn:foundIn ?oldHabitat
  }
}
INSERT {
  GRAPH <http://pokemon.outofbits.com/dataset/pokeapi-co> {
    ?s pkmn:foundIn ?newHabitat
  }
}
WHERE {
  GRAPH <http://pokemon.outofbits.com/dataset/pokeapi-co> {
    ?s pkmn:foundIn ?oldHabitat
  }
  FILTER(CONTAINS(STR(?oldHabitat), "Habitat_"))
  BIND(IRI(REPLACE(STR(?oldHabitat), "Habitat_", "Habitat:")) AS ?newHabitat)
}
```

---

## Patch 6: Fix EggGroup URIs

#### Problem
Species reference egg groups via `inEggGroup` using colon-separated URIs (e.g., `EggGroup:Bug`) but the actual EggGroup instances use underscore URIs (`EggGroup_Bug`). All 15 referenced egg groups are dangling references. Species can belong to multiple egg groups, so there are more triples affected than the 15 distinct values.

The mismatch exists in two named graphs: `pokeapi-co` and `bulbapedia`.

#### Verification Query
```sparql
PREFIX pkmn: <https://pokemonkg.org/ontology#>

SELECT DISTINCT ?eg WHERE {
  GRAPH ?g { ?s pkmn:inEggGroup ?eg }
  FILTER(CONTAINS(STR(?eg), "EggGroup:"))
}
ORDER BY ?eg
```

Expected result before fix: 15 URIs with colon separator (`EggGroup:Amorphous`, `EggGroup:Bug`, etc.).

#### Fix Query
```sparql
PREFIX pkmn: <https://pokemonkg.org/ontology#>

DELETE {
  GRAPH ?g { ?s pkmn:inEggGroup ?oldEg }
}
INSERT {
  GRAPH ?g { ?s pkmn:inEggGroup ?newEg }
}
WHERE {
  VALUES ?g {
    <http://pokemon.outofbits.com/dataset/pokeapi-co>
    <https://pokemonkg.org/dataset/bulbapedia>
  }
  GRAPH ?g { ?s pkmn:inEggGroup ?oldEg }
  FILTER(CONTAINS(STR(?oldEg), "EggGroup:"))
  BIND(IRI(REPLACE(STR(?oldEg), "EggGroup:", "EggGroup_")) AS ?newEg)
}
```

#### Post-Fix Verification
```sparql
PREFIX pkmn: <https://pokemonkg.org/ontology#>

SELECT DISTINCT ?eg WHERE {
  ?s pkmn:inEggGroup ?eg .
  ?eg a pkmn:EggGroup .
}
ORDER BY ?eg
```

Expected result: 15 EggGroup URIs with underscore separator, all resolving to actual EggGroup instances.

#### Rollback Query
```sparql
PREFIX pkmn: <https://pokemonkg.org/ontology#>

DELETE {
  GRAPH ?g { ?s pkmn:inEggGroup ?oldEg }
}
INSERT {
  GRAPH ?g { ?s pkmn:inEggGroup ?newEg }
}
WHERE {
  VALUES ?g {
    <http://pokemon.outofbits.com/dataset/pokeapi-co>
    <https://pokemonkg.org/dataset/bulbapedia>
  }
  GRAPH ?g { ?s pkmn:inEggGroup ?oldEg }
  FILTER(CONTAINS(STR(?oldEg), "EggGroup_"))
  BIND(IRI(REPLACE(STR(?oldEg), "EggGroup_", "EggGroup:")) AS ?newEg)
}
```

---

## Patch 7: Add Berry Labels

#### Problem
Berry instances have no `rdfs:label` property. The only way to identify a berry by name is to parse the URI local name (e.g., `berry/cheri` → "Cheri"). This makes it difficult to display berry names in query results or UI.

All 64 berries are affected, all in the `pokeapi-co` graph.

#### Verification Query
```sparql
PREFIX pkmn: <https://pokemonkg.org/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT (COUNT(*) as ?unlabeled) WHERE {
  GRAPH <http://pokemon.outofbits.com/dataset/pokeapi-co> {
    ?berry a pkmn:Berry .
    FILTER NOT EXISTS { ?berry rdfs:label ?label }
  }
}
```

Expected result before fix: 64 unlabeled berries.

#### Fix Query
```sparql
PREFIX pkmn: <https://pokemonkg.org/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

INSERT {
  GRAPH <http://pokemon.outofbits.com/dataset/pokeapi-co> {
    ?berry rdfs:label ?label .
  }
}
WHERE {
  GRAPH <http://pokemon.outofbits.com/dataset/pokeapi-co> {
    ?berry a pkmn:Berry .
    FILTER NOT EXISTS { ?berry rdfs:label ?any }
  }
  BIND(REPLACE(STR(?berry), ".*/", "") AS ?rawName)
  BIND(CONCAT(UCASE(SUBSTR(?rawName, 1, 1)), SUBSTR(?rawName, 2)) AS ?label)
}
```

#### Post-Fix Verification
```sparql
PREFIX pkmn: <https://pokemonkg.org/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?berry ?label WHERE {
  GRAPH <http://pokemon.outofbits.com/dataset/pokeapi-co> {
    ?berry a pkmn:Berry ;
           rdfs:label ?label .
  }
}
ORDER BY ?label
```

Expected result: 64 berries with capitalized labels (Aguav, Apicot, Aspear, ..., Yache).

#### Rollback Query
```sparql
PREFIX pkmn: <https://pokemonkg.org/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

DELETE {
  GRAPH <http://pokemon.outofbits.com/dataset/pokeapi-co> {
    ?berry rdfs:label ?label .
  }
}
WHERE {
  GRAPH <http://pokemon.outofbits.com/dataset/pokeapi-co> {
    ?berry a pkmn:Berry ;
           rdfs:label ?label .
  }
}
```

---

## Patch 9: Add Shape Labels

#### Problem
Shape instances have no `rdfs:label` property. When `hasShape` is inlined, the ORM tries to materialize Shape objects but fails validation because `name` (mapped from `rdfs:label`) is required. The 14 Shape instances live in the default graph.

#### Verification Query
```sparql
PREFIX pkmn: <https://pokemonkg.org/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT (COUNT(*) as ?unlabeled) WHERE {
  ?shape a pkmn:Shape .
  FILTER NOT EXISTS { ?shape rdfs:label ?label }
}
```

Expected result before fix: 14 unlabeled Shape instances.

#### Fix Query
```sparql
PREFIX pkmn: <https://pokemonkg.org/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

INSERT {
  ?shape rdfs:label ?label .
}
WHERE {
  ?shape a pkmn:Shape .
  FILTER NOT EXISTS { ?shape rdfs:label ?any }
  BIND(REPLACE(STR(?shape), ".*Shape_", "") AS ?label)
}
```

#### Post-Fix Verification
```sparql
PREFIX pkmn: <https://pokemonkg.org/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?shape ?label WHERE {
  ?shape a pkmn:Shape ;
         rdfs:label ?label .
}
ORDER BY ?label
```

Expected result: 14 Shapes with labels (Armor, Arms, Ball, Blob, BugWings, Fish, Heads, Humanoid, Legs, Quadruped, Squiggle, Tentacles, Upright, Wings).

#### Rollback Query
```sparql
PREFIX pkmn: <https://pokemonkg.org/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

DELETE {
  ?shape rdfs:label ?label .
}
WHERE {
  ?shape a pkmn:Shape ;
         rdfs:label ?label .
}
```

---

## Patch 8: Add QuantityValue Types (pokeapi-co)

#### Problem
QuantityValue nodes for berry sizes in the `pokeapi-co` graph have no explicit `rdf:type`. This is the same issue as Patch 2, but Patch 2 only covered the `bulbapedia` graph (Species height/weight). Berry size data lives in `pokeapi-co`, so those 64 QuantityValue nodes remain untyped, preventing ORM materialization.

#### Verification Query
```sparql
PREFIX qudt: <http://qudt.org/schema/qudt/>

SELECT (COUNT(*) as ?untyped) WHERE {
  GRAPH <http://pokemon.outofbits.com/dataset/pokeapi-co> {
    ?qty qudt:quantityValue ?qv .
    ?qv qudt:value ?val .
    FILTER NOT EXISTS { ?qv a qudt:QuantityValue }
  }
}
```

Expected result before fix: 64 untyped QuantityValue nodes.

#### Fix Query
```sparql
PREFIX qudt: <http://qudt.org/schema/qudt/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

INSERT {
  GRAPH <http://pokemon.outofbits.com/dataset/pokeapi-co> {
    ?qv rdf:type qudt:QuantityValue .
  }
}
WHERE {
  GRAPH <http://pokemon.outofbits.com/dataset/pokeapi-co> {
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
  GRAPH <http://pokemon.outofbits.com/dataset/pokeapi-co> {
    ?qv a qudt:QuantityValue .
  }
}
```

Expected result: 64 typed QuantityValue instances.

#### Rollback Query
```sparql
PREFIX qudt: <http://qudt.org/schema/qudt/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

DELETE {
  GRAPH <http://pokemon.outofbits.com/dataset/pokeapi-co> {
    ?qv rdf:type qudt:QuantityValue .
  }
}
WHERE {
  GRAPH <http://pokemon.outofbits.com/dataset/pokeapi-co> {
    ?qv a qudt:QuantityValue .
    ?qv qudt:value ?val .
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
sparql -P supply update -f patch4.sparql
sparql -P supply update -f patch5.sparql
sparql -P supply update -f patch6.sparql
sparql -P supply update -f patch7.sparql
sparql -P supply update -f patch8.sparql
sparql -P supply update -f patch9.sparql
```

Verify each patch after execution using the post-fix verification queries above.

---

## Patch 10: Rename PokeType_Water → PokéType_Water

#### Problem
The Water type instance URI uses `PokeType_Water` (no accent) while all other 17 type instances use `PokéType_*` (with accent). Meanwhile, 321 species reference `PokéType_Water` (with accent) via `hasType`, creating a dangling reference — the species point to a URI that has no instance data.

This causes Pydantic validation failures during ORM hydration because the deserializer cannot resolve `PokéType_Water` into a `Type` object.

#### Verification Query
```sparql
PREFIX pkmn: <https://pokemonkg.org/ontology#>

SELECT
  (COUNT(DISTINCT ?ref) AS ?species_referencing_accented)
WHERE {
  ?ref pkmn:hasType <https://pokemonkg.org/ontology#PokéType_Water> .
}
```

Confirm the non-accented instance exists:
```sparql
SELECT ?p ?o WHERE {
  <https://pokemonkg.org/ontology#PokeType_Water> ?p ?o .
}
```

Expected: 321 species reference the accented URI; the non-accented URI has ~6 triples.

#### Fix Query
```sparql
DELETE {
  <https://pokemonkg.org/ontology#PokeType_Water> ?p ?o .
}
INSERT {
  <https://pokemonkg.org/ontology#PokéType_Water> ?p ?o .
}
WHERE {
  <https://pokemonkg.org/ontology#PokeType_Water> ?p ?o .
}
```

#### Post-Fix Verification
```sparql
PREFIX pkmn: <https://pokemonkg.org/ontology#>

SELECT ?type WHERE {
  ?type a pkmn:Type .
  FILTER(CONTAINS(STR(?type), "Water"))
}
```

Expected: Only `PokéType_Water` (accented) should exist as a Type instance. No `PokeType_Water` (non-accented) should remain.

```sparql
SELECT (COUNT(*) AS ?cnt) WHERE {
  <https://pokemonkg.org/ontology#PokeType_Water> ?p ?o .
}
```

Expected: 0 triples for the old URI.

#### Rollback Query
```sparql
DELETE {
  <https://pokemonkg.org/ontology#PokéType_Water> ?p ?o .
}
INSERT {
  <https://pokemonkg.org/ontology#PokeType_Water> ?p ?o .
}
WHERE {
  <https://pokemonkg.org/ontology#PokéType_Water> ?p ?o .
  FILTER(?p != <https://pokemonkg.org/ontology#hasType>)
}
```

Note: The rollback uses a FILTER to only move back the instance's own triples (rdf:type, rdfs:label, rdfs:comment), not the `hasType` references from species.
