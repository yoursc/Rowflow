DROP TABLE IF EXISTS sys_conf;
CREATE TABLE IF NOT EXISTS sys_config
(
    id  INT PRIMARY KEY NOT NULL,
    app CHAR(100)       NOT NULL,
    k   CHAR(100)       NOT NULL,
    v   CHAR(100)
);

DROP TABLE IF EXISTS meta_table;
CREATE TABLE IF NOT EXISTS meta_table
(
    t_uuid CHAR(37) PRIMARY KEY NOT NULL,
    t_name CHAR(100)            NOT NULL,
    t_type CHAR(100)            NOT NULL,
    t_note CHAR(100)
);
INSERT INTO meta_table (t_uuid, t_name, t_type, t_note)
VALUES ('A1A2A3', 'test_table', '123456','this is a test table');
INSERT INTO meta_table (t_uuid, t_name, t_type, t_note)
VALUES ('A1A2A6', 'test_table', '123456','this is a test table');


DROP TABLE IF EXISTS meta_column;
CREATE TABLE IF NOT EXISTS meta_column
(
    c_uuid CHAR(32) PRIMARY KEY NOT NULL,
    c_name CHAR(100)            NOT NULL,
    c_type CHAR(100)            NOT NULL,
    c_note CHAR(100)
);

DROP TABLE IF EXISTS sys_user;
CREATE TABLE IF NOT EXISTS sys_user
(
    id       INT PRIMARY KEY NOT NULL,
    username CHAR(100)       NOT NULL,
    password CHAR(100)       NOT NULL,
    note     CHAR(100)
);
INSERT INTO sys_user (id, username, password)
VALUES ('1', 'root', '123456');
