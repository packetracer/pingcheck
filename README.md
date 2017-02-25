# pingcheck
Pings a host, posts to slack channel if timeout occurs

INSTALLATION:
Copy script to whereever the hell it is you keep your scripts.  If you don't have a directory for this now is a fantastic time to designate one.

USAGE:
[SCHEDULED TASK]:
Windows: Create a scheduled task, run as desired.

Debian:  edit crontab and create entry to run at desired interval.
*Example:*
* * * * * python  /home/rjp/py/pingcheck.py 8.8.8.8
This will run the script every minute against Google address 8.8.8.8

[MANUALLY]:
execute the script with python
*Example:*
>python pingcheck.py <IP>
i.e.
>python pingcheck.py 8.8.8.8
