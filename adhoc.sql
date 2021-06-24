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

