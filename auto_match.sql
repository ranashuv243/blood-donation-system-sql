-- Match donors with requests (same blood group + available donors)
SELECT 
    d.name AS donor_name,
    d.blood_group,
    r.patient_name,
    r.hospital_name,
    r.urgency_level
FROM Donors d
JOIN BloodRequests r 
ON d.blood_group = r.blood_group_needed
WHERE d.last_donation_date <= DATE_SUB(CURDATE(), INTERVAL 3 MONTH);
