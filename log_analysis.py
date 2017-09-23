#!/usr/bin/python3
import psycopg2


def connect(database_name):
    '''Connect to the PostgreSQL database. Returns a database connection.'''
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        c = db.cursor()
        return db, c
    except psycopg2.Error as e:
        print("Unable to connect to database")
        sys.exit(1)


def get_query_results(query):
    '''
    Objective of this funciton is to get query results from the databse
    INPUT: takes in query as an input
    Outputs: returns results from the qurey. 
    '''
    db, c = connect("news")
    c.execute(query)
    db.commit()
    results = c.fetchall()
    db.close()
    return results


def get_top_articlse():

    '''
    Objective of get_top_articles() is return top three viwed articles.
    INPUTS: There a no imputs
    OUTPUTS: Is a list of top three viewd articles.
    VIEWS IN PostgreSQL: path_views view must be created, see readme.md
    file for more details.
    '''

    top_views_articles = '''SELECT title, path_views.views
    FROM articles
    JOIN path_views on articles.slug = path_views.path
    LIMIT 3;'''

    results = get_query_results(top_views_articles)

    return results


def report_top_three_articles(top_three_articles):
    '''
    Objective of this function is to print top three articles and their
    view count
    INPUTS: top_three_artciles is an input in a list format with tuples as
    values for the list
    OUTPUTS: It prints/desplys the top three article titles and their view
    counts.
    '''
    print("")
    print("The three most popular articles of all time:")
    print("")
    for article in top_three_articles:
        print(article[0]+" - "+str(article[1])+" views")


def get_author_views():
    '''
    Objective of this function is to get views per author
    INPUT: No inputs
    OUTPUTS: Returns a list of authors and their total views
    VIEWS IN PostgreSQL: author_views view must be created, see readme.md
    file for more details.
    '''
    author_views = '''SELECT authors.name, author_views.total_views
    FROM authors JOIN author_views
    ON authors.id = author_views.author;'''

    results = get_query_results(author_views)

    return results


def report_author_views(author_view_list):

    '''
    Objective of report_author_views() function is to print top authors and
    their total views
    INPUTS: author_view_list is an input in a list format with tuples as
    values for the list
    OUTPUTS: It prints/desplys the authors and their view counts.
    '''

    print("")
    print("List from the most popular author to the least:")
    print("")

    for author in author_view_list:
        print(author[0] + " - " + str(author[1]) + " views")


def get_most_error_per_day():

    '''
    Objective of get_most_error_per_day() function is to get most error
    rate per day
    INPUTS: There are no inputs to this function
    OUTPUTS: it returns a list of any days that has more than 1% error rate
    VIEWS IN PostgreSQL: error_per_day, requests_per_day, and
    error_rate_per_day
    views must be created,
    see readme.md file for more details.
    '''

    error_rate = '''SELECT * FROM error_rate_per_day
    WHERE percentage_error > 1;'''

    results = get_query_results(error_rate)

    return results


def report_most_error_per_day(most_error):
    '''
    Objective of report_most_error_per_day() function is to print
    days and error rate
    with more than 1% error rate per day
    INPUTS: most_error is an input in a list format with tuples
    as values for the list
    OUTPUTS: It prints/desplys the days and their error rate.
    '''

    print(" ")
    print("On following days error occured more than 1 %:")
    print(" ")

    for days in most_error:
        print(str(days[0]) + " - "
              + str((format(days[1], '.2f'))) + "%  errors"
              )


def final_report():
    '''
    Objective of this function is to call all the the reporting functions.
    INPUTS: There are no inputs
    OUTPUTS: There are no outputs
    '''

    report_top_three_articles(get_top_articlse())
    report_author_views(get_author_views())
    report_most_error_per_day(get_most_error_per_day())


if __name__ == '__main__':
    final_report()