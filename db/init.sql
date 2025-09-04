DROP TABLE IF EXISTS sys_conf;
CREATE TABLE IF NOT EXISTS sys_config
(
    id  INT UNSIGNED PRIMARY KEY NOT NULL,
    app CHAR(100)                NOT NULL,
    k   CHAR(100)                NOT NULL,
    v   CHAR(100)
);


DROP TABLE IF EXISTS sys_user;
CREATE TABLE IF NOT EXISTS sys_user
(
    id              INT UNSIGNED PRIMARY KEY NOT NULL,
    username        CHAR(100)                NOT NULL,
    password        CHAR(100)                NOT NULL,
    description     CHAR(100),
    create_user     INT UNSIGNED,
    create_datetime TIMESTAMP,
    modify_user     INT UNSIGNED,
    modify_datetime TIMESTAMP
);
INSERT INTO sys_user (id, username, password, create_user, create_datetime)
VALUES ('0', 'system', '123456', 0, now()),
       ('1', 'root', '123456', 0, now()),
       ('2', 'test', '123456', 0, now());


DROP TABLE IF EXISTS meta_table;
CREATE TABLE IF NOT EXISTS meta_table
(
    t_uuid          CHAR(15) PRIMARY KEY NOT NULL,
    t_name          CHAR(100)            NOT NULL,
    t_type          CHAR(100)            NOT NULL,
    t_desc          CHAR(100),
    create_user     INT UNSIGNED,
    create_datetime TIMESTAMP,
    modify_user     INT UNSIGNED,
    modify_datetime TIMESTAMP
);
INSERT INTO meta_table (t_uuid, t_name, t_type, t_desc, create_user, create_datetime)
VALUES ('tab_0123456789a', 'test_table_01', 'base_table', 'Create this table by database init batch.', 0, now()),
       ('tab_0123456789b', 'test_table_02', 'base_table', 'Create this table by database init batch.', 0, now());


DROP TABLE IF EXISTS meta_column;
CREATE TABLE IF NOT EXISTS meta_column
(
    c_uuid          CHAR(37) PRIMARY KEY NOT NULL,
    c_name          CHAR(100)            NOT NULL,
    c_type          CHAR(100)            NOT NULL,
    c_desc          CHAR(100),
    t_uuid          CHAR(15)             NOT NULL,
    create_user     INT UNSIGNED,
    create_datetime TIMESTAMP,
    modify_user     INT UNSIGNED,
    modify_datetime TIMESTAMP
);
INSERT INTO meta_column (c_uuid, c_name, c_type, c_desc, t_uuid, create_user, create_datetime)
VALUES ('col_00000001', 'id', 'INT', 'Create this column by database init batch.', 'tab_0123456789a', 0, now()),
       ('col_00000002', 'name', 'CHAR(10)', 'Create this column by database init batch.', 'tab_0123456789a', 0, now()),
       ('col_00000003', 'name', 'CHAR(10)', 'Create this column by database init batch.', 'tab_0123456789a', 0, now()),
       ('col_00000004', 'name', 'CHAR(10)', 'Create this column by database init batch.', 'tab_0123456789a', 0, now()),
       ('col_000000a1', 'id', 'INT', 'Create this column by database init batch.', 'tab_0123456789b', 0, now()),
       ('col_000000a2', 'name', 'CHAR(10)', 'Create this column by database init batch.', 'tab_0123456789b', 0, now()),
       ('col_000000a3', 'name', 'CHAR(10)', 'Create this column by database init batch.', 'tab_0123456789b', 0, now()),
       ('col_000000a4', 'name', 'CHAR(10)', 'Create this column by database init batch.', 'tab_0123456789b', 0, now());
