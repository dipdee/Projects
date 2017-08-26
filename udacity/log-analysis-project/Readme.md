In this project we work with the database.The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, code answer questions about the site's user activity.

You need to use a virtual machine (VM) to run an SQL database server.

VirtualBox is the software that actually runs the virtual machine. You can download it from [HERE](virtualbox.org). Install the platform package for your operating system.

Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from [vagrantup.com](https://www.vagrantup.com/downloads.html).
[Here](https://drupalize.me/videos/installing-vagrant-and-virtualbox?p=1526) is the link that shows how to start vagrant.

You will need to download and unzip **newsdata.sql.zip** file.The file inside is called **newsdata.sql** Put this file into the **vagrant** directory, which is shared with your virtual machine.

To load the data, use the command `psql -d news -f newsdata.sql`

Once you have the data loaded into your database, connect to your database using `psql -d news`

Views that need to be created:
*-Top three articles*
`CREATE VIEW title_views as SELECT articles.title, COUNT(*) AS views FROM articles, log WHERE log.path = CONCAT('/article/', articles.slug) AND status = '200 OK' GROUP BY articles.title ORDER BY views DESC LIMIT 3;`

*-Top authors*
`CREATE VIEW author_count as SELECT authors.name, COUNT(articles.slug) FROM authors, articles, log WHERE log.path = CONCAT('/article/', articles.slug) AND authors.id = articles.author GROUP BY authors.name ORDER BY COUNT DESC;`

*-Finding the  errors* **Please note that here need to create 3 views**
`CREATE VIEW error_log as SELECT date(log.time) as date, COUNT(log.status)
FROM log WHERE status not like '200 OK' GROUP BY date;`

`CREATE VIEW all_log as SELECT date(log.time) as date, COUNT(log.status)
FROM log GROUP BY date;`

`CREATE VIEW total_log as SELECT all_log.date, 100.0 * error_log.count / all_log.count as err_pct FROM all_log, error_log where all_log.date = error_log.date;`

After the views are created you have to run a python file *reporting.py*
that shows the answers for the questions described in Description.md file.
