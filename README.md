# logs-analysis
A program that analysis logs from a news website and answers some important business questions.

## For this program you will need the following files:
1. log_analysis.py 
2. newsdata.sql


**newsdata.sql** file can be [downloaded](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) here. 

## You will need to create following views in the news database:
1. path_views 
2. author_views
3. error_per_day
4. requests_per_day
5. error_rate_per_day

## PostgreSQL Code for all views:

1. PostgreSQL code to create **path_views** view:
```
	CREATE VIEW path_views AS
	SELECT  substring(path,10) AS path, COUNT(*) AS views
	FROM log
	WHERE path LIKE '%article%' 
	AND status LIKE '%2%'
	GROUP BY path
	ORDER BY views desc;
```
2. PostgreSQL code to create **author_views** view:
```
	CREATE VIEW author_views AS
	SELECT articles.author, SUM(path_views.views) AS total_views
	FROM path_views JOIN articles
	ON path_views.path = articles.slug
	GROUP BY articles.author
	ORDER BY total_views DESC;
```

3. PostgreSQL code to create **error_per_day** view:
```
	CREATE VIEW error_per_day AS
	SELECT DATE(time), COUNT(*) as count
	FROM log 
	WHERE status LIKE '%404%'
	GROUP BY date
	ORDER BY count DESC;
```
4. PostgreSQL code to create **requests_per_day** view:
```
	CREATE VIEW requests_per_day AS
	SELECT DATE(time), COUNT(*) as count
	FROM log 
	GROUP BY date
	ORDER BY count DESC;
```

5. PostgreSQL code to create **error_rate_per_day** view:
```
	CREATE VIEW error_rate_per_day AS
	SELECT error_per_day.date, error_per_day.count*100/requests_per_day.count::FLOAT4 AS percentage_error
	FROM error_per_day JOIN requests_per_day
	ON error_per_day.date = requests_per_day.date
	ORDER BY percentage_error DESC;
```


