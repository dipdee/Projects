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
    conn.execute("""select date, err_pct from total_log where err_pct > 1
                    order by err_pct desc;""")
    result = conn.fetchall()
    print '\n' + "Days when requests lead to errors:" + '\n'
    for date, err_pct in result:
        print "     On the %s were %.2f%% requests,"\
              " that lead to errors" % (date, err_pct)
    conn.close()
    datb.close()


if __name__ == "__main__":
    popular_articles()
    popular_authors()
    log_errors()
