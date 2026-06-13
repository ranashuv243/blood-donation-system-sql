CREATE VIEW AvailableDonors AS
SELECT name, blood_group, city, phone
FROM Donors
WHERE last_donation_date <= DATE_SUB(CURDATE(), INTERVAL 3 MONTH);
