# GimmeLog
GimmeLog analyzes all of the requests types coming to your websever and counts how many are being sent to your webserver.  

# Getting Started

Have your log files in the same directory as the program, 

The format of the log files: 

```LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"" combined```

To run
```python3 gimmelog.py ``` or ```python3 gimmelog -d logs.txt```

You can also specify a file to read from with the options `-d or --default` but this will skip to count the Total of 200 Requests.  
