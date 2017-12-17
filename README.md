# Transpile.py

Executes a command whenever a watch file is changed (mtime is modified). 
```
usage: transpile.py [-h] -f FILE -c COMMAND [-v-]

A simple python transpiler to run a command whenver a file changes

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  The file path toe hte file to be watched for changes
                        (changes means change in mtime
  -c COMMAND, --command COMMAND
                        The command to be run whenever the watched file
                        changes
  -v-, --version        show program's version number and exit

Usage: python transpile.py -f README.md -c pandoc README.md > /tmp/README.html
```


