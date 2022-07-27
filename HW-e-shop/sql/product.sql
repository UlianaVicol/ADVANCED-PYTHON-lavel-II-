-- DDL instructions (CREATE, ALTER, DROP)
CREATE TABLE "Product"
(
    id          integer PRIMARY KEY,
    name        character varying(121),
    price_value numeric,
    price_unit  character varying(5),
    bar_code    character varying(15) UNIQUE,
    quantity    integer
);

ALTER TABLE "Product"
DROP COLUMN bar_code ;

-- DWML INSTRUCTIONS (CRUD)

INSERT INTO "Product"(id, name, price, bar_code)
VALUES (1, 'First Product', 100, '1234567890123');
INSERT INTO "Product"(id, name, price, bar_code)
VALUES (2, 'Second Product', 200, '2234567890123');
INSERT INTO "Product"(id, name, price, bar_code)
VALUES (3, 'Third Product', 300, '3234567890123');
INSERT INTO "Product"(id, name, price, bar_code)
VALUES (4, 'Fourth Product', 400, '4234567890123');

SELECT * FROM "Product";






