DROP TABLE IF EXISTS sys_conf;

CREATE TABLE sys_conf
(
    ID INT PRIMARY KEY NOT NULL,
    K  CHAR(20),
    V  CHAR(20)
);
