import { AppointmentStatus } from './AppointmentStatus.js';

export class Appointment {
    constructor(date, status = AppointmentStatus.PENDING, reason, comment, diagnosis, recommend, file_urls = [], pet, client, doctor, procedure, day) {
        this.date = date;
        this.status = status;
        this.reason = reason;
        this.comment = comment;
        this.diagnosis = diagnosis;
        this.recommend = recommend;
        this.file_urls = file_urls;
        this.pet = pet;
        this.client = client;
        this.doctor = doctor;
        this.procedure = procedure;
        this.day = day;
    }

    setStatus(newStatus) {
        const values = Object.values(AppointmentStatus);
        if (!values.includes(newStatus)) {
            throw new Error(`Invalid status: ${newStatus}`);
        }
        this.status = newStatus;
    }
}
