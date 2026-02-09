export type ThingId = string;
export type NamedIndividualId = string;
export type PersonId = string;
export type ColourId = string;
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
    
    Cave = "Cave",
    Forest = "Forest",
    Grassland = "Grassland",
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
 * Color or colour is the visual perceptual property corresponding in humans to the categories called red, yellow, blue and others.
 */
export interface Colour extends Thing {
    /** Cyan component in CMYK color model (0-100) */
    cyanic?: number,
    /** Magenta component in CMYK color model (0-100) */
    magenta?: number,
    /** Yellow component in CMYK color model (0-100) */
    colourYellow?: number,
    /** Black (K) component in CMYK color model (0-100) */
    black?: number,
    /** The wavelength of the color in meters (e.g., 4.5e-07 for blue) */
    wavelength?: number,
    /** The frequency of the color in Hz */
    frequency?: number,
    /** Hexadecimal RGB color code (e.g., "0000FF" for blue) */
    colourHexCode?: string,
    /** Cultural or symbolic meanings associated with this colour */
    connotation?: ConnotationId[],
    /** URL to a representative image of this colour */
    thumbnail?: string,
}


/**
 * Cultural or symbolic meaning associated with a colour. Imported from DBpedia as generic owl:Thing resources.
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
    hasQuantityKind?: QuantityKindId[],
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
    unit?: UnitId,
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
    hasQuantityKind?: QuantityKindId[],
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



export interface Ability extends Thing {
    /** A description of the effect of the entity */
    effectDescription?: string[],
}


/**
 * Battle items are items that can be used during battles.
 */
export interface BattleItem extends Item {
}



export interface Berry extends Food {
    hasSize?: Quantity,
}



export interface EggGroup extends NamedIndividual {
}



export interface Flavor extends NamedIndividual {
}



export interface Food extends Item {
    /** A Pokemon has a flavor */
    hasFlavor?: FlavorId[],
    firmness?: number,
    smoothness?: number,
}


/**
 * A game is a type of media that can be played by people.
 */
export interface Game extends Thing {
}



export interface Generation extends Thing {
    /** ['A Pokedex entry features a species'] */
    featuresSpecies?: SpeciesId[],
}


/**
 * A gym is a location that can be battled at.
 */
export interface Gym extends Place {
}



export interface GymLeader extends Trainer {
}


/**
 * Hidden Machine
 */
export interface HM extends Item {
}


/**
 * A habitat is a type of environment that certain Pokemon belong to.
 */
export interface Habitat extends NamedIndividual {
}


/**
 * A hold item is an item that can be held by a Pokemon.
 */
export interface HoldItem extends Item {
}



export interface Item extends Thing {
}



export interface Pokedex extends Thing {
}


/**
 * A Pokemon
 */
export interface Pokemon {
}


/**
 * A pokedex entry is a description of a Pokemon.
 */
export interface PokedexEntry extends Thing {
}



export interface Pokeball extends Item {
}



export interface Place extends Thing {
}


/**
 * Shapes are categories that certain Pokemon belong to, which determine which Pokemon they can breed with.
 */
export interface Shape extends NamedIndividual {
}



export interface Region extends Place {
}


/**
 * A species is a category of Pokemon that share common features.
 */
export interface Species extends NamedIndividual {
    /** A Pokemon has a color */
    hasColour?: ColourId,
    mayHaveHiddenAbility?: ("mayHaveAbility")[],
    /** A Pokemon may have an ability */
    mayHaveAbility?: AbilityId[],
    isAbleToApply?: MoveId[],
    hasHeight?: Quantity,
    hasWeight?: Quantity,
    /** A depiction of the person */
    depiction?: string,
    inEggGroup?: EggGroupId[],
    /** A Pokemon has a type */
    hasType?: Type[],
    /** The shape of a berry is a measure of how good it  is for making a Potion. */
    hasShape?: ShapeId,
    hasGenus?: string,
    hasCatchRate?: number,
    /** A place is found in a location */
    foundIn?: HabitatId[],
}



export interface Move extends Thing {
    /** A description of the effect of the entity */
    effectDescription?: string[],
    /** A Pokemon has a type */
    hasType?: Type[],
}


/**
 * A move learning is a way that a Pokemon can learn a move.
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
 * Medicine items can heal various afflictions of a Pokemon.
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



export interface TM extends Item, MoveLearning {
}


/**
 * A town is a type of place that can be visited.
 */
export interface Town extends Place {
}


/**
 * A trainer is a person who is able to catch Pokemon.
 */
export interface Trainer extends Person {
}



export interface Type extends NamedIndividual {
}



