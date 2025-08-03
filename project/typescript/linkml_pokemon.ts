export type ThingId = string;
export type NamedThingId = string;
export type PersonId = string;
export type ColourId = string;
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
export interface NamedThing extends Thing {
}


/**
 * A person is a human being
 */
export interface Person extends NamedThing {
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



export interface EggGroup extends Thing {
}



export interface Flavor extends Thing {
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
export interface Habitat extends NamedThing {
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
export interface PokedexEntry extends NamedThing {
}



export interface Pokeball extends Item {
}



export interface Place extends Thing {
}


/**
 * Shapes are categories that certain Pokemon belong to, which determine which Pokemon they can breed with.
 */
export interface Shape extends NamedThing {
}



export interface Region extends Place {
}


/**
 * A species is a category of Pokemon that share common features.
 */
export interface Species extends NamedThing {
    /** A Pokemon has a color */
    hasColour?: Colour[],
    mayHaveHiddenAbility?: AbilityId[],
    /** A Pokemon may have an ability */
    mayHaveAbility?: AbilityId[],
    isAbleToApply?: MoveId[],
    hasHeight?: string,
    hasWeight?: string,
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



export interface Type extends NamedThing {
}



