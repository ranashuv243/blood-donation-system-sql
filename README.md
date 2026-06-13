🩸 Blood Donation Management System

A SQL-based database project designed to efficiently manage blood donors, emergency blood requests, and donor-request matching system.
This project demonstrates real-world database design, relationships, and query optimization using MySQL.

🚀 Project Overview

The Blood Donation Management System is built to solve emergency blood shortage problems by connecting:

Donors with available blood
Patients in urgent need
Hospitals and blood requests

It includes a structured relational database and automated matching queries using SQL JOIN operations.

🎯 Features
🧑‍🤝‍🧑 Donor management system
🏥 Blood request tracking
🔄 Automated donor-request matching
📊 Available donor filtering system
⚡ SQL views for quick data access
🧠 Advanced SQL JOIN queries
🗂️ Database Structure
📌 Tables
Donors
donor_id (PK)
name
blood_group
phone
city
last_donation_date
BloodRequests
request_id (PK)
patient_name
blood_group_needed
hospital_name
urgency_level
request_date
Donations
donation_id (PK)
donor_id (FK)
request_id (FK)
donation_date
status
🧠 Key SQL Concepts Used
JOIN (Inner Join for matching donors & requests)
VIEW (for available donors list)
DATE filtering (eligibility check)
FOREIGN KEY relationships
Relational database design
⚙️ How to Run This Project
1️⃣ Create Database

Run schema.sql in MySQL:

CREATE DATABASE BloodDonationSystem;
USE BloodDonationSystem;
2️⃣ Insert Sample Data

Generate or import:

sample_data.sql
3️⃣ Run Queries

Execute:

auto_match.sql → for donor matching system
views.sql → for available donors
4️⃣ (Optional) Generate Data

Run Python script:

python generator.py

It will create:

sample_data.sql (50–100+ records)
🔍 Sample Query
SELECT 
    d.name,
    d.blood_group,
    r.patient_name,
    r.hospital_name
FROM Donors d
JOIN BloodRequests r
ON d.blood_group = r.blood_group_needed;
📊 Example Use Case
A patient needs A+ blood
System finds all A+ donors
Filters eligible donors (last donation > 3 months)
Matches donor with request
📁 Project Structure
Blood-Donation-System/
│
├── schema.sql
├── generator.py
├── sample_data.sql
├── auto_match.sql
├── views.sql
└── README.md
💡 Future Improvements
🌐 Web-based UI (React / PHP / Node.js)
📱 Mobile app integration
🔔 SMS/Email notification system
🤖 AI-based donor prediction system
🏆 Learning Outcome

This project demonstrates:

Database design skills (ER modeling)
SQL query optimization
Real-world problem solving
Backend system thinking
👨‍💻 Author

Sohan Rana
Software Engineering Student
Daffodil International University (DIU), Bangladesh

⭐ If you like this project

Give a ⭐ on the repository and feel free to contribute!
