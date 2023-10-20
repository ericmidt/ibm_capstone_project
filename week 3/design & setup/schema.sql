-- This script was generated by a beta version of the ERD tool in pgAdmin 4.
-- Please log an issue at https://redmine.postgresql.org/projects/pgadmin4/issues/new if you find any bugs, including reproduction steps.
BEGIN;


CREATE TABLE public."softcartDimDate"
(
    "DateID" integer NOT NULL,
    "Date" date NOT NULL,
    "Weekday" character varying,
    "Month" integer,
    "MonthName" character varying,
    "Quarter" integer,
    "QuarterName" character varying,
    "Year" integer,
    PRIMARY KEY ("DateID")
);

CREATE TABLE public."softcartDimCategory"
(
    "CategoryID" integer NOT NULL,
    "Category" character varying NOT NULL,
    PRIMARY KEY ("CategoryID")
);

CREATE TABLE public."softcartDimItem"
(
    "ItemID" integer NOT NULL,
    "Item" character varying NOT NULL,
    PRIMARY KEY ("ItemID")
);

CREATE TABLE public."softcartDimCountry"
(
    "CountryID" integer NOT NULL,
    "Country" character varying NOT NULL,
    PRIMARY KEY ("CountryID")
);

CREATE TABLE public."softcartFactSales"
(
    "OrderID" integer NOT NULL,
    "ItemID" integer NOT NULL,
    "Price" numeric NOT NULL,
    "CountryID" integer NOT NULL,
    "DateID" integer NOT NULL,
    "CategoryID" integer NOT NULL,
    PRIMARY KEY ("OrderID")
);

ALTER TABLE public."softcartFactSales"
    ADD FOREIGN KEY ("CountryID")
    REFERENCES public."softcartDimCountry" ("CountryID")
    NOT VALID;


ALTER TABLE public."softcartFactSales"
    ADD FOREIGN KEY ("CategoryID")
    REFERENCES public."softcartDimCategory" ("CategoryID")
    NOT VALID;


ALTER TABLE public."softcartFactSales"
    ADD FOREIGN KEY ("ItemID")
    REFERENCES public."softcartDimItem" ("ItemID")
    NOT VALID;


ALTER TABLE public."softcartFactSales"
    ADD FOREIGN KEY ("DateID")
    REFERENCES public."softcartDimDate" ("DateID")
    NOT VALID;

END;