#!/usr/bin/python
import subprocess
import sys
#app_name = sys.argv[1]

app_list = []
def search_command_output(app_name):
    with open('command_output', 'w') as f:
        f.write(subprocess.check_output(["docker", "service", "ls"]))
    with open('command_output', 'r') as f:
        column_no = f.readline().split().index('NAME')
        for line in f: 
            app_names = line.split()[column_no]
            app_list.append(app_names)
    if app_name in app_list:
        return 'present'
