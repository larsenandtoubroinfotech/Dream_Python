#!/usr/bin/python
from sys import argv
from subprocess import Popen,PIPE,STDOUT,call
import os
import commands
import sys
import subprocess, sys
#print sys.argv
#script_name , app_file = argv 
app_file = sys.argv[1]
print "app_file ::",app_file
file_extension = app_file.split(".")[1]
print "file_extension ::",file_extension
service_name = app_file.split(".")[0]
print "service_name ::",service_name
def java_application( app_file ):
        os.chdir("/home/shefali/app/")
        class_file = subprocess.Popen(["jar" , "tf" , app_file], stdout=subprocess.PIPE)
	for line in class_file.stdout:
              if ".class" in line:
                     class_file = line.rstrip()
                     print "class_file ::",class_file
                     break
        subprocess.call(["jar" , "xvf" , app_file , class_file], stdout=subprocess.PIPE)
        major_version = subprocess.Popen(["javap" , "-cp" , app_file , "-verbose" , class_file], stdout=subprocess.PIPE)
        for line in major_version.stdout: 
              if "major" in line:
                        major_version = line.rstrip().split(":")[1].split(" ")[1]
                        print "major_version ::",major_version
        jdk_version_file = open('/home/shefali/scripts/jdk_version')
	for line in jdk_version_file:
               if major_version in line:        
			java_version = line.split(":")[1].split(".")[1].rstrip()
			print "Java Version ::",java_version
			apache_tomcat="apache-tomcat-"+java_version
			print "Apache Tomcat ::",apache_tomcat
			java_software="jdk-"+java_version
			print "Java Software ::",java_software
                        image_name=java_software+"_"+apache_tomcat
                        print "image_name ::",image_name
                        exit()
                        ####################################
                        #for identifying the image is present in registry or not
                        result = subprocess.check_output(["curl", "-k", "https://citi.docker.com:5000/v2/_catalog"])
                        print "result", result
                        with open('some_file.txt', 'w') as f:
                             f.write(result)
                        with open('some_file.txt', 'r') as f:
                             for line in f:
                                print line
                                if image_name in line:
                                    print "Line :: ", line
                                    #image_status = "present"
                                    #os.system("python container_creation.py "+image_status+" "+service_name)
                                else:
                        ###################################
                        #for replacing @apavhe_package in the dockerfile
                        #getting tomcat package tar name from repository
                                    #image_status = "absent"
                                    proc = subprocess.Popen("python phtn_test.py http://10.101.3.141/package_repository/debian/ "+apache_tomcat,stdout=subprocess.PIPE,shell=True)
                                    print proc
                                    (out, err) = proc.communicate()
                                    outwithoutreturn = out.rstrip('\n')
                                    print "out ::", out
                                    print "outwithoutreturn ::", outwithoutreturn
                        #calling replace script   
                                    os.system("python replace_words.py "+outwithoutreturn+" @apache_package")                       
                        #for replacing @jdk_package in the dockerfile
                        #getting java package tar name from repository
                                    proc = subprocess.Popen("python phtn_test.py http://10.101.3.141/package_repository/debian/ "+java_software,stdout=subprocess.PIPE,shell=True)
                                    print proc
                                    (out, err) = proc.communicate()
                                    outwithoutreturn = out.rstrip('\n')
                                    print "out ::", out
                                    print "outwithoutreturn ::", outwithoutreturn
                        #calling replace script
                                    os.system("python replace_words.py "+outwithoutreturn+" @jdk_package")
                                    subprocess.Popen("docker build -f /home/shefali/docker/java_tomcat/dockerfile_base -t "+image_name+" /home/shefali/docker/java_tomcat",stdout=subprocess.PIPE,shell=True)
                        os.system("python replace_words.py "+app_file+" @war_name")
                        os.system("python container_creation.py "+service_name)              
if file_extension == "war":
	java_application( app_file )
