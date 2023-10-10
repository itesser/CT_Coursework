CREATE TABLE IF NOT EXISTS customers(
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    address VARCHAR(150),
    billing_invo VARCHAR(100)
);
-- brand table creation
CREATE TABLE IF NOT EXISTS brands(
    seller_id SERIAL PRIMARY KEY,
    brand_name VARCHAR(150),
    contact_number VARCHAR(15),
    address VARCHAR(150)
);
-- inventory table creation
CREATE TABLE IF NOT EXISTS inventory(
    upc SERIAL PRIMARY KEY,
    product_amount INTEGER
);
-- product table creation
CREATE TABLE IF NOT EXISTS product(
    item_id SERIAL PRIMARY KEY,
    amount NUMERIC(5,2),
    prod_name VARCHAR(100),
    upc INTEGER NOT NULL, 
    seller_id INTEGER NOT NULL,
    FOREIGN KEY(seller_id) REFERENCES brands(seller_id),
    FOREIGN KEY(upc) REFERENCES inventory(upc)
);
-- order table creation
CREATE TABLE IF NOT EXISTS orders(
    order_id SERIAL PRIMARY KEY,
    order_date DATE DEFAULT CURRENT_DATE,
    sub_total NUMERIC(8,2),
    total_cost NUMERIC(10,2),
    upc INTEGER NOT NULL,
    FOREIGN KEY(upc) REFERENCES inventory(upc)
);
-- cart table creation
CREATE TABLE IF NOT EXISTS carts(
    cart_id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_id INTEGER NOT NULL,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY(order_id) REFERENCES orders(order_id)
);