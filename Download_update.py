import os
import wget

url = 'https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.hpp'
try :
    os.mkdir("offsets/")
    os.chdir("offsets/")
    wget.download(url, 'csgo.hpp')
except:
    print("Make backup of offsets folder before continue!")

print("Offset download successfully")


