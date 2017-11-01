import psycopg2
DBNAME = "news"

# 1. Query for three most popular articles of all time.
query1 = "select title,views from article_view limit 3"

# 2. Query for the most popular article authors of all time.
query2 = """select authors.name,sum(article_view.views) as views from
article_view,authors where authors.id = article_view.author
group by authors.name order by views desc"""

# 3. Query for days with more than 1% of request that lead to an error.
query3 = "select * from error_log_view where \"Percent Error\" > 1"

# Initializing Store results
query1_result = arr()
query1_result['title'] = "\n1. The 3 most popular articles of all time are:\n"

query2_result = arr()
query2_result['title'] = """\n2. The most popular article authors of
all time are:\n"""

query3_result = arr()
query3_result['title'] = """\n3. Days with more than 1% of request that
lead to an error:\n"""


# function returns query result
def get_query_results(query):
    db = psycopg2.connect(database = DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


def print_query_results(query_result):
    print (query_result['title'])
    for result in query_result['results']:
        print ('\t\t' + str(result[0]) + ' ===> ' + str(result[1]) + ' Views')


def print_error_query_results(query_result):
    print (query_result['title'])
    for result in query_result['results']:
        print ('\t\t' + str(result[0]) + ' ===> ' + str(result[1]) + ' %%')


# stores query result
query1_result['results'] = get_query_results(query1)
query2_result['results'] = get_query_results(query2)
query3_result['results'] = get_query_results(query3)

# print formatted output
print_query_results(query1_result)
print_query_results(query2_result)
print_error_query_results(query3_result)

