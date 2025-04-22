export class PetType {
    constructor(type_name, pets = [], procedures = []) {
        this.type_name = type_name;
        this.pets = pets;
        this.procedures = procedures;
    }
}
