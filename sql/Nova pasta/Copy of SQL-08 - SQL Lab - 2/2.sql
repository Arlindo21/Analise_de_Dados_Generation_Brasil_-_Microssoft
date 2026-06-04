SELECT Products.ProductName, SUM(Orders.Quantity) AS TotalQuantity
FROM Orders
JOIN Products ON 