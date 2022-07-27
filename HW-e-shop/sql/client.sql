CREATE TABLE "Client"
(
    id     numeric(21) PRIMARY KEY,
    name   character varying(61),
    email  character varying(121) UNIQUE,
    phone  character varying(21) UNIQUE,
    is_vip boolean  DEFAULT false,
    password character varying(121) NOT NULL
);

ALTER TABLE "Client"
ADD COLUMN password character varying(121) NOT NULL;

ALTER TABLE "Client" 
DROP COLUMN pass;

