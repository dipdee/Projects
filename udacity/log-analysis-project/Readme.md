You will need to unzip **newsdata.sql.zip** file after downloading it. The file inside is called **newsdata.sql** Put this file into the [vagrant](https://www.vagrantup.com/downloads.html) directory, which is shared with your virtual machine.

To load the data, use the command `psql -d news -f newsdata.sql`

Once you have the data loaded into your database, connect to your database using `psql -d news`

Views that need to be created:
*-Top three articles*
`CREATE VIEW title_views as SELECT articles.title, COUNT(*) AS views FROM articles, log WHERE log.path = CONCAT('/article/', articles.slug) AND status = '200 OK' GROUP BY articles.title ORDER BY views DESC LIMIT 3;`

*-Top authors*
`CREATE VIEW author_count as SELECT authors.name, COUNT(articles.slug) FROM authors, articles, log WHERE log.path = CONCAT('/article/', articles.slug) AND authors.id = articles.author GROUP BY authors.name ORDER BY COUNT DESC;`

*-Finding the  errors* **Please note that here need to create 3 views**
`CREATE VIEW error_log as SELECT date(log.time), count(log.status), log.status FROM log WHERE status NOT LIKE '200 OK' GROUP BY log.time, log.status;`

`CREATE VIEW all_log as SELECT date(log.time), COUNT(log.status), log.status FROM log GROUP BY log.time, log.status;`

`CREATE VIEW total_log as SELECT date, sum(count), status FROM all_log NATURAL INNER JOIN error_log GROUP BY all_log.date, all_log.status;`
