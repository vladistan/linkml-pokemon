export type ThingId = string;
export type NamedIndividualId = string;
export type PersonId = string;
export type ColourId = string;
export type EndianTypeId = string;
export type SystemOfQuantityKindsId = string;
export type RuleTypeId = string;
export type QuantityId = string;
export type QuantifiableId = string;
export type CardinalityTypeId = string;
export type AspectId = string;
export type QuantityKindDimensionVectorSIId = string;
export type PhysicalConstantId = string;
export type EncodingId = string;
export type EnumerationId = string;
export type SystemOfUnitsId = string;
export type PrefixId = string;
export type AbstractQuantityKindId = string;
export type OrderedTypeId = string;
export type EnumeratedValueId = string;
export type ConceptId = string;
export type QuantityValueId = string;
export type DataEncodingId = string;
export type UCUMcsId = string;
export type UnitId = string;
export type DatatypeId = string;
export type VerifiableId = string;
export type QuantityKindId = string;
export type UCUMcs-termId = string;
export type QuantityKindDimensionVectorId = string;
export type RuleId = string;
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
    /** Black component in CMYK color model */
    black?: number,
    /** Cyan component in CMYK color model */
    cyanic?: number,
    /** Magenta component in CMYK color model */
    magenta?: number,
    /** Yellow component in CMYK color model */
    yellow?: number,
    /** Hue component in HSV color model */
    hue?: number,
    /** Saturation component in HSV color model */
    saturation?: number,
    /** Value/Lightness component in HSV color model */
    value?: number,
    /** Red component in RGB color model (0-255) */
    red?: number,
    /** Green component in RGB color model (0-255) */
    green?: number,
    /** Blue component in RGB color model (0-255) */
    blue?: number,
    /** The wavelength of the color in nanometers */
    wavelength?: number,
}


/**
 * Endian Type
 */
export interface EndianType extends EnumeratedValue {
}


/**
 * A system of quantity kinds is a set of one or more quantity kinds together with a set of zero or more algebraic equations that define relationships between quantity kinds in the set. In the physical sciences, the equations relating quantity kinds are typically physical laws and definitional relations, and constants of proportionality. Examples include Newton’s First Law of Motion, Coulomb’s Law, and the definition of velocity as the instantaneous change in position.  In almost all cases, the system identifies a subset of base quantity kinds. The base set is chosen so that all other quantity kinds of interest can be derived from the base quantity kinds and the algebraic equations. If the unit system is explicitly associated with a quantity kind system, then the unit system must define at least one unit for each quantity kind.  From a scientific point of view, the division of quantities into base quantities and derived quantities is a matter of convention.
 */
export interface SystemOfQuantityKinds extends Concept {
}


/**
 * Rule Type
 */
export interface RuleType extends EnumeratedValue {
}


/**
 * <p class="lm-para">A <b>quantity</b> is the measurement of an observable property of a particular object, event, or physical system.
  A quantity is always associated with the context of measurement (i.e. the thing measured, the measured value, the accuracy of measurement, etc.) whereas the
  underlying <b>quantity kind</b> is independent of any particular measurement. Thus, length is a quantity kind while the height of a rocket is a specific
  quantity of length; its magnitude that may be expressed in meters, feet, inches, etc. Examples of physical quantities include physical constants, such as
  the speed of light in a vacuum, Planck's constant, the electric permittivity of free space, and the fine structure constant. </p>
<p class="lm-para">In other words, quantities are quantifiable aspects of the world, such as the duration of a movie, the distance between two points,
velocity of a car, the pressure of the atmosphere, and a person's weight; and units are used to describe their numerical measure.</p>
<p class="lm-para">Many <b>quantity kinds</b> are related to each other by various physical laws, and as a result, the associated units of some quantity
kinds can be expressed as products (or ratios) of powers of other quantity kinds (e.g., momentum is mass times velocity and velocity is defined as distance
divided by time). In this way, some quantities can be calculated from other measured quantities using their associations to the quantity kinds in these
expressions. These quantity kind relationships are also discussed in dimensional analysis. Those that cannot be so expressed can be regarded
as "fundamental" in this sense.</p>
<p class="lm-para">A quantity is distinguished from a "quantity kind" in that the former carries a value and the latter is a type specifier.</p>
 */
export interface Quantity extends Quantifiable, Concept {
}


/**
 * <p><em>Quantifiable</em> ascribes to some thing the capability of being measured, observed, or counted.</p>
 */
export interface Quantifiable extends Aspect {
}


/**
 * 
  In mathematics, the cardinality of a set is a measure of the number of elements of the set.
  For example, the set $A = {2, 4, 6}$ contains 3 elements, and therefore $A$ has a cardinality of 3.
  There are two approaches to cardinality: one which compares sets directly using bijections and injections,
   and another which uses cardinal numbers.
  
 */
export interface CardinalityType extends EnumeratedValue {
}



export interface Aspect extends Thing {
}


/**
 * Quantity Kind Dimension vector (SI)
 */
export interface QuantityKindDimensionVectorSI extends QuantityKindDimensionVector {
}


/**
 * A physical constant is a physical quantity that is generally believed to be both universal in nature and constant in time. It can be contrasted with a mathematical constant, which is a fixed numerical value but does not directly involve any physical measurement. There are many physical constants in science, some of the most widely recognized being the speed of light in vacuum c, Newton's gravitational constant G, Planck's constant h, the electric permittivity of free space ε0, and the elementary charge e. Physical constants can take many dimensional forms, or may be dimensionless depending on the system of quantities and units used.
 */
export interface PhysicalConstant extends Quantity {
}


/**
 * An encoding is a rule or algorithm that is used to convert data from a native, or unspecified form into a specific form that satisfies the encoding rules. Examples of encodings include character encodings, such as UTF-8.
 */
export interface Encoding extends Concept {
}


/**
 * <p>An enumeration is a set of literals from which a single value is selected. Each literal can have a tag as an integer within a standard encoding appropriate to the range of integer values. Consistency of enumeration types will allow them, and the enumerated values, to be referred to unambiguously either through symbolic name or encoding. Enumerated values are also controlled vocabularies and as such need to be standardized. Without this consistency enumeration literals can be stated differently and result in  data conflicts and misinterpretations.</p>

<p>The tags are a set of positive whole numbers, not necessarily contiguous and having no numerical significance, each corresponding to the associated literal identifier. An order attribute can also be given on the enumeration elements. An enumeration can itself be a member of an enumeration. This allows enumerations to be enumerated in a selection. Enumerations are also subclasses of <em>Scalar Datatype</em>. This allows them to be used as the reference of a datatype specification.</p>
 */
export interface Enumeration extends Concept {
}


/**
 * A system of units is a set of units which are chosen as the reference scales for some set of quantity kinds together with the definitions of each unit. Units may be defined by experimental observation or by proportion to another unit not included in the system. If the unit system is explicitly associated with a quantity kind system, then the unit system must define at least one unit for each quantity kind.
 */
export interface SystemOfUnits extends Verifiable, Concept {
}


/**
 * Prefix
 */
export interface Prefix extends Verifiable, Concept {
}


/**
 * Quantity Kind (abstract)
 */
export interface AbstractQuantityKind extends Concept {
}


/**
 * Describes how a data or information structure is ordered.
 */
export interface OrderedType extends EnumeratedValue {
}


/**
 * <p>This class is for all enumerated and/or coded values.  For example, it contains the dimension objects that are the basis elements in some abstract vector space associated with a quantity kind system. Another use is for the base dimensions for quantity systems. Each quantity kind system that defines a base set has a corresponding ordered enumeration whose elements are the dimension objects for the base quantity kinds. The order of the dimensions in the enumeration determines the canonical order of the basis elements in the corresponding abstract vector space.</p>

<p>An enumeration is a set of literals from which a single value is selected. Each literal can have a tag as an integer within a standard encoding appropriate to the range of integer values. Consistency of enumeration types will allow them, and the enumerated values, to be referred to unambiguously either through symbolic name or encoding. Enumerated values are also controlled vocabularies and as such need to be standardized. Without this consistency enumeration literals can be stated differently and result in  data conflicts and misinterpretations.</p>

<p>The tags are a set of positive whole numbers, not necessarily contiguous and having no numerical significance, each corresponding to the associated literal identifier. An order attribute can also be given on the enumeration elements. An enumeration can itself be a member of an enumeration. This allows enumerations to be enumerated in a selection. Enumerations are also subclasses of Scalar Datatype. This allows them to be used as the reference of a datatype specification.</p>
 */
export interface EnumeratedValue extends Verifiable, Concept {
}


/**
 * The root class for all QUDT concepts.
 */
export interface Concept extends Thing {
    /** guidance */
    guidance?: string[],
    /** The "qudt:id" is an identifier string that uniquely identifies a QUDT concept.  The identifier is constructed using a prefix. For example, units are coded using the pattern: "UCCCENNNN", where "CCC" is a numeric code or a category and "NNNN" is a digit string for a member element of that category. For scaled units there may be an addition field that has the format "QNN" where "NN" is a digit string representing an exponent power, and "Q" is a qualifier that indicates with the code "P" that the power is a positive decimal exponent, or the code "N" for a negative decimal exponent, or the code "B" for binary positive exponents. */
    qudt_id?: string,
}


/**
 * A <i>Quantity Value</i> expresses the magnitude and kind of a quantity and is given by the product of a numerical value <code>n</code> and a unit of measure <code>U</code>. The number multiplying the unit is referred to as the numerical value of the quantity expressed in that unit. Refer to <a href="http://physics.nist.gov/Pubs/SP811/sec07.html">NIST SP 811 section 7</a> for more on quantity values.
 */
export interface QuantityValue extends Quantifiable, Concept {
}


/**
 * <p><em>Data Encoding</em> expresses the properties that specify how data is represented at the bit and byte level. These properties are applicable to describing raw data.</p>
 */
export interface DataEncoding extends Aspect {
}


/**
 * Lexical pattern for the case-sensitive version of UCUM code
 */
export interface UCUMcs extends Thing {
}


/**
 * 
  A unit of measure, or unit, is a particular quantity value that has been chosen as a scale for measuring other quantities the same kind (more generally of equivalent dimension).
  For example, the meter is a quantity of length that has been rigorously defined and standardized by the BIPM (International Board of Weights and Measures).
  Any measurement of the length can be expressed as a number multiplied by the unit meter.
  More formally, the value of a physical quantity Q with respect to a unit (U) is expressed as the scalar multiple of a real number (n) and U, as  $Q = nU$.
  
 */
export interface Unit extends Verifiable, Concept {
    /** has reciprocal unit */
    hasReciprocalUnit?: UnitId[],
    /** This property relates a unit of measure with a system of units that either a) defines the unit or b) allows the unit to be used within the system. */
    isUnitOfSystem?: SystemOfUnitsId[],
    /** om unit */
    omUnit?: string[],
    /** unit for */
    unitFor?: string[],
}


/**
 * 
   <p>A <em>Datatype</em> is a definition of the type of the "value" of a data item (for example, "all integers between 0 and 10"),
   and the allowable operations on those values; the meaning of the data; and the way values of that type can be stored.
  Some types are primitive - built-in to the language, with no visible internal structure.
  For example "Boolean"; others are composite - constructed from one or more other types (of either kind).
  For example lists, arrays, structures, unions.
  Some languages provide strong typing, others allow implicit type conversion and/or explicit type conversion.
  </p>
 */
export interface Datatype extends Concept {
}



export interface Verifiable extends Aspect {
}


/**
 * A <b>Quantity Kind</b> is any observable property that can be measured and quantified numerically. Familiar examples include physical properties such as length, mass, time, force, energy, power, electric charge, etc. Less familiar examples include currency, interest rate, price to earning ratio, and information capacity.
 */
export interface QuantityKind extends Verifiable, AbstractQuantityKind {
    /** belongs to system of quantities */
    belongsToSystemOfQuantities?: SystemOfQuantityKindsId[],
}


/**
 * Lexical pattern for the terminal symbols in the case-sensitive version of UCUM code
 */
export interface UCUMcs-term extends Thing {
}


/**
 * <p class="lm-para">A  <em>Quantity Kind Dimension Vector</em> describes the dimensionality of a quantity kind in the context of a system of units. In the SI system of units, the dimensions of a quantity kind are expressed as a product of the basic physical dimensions mass ($M$), length ($L$), time ($T$) current ($I$), amount of substance ($N$), luminous intensity ($J$) and absolute temperature ($\theta$) as $dim \, Q = L^{\alpha} \, M^{\beta} \, T^{\gamma} \, I ^{\delta} \, \theta ^{\epsilon} \, N^{\eta} \, J ^{\nu}$.</p>

<p class="lm-para">The rational powers of the dimensional exponents, $\alpha, \, \beta, \, \gamma, \, \delta, \, \epsilon, \ , \eta, \, \nu$, are positive, negative, or zero.</p>

<p class="lm-para">For example, the dimension of the physical quantity kind $\it{speed}$ is $\ boxed{length/time}$, $L/T$ or $LT^{-1}$, and the dimension of the physical quantity kind force is $\boxed{mass \times acceleration}$ or $\boxed{mass \times (length/time)/time}$, $ML/T^2$ or $MLT^{-2}$ respectively.</p>
 */
export interface QuantityKindDimensionVector extends Concept {
}


/**
 * Rule
 */
export interface Rule extends Verifiable, Concept {
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
    hasSize?: string,
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
    mayHaveHiddenAbility?: AbilityId[],
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



