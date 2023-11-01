SELECT * FROM dojos;
SELECT * FROM ninjas;

INSERT INTO dojos (name, created_at, updated_at) VALUES ("BESTdojo", CURRENT_DATE(), CURRENT_DATE());
INSERT INTO dojos (name, created_at, updated_at) VALUES ("GOJODOJO", CURRENT_DATE(), CURRENT_DATE());
INSERT INTO dojos (name, created_at, updated_at) VALUES ("TOP DOJO", CURRENT_DATE(), CURRENT_DATE());

SET SQL_SAFE_UPDATES = 0;
DELETE FROM dojos;

INSERT INTO dojos (name, created_at, updated_at) VALUES ("BESTdojo", CURRENT_DATE(), CURRENT_DATE());
INSERT INTO dojos (name, created_at, updated_at) VALUES ("GOJODOJO", CURRENT_DATE(), CURRENT_DATE());
INSERT INTO dojos (name, created_at, updated_at) VALUES ("TOP DOJO", CURRENT_DATE(), CURRENT_DATE());

INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) VALUES ("Dork", "Dork", 90, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP(), 4);
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) VALUES ("James", "Guy", -1, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP(), 4);
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) VALUES ("Main", "Character", 8, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP(), 4);

INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) VALUES ("Dopey", "Jo", 25, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP(), 5);
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) VALUES ("Nan", "Stark", 35, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP(), 5);
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) VALUES ("Dank", "Cappy", 67, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP(), 5);

INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) VALUES ("Snob", "Jack", 20, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP(), 6);
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) VALUES ("Bae", "Snap", 56, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP(), 6);
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) VALUES ("Stab", "Johnson", 10, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP(), 6);

SELECT * FROM ninjas WHERE dojo_id = 4;

SELECT * FROM ninjas WHERE dojo_id = 6;

SELECT dojo_id FROM ninjas WHERE id = 9;

SELECT * FROM ninjas JOIN dojos ON dojos.id = ninjas.dojo_id WHERE ninjas.id = 6;

SELECT * FROM ninjas JOIN dojos ON dojos.id = ninjas.dojo_id;