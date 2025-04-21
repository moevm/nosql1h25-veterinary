export class Office {
    constructor(name, address, email, phone_number, opening_hours, meta, doctors = [], appointments = [], procedures = []) {
        this.name = name;
        this.address = address;
        this.email = email;
        this.phone_number = phone_number;
        this.opening_hours = opening_hours;
        this.meta = meta;
        this.doctors = doctors;
        this.appointments = appointments;
        this.procedures = procedures;
    }
}
