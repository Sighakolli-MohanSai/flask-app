CREATE TABLE IF NOT EXISTS users
(
    id INT AUTO_INCREMENT PRIMARY KEY,

    username VARCHAR(50) UNIQUE NOT NULL,

    firstname VARCHAR(50) NOT NULL,

    lastname VARCHAR(50) NOT NULL,

    password VARCHAR(100) NOT NULL,

    favourite_movie VARCHAR(100) NOT NULL
);
