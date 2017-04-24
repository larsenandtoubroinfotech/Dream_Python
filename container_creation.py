#!/usr/bin/python
import subprocess
import sys
import shutil
import search_parameter_column_command
service_name = sys.argv[1].lower()
image_name = "citi.docker.com:5000/"+service_name
base_image_name = sys.argv[2]
shutil.copy("/home/shefali/docker/java_tomcat/entrypoint.sh", ".")
shutil.copy("/home/shefali/docker/java_tomcat/dockerfile", ".")
subprocess.call(["python", "/home/shefali/scripts/python_scripts/replace_words.py", base_image_name, "@image_name", "dockerfile"])
subprocess.call(["docker", "build", "-f", "dockerfile", "-t", image_name, "."])
subprocess.call(["docker", "push", image_name])
status = search_parameter_column_command.search_command_output(service_name)
if status == "present":
    subprocess.call(["docker", "service", "update", "--image", image_name, service_name])
else:
    subprocess.call(["docker", "service", "create", "--network", "my_network", "-p", "4100:8080", "--name", service_name, image_name])
