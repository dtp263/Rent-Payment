Rent-Payment
============
Django project with:
--------------------
	+ django 1.5
	+ django-auth
	+ SQLite3 Database
	+ virtualenv v1.8.4
	+ jquery v1.8.3
	+ Bootstrap (v3.0.0)
	+ south v.7.6
	
Requires:
--------------------
	- Python v2.7.5
	- Pip
	- Virtualenv
	
To get site running initially:
----------------------------------------------------------------------

(The command line must be in the root folder of the directory. Python, 
Pip, and Virtualenv must all be installed correctly.)

	$ virtualenv <yourEnvironmentName>
	$ workon <yourEnvironmentName>
	$ pip install -r requirements.txt
	$ cd roomer    # This takes you to the directory with all of the working files
	$ 
	$ #These next steps format and sync the db according to the files.
	$ ./manage.py syncdb   # It will ask you for some information to set up the admin acct
						   # May give you an error saying your missing some tables
	$ ./manage.py migrate core
	$ ./manage.py syncdb   # Straighten everything one last time
	$ ./manage.py runserver
	
After these steps you can go to a browser and type "localhost:8000".

--------------------------------------------------------------------------ss

If you change the models you must migrate the new schema to the db.
SQLite3 does not make this very easy so:

	1. delete "Rent-Payment/roomer/appdb"
	2. delete "Rent-Payment/roomer/core/migrations/0001_initial.py"
	
	$ ./manage.py schemamigration core --initial
	$ ./manage.py syncdb
	$ 		# Will prompt for info to create admin acct
	$ 		# will have an error syncing core
	$ ./manage.py migrate core
	$ ./manage.py syncdb

