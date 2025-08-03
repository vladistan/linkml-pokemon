LINKML_SCHEMA_NAME="linkml_pokemon"
LINKML_SCHEMA_AUTHOR="Vlad Korolev <vlad@v-lad.org>"
LINKML_SCHEMA_DESCRIPTION="Pokemon Ontology expressed as LinkML"
LINKML_SCHEMA_SOURCE_PATH="src/linkml_pokemon/schema/linkml_pokemon.yaml"
LINKML_SCHEMA_GOOGLE_SHEET_ID="1wVoaiFg47aT9YWNeRfTZ8tYHN8s8PAuDx5i2HUcDpvQ"
LINKML_SCHEMA_GOOGLE_SHEET_TABS="personinfo enums"

LINKML_GENERATORS_CONFIG_YAML="--config-file config.yaml"

## pass args to workaround genowl rdfs config bug (linkml#1453)
##   (i.e. --no-type-objects --no-metaclasses --metadata-profile rdfs)
LINKML_GENERATORS_OWL_ARGS="--no-type-objects --metadata-profile rdfs"
