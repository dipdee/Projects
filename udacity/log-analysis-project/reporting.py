#!/usr/bin/env python

'''
Logs Analysis Project.

Please note that this code will work only if database views were created.
Views are described in Readme.md.
'''
import psycopg2


def popular_articles():
    '''
    This function returns TOP 3 popular articles.
    '''
    datb = psycopg2.connect(database='news')
    conn = datb.cursor()
    conn.execute("select * from title_views;")
    result = conn.fetchall()
    print "Three most popular articles are:" + '\n'
    for title, views in result:
        print "     %s | %s total views" % (title, views)
    conn.close()
    datb.close()


def popular_authors():
    '''
    This function returns all popular authors.
    '''
    datb = psycopg2.connect(database='news')
    conn = datb.cursor()
    conn.execute("select * from  author_count;")
    result = conn.fetchall()
    print '\n' + "The most popular authors are:" + '\n'
    for name, count in result:
        print "     %s | %s total views" % (name, count)
    conn.close()
    datb.close()


def log_errors():
    '''
    This function returns all errors waht were returned on different days.
    '''
    datb = psycopg2.connect(database='news')
    conn = datb.cursor()
    conn.execute("""select date, ROUND((100* sum / (SUM(sum) OVER ())),1),status"
                    " from total_log order by round desc;""")
    result = conn.fetchall()
    print '\n' + "Days when requests lead to errors:" + '\n'
    for output in result:
# I used output instead of date and round, because round is a build-in function.
        print "     On the %s were %s%% requests,"\
              " that lead to errors" % (output[0], output[1])
    conn.close()
    datb.close()


if __name__ == "__main__":
    popular_articles()
    popular_authors()
    log_errors()
