
import sys, os
#sys.path.append(os.getcwd())
#sys.path += ["whatever"]
#print(sys.path)

pwd = os.getcwd()
#set_path = "export PATH=$PATH:"+pwd
#os.system(set_path)
#os.system("echo $PATH")
#print(sys.path)

os.environ["PATH"] += ":" + pwd
print(os.environ["PATH"])

from selenium import webdriver
browser = webdriver.Firefox()

