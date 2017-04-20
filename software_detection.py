#!/usr/bin/python
import os
import sys
import subprocess
import image_in_registry 
import shutil
app_file = sys.argv[1]
file_extension = app_file.split(".")[1]
service_name = app_file.split(".")[0]
registry_url = "https://citi.docker.com:5000/v2/_catalog"
apache_repository_url = "http://10.101.3.141/package_repository/debian/"
scripts_path = "/home/shefali/scripts/python_scripts"
if os.path.exists("/home/shefali/app/"+service_name):
        os.rmdir("/home/shefali/app/"+service_name)
os.makedirs("/home/shefali/app/"+service_name)
###below mentioned line can be removed later
shutil.copy("/home/shefali/app/"+app_file, "/home/shefali/app/"+service_name)
os.chdir("/home/shefali/app/"+service_name)
def java_application(app_file):
        class_file = subprocess.Popen(["jar", "tf", app_file], stdout=subprocess.PIPE).stdout
	for line in class_file:
              if ".class" in line:
                     class_file = line.rstrip()
                     break
        subprocess.call(["jar", "xvf", app_file, class_file], stdout=subprocess.PIPE)
        major_version = subprocess.Popen(["javap", "-cp", app_file, "-verbose", class_file], stdout=subprocess.PIPE).stdout
        for line in major_version: 
              if "major" in line:
                        major_version = line.rstrip().split(":")[1].split(" ")[1]
	for line in open('/home/shefali/scripts/jdk_version'):
               if major_version in line:        
			java_version = line.split(":")[1].split(".")[1].rstrip()
			apache_tomcat="apache-tomcat-"+java_version
			java_software="jdk-"+java_version
                        image_name=java_software+"_"+apache_tomcat
        image_status=image_in_registry.image_search(registry_url , image_name)
        if image_status == "present":
               subprocess.call(["python", "container_creation.py", service_name])
        else:
               tomcat_package_name = subprocess.check_output(["python", ""+scripts_path+"/phtn_test.py", apache_repository_url, apache_tomcat]).rstrip()
               subprocess.call(["python", ""+scripts_path+"/replace_words.py", tomcat_package_name, "@apache_package", "/home/shefali/docker/java_tomcat/dockerfile_base"])     
               java_package_name = subprocess.check_output(["python", ""+scripts_path+"/phtn_test.py", apache_repository_url , java_software]).rstrip()
               subprocess.call(["python", ""+scripts_path+"/replace_words.py", java_package_name, "@jdk_package", "/home/shefali/docker/java_tomcat/dockerfile_base"])
               subprocess.call(["docker", "build", "-f", "/home/shefali/docker/java_tomcat/dockerfile_base", "-t", image_name, "/home/shefali/docker/java_tomcat"])
               subprocess.call(["python", ""+scripts_path+"/replace_words.py", app_file, "@war_name"])
               subprocess.call(["python", ""+scripts_path+"/container_creation.py", service_name])              
if file_extension == "war":
	java_application( app_file )
