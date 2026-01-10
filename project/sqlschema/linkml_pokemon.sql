-- # Class: Ability
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Class: BattleItem Description: Battle items are items that can be used during battles.
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Class: Berry
--     * Slot: hasSize
--     * Slot: firmness
--     * Slot: smoothness
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Class: EggGroup
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Class: Flavor
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Class: Food
--     * Slot: firmness
--     * Slot: smoothness
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Class: Game Description: A game is a type of media that can be played by people.
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Class: Generation
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Class: Gym Description: A gym is a location that can be battled at.
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Class: GymLeader
--     * Slot: depiction Description: A depiction of the person
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Class: HM Description: Hidden Machine
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Class: Habitat Description: A habitat is a type of environment that certain Pokemon belong to.
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Class: HoldItem Description: A hold item is an item that can be held by a Pokemon.
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Class: Item
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Class: Pokedex
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Class: Pokemon Description: A Pokemon
--     * Slot: id
-- # Class: PokedexEntry Description: A pokedex entry is a description of a Pokemon.
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Class: Pokeball
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Abstract Class: Place
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Class: Shape Description: Shapes are categories that certain Pokemon belong to, which determine which Pokemon they can breed with.
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Class: Region
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Class: Species Description: A species is a category of Pokemon that share common features.
--     * Slot: hasColour Description: A Pokemon has a color
--     * Slot: depiction Description: A depiction of the person
--     * Slot: hasShape Description: The shape of a berry is a measure of how good it  is for making a Potion.
--     * Slot: hasGenus
--     * Slot: hasCatchRate
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
--     * Slot: hasHeight_id
--     * Slot: hasWeight_id
-- # Class: Move
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Class: MoveLearning Description: A move learning is a way that a Pokemon can learn a move.
--     * Slot: id
-- # Class: LearningByLevelingUp Description: A move that is learned by leveling up.
--     * Slot: id
-- # Class: LearningThroughBreeding Description: A move that is learned by breeding.
--     * Slot: id
-- # Class: Medicine Description: Medicine items can heal various afflictions of a Pokemon.
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Class: SpecialMove Description: A special move is a type of move that can be used during battles.
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Class: PhysicalMove Description: A physical move is a type of move that can be used during battles.
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Class: StatusMove Description: A status move is a type of move that can be used during battles.
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Class: TM
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Class: Town Description: A town is a type of place that can be visited.
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Class: Trainer Description: A trainer is a person who is able to catch Pokemon.
--     * Slot: depiction Description: A depiction of the person
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Class: Type
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
--     * Slot: Species_id Description: Autocreated FK slot
--     * Slot: Move_id Description: Autocreated FK slot
--     * Slot: SpecialMove_id Description: Autocreated FK slot
--     * Slot: PhysicalMove_id Description: Autocreated FK slot
--     * Slot: StatusMove_id Description: Autocreated FK slot
-- # Abstract Class: Thing Description: An rdfs:Resource that defines name and description
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Abstract Class: NamedIndividual Description: A Thing that requires a name
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Class: Person Description: A person is a human being
--     * Slot: depiction Description: A depiction of the person
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Class: Colour Description: Color or colour is the visual perceptual property corresponding in humans to the categories called red, yellow, blue and others.
--     * Slot: black Description: Black component in CMYK color model
--     * Slot: cyanic Description: Cyan component in CMYK color model
--     * Slot: magenta Description: Magenta component in CMYK color model
--     * Slot: yellow Description: Yellow component in CMYK color model
--     * Slot: hue Description: Hue component in HSV color model
--     * Slot: saturation Description: Saturation component in HSV color model
--     * Slot: value Description: Value/Lightness component in HSV color model
--     * Slot: red Description: Red component in RGB color model (0-255)
--     * Slot: green Description: Green component in RGB color model (0-255)
--     * Slot: blue Description: Blue component in RGB color model (0-255)
--     * Slot: wavelength Description: The wavelength of the color in nanometers
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Class: Quantity Description: A physical quantity.
--     * Slot: hasValue Description: The numeric value of the quantity.
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
--     * Slot: hasQuantityKind_id Description: The kind of quantity (e.g., Length, Mass, Time).
-- # Class: QuantityKind
--     * Slot: id
-- # Class: Unit Description: A unit of measure.
--     * Slot: id Description: A unique identifier
--     * Slot: name Description: Human-readable label for the entity
--     * Slot: description Description: A description of the entity
-- # Class: Ability_effectDescription
--     * Slot: Ability_id Description: Autocreated FK slot
--     * Slot: effectDescription Description: A description of the effect of the entity
-- # Class: Berry_hasFlavor
--     * Slot: Berry_id Description: Autocreated FK slot
--     * Slot: hasFlavor_id Description: A Pokemon has a flavor
-- # Class: Food_hasFlavor
--     * Slot: Food_id Description: Autocreated FK slot
--     * Slot: hasFlavor_id Description: A Pokemon has a flavor
-- # Class: Generation_featuresSpecies
--     * Slot: Generation_id Description: Autocreated FK slot
--     * Slot: featuresSpecies_id Description: ['A Pokedex entry features a species']
-- # Class: Species_mayHaveHiddenAbility
--     * Slot: Species_id Description: Autocreated FK slot
--     * Slot: mayHaveHiddenAbility_id
-- # Class: Species_mayHaveAbility
--     * Slot: Species_id Description: Autocreated FK slot
--     * Slot: mayHaveAbility_id Description: A Pokemon may have an ability
-- # Class: Species_isAbleToApply
--     * Slot: Species_id Description: Autocreated FK slot
--     * Slot: isAbleToApply_id
-- # Class: Species_inEggGroup
--     * Slot: Species_id Description: Autocreated FK slot
--     * Slot: inEggGroup_id
-- # Class: Species_foundIn
--     * Slot: Species_id Description: Autocreated FK slot
--     * Slot: foundIn_id Description: A place is found in a location
-- # Class: Move_effectDescription
--     * Slot: Move_id Description: Autocreated FK slot
--     * Slot: effectDescription Description: A description of the effect of the entity
-- # Class: SpecialMove_effectDescription
--     * Slot: SpecialMove_id Description: Autocreated FK slot
--     * Slot: effectDescription Description: A description of the effect of the entity
-- # Class: PhysicalMove_effectDescription
--     * Slot: PhysicalMove_id Description: Autocreated FK slot
--     * Slot: effectDescription Description: A description of the effect of the entity
-- # Class: StatusMove_effectDescription
--     * Slot: StatusMove_id Description: Autocreated FK slot
--     * Slot: effectDescription Description: A description of the effect of the entity
-- # Class: Quantity_hasUnit
--     * Slot: Quantity_id Description: Autocreated FK slot
--     * Slot: hasUnit_id

CREATE TABLE "Ability" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Ability_id" ON "Ability" (id);

CREATE TABLE "BattleItem" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_BattleItem_id" ON "BattleItem" (id);

CREATE TABLE "Berry" (
	"hasSize" TEXT,
	firmness INTEGER,
	smoothness INTEGER,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Berry_id" ON "Berry" (id);

CREATE TABLE "EggGroup" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_EggGroup_id" ON "EggGroup" (id);

CREATE TABLE "Flavor" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Flavor_id" ON "Flavor" (id);

CREATE TABLE "Food" (
	firmness INTEGER,
	smoothness INTEGER,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Food_id" ON "Food" (id);

CREATE TABLE "Game" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Game_id" ON "Game" (id);

CREATE TABLE "Generation" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Generation_id" ON "Generation" (id);

CREATE TABLE "Gym" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Gym_id" ON "Gym" (id);

CREATE TABLE "GymLeader" (
	depiction TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_GymLeader_id" ON "GymLeader" (id);

CREATE TABLE "HM" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_HM_id" ON "HM" (id);

CREATE TABLE "Habitat" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Habitat_id" ON "Habitat" (id);

CREATE TABLE "HoldItem" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_HoldItem_id" ON "HoldItem" (id);

CREATE TABLE "Item" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Item_id" ON "Item" (id);

CREATE TABLE "Pokedex" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Pokedex_id" ON "Pokedex" (id);

CREATE TABLE "Pokemon" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Pokemon_id" ON "Pokemon" (id);

CREATE TABLE "PokedexEntry" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_PokedexEntry_id" ON "PokedexEntry" (id);

CREATE TABLE "Pokeball" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Pokeball_id" ON "Pokeball" (id);

CREATE TABLE "Place" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Place_id" ON "Place" (id);

CREATE TABLE "Shape" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Shape_id" ON "Shape" (id);

CREATE TABLE "Region" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Region_id" ON "Region" (id);

CREATE TABLE "Move" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Move_id" ON "Move" (id);

CREATE TABLE "MoveLearning" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_MoveLearning_id" ON "MoveLearning" (id);

CREATE TABLE "LearningByLevelingUp" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_LearningByLevelingUp_id" ON "LearningByLevelingUp" (id);

CREATE TABLE "LearningThroughBreeding" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_LearningThroughBreeding_id" ON "LearningThroughBreeding" (id);

CREATE TABLE "Medicine" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Medicine_id" ON "Medicine" (id);

CREATE TABLE "SpecialMove" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_SpecialMove_id" ON "SpecialMove" (id);

CREATE TABLE "PhysicalMove" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_PhysicalMove_id" ON "PhysicalMove" (id);

CREATE TABLE "StatusMove" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_StatusMove_id" ON "StatusMove" (id);

CREATE TABLE "TM" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_TM_id" ON "TM" (id);

CREATE TABLE "Town" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Town_id" ON "Town" (id);

CREATE TABLE "Trainer" (
	depiction TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Trainer_id" ON "Trainer" (id);

CREATE TABLE "Thing" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Thing_id" ON "Thing" (id);

CREATE TABLE "NamedIndividual" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_NamedIndividual_id" ON "NamedIndividual" (id);

CREATE TABLE "Person" (
	depiction TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Person_id" ON "Person" (id);

CREATE TABLE "Colour" (
	black FLOAT,
	cyanic FLOAT,
	magenta FLOAT,
	yellow FLOAT,
	hue FLOAT,
	saturation FLOAT,
	value FLOAT,
	red INTEGER,
	green INTEGER,
	blue INTEGER,
	wavelength FLOAT,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Colour_id" ON "Colour" (id);

CREATE TABLE "QuantityKind" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_QuantityKind_id" ON "QuantityKind" (id);

CREATE TABLE "Unit" (
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Unit_id" ON "Unit" (id);

CREATE TABLE "Quantity" (
	"hasValue" TEXT,
	id TEXT NOT NULL,
	name TEXT,
	description TEXT,
	"hasQuantityKind_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("hasQuantityKind_id") REFERENCES "QuantityKind" (id)
);
CREATE INDEX "ix_Quantity_id" ON "Quantity" (id);

CREATE TABLE "Ability_effectDescription" (
	"Ability_id" TEXT,
	"effectDescription" TEXT,
	PRIMARY KEY ("Ability_id", "effectDescription"),
	FOREIGN KEY("Ability_id") REFERENCES "Ability" (id)
);
CREATE INDEX "ix_Ability_effectDescription_effectDescription" ON "Ability_effectDescription" ("effectDescription");
CREATE INDEX "ix_Ability_effectDescription_Ability_id" ON "Ability_effectDescription" ("Ability_id");

CREATE TABLE "Berry_hasFlavor" (
	"Berry_id" TEXT,
	"hasFlavor_id" TEXT,
	PRIMARY KEY ("Berry_id", "hasFlavor_id"),
	FOREIGN KEY("Berry_id") REFERENCES "Berry" (id),
	FOREIGN KEY("hasFlavor_id") REFERENCES "Flavor" (id)
);
CREATE INDEX "ix_Berry_hasFlavor_Berry_id" ON "Berry_hasFlavor" ("Berry_id");
CREATE INDEX "ix_Berry_hasFlavor_hasFlavor_id" ON "Berry_hasFlavor" ("hasFlavor_id");

CREATE TABLE "Food_hasFlavor" (
	"Food_id" TEXT,
	"hasFlavor_id" TEXT,
	PRIMARY KEY ("Food_id", "hasFlavor_id"),
	FOREIGN KEY("Food_id") REFERENCES "Food" (id),
	FOREIGN KEY("hasFlavor_id") REFERENCES "Flavor" (id)
);
CREATE INDEX "ix_Food_hasFlavor_Food_id" ON "Food_hasFlavor" ("Food_id");
CREATE INDEX "ix_Food_hasFlavor_hasFlavor_id" ON "Food_hasFlavor" ("hasFlavor_id");

CREATE TABLE "Move_effectDescription" (
	"Move_id" TEXT,
	"effectDescription" TEXT,
	PRIMARY KEY ("Move_id", "effectDescription"),
	FOREIGN KEY("Move_id") REFERENCES "Move" (id)
);
CREATE INDEX "ix_Move_effectDescription_effectDescription" ON "Move_effectDescription" ("effectDescription");
CREATE INDEX "ix_Move_effectDescription_Move_id" ON "Move_effectDescription" ("Move_id");

CREATE TABLE "SpecialMove_effectDescription" (
	"SpecialMove_id" TEXT,
	"effectDescription" TEXT,
	PRIMARY KEY ("SpecialMove_id", "effectDescription"),
	FOREIGN KEY("SpecialMove_id") REFERENCES "SpecialMove" (id)
);
CREATE INDEX "ix_SpecialMove_effectDescription_effectDescription" ON "SpecialMove_effectDescription" ("effectDescription");
CREATE INDEX "ix_SpecialMove_effectDescription_SpecialMove_id" ON "SpecialMove_effectDescription" ("SpecialMove_id");

CREATE TABLE "PhysicalMove_effectDescription" (
	"PhysicalMove_id" TEXT,
	"effectDescription" TEXT,
	PRIMARY KEY ("PhysicalMove_id", "effectDescription"),
	FOREIGN KEY("PhysicalMove_id") REFERENCES "PhysicalMove" (id)
);
CREATE INDEX "ix_PhysicalMove_effectDescription_effectDescription" ON "PhysicalMove_effectDescription" ("effectDescription");
CREATE INDEX "ix_PhysicalMove_effectDescription_PhysicalMove_id" ON "PhysicalMove_effectDescription" ("PhysicalMove_id");

CREATE TABLE "StatusMove_effectDescription" (
	"StatusMove_id" TEXT,
	"effectDescription" TEXT,
	PRIMARY KEY ("StatusMove_id", "effectDescription"),
	FOREIGN KEY("StatusMove_id") REFERENCES "StatusMove" (id)
);
CREATE INDEX "ix_StatusMove_effectDescription_effectDescription" ON "StatusMove_effectDescription" ("effectDescription");
CREATE INDEX "ix_StatusMove_effectDescription_StatusMove_id" ON "StatusMove_effectDescription" ("StatusMove_id");

CREATE TABLE "Species" (
	"hasColour" TEXT,
	depiction TEXT,
	"hasShape" TEXT,
	"hasGenus" TEXT,
	"hasCatchRate" INTEGER,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	"hasHeight_id" TEXT,
	"hasWeight_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("hasColour") REFERENCES "Colour" (id),
	FOREIGN KEY("hasShape") REFERENCES "Shape" (id),
	FOREIGN KEY("hasHeight_id") REFERENCES "Quantity" (id),
	FOREIGN KEY("hasWeight_id") REFERENCES "Quantity" (id)
);
CREATE INDEX "ix_Species_id" ON "Species" (id);

CREATE TABLE "Quantity_hasUnit" (
	"Quantity_id" TEXT,
	"hasUnit_id" TEXT,
	PRIMARY KEY ("Quantity_id", "hasUnit_id"),
	FOREIGN KEY("Quantity_id") REFERENCES "Quantity" (id),
	FOREIGN KEY("hasUnit_id") REFERENCES "Unit" (id)
);
CREATE INDEX "ix_Quantity_hasUnit_Quantity_id" ON "Quantity_hasUnit" ("Quantity_id");
CREATE INDEX "ix_Quantity_hasUnit_hasUnit_id" ON "Quantity_hasUnit" ("hasUnit_id");

CREATE TABLE "Type" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	"Species_id" TEXT,
	"Move_id" TEXT,
	"SpecialMove_id" TEXT,
	"PhysicalMove_id" TEXT,
	"StatusMove_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Species_id") REFERENCES "Species" (id),
	FOREIGN KEY("Move_id") REFERENCES "Move" (id),
	FOREIGN KEY("SpecialMove_id") REFERENCES "SpecialMove" (id),
	FOREIGN KEY("PhysicalMove_id") REFERENCES "PhysicalMove" (id),
	FOREIGN KEY("StatusMove_id") REFERENCES "StatusMove" (id)
);
CREATE INDEX "ix_Type_id" ON "Type" (id);

CREATE TABLE "Generation_featuresSpecies" (
	"Generation_id" TEXT,
	"featuresSpecies_id" TEXT,
	PRIMARY KEY ("Generation_id", "featuresSpecies_id"),
	FOREIGN KEY("Generation_id") REFERENCES "Generation" (id),
	FOREIGN KEY("featuresSpecies_id") REFERENCES "Species" (id)
);
CREATE INDEX "ix_Generation_featuresSpecies_Generation_id" ON "Generation_featuresSpecies" ("Generation_id");
CREATE INDEX "ix_Generation_featuresSpecies_featuresSpecies_id" ON "Generation_featuresSpecies" ("featuresSpecies_id");

CREATE TABLE "Species_mayHaveHiddenAbility" (
	"Species_id" TEXT,
	"mayHaveHiddenAbility_id" TEXT,
	PRIMARY KEY ("Species_id", "mayHaveHiddenAbility_id"),
	FOREIGN KEY("Species_id") REFERENCES "Species" (id),
	FOREIGN KEY("mayHaveHiddenAbility_id") REFERENCES "Ability" (id)
);
CREATE INDEX "ix_Species_mayHaveHiddenAbility_mayHaveHiddenAbility_id" ON "Species_mayHaveHiddenAbility" ("mayHaveHiddenAbility_id");
CREATE INDEX "ix_Species_mayHaveHiddenAbility_Species_id" ON "Species_mayHaveHiddenAbility" ("Species_id");

CREATE TABLE "Species_mayHaveAbility" (
	"Species_id" TEXT,
	"mayHaveAbility_id" TEXT,
	PRIMARY KEY ("Species_id", "mayHaveAbility_id"),
	FOREIGN KEY("Species_id") REFERENCES "Species" (id),
	FOREIGN KEY("mayHaveAbility_id") REFERENCES "Ability" (id)
);
CREATE INDEX "ix_Species_mayHaveAbility_mayHaveAbility_id" ON "Species_mayHaveAbility" ("mayHaveAbility_id");
CREATE INDEX "ix_Species_mayHaveAbility_Species_id" ON "Species_mayHaveAbility" ("Species_id");

CREATE TABLE "Species_isAbleToApply" (
	"Species_id" TEXT,
	"isAbleToApply_id" TEXT,
	PRIMARY KEY ("Species_id", "isAbleToApply_id"),
	FOREIGN KEY("Species_id") REFERENCES "Species" (id),
	FOREIGN KEY("isAbleToApply_id") REFERENCES "Move" (id)
);
CREATE INDEX "ix_Species_isAbleToApply_isAbleToApply_id" ON "Species_isAbleToApply" ("isAbleToApply_id");
CREATE INDEX "ix_Species_isAbleToApply_Species_id" ON "Species_isAbleToApply" ("Species_id");

CREATE TABLE "Species_inEggGroup" (
	"Species_id" TEXT,
	"inEggGroup_id" TEXT,
	PRIMARY KEY ("Species_id", "inEggGroup_id"),
	FOREIGN KEY("Species_id") REFERENCES "Species" (id),
	FOREIGN KEY("inEggGroup_id") REFERENCES "EggGroup" (id)
);
CREATE INDEX "ix_Species_inEggGroup_Species_id" ON "Species_inEggGroup" ("Species_id");
CREATE INDEX "ix_Species_inEggGroup_inEggGroup_id" ON "Species_inEggGroup" ("inEggGroup_id");

CREATE TABLE "Species_foundIn" (
	"Species_id" TEXT,
	"foundIn_id" TEXT,
	PRIMARY KEY ("Species_id", "foundIn_id"),
	FOREIGN KEY("Species_id") REFERENCES "Species" (id),
	FOREIGN KEY("foundIn_id") REFERENCES "Habitat" (id)
);
CREATE INDEX "ix_Species_foundIn_Species_id" ON "Species_foundIn" ("Species_id");
CREATE INDEX "ix_Species_foundIn_foundIn_id" ON "Species_foundIn" ("foundIn_id");
