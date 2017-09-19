# logs-analysis
A program that analysis logs form a news website and answers some important business questions.

This program you will need the following files:
1. log_analysis.py 
2. newsdata.sql


newsdata.sql file can be downloaded from: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

You will need to create follwoing views in the news database:
1. path_views 


1. PostgreSQL code to create path_views view:
'''
	CREATE VIEW path_views AS
	SELECT  path, COUNT(*) AS views
	FROM log
	WHERE path LIKE '%article%' 
	AND status LIKE '%2%'
	GROUP BY path
	ORDER BY views desc;
'''
