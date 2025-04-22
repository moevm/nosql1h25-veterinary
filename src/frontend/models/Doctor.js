import { User } from './User.js';

export class Doctor extends User {
    constructor(second_name, first_name, last_name, login, password_hash, birth_date, email, gender, phone_number, role, experience, specialization) {
        super(second_name, first_name, last_name, login, password_hash, birth_date, email, gender, phone_number, role);
        this.experience = experience;
        this.specialization = specialization;
    }
}
