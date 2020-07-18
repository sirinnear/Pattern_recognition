from glob import glob
from urllib.request import urlretrieve
import ssl
import sys

files = glob('data/*.csv')
fmt = 'https://github.com/muic-pattern-rekt-2018/Homework-01-Bayes/raw/master/{0}'

try:
  for f in files:
    url = fmt.format(f)
    print('Downloading : {0}'.format(f))
    urlretrieve(url, f)
    print()
except ssl.SSLCertVerificationError as e:
  print(e)
  v = sys.version_info[0]+'.'+sys.version_info[1]
  print('If you are on OSX you may need to install all the certificates by running')
  print('/Applications/Python\\ {0}/Install\\ Certificates.command'.format(v))
  print('see the very bottom of https://www.python.org/downloads/release/python-370/')
#https://github.com/muic-pattern-rekt-2018/Homework-01-Bayes/raw/master/data/mushrooms_homework_test.csv
