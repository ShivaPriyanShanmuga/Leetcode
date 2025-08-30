-- Write your MySQL query statement below
SELECT t.name as Customers FROM (
    SELECT name, Orders.customerId
    FROM Customers 
    LEFT JOIN Orders
    ON Orders.customerId = Customers.id
) AS t WHERE t.customerId IS NUll;