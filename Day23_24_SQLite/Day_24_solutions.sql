--1. get total sales for all years using invoice table
--you will want to use SUBSTR to get the year from the invoice date
--you will want to use SUM to get the total sales for each year

--SELECT
--	SUBSTRING(InvoiceDate,1,4) Years,
--	SUM(Total) YearlySales
--FROM
--	invoices i
--GROUP BY
--	Years


--# 2. get total sales for each country - use invoice table
--# you will also need to join with the customer table - those have country info

--SELECT
--	c.Country,
--	SUM(Total) SalesByCountry
--FROM
--	invoices i
--JOIN customers c 
--ON i.CustomerId = c.CustomerId 
--GROUP BY
--	c.Country


--# 3. a count tracks in each playlist - use playlist_track table

--SELECT
--	pt.PlaylistId,
--	COUNT(pt.TrackId) Tracks_in_playlist 
--FROM
--	playlist_track pt 
--GROUP BY
--	pt.PlaylistId

	
--# 3. b extra challenge get total track lenght in minutes for each playlist
--# you will need to join with the track table

--SELECT
--	pt.PlaylistId,
--	COUNT(pt.TrackId) TracksInPlaylist,
--	SUM(t.Milliseconds)/(1000*60) PlaylistLengthMinutes
--FROM
--	playlist_track pt 
--JOIN tracks t 
--ON pt.TrackId = t.TrackId 
--GROUP BY
--	pt.PlaylistId


--# 3. c cherry on top - provide names of these playlists
--# so you will want to join with the playlist table as well

SELECT
	pt.PlaylistId,
	p.Name,
	COUNT(pt.TrackId) TracksInPlaylist,
	SUM(t.Milliseconds)/(1000*60) PlaylistLengthMinutes
FROM
	playlist_track pt 
JOIN tracks t 
ON pt.TrackId = t.TrackId 
JOIN playlists p  
ON pt.PlaylistId = p.PlaylistId 
GROUP BY
	pt.PlaylistId