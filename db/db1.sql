CREATE TABLE "person"(
    "id" INTEGER NOT NULL,
    "fName" VARCHAR(255) NOT NULL,
    "lName" VARCHAR(255) NOT NULL,
    "cardId" INTEGER NOT NULL
);
ALTER TABLE
    "person" ADD PRIMARY KEY("id");
CREATE TABLE "employee"(
    "id" INTEGER NOT NULL,
    "perosn_id" INTEGER NOT NULL,
    "moroInfo" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "employee" ADD PRIMARY KEY("id");
CREATE TABLE "student"(
    "id" INTEGER NOT NULL,
    "perosn_id" INTEGER NOT NULL,
    "stuNumber" INTEGER NOT NULL,
    "moreInfo" INTEGER NOT NULL
);
ALTER TABLE
    "student" ADD PRIMARY KEY("id");
ALTER TABLE
    "employee" ADD CONSTRAINT "employee_perosn_id_foreign" FOREIGN KEY("perosn_id") REFERENCES "person"("id");
ALTER TABLE
    "student" ADD CONSTRAINT "student_perosn_id_foreign" FOREIGN KEY("perosn_id") REFERENCES "person"("id");



import numpy as np