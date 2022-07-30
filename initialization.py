import re, os, platform
from operator import itemgetter
from pathlib import Path
#-----------------------------------------------------
def fullyqualifydirs(mylist):
    mydircode = N.join(mylist)
    return mydircode
#------------------------------------------------------------------
myos = platform.system()
#-----------------------------------------------------
if (myos == "Linux" or myos == "linux2"):
    # linux
    N="/"
    homedirectory = str(Path.home())
    print(homedirectory)
    mylist = [ homedirectory, 'google/serpapi/indias/stratozone/discovery' ]
    basedir = fullyqualifydirs(mylist)
elif myos == "win32" or myos == "Windows":
    # Windows 
    N="\\"    
    basedir = 'C:\\google\\serpapi\\indias\\stratozone\\discovery'  
#-----------------------------------------------------------------

#--------------------------------------------------------------------
def mkingdirs(givenlist):
    mymanog = ''.join(givenlist)
    mk_dir = Path(mymanog)
    mk_dir.mkdir(parents=True, exist_ok=True)
    return mk_dir
#-------------------------------------------------------------------
workingdir = mkingdirs(basepath)
os.chdir(workingdir)
#-------------------------------------------------------------------
cwd = os.getcwd()
myd = cwd.split(N)
#-----------------------------------------------------------------
def getstringswitch(check_string_name):
    dict={
           's0' : myd[0], 
           's1' : myd[1], 
           's2' : myd[2], 
           's3' : myd[3],
           's4' : myd[4],
           's5' : myd[5],
           'd'  : 'data',
           'max_gs' : 10
          }
    return dict.get(check_string_name, cwd)

givenlist = [basepath,N,getstringswitch(check_string_name = 'd')]

mkdirlist = mkingdirs(givenlist)

print (mkdirlist)
