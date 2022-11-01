-- # Task 1
-- # provide a query that shows total sales by each sales agent
-- # will require to join with the customer table
-- # will require to join with the invoice table

SELECT
	e.LastName,
	e.FirstName,
	SUM(i.Total) SalesByAgent
FROM customers c 
JOIN employees e ON c.SupportRepId = e.EmployeeId 
JOIN invoices i ON c.CustomerId = i.CustomerId 
GROUP BY e.EmployeeId 


--# Task 2
--# QUERY TO find the top selling track of 2012
--# will require use track table
--# will requiret to join with invoice items table
--# will require to join with the invoice table

SELECT
	t.Name,
	SUBSTRING(i.InvoiceDate,1,4) ReleaseYear,
	SUM(i.Total) SalesByTrack
FROM invoice_items ii 
JOIN invoices i ON ii.InvoiceId = i.InvoiceId 
JOIN tracks t ON ii.TrackId = t.TrackId 
GROUP BY ii.TrackId 
HAVING ReleaseYear = "2012"
ORDER BY SalesByTrack DESC