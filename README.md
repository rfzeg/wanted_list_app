# wanted_list app repository

Author: Roberto Zegers R.  
Date: June 2021  
License: BSD-3-Clause  

## Description

Minimal Flask app using PostgreSQL via SQLAlchemy.  


## Usage

Note: You must have a postgres server running before you can run <strong>createdb</strong>. Do it by connecting to a <strong>PostgreSQL database cluster</strong> first, with the command <code style="background: black; color: white;">pg_ctl -D my_db_cluster start</code>.<br>

Manually create the database <code>whishlistdb</code> first, do it using the <code style="background: black; color: white;">createdb</code> command line tool installed with Postgres:
<pre style="background: black; color: white; overflow: hidden; white-space: break-spaces;padding: 6px;">createdb whishlistdb
</pre>

You will also have to create some database records using <code>psql</code>.<br> 
Connect <code>psql</code> to the <strong>whishlistdb</strong> database:
<pre style="background: black; color: white; overflow: hidden; white-space: break-spaces;padding: 6px;">psql whishlistdb
</pre>

Now run the application using:<br>

<br>
<pre style="background: black; color: white; overflow: hidden; white-space: break-spaces;padding: 6px;">
$ python3 app.py
</pre><br>

Enter the URL <code> http://127.0.0.1:5000/</code> on your browser to display the app.<br>

It will just show a blank page.<br>

On your terminal tab running <strong>psql</strong> insert new records into the <strong>whishes</strong> table:
    
<pre style="background: black; color: white; overflow: hidden; white-space: break-spaces;padding: 6px;">    
whishlistdb=# INSERT INTO whishes (description) VALUES ('Thing 1');
INSERT 0 1
whishlistdb=# INSERT INTO whishes (description) VALUES ('Thing 2');
INSERT 0 1
whishlistdb=# INSERT INTO whishes (description) VALUES ('Thing 3');
INSERT 0 1
whishlistdb=# INSERT INTO whishes (description) VALUES ('Thing 4');
INSERT 0 1
whishlistdb=#
</pre>

Verify that the new database records got added:<br>
    
<pre style="background: black; color: white; overflow: hidden; white-space: break-spaces;padding: 6px;">whishlistdb=# SELECT * FROM whishes;
</pre>

Finally enter the URL <code> http://127.0.0.1:5000/</code>  on your browser and refresh is neccesary.<br> 

Expected result:<br>

<div> 
<img src="docs/images/expected-result-1.png" align="left" /> 
</div> 
<br clear="all"> 

