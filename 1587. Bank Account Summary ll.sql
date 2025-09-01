-- Write your MySQL query statement below
SELECT Users.name AS NAME, t.amt AS BALANCE
FROM Users
LEFT JOIN (
    SELECT account, SUM(amount) AS amt
    FROM Transactions
    GROUP BY account
    ) AS t
ON t.account = Users.account
WHERE t.amt > 10000;