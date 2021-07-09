#### This file created for backup purposes only.

#### Find the top five states
SELECT count(state) as c, state 
FROM GIstandards.findings f, GIstandards.STstandards s
WHERE f.STstandardsId=s.id
GROUP BY state
order by c desc


#### Count all states with keywords in CTE
SELECT DISTINCT state 
FROM GIstandards.findings f, GIstandards.STstandards s
WHERE f.STstandardsId=s.id
AND standardArea='CTE'
GROUP BY state
order by state

### extract non-trivial GIS use
SELECT keyword, quote FROM GIstandards.findings 
where (keyword='geographic information system' 
OR keyword = '(GIS'
OR keyword = ' GIS')
AND NOT quote = ''
AND NOT (quote LIKE '%example%' OR quote LIKE '%sample%')


## scatterplot SELECT s.state, count(f.keyword) as spatialcount, s.statekeywordcount,  (s.statekeywordcount - count(f.keyword)) AS geocount
FROM GIstandards.findings f, GIstandards.STstandards s
WHERE (f.STstandardsId=s.id) 
	AND (f.keyword = ' spatial')
GROUP BY state, statekeywordcount
order by state desc

