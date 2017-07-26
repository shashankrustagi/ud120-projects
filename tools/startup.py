
import urllib
import urllib.request
data = urllib.request.urlretrieve("https://www.cs.cmu.edu/~./enron/enron_mail_20150507.tgz")
import tarfile
import os
os.chdir("..")
tfile = tarfile.open("enron_mail_20150507.tgz", "r:gz")
tfile.extractall(".")
