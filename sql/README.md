# Info
The SQL for this project is done using SQLLite, which is in the standard library. The files in this folder are as follows:

## sql_init
sql_init will initialize the SQL tables for the project as follows:
    
**CNAMEpackets**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domainName\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sourceAddress\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CNAMEAlias\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hasAType\
**ip**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domainName\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip\
**cookie**\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domainName\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;src_ip text\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domain_setting\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;httponly\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;secure

This should be run once if the table does not exist in the directory in order to create the table.

## sql_func
This file adds a variety of functions that can be used to help access the SQL database. To use them in
another module in the main directory, place the following in the header:

```
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import sql.sql_func as sql
```