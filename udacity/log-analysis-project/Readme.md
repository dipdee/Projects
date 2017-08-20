You will need to unzip **newsdata.sql.zip** file after downloading it. The file inside is called **newsdata.sql** Put this file into the [vagrant](https://www.vagrantup.com/downloads.html) directory, which is shared with your virtual machine.

To load the data, use the command `psql -d news -f newsdata.sql`

Once you have the data loaded into your database, connect to your database using `psql -d news`

Views that need to be created:
*-Top three articles*
`CREATE VIEW title_views as SELECT articles.title, COUNT(*) AS views FROM articles, log WHERE log.path = CONCAT('/article/', articles.slug) AND status = '200 OK' GROUP BY articles.title ORDER BY views DESC LIMIT 3;`

*-Top authors*
`create view author_count as select authors.name, articles.title, articles.author, count(articles.slug) from authors, articles, log where log.path like '%' ||articles.slug|| '%' and authors.id = articles.author group by authors.name, articles.slug, articles.title, articles.author order by authors.name;`

*-Finding the  errors* **Please note that here need to create 2 views**
`create view error_log as select date(log.time), count(log.status), log.status from log where status not like '200 OK' group by log.time, log.status;`
`create view error_log2 as select date, sum(count), status from error_log where date = date group by date, status order by sum desc;`
