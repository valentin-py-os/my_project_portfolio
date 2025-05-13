SELECT CASE
   WHEN url LIKE '%github%' THEN 'GitHub'
   WHEN url like '%medium.com%' then 'Medium'
   WHEN url like '%nytimes.com%' then 'New York Times'
   ELSE 'Other'  
  END AS 'Source',
  count(url)
FROM hacker_news
group by 1;

SELECT timestamp
FROM hacker_news
LIMIT 10;

SELECT timestamp,
   strftime('%H', timestamp)
FROM hacker_news
GROUP BY 1
LIMIT 20;

SELECT strftime('%H', timestamp) as 'Hour', 
   round(avg(score), 1) as 'Average score',
   COUNT(*) as 'Number of stories'
FROM hacker_news
where timestamp is not null
GROUP BY 1
ORDER BY 2 DESC;
