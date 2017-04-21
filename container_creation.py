#!/usr/bin/python
import subprocess
import sys
import shutil
service_name = sys.argv[1].lower()
image_name = "citi.docker.com:5000/"+service_name
base_image_name = sys.argv[2]
shutil.copy("/home/shefali/docker/java_tomcat/entrypoint.sh", ".")
shutil.copy("/home/shefali/docker/java_tomcat/dockerfile", ".")
subprocess.call(["python", "/home/shefali/scripts/python_scripts/replace_words.py", base_image_name, "@image_name", "dockerfile"])
subprocess.call(["docker", "build", "-f", "dockerfile", "-t", image_name, "."])
subprocess.call(["docker", "push", image_name])
subprocess.call(["docker", "service", "create", "--network", "my_network", "-p", "4100:8080", "--name", service_name, image_name])
