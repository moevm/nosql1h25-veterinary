export class Procedure {
    constructor(name, cost, description, available, appointments = [], pet_types = [], offices = []) {
        this.name = name;
        this.cost = cost;
        this.description = description;
        this.available = available;
    }
}
