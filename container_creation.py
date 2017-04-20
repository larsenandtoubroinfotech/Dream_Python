#!/usr/bin/python
import subprocess
import sys
service_name = sys.argv[1].lower()
image_name = "citi.docker.com:5000/"+service_name+""
subprocess.call(["docker", "build", "-f", "/home/shefali/docker/java_tomcat/dockerfile", "-t", image_name, "/home/shefali/docker/java_tomcat/"])
subprocess.call(["docker", "push", image_name])

subprocess.call(["docker", "service", "create", "--network", "my_network", "-p", "4000:8080", "--name", service_name, image_name])
