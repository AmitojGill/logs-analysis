'''
This program uses python 3.0
'''
import psycopg2

def debug_statment(text):
	print ("DEBUG MEESSAGE: >>>   " + text)

DBNAME = "news"


def get_top_articlse():

	''' Following view need to be crearted path_view created'''

	'''
		CREATE view path_views as
		select path, count(*) as views
		from log
		where path like '%article%' 
		and status like '%2%'
		group by path
		order by views desc;

	'''

	top_viewed_paths =  '''select * from path_views'''


	db = psycopg2.connect(dbname = DBNAME)
	c = db.cursor()


	c.execute(top_viewed_paths)

	top_views_articles = ''' SELECT title, path_views.views FROM articles JOIN path_views on articles.slug = path_views.substrings LIMIT 3; '''

	
	for row in c.fetchall():
		print row


	return c.fetchall()
	db.close()


get_top_articlse()
