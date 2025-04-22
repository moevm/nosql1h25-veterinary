import { User } from './User.js';

export class Client extends User {
    constructor(second_name, first_name, last_name, login, password_hash, birth_date, email, gender, phone_number, role) {
        super(second_name, first_name, last_name, login, password_hash, birth_date, email, gender, phone_number, role);
    }
}
