CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> df3bc8061d32

CREATE TABLE employee (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    name VARCHAR(100) NOT NULL, 
    email VARCHAR(100) NOT NULL, 
    ciudad VARCHAR(100) NOT NULL, 
    PRIMARY KEY (id)
);

INSERT INTO alembic_version (version_num) VALUES ('df3bc8061d32');

-- Running upgrade df3bc8061d32 -> ff27e943164a

ALTER TABLE employee ADD COLUMN edad INTEGER NOT NULL;

ALTER TABLE employee ADD COLUMN cargo VARCHAR(100) NOT NULL;

UPDATE alembic_version SET version_num='ff27e943164a' WHERE alembic_version.version_num = 'df3bc8061d32';

-- Running upgrade ff27e943164a -> 8076b959cec9

CREATE TABLE employee (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    name VARCHAR(100) NOT NULL, 
    email VARCHAR(100) NOT NULL, 
    ciudad VARCHAR(100) NOT NULL, 
    edad INTEGER NOT NULL, 
    cargo VARCHAR(100) NOT NULL, 
    PRIMARY KEY (id)
);

UPDATE alembic_version SET version_num='8076b959cec9' WHERE alembic_version.version_num = 'ff27e943164a';

