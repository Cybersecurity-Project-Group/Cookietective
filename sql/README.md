# Info
The SQL for this project is done using SQLLite, which is in the standard library. The files in this folder are as follows:

## sql_init
sql_init will initialize the SQL table called 'packets' with the following columns:
    website - holds tbe URL of the website
    ip - holds the ip address associated with the website
    vulnerability - holds the name of the vulnerability found

This should be run once if the table does not exist in the directory in order to create the table.

## sql_func
This file adds a variety of functions that can be used to help access the SQL database. To use them in
another module in the main directory, place the following in the header:

```
import sys
sys.path.append('sql')

import sql_func

from my_module import my_function
```

#### addEntry(website, ip, vulnerability)
This function will add an entry to the sql table with the values specified in the arguments.

#### fetchEntryWebsite(website)
This function will return the entries from the database that match the website given.