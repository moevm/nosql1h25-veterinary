export class Pet {
    constructor(name, breed, birthdate, gender, photo_url, owner, pet_type, appointments = []) {
        this.name = name;
        this.breed = breed;
        this.birthdate = birthdate;
        this.gender = gender;
        this.photo_url = photo_url;
        this.owner = owner;
        this.pet_type = pet_type;
        this.appointments = appointments;
    }
}
