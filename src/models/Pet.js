export class Pet {
    constructor(name, breed, birthdate, gender, photo_url, owner, pet_type, appointments = []) {
        this.name = name;
        this.breed = breed;
        this.birthdate = birthdate;
        this.gender = gender;
    }
}
