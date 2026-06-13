import random
from datetime import datetime, timedelta

blood_groups = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
cities = ["Dhaka", "Gazipur", "Narayanganj", "Savar", "Narsingdi", "Tongi"]

names = ["Rahim", "Karim", "Sadia", "Nafisa", "Sohan", "Rakib", "Jannat", "Rafi", "Tanvir", "Mehedi", "Anika", "Tanjim"]
surnames = ["Uddin", "Ahmed", "Khan", "Islam", "Hossain", "Rahman", "Chowdhury"]

hospitals = ["Dhaka Medical", "Square Hospital", "United Hospital", "Apollo Hospital", "Ibn Sina"]

def rand_date():
    start = datetime(2024, 1, 1)
    end = datetime(2025, 6, 1)
    return (start + timedelta(days=random.randint(0, (end-start).days))).date()

def phone():
    return "01" + str(random.randint(300000000, 999999999))

file = open("sample_data.sql", "w", encoding="utf-8")

# ---------------- DONORS (70) ----------------
file.write("-- DONORS\n")
for i in range(70):
    name = random.choice(names) + " " + random.choice(surnames)
    bg = random.choice(blood_groups)
    city = random.choice(cities)
    last = rand_date()
    ph = phone()

    file.write(f"""
INSERT INTO Donors (name, blood_group, phone, city, last_donation_date)
VALUES ('{name}', '{bg}', '{ph}', '{city}', '{last}');
""")

# ---------------- REQUESTS (50) ----------------
file.write("\n-- REQUESTS\n")
for i in range(50):
    patient = random.choice(names) + " " + random.choice(surnames)
    bg = random.choice(blood_groups)
    hospital = random.choice(hospitals)
    urgency = random.choice(["Low", "Medium", "High"])

    file.write(f"""
INSERT INTO BloodRequests (patient_name, blood_group_needed, hospital_name, urgency_level)
VALUES ('{patient}', '{bg}', '{hospital}', '{urgency}');
""")

file.close()

print("DONE: sample_data.sql generated ")
