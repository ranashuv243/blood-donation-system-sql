CREATE DATABASE BloodDonationSystem;
USE BloodDonationSystem;

CREATE TABLE Donors (
    donor_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    blood_group VARCHAR(5),
    phone VARCHAR(15),
    city VARCHAR(50),
    last_donation_date DATE
);

CREATE TABLE BloodRequests (
    request_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_name VARCHAR(100),
    blood_group_needed VARCHAR(5),
    hospital_name VARCHAR(100),
    urgency_level VARCHAR(20),
    request_date DATE DEFAULT CURRENT_DATE
);

CREATE TABLE Donations (
    donation_id INT PRIMARY KEY AUTO_INCREMENT,
    donor_id INT,
    request_id INT,
    donation_date DATE DEFAULT CURRENT_DATE,
    status VARCHAR(20) DEFAULT 'Pending',
    FOREIGN KEY (donor_id) REFERENCES Donors(donor_id),
    FOREIGN KEY (request_id) REFERENCES BloodRequests(request_id)
);
