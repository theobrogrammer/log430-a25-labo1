-- Créer le tableau Users
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(80) NOT NULL,
    email VARCHAR(80) NOT NULL
);

-- Créer des enregistrements dans Users
INSERT INTO users (name, email) VALUES
('Ada Lovelace', 'alovelace@example.com'),
('Adele Goldberg', 'agoldberg@example.com'),
('Alan Turing', 'aturing@example.com');

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(80) NOT NULL,
    brand VARCHAR(20) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

-- Créer des enregistrements dans Products
INSERT INTO products (name, brand, price) VALUES
('ThinkPad X1', 'Lenovo', 1999.99),
('MacBook Air', 'Apple', 1499.00),
('Surface Laptop', 'Microsoft', 1299.00),
('Galaxy S24', 'Samsung', 999.99),
('iPhone 15', 'Apple', 1199.00);
