# config.public.mk

# This file is public in git. No sensitive info allowed.
# These variables are sourced in Makefile, following make-file conventions.
# Be aware that this file does not follow python or bash conventions, so may appear a little unfamiliar.

###### schema definition variables, used by makefile

# Note: makefile variables should not be quoted, as makefile handles quoting differently than bash
LINKML_SCHEMA_NAME=linkml_pokemon
LINKML_SCHEMA_AUTHOR=Vlad Korolev <vlad@v-lad.org>
LINKML_SCHEMA_DESCRIPTION=Pokemon Ontology expressed as LinkML
LINKML_SCHEMA_SOURCE_PATH=src/linkml_pokemon/schema/linkml_pokemon.yaml
LINKML_SCHEMA_GOOGLE_SHEET_ID=1wVoaiFg47aT9YWNeRfTZ8tYHN8s8PAuDx5i2HUcDpvQ
LINKML_SCHEMA_GOOGLE_SHEET_TABS=personinfo enums

###### linkml generator variables, used by makefile

## gen-project configuration file
LINKML_GENERATORS_CONFIG_YAML= --config-file config.yaml

## pass args if gendoc ignores config.yaml (i.e. --no-mergeimports)
LINKML_GENERATORS_DOC_ARGS=

## pass args to workaround genowl rdfs config bug (linkml#1453)
##   (i.e. --no-type-objects --no-metaclasses --metadata-profile rdfs)
LINKML_GENERATORS_OWL_ARGS= --no-type-objects --metadata-profile rdfs 

## pass args to trigger experimental java/typescript generation
LINKML_GENERATORS_JAVA_ARGS=
LINKML_GENERATORS_TYPESCRIPT_ARGS=

