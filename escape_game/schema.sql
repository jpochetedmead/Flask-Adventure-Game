DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name varchar(50) UNIQUE NOT NULL, --added as experiment
  username varchar(50) UNIQUE NOT NULL,
  email varchar(50) UNIQUE NOT NULL, --added as experiment
  password varchar(50) NOT NULL
);
