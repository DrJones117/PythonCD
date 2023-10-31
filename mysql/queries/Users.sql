SELECT * FROM users;

INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES ("Judah", "Kahler", "blahblahblahblah", "2023-10-31 17:05:00","2023-10-31 17:05:00" );

INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES ("Jeff", "Guy", "Email.gmail.com", "2023-10-31 17:07:00","2023-10-31 17:07:00" );

INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES ("Beth", "Jo", "flash.mail.gmail.com", "2023-10-31 17:08:00","2023-10-31 17:08:00" );

SELECT * FROM users WHERE email = "Email.gmail.com";

SELECT * FROM users WHERE id = 1;

UPDATE users SET email = "Pancakes" WHERE id = 3;

DELETE FROM users WHERE id = 2;

SELECT * FROM users ORDER BY first_name;

SELECT * FROM users ORDER BY first_name DESC;



