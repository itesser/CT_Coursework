CREATE TABLE IF NOT EXISTS dealer_depts(
dept_id INTEGER PRIMARY KEY,
dept_name VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS employees(
employee_id INTEGER PRIMARY KEY,
name VARCHAR(40),
dept_id INTEGER,
FOREIGN KEY(dept_id) REFERENCES dealer_depts(dept_id)
);

CREATE TABLE IF NOT EXISTS owners(
owner_id INTEGER PRIMARY KEY,
contact_info VARCHAR(255),
billing_info VARCHAR(255),
owner_name VARCHAR(255)
);


CREATE TABLE IF NOT EXISTS vehicles(
car_id INTEGER PRIMARY KEY,
owner_id INTEGER,
 FOREIGN KEY(owner_id) REFERENCES owners(owner_id),
make_model VARCHAR(60),
milage INTEGER
);

CREATE TABLE IF NOT EXISTS service_dept(
service_id INTEGER PRIMARY KEY,
car_id INTEGER,
 FOREIGN KEY(car_id) REFERENCES vehicles(car_id),
service_date DATETIME
);

CREATE TABLE IF NOT EXISTS service_records(
service_id INTEGER,
 FOREIGN KEY(service_id) REFERENCES service_dept(service_id),
employee_id INTEGER,
 FOREIGN KEY(employee_id) REFERENCES employees(employee_id),
work_done VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS car_sales(
invoice_id SERIAL PRIMARY KEY,
employee_id INTEGER,
 FOREIGN KEY(employee_id) REFERENCES employees(employee_id),
sale_date DATETIME,
car_id INTEGER,
 FOREIGN KEY(car_id) REFERENCES vehicles(car_id),
owner_id INTEGER,
 FOREIGN KEY(owner_id) REFERENCES owners(owner_id)
);

INSERT INTO dealer_depts
VALUES(
1,
'sales'
);

INSERT INTO dealer_depts
VALUES(
2,
'service'
);

INSERT INTO dealer_depts
VALUES(
3,
'support'
);

INSERT INTO employees
VALUES(
101,
'Veronica',
1
);

INSERT INTO employees
VALUES(
201,
'Mark',
2
);

INSERT INTO employees
VALUES(
301,
'Shelby',
3
);

INSERT INTO owners
VALUES(
1000,
'555-555-5555',
'1 Dealer Way',
'Dealership'
);

INSERT INTO owners
VALUES(
1001,
'555-686-4040',
'468 Jasper Way',
'Andrew Bell'
);

INSERT INTO owners
VALUES(
1002,
'555-842-7615',
'8946 Harper St',
'Bob Matthews'
);

INSERT INTO owners
VALUES(
1003,
'555-697-5197',
'68 Gogh Blvd',
'Helen Boylen'
);

INSERT INTO owners
VALUES(
1004,
'555-215-1242',
'1554 clark st',
'Debbie Browning'
);

INSERT INTO vehicles
VALUES(
10001,
1001,
'Ford Mustang',
45600
);

INSERT INTO vehicles
VALUES(
10002,
1002,
'Honda Odyssey',
64065
);

INSERT INTO vehicles
VALUES(
10003,
1003,
'Jeep Jeep',
4681
);

INSERT INTO vehicles
VALUES(
10004,
1000,
'Ford Focus',
21
);

INSERT INTO vehicles
VALUES(
10005,
1000,
'Honda FIt',
104
);

INSERT INTO vehicles
VALUES(
10006,
1000,
'Nissan Versa',
2468
);

INSERT INTO vehicles
VALUES(
10007,
1004,
'Dodge Stratus',
75900
);

INSERT INTO car_sales
VALUES(
1101,
101,
'2021-05-18',
10001,
1001

);

INSERT INTO car_sales
VALUES(
1102,
101,
'2022-11-12',
10002,
1003

);

INSERT INTO car_sales
VALUES(
1103,
101,
'2023-08-09',
10003,
1002

);

INSERT INTO service_dept
VALUES(
2201,
10002,
'2023-04-21'
);

INSERT INTO service_dept
VALUES(
2202,
10002,
'2023-04-21'
);

INSERT INTO service_dept
VALUES(
2203,
10003,
'2023-09-04'
);

INSERT INTO service_records
VALUES(
2202,
201,
'tire rotation'
);

INSERT INTO service_records
VALUES(
2202,
201,
'oil change'
);

INSERT INTO service_records
VALUES(
2203,
201,
'tighten sprockets'
);

