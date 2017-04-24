#!/usr/bin/python
import subprocess
f = open('command_output', 'w')
f = subprocess.Popen(["docker", "service", "ls"], stdout=subprocess.PIPE)

print f
#for line in open('command_output', 'w'):
#commmand_output = subprocess.Popen(["docker", "service", "ls"], stdout=subprocess.PIPE).stdout
#print commmand_output
