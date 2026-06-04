SELECT Customers.CustomerName, SUM(Orders.Total) AS TotalSales
FROM Orders
JOIN Customers ON 