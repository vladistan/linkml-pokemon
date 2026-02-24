export type ThingId = string;
export type NamedIndividualId = string;
export type PersonId = string;
export type ColorId = string;
export type ConnotationId = string;
export type ConceptId = string;
export type QuantityId = string;
export type QuantityValueId = string;
export type AbstractQuantityKindId = string;
export type QuantityKindId = string;
export type UnitId = string;
export type DerivedUnitId = string;
export type SystemOfUnitsId = string;
export type QuantityKindDimensionVectorId = string;
export type QuantityKindDimensionVectorSIId = string;
export type QuantityKindDimensionVectorCGSId = string;
export type QuantityKindDimensionVectorImperialId = string;
export type QuantityKindDimensionVectorISOId = string;
export type PrefixId = string;
export type DecimalPrefixId = string;
export type AbilityId = string;
export type BattleItemId = string;
export type BerryId = string;
export type EggGroupId = string;
export type FlavorId = string;
export type FoodId = string;
export type GameId = string;
export type GenerationId = string;
export type GymId = string;
export type GymLeaderId = string;
export type HMId = string;
export type HabitatId = string;
export type HoldItemId = string;
export type ItemId = string;
export type PokedexId = string;
export type PokedexEntryId = string;
export type PokeballId = string;
export type PlaceId = string;
export type ShapeId = string;
export type RegionId = string;
export type SpeciesId = string;
export type MoveId = string;
export type MedicineId = string;
export type SpecialMoveId = string;
export type PhysicalMoveId = string;
export type StatusMoveId = string;
export type TMId = string;
export type TownId = string;
export type TrainerId = string;
export type TypeId = string;

export enum HabitatEnum {

    /** A hollow underground area, typically formed in rocky or mountainous terrain. */
    Cave = "Cave",
    /** A dense area covered with trees and undergrowth. */
    Forest = "Forest",
    /** An open area of land covered predominantly with grasses and low vegetation. */
    Grassland = "Grassland",
    /** A large elevated landform rising steeply above the surrounding terrain. */
    Mountain = "Mountain",
    /** An uncommon or hard-to-reach environment with no single fixed location. */
    Rare = "Rare",
    /** Harsh, uneven landscape such as deserts, volcanic areas, or rocky wastelands. */
    Rough_terrain = "Rough terrain",
    /** Open deep water far from shore, including oceans and large lakes. */
    Sea = "Sea",
    /** A densely developed area with buildings, roads, and other human-made structures. */
    Urban = "Urban",
    /** The transitional zone where land meets water, including shorelines, riverbanks, and wetlands. */
    WaterAPOSTROPHEs_edge = "Water's edge",
};


/**
 * An rdfs:Resource that defines name and description
 */
export interface Thing {
    /** A unique identifier */
    id: string,
    /** Human-readable label for the entity */
    name?: string,
    /** A description of the entity */
    description?: string,
}


/**
 * A Thing that requires a name
 */
export interface NamedIndividual extends Thing {
}


/**
 * A person is a human being
 */
export interface Person extends NamedIndividual {
    /** A depiction of the person */
    depiction?: string,
}


/**
 * CMYK color space coordinates (0-100).
 */
export interface CmykColor {
    /** Cyan component in CMYK color model (0-100) */
    cmykC?: number,
    /** Magenta component in CMYK color model (0-100) */
    cmykM?: number,
    /** Yellow component in CMYK color model (0-100) */
    cmykY?: number,
    /** Black (K) component in CMYK color model (0-100) */
    cmykK?: number,
}


/**
 * Color is the visual perceptual property corresponding in humans to the categories called red, yellow, blue and others.
 */
export interface Color extends Thing, CmykColor {
    /** The wavelength of the color in meters (e.g., 4.5e-07 for blue) */
    wavelength?: number,
    /** The frequency of the color in Hz */
    frequency?: number,
    /** Hexadecimal RGB color code (e.g., "0000FF" for blue) */
    colorHexCode?: string,
    /** Cultural or symbolic meanings associated with this color */
    connotation?: ConnotationId[],
    /** URL to a representative image of this color */
    thumbnail?: string,
}


/**
 * Cultural or symbolic meaning associated with a color. Imported from DBpedia as generic owl:Thing resources.
 */
export interface Connotation extends Thing {
}


/**
 * The root class for all QUDT concepts
 */
export interface Concept extends Thing {
    /** Short alphanumeric abbreviation for a unit */
    abbreviation?: string,
    /** Whether this entity is deprecated */
    deprecated?: boolean,
    /** Plain text description */
    plainTextDescription?: string,
}


/**
 * An abstract type class that defines properties that can be reused
 */
export interface Aspect {
}


/**
 * Ascribes to some thing the capability of being measured, observed, or counted
 */
export interface Quantifiable extends Aspect {
    /** Unit associated with a quantifiable entity */
    hasUnit?: UnitId,
    /** Standard uncertainty of the measurement */
    standardUncertainty?: string,
    /** Relative standard uncertainty of the measurement */
    relativeStandardUncertainty?: number,
}


/**
 * Holds properties that provide external knowledge and specifications of a given resource
 */
export interface Verifiable extends Aspect {
    /** DBpedia URI for this entity */
    dbpediaMatch?: string,
    /** Wikidata URI for this entity */
    wikidataMatch?: string,
    /** Informative reference URL */
    informativeReference?: string[],
    /** ISO normative reference URI */
    isoNormativeReference?: string[],
    /** Normative reference URI */
    normativeReference?: string[],
}


/**
 * A measured quantity with kind and value
 */
export interface Quantity extends Concept, Quantifiable {
    /** Associates a quantity with its kind (e.g., Height, Weight) */
    hasQuantityKind?: QuantityKind[],
    /** The value component of a quantity */
    quantityValue?: QuantityValueId[],
}


/**
 * Numeric value with unit
 */
export interface QuantityValue extends Concept {
    /** Numeric value of a quantity */
    numericValue?: number,
    /** Unit of measurement */
    unit?: Unit,
}


/**
 * Abstract base for quantity kinds, constraining symbol and broader
 */
export interface AbstractQuantityKind extends Concept {
    /** Symbol for a unit (e.g., "m" for meter) */
    symbol?: string,
    /** Broader/parent quantity kind */
    broader?: QuantityKindId[],
}


/**
 * Kind of quantity (e.g., Length, Mass, Height, Weight)
 */
export interface QuantityKind extends AbstractQuantityKind, Verifiable {
    /** LaTeX representation of symbol */
    latexSymbol?: string,
    /** Dimension vector for a unit or quantity kind */
    hasDimensionVector?: QuantityKindDimensionVectorId,
    /** Units applicable to a quantity kind */
    applicableUnit?: UnitId[],
    /** Equivalent quantity kind or unit */
    exactMatch?: string[],
}


/**
 * Unit of measurement
 */
export interface Unit extends Concept, Verifiable {
    /** Symbol for a unit (e.g., "m" for meter) */
    symbol?: string,
    /** LaTeX representation of symbol */
    latexSymbol?: string,
    /** Multiplier to convert to base unit */
    conversionMultiplier?: number,
    /** Offset to convert to base unit */
    conversionOffset?: number,
    /** Dimension vector for a unit or quantity kind */
    hasDimensionVector?: QuantityKindDimensionVectorId,
    /** Associates a quantity with its kind (e.g., Height, Weight) */
    hasQuantityKind?: QuantityKind[],
    /** System of units this unit belongs to */
    isUnitOfSystem?: SystemOfUnitsId[],
    /** Systems where this unit is applicable */
    applicableSystem?: SystemOfUnitsId[],
    /** Prefix for a unit (e.g., Kilo, Milli) */
    prefix?: PrefixId,
    /** Base unit this unit is a scaling of */
    scalingOf?: UnitId,
    /** UCUM code for the unit */
    ucumCode?: string,
}


/**
 * Unit derived from base units (e.g., KiloM)
 */
export interface DerivedUnit extends Unit {
}


/**
 * A coherent system of units (e.g., SI, CGS)
 */
export interface SystemOfUnits extends Concept {
    /** Base units defined by this system */
    hasBaseUnit?: UnitId[],
    /** Prefix for a unit (e.g., Kilo, Milli) */
    prefix?: PrefixId,
}


/**
 * Dimension vector expressing quantity in base dimensions
 */
export interface QuantityKindDimensionVector extends Concept {
    /** LaTeX representation of symbol */
    latexSymbol?: string,
    /** Exponent for length dimension (L) */
    dimensionExponentForLength?: number,
    /** Exponent for mass dimension (M) */
    dimensionExponentForMass?: number,
    /** Exponent for time dimension (T) */
    dimensionExponentForTime?: number,
    /** Exponent for electric current dimension (I) */
    dimensionExponentForElectricCurrent?: number,
    /** Exponent for temperature dimension (Θ) */
    dimensionExponentForThermodynamicTemperature?: number,
    /** Exponent for amount of substance dimension (N) */
    dimensionExponentForAmountOfSubstance?: number,
    /** Exponent for luminous intensity dimension (J) */
    dimensionExponentForLuminousIntensity?: number,
    /** Dimensionless exponent */
    dimensionlessExponent?: number,
}


/**
 * SI dimension vector
 */
export interface QuantityKindDimensionVectorSI extends QuantityKindDimensionVector {
}


/**
 * CGS dimension vector
 */
export interface QuantityKindDimensionVectorCGS extends QuantityKindDimensionVector {
}


/**
 * Imperial dimension vector
 */
export interface QuantityKindDimensionVectorImperial extends QuantityKindDimensionVector {
}


/**
 * ISO dimension vector
 */
export interface QuantityKindDimensionVectorISO extends QuantityKindDimensionVector {
}


/**
 * Unit prefix (e.g., Kilo, Milli)
 */
export interface Prefix extends Concept, Verifiable {
    /** Symbol for a unit (e.g., "m" for meter) */
    symbol?: string,
    /** Numeric multiplier for the prefix (e.g., 1000 for Kilo) */
    prefixMultiplier?: number,
    /** UCUM code for the unit */
    ucumCode?: string,
    /** Equivalent quantity kind or unit */
    exactMatch?: string[],
}


/**
 * Decimal prefix (powers of 10)
 */
export interface DecimalPrefix extends Prefix {
}


/**
 * Abilities were introduced in Generation III as an all new game mechanic. Each and every Pokémon has an ability, and can only have one at a time. Some abilities are exclusive to certain Pokémon and Evolution lines, while others are known by many Pokémon.
 */
export interface Ability extends Thing {
    /** A description of the effect of the entity */
    effectDescription?: string[],
}


/**
 * Battle items are items that can be used during battles.
 */
export interface BattleItem extends Item {
}


/**
 * Berries are small, juicy, fleshy fruit. As in the real world, a large variety exists in the Pokémon world, with a large range of flavors, names, and effects. First found in the Generation II games, many Berries have since became critical help items in battle, where their various effects include HP and status condition restoration, stat enhancement, and even damage negation.
 */
export interface Berry extends Food {
    /** The physical size of an entity, expressed as a quantity with unit. */
    hasSize?: Quantity,
}


/**
 * Egg group is a category that determines which Pokémon are able to interbreed. The concept was introduced in Generation II, along with breeding. Similar to types, a Pokémon may belong to either one or two egg groups.
 */
export interface EggGroup extends NamedIndividual {
}


/**
 * Flavor is a special set of attributes that certain foods in the Pokémon world have. Most of the foods can have more than one flavor, and the flavor determines which Pokémon can eat them.
 */
export interface Flavor extends NamedIndividual {
}


/**
 * Food items are consumable items in the Pokémon world that can have flavors, firmness, and smoothness attributes.
 */
export interface Food extends Item {
    /** A Pokémon has a flavor */
    hasFlavor?: FlavorId[],
    /** How firm a berry or food item feels, affecting its use in Pokéblock or Poffin making. */
    firmness?: number,
    /** How smooth a berry or food item is, affecting its use in Pokéblock or Poffin making. */
    smoothness?: number,
}


/**
 * A game is a type of media that can be played by people.
 */
export interface Game extends Thing {
}


/**
 * Generations refers to the Pokémon game series. It is a group of games that were released at or around the same time. It also means that games in the same generation are compatible with the others, containing the same Pokémon and the number of moves there are to be learned.
 */
export interface Generation extends Thing {
    /** ['A Pokédex entry features a species'] */
    featuresSpecies?: SpeciesId[],
}


/**
 * A gym is a location that can be battled at.
 */
export interface Gym extends Place {
}


/**
 * A gym leader is the highest ranking member and owner of an official Pokémon gym. Gym leaders use their gym and their Pokémon to test the skills of trainers that challenge them, and if said trainers win a battle, the gym leader will gift them a badge that's unique to that specific gym.
 */
export interface GymLeader extends Trainer {
}


/**
 * Hidden Machine
 */
export interface HM extends Item {
}


/**
 * A habitat is a type of environment that certain Pokémon belong to.
 */
export interface Habitat extends NamedIndividual {
}


/**
 * A hold item is an item that can be held by a Pokémon.
 */
export interface HoldItem extends Item {
}


/**
 * An item is an object in the Pokémon games which the player can pick up, keep in their Bag, and use in some manner. They have various uses, including healing, powering up, helping one to catch Pokémon, or to access a new area.
 */
export interface Item extends Thing {
}


/**
 * The Pokédex is an electronic device designed to catalog and provide information regarding the various species of Pokémon featured in the Pokémon video game, anime and manga series.
 */
export interface Pokedex extends Thing {
}


/**
 * A Pokémon
 */
export interface Pokemon {
}


/**
 * A Pokédex entry is a description of a Pokémon.
 */
export interface PokedexEntry extends Thing {
}


/**
 * A Poké Ball is a type of item that is critical to a Trainer's quest, used for catching and storing Pokémon.
 */
export interface Pokeball extends Item {
}


/**
 * Entities that have a somewhat fixed, physical extension.
 */
export interface Place extends Thing {
}


/**
 * Shapes are categories that certain Pokémon belong to, which determine which Pokémon they can breed with.
 */
export interface Shape extends NamedIndividual {
}


/**
 * Regions are areas in the Pokémon universe that are smaller parts of a nation.
 */
export interface Region extends Place {
}


/**
 * A species is a category of Pokémon that share common features.
 */
export interface Species extends NamedIndividual {
    /** A Pokémon has a color */
    hasColor?: Color,
    /** A special ability only obtainable through specific encounters or events, not through normal gameplay. */
    mayHaveHiddenAbility?: ("mayHaveAbility")[],
    /** A Pokémon may have an ability */
    mayHaveAbility?: AbilityId[],
    /** Moves that a Pokémon can use in battle or in the overworld. */
    isAbleToApply?: MoveId[],
    /** How tall a Pokémon species is, expressed as a quantity with unit. */
    hasHeight?: Quantity,
    /** How heavy a Pokémon species is, expressed as a quantity with unit. */
    hasWeight?: Quantity,
    /** A depiction of the person */
    depiction?: string,
    /** Which egg group a species belongs to, controlling which Pokémon can breed together. */
    inEggGroup?: EggGroupId[],
    /** A Pokémon has a type */
    hasType?: Type[],
    /** The shape of a berry is a measure of how good it is for making a Potion. */
    hasShape?: Shape,
    /** The species category label shown in the Pokédex, such as "Seed Pokémon" for Bulbasaur. */
    hasGenus?: string,
    /** Determines how easy a Pokémon species is to catch, with higher values meaning easier capture. */
    hasCatchRate?: number,
    /** A place is found in a location */
    foundIn?: Habitat[],
}


/**
 * A move is a special ability of a Pokémon.
 */
export interface Move extends Thing {
    /** A description of the effect of the entity */
    effectDescription?: string[],
    /** A Pokémon has a type */
    hasType?: Type[],
}


/**
 * A move learning is a way that a Pokémon can learn a move.
 */
export interface MoveLearning {
}


/**
 * A move that is learned by leveling up.
 */
export interface LearningByLevelingUp extends MoveLearning {
}


/**
 * A move that is learned by breeding.
 */
export interface LearningThroughBreeding extends MoveLearning {
}


/**
 * Medicine items can heal various afflictions of a Pokémon.
 */
export interface Medicine extends Item {
}


/**
 * A special move is a type of move that can be used during battles.
 */
export interface SpecialMove extends Move {
}


/**
 * A physical move is a type of move that can be used during battles.
 */
export interface PhysicalMove extends Move {
}


/**
 * A status move is a type of move that can be used during battles.
 */
export interface StatusMove extends Move {
}


/**
 * A Technical Machine is an item that can be used to teach a Pokémon a move.
 */
export interface TM extends Item, MoveLearning {
}


/**
 * A town is a type of place that can be visited.
 */
export interface Town extends Place {
}


/**
 * A trainer is a person who is able to catch Pokémon.
 */
export interface Trainer extends Person {
}


/**
 * All Pokémon creatures and their moves are assigned certain types. Each type has several strengths and weaknesses in both attack and defense.
 */
export interface Type extends NamedIndividual {
}
