'''
This program uses python 3.0
'''
import psycopg2

def debug_statment(text):
	print ("DEBUG MEESSAGE: >>>   " + text)

DBNAME = "news"


def get_top_articlse():

	'''
	Objective of get_top_articles() is return top three viwed articles.
	INPUTS: There a no imputs
	OUTPUTS: Is a list of top three viewd articles. 
	VIEWS IN PostgreSQL: path_views view must be created, see readme.md file for more details.
	'''

	top_viewed_paths =  '''select * from path_views'''


	db = psycopg2.connect(dbname = DBNAME)
	c = db.cursor()


	c.execute(top_viewed_paths)

	top_views_articles = '''SELECT title, path_views.views FROM articles JOIN path_views on articles.slug = path_views.path LIMIT 3;'''

	c.execute(top_views_articles)

	top_three_articles =  c.fetchall()

	return top_three_articles
	db.close()




def report_top_three_articles(top_three_articles):

	'''
	Objective of this function is to print top three articles and their view count
	INPUTS: top_three_artciles is an input in a list format with tuples as values for the list
	OUTPUTS: It prints/desplys the top three article titles and their view counts. 
	'''

	print ("The three most popular articles of all time:")
	print("")
	for article in top_three_articles:
		print (article[0] + " - " + str(article[1]) + " views")




def final_report():
	report_top_three_articles(get_top_articlse())

re


final_report()   
