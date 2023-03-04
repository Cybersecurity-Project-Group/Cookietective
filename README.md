# CoolestProject

Emulator Notes


Non-Emulator Notes:
Application that checks if a web application uses SQL and, if so, try to exploit using injection commands:
Basically, I’m thinking of maybe making an application that can scan inputted web applications for possible SQL injection points. It seems like similar projects have already been done, but this feels like something fun and technical that we could work on. Basic premise of these websites seems to be that you could create a program to scan the HTML inspection part and see if there are any parameters that could be being used for SQL queries, then if it finds some try to inject some queries into it to search for things like error messages.

There are similar tools on the internet so I don’t know if it would be something repetitive, but it does mean it seems like something possible that could be done

https://www.quora.com/How-do-I-know-what-DB-a-website-page-is-using 
https://brainly.in/question/11851081#:~:text=Answer%3A,database%20error%20will%20be%20shown. 
https://security.stackexchange.com/questions/25213/how-to-know-which-database-is-behind-a-web-application 
https://www.quora.com/How-can-I-know-what-database-any-site-uses Some tools that you can use for analyzing websites’ HTML code for DB stuff
Some similar tools already exist: https://resources.infosecinstitute.com/topic/best-free-and-open-source-sql-injection-tools/#:~:text=SQLninja%20is%20a%20SQL%20injection,information%20from%20the%20database%20server.
Could also search for open SQL ports on the web\
Scan around on port 1433 for old, unpatched SQL communications to grab information and steal it for personal gain
Profit


Pypi:

This is something that I have done less research on but basic idea is what professor said about Pypi malicious packets. Not sure if this is too similar to the other group’s idea about scanning into VSCode extensions though.

https://securitylabs.datadoghq.com/articles/guarddog-identify-malicious-pypi-packages/

Game emulator

Alex Prior mentioned we could use Bluestack to emulate Android for Windows and macOS to run Android apps. Might be able to use it to emulate our own Android app => create app without having to be on Google store or have any kind of validation stuff (doesn’t touch react native).  
