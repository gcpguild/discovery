"""
    Machine Data Collection: In-house Tool by Google Cloud Nature Labs. 
    Application : Collect the machine data like CPU, Memory, Network for the purpose of business and architecture decisions for Google Cloud adoption.
    Purpose     : This application helps to collect the 'machine data' 
    Language    : This program is developed in Python language. 
    Function    : Collect the Machine data of the computers like CPU, Disk, Swap, Network Informattion, Environment Variable
    Data Type   : The data is colleted in both JSON and CSV format.
    Path        : This program should be placed in the appropriate folder.
    For Windows, the code path is :
    -------------------------------
        C:\google\serpapi\indias\stratozone\discovery
        ---------------------------------------------
    For Linux, the code path is :
    -----------------------------
        $HOME/google/serpapi/indias/stratozone/discovery
        -------------------------------------------
    Application deployment : Google Cloud adoption in  Infrastructure Modernization 
    
    Functional scope : Discovery and Assessment for Cloud adoption in Google 
    
    Google services Used : Cloud Build, Cloud Code, Compute Engine 
   
    Development : Cloud Code IDE Plugins 
    -------------------------------------
    Modules list :
    -----------------
    json        : JSON (JavaScript Object Notation) <http://json.org> is a subset of JavaScript syntax (ECMA-262 3rd edition) used as a lightweight data interchange format.
    socket      : This module provides socket operations and some related functions. On Unix, it supports IP (Internet Protocol) and Unix domain sockets. On other systems, it only supports IP. Functions specific for a socket are available as methods of the socket object.
    platform    : This module tries to retrieve as much platform-identifying data as possible. It makes this information available via function APIs. If called from the command line, it prints the platform information concatenated as single string to stdout. The output format is useable as part of a filename.This module tries to retrieve as much platform-identifying data as possible. It makes this information available via function APIs.
    datetime    : datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])
    re          : Support for regular expressions (RE). This module provides regular expression matching operations similar to those found in Perl. It supports both 8-bit and Unicode strings; both the pattern and the strings being processed can contain null bytes and characters outside the US ASCII range.
    os          : OS routines for NT or Posix depending on what system we're on.
    uuid        : UUID objects (universally unique identifiers) according to RFC 4122.
    logging     : Logging package for Python. Based on PEP 282 and comments thereto in comp.lang.python.
    platform    : This module tries to retrieve as much platform-identifying data as possible. It makes this information available via function APIs.
    pandas      : Pandas is an open-source library that is built on top of NumPy library. https://pandas.pydata.org. This is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language
    subprocess  : A subprocess in Python is a task that a python script delegates to the Operative system (OS). The subprocess library allows us to execute and manage subprocesses directly from Python. That involves working with the standard input stdin, standard output stdout, and return codes.
    pathlib     : Pathlib module in Python provides various classes representing file system paths with semantics appropriate for different operating systems. This module offers classes representing filesystem paths with semantics appropriate for different operating systems
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    CPU Info   : Returns the CPU info by using the best sources of information for your OS. Returns the result in a json string
    Generate the Google Big Query for the compute engine for performance
    Written by Kyndryl for project location in Nature Labs Project
    Author : ramamurthy.valavandan@kyndryl.com
    gcloud components 
"""
ipfilename = "machine_data"
fileformat = [ 'json', 'csv', 'txt' ]

machine_data_dict_obj = {'Machine_Data':'json', 
            'System_Data':'csv',
            'Environment_Data':'txt'} 

machine = []

#.........................................................................
import sys
from subprocess import check_output
import json, re, csv, openpyxl, sys, os
from pathlib import Path
import pandas as pd
from subprocess import check_output
import platform,socket,re,uuid,json,psutil,logging, platform, cpuinfo, uuid
from datetime import datetime
import socket

Host_or_Node_or_Machine_or_Env_Name = socket.gethostname()
IP_Address = socket.gethostbyname(Host_or_Node_or_Machine_or_Env_Name)
m = ("{}{}".format("Host Name:", Host_or_Node_or_Machine_or_Env_Name))
machine.append(m)
m = ("{}{}".format("IP address :", IP_Address))
machine.append(m)
#-----------------------------------------------------------------------------------------------------
uname = platform.uname()
myos = platform.system()
#-----------------------------------------------------
def fullyqualifydirs(mylist):
    mydircode = N.join(mylist)
    return mydircode
#-----------------------------------------------------
if (myos == "Linux" or myos == "linux2"):
    # linux
    N="/"
    homedirectory = str(Path.home())
    print(homedirectory)
    mylist = [ homedirectory, 'google/serpapi/indias/stratozone/dicovery' ]
    basedir = fullyqualifydirs(mylist)
elif myos == "win32" or myos == "Windows":
    # Windows 
    N="\\"    
    basedir = 'C:\\google\\serpapi\\indias\\stratozone\\discovery'  
#--------------------------------------------------------------
if not basedir:
    basedir = os.getcwd()
#-----------------------------------------------------------------------------------------------------
mylist = [basedir, 'initialization.py']
initialdirectoryconfig = fullyqualifydirs(mylist)
#--------------------------------------------------------------------------------------------------
def conliststr(myip,sep,ff):
    jfname = sep.join(str(x) for x in myip)
    s = ("{}{}{}".format(jfname,'.',ff))
    return s
#-----------------------------------------------------------------------------------------------------
def removen(string):
    for m in ('\n', '\r'):
        clean_string = re.sub(m, '', string)
        clean_string = clean_string.replace(m, '')
        clean_string = clean_string.rstrip()
        clean_string = clean_string.strip(m)
        clean_string = re.sub(m,' ', clean_string)
        mymano = ''
        for x in clean_string:
            mymano += ''+ x
        return mymano
#------------------------------------------------------------------------------------------------------
getdirectory = removen(check_output([sys.executable, initialdirectoryconfig], universal_newlines=True))
#------------------------------------------------------------------------------------------------------
ss = '_' 
iafilelist = [ipfilename,uname.node]
#------------------------------------------------------------------------------------------------------
for f in fileformat:
    ffile = conliststr(myip = iafilelist,sep = ss, ff = f)
    #print(ffile)
#------------------------------------------------------------------------------------------------------
def jsoning(fileext):
    mylist = [getdirectory, finfile ]
    machine_data_json = fullyqualifydirs(mylist)
    return machine_data_json
#-----------------------------------------------------
def csving(fileext):
    mylist = [getdirectory, finfile ]
    machine_data_csv = fullyqualifydirs(mylist)
    return machine_data_csv
#-----------------------------------------------------   
def txting(fileext):
    mylist = [getdirectory, finfile ]
    machine_data_txt = fullyqualifydirs(mylist)
    return machine_data_txt
#-----------------------------------------------------
def getSystemInfo():
    try:
        info={}
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)
#-----------------------------------------------------
#machinejson = json.loads(getSystemInfo())
machinejson = getSystemInfo()
#-----------------------------------------------------
cpuinfojson = json.loads(cpuinfo.get_cpu_info_json())
#-----------------------------------------------------
envinfojson = json.dumps(dict(os.environ))
#-----------------------------------------------------
#print(envinfojson)
#-----------------------------------------------------
def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
#-----------------------------------------------------
sysname = ('{}{}'.format('Operating System :', {uname.system}))
machine.append(sysname)
namenode = ('{}{}'.format('Machine or Node Name:', {uname.node}))
machine.append(namenode)
m = ('{}{}'.format('OS Release:', {uname.release}))
machine.append(m)
m = ("{}{}".format('OS Version:', {uname.version}))
machine.append(m)
m =("{}{}".format('Machine Type:', {uname.machine}))
machine.append(m)
m =("{}{}".format('CPU Processor:', {uname.processor}))
machine.append(m)
#-----------------------------------------------------
# Boot Time
boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)
#-----------------------------------------------------
mymachinelist = ['Boot Time (YYYY/MM/DD - Hrs-Mins-Secs):', 
                {bt.year}, 
                '/', 
                {bt.month},
                 '/', 
                 {bt.day},
                 '-',
                 {bt.hour},
                 '-',
                 {bt.minute},
                 '-', 
                 {bt.second} ] 
#-----------------------------------------------------
#g = addingmachinedata(mymachinelist)
#-----------------------------------------------------
s = ''.join(str(x) for x in mymachinelist)
#-----------------------------------------------------
machine.append(s)
#-----------------------------------------------------
m = ("{}{}".format("CPU Physical cores:", psutil.cpu_count(logical=False)))
machine.append(m)
#---------------------------------------------------------------------
m = ("{}{}".format("CPU Total cores:", psutil.cpu_count(logical=True)))
machine.append(m)
#--------------------------------------------------------------------
# CPU frequencies
cpufreq = psutil.cpu_freq()
m = ("{}{}{}".format("CPU Max Frequency:", {cpufreq.max}, "Mhz"))
machine.append(m)
m = ("{}{}{}".format("CPU Min Frequency:", {cpufreq.min}, "Mhz"))
machine.append(m)
m = ("{}{}{}".format("CPU Current Frequency:", {cpufreq.current}, "Mhz"))
machine.append(m)
# CPU usage
#-------------------------------------------------------------------------
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    cp = []
    c1 = ("{}{}{}{}{}{}{}{}".format("CPU Core", '(', i, ')', ':', {percentage}, '%', ' | '))
    
    c2 = ("{}{}{}".format("Total CPU Usage:", {psutil.cpu_percent()}, "%")) 
    cp = c1 + c2
    cpc = ''.join(cp)
    machine.append(cpc)
#----------------------------------------------------------------------------
svmem = psutil.virtual_memory()
m = ("{}{}".format("Total virtual_memory:", {get_size(svmem.total)}))
machine.append(m)
m = ("{}{}".format("Available virtual_memory:", {get_size(svmem.available)}))
machine.append(m)
m = ("{}{}".format("Used virtual_memory:", {get_size(svmem.used)}))
machine.append(m)
m = ("{}{}{}".format("Percentage virtual_memory:", {svmem.percent}, "%"))
machine.append(m)
#----------------------------------------------------------------------------
# get the swap memory details (if exists)
swap = psutil.swap_memory()
m = ("{}{}".format("Total Swap Memory:", {get_size(swap.total)}))
machine.append(m)
m = ("{}{}".format("Free Swap Memory:", {get_size(swap.free)}))
machine.append(m)
m = ("{}{}".format("Used Swap Memory:", {get_size(swap.used)}))
machine.append(m)
m = ("{}{}{}".format("Percentage of Swap Memory:", {swap.percent}, "%"))
machine.append(m)
#------------------------------------------------------------------------------
# Disk Information
#------------------------------------------------------------------------------
# get all disk partitions

partitions = psutil.disk_partitions()
for partition in partitions:
    try:
        mds = []
        m1 = ("{}{}{}".format("Device:", {partition.device}, ' | '))
        
        m2 = ("{}{}{}".format("Mountpoint:", {partition.mountpoint}, ' | '))
        
        m3 = ("{}{}{}".format("File system type:", {partition.fstype}, ' | '))
       
        partition_usage = psutil.disk_usage(partition.mountpoint)
        m4 = ("{}{}{}".format("Total Size:", {get_size(partition_usage.total)}, ' | '))
       
        m5 = ("{}{}{}".format("Used:", {get_size(partition_usage.used)}, ' | '))
       
        m6 = ("{}{}{}".format("Free:", {get_size(partition_usage.free)}, ' | '))
        
        m7 = ("{}{}{}".format("Percentage:", {partition_usage.percent}, "%"))
        mds = m1 + m2 + m3 + m4 + m5 + m6 + m7
        mdst = ''.join(mds)
        machine.append(mdst)
    except PermissionError:
        # this can be catched due to the disk that
        # isn't ready
        continue  
# get IO statistics since boot
disk_io = psutil.disk_io_counters()
m = ("{}{}".format("Disk IO read Count:", {get_size(disk_io.read_bytes)}))
machine.append(m)
m = ("{}{}".format("Disk IO write Count:", {get_size(disk_io.write_bytes)}))
machine.append(m)
#-----------------------------------------------------------------------
# Network information
# get all network interfaces (virtual and physical)
if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
  
    for address in interface_addresses:
        ipa = []
        if str(address.family) == 'AddressFamily.AF_INET':
            i1 = ("{}{}{}".format("IP Address:", {address.address}, ' | '))
           
            i2 = ("{}{}{}".format("Netmask:", {address.netmask}, ' | '))
            
            i3 = ("{}{}{}".format("Broadcast IP:", {address.broadcast}, ' | '))
            
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            i4 = ("{}{}".format("Netmask:", {address.netmask}))
            
            ipa = i1 + i2 + i3 + i4
            paty = ''.join(ipa)
            machine.append(paty)
          
# get IO statistics since boot
net_io = psutil.net_io_counters()
m = ("{}{}{}".format("Total Bytes Sent:", {get_size(net_io.bytes_sent)}, ' | '))
machine.append(m)
m = ("{}{}{}".format("Total Bytes Received:", {get_size(net_io.bytes_recv)}, ' | '))
machine.append(m)
#---------------------------------------------------------------------------             

import ipaddress

m = ("{}{}".format("IPv6Network_netmask:", {ipaddress.IPv6Network("::/112").netmask}))
machine.append(m)

m = ("{}{}".format("IPv6Network_hostmask:", {ipaddress.IPv6Network("::/112").hostmask}))
machine.append(m)

# Import libraries
import netifaces

m = ("{}{}".format("Gateway:", netifaces.gateways()))
machine.append(m)
# Getting interfaces
interfaces = netifaces.interfaces()

# Showing interfaces
for i in range(0,len(interfaces)):
    ifc = []
    # Getting interface status
    addrs = netifaces.ifaddresses(str(interfaces[i]))
    m = ("{}{}".format("netifaces_ifaddresses:", addrs))
    machine.append(m)

#----------------------------------------------------------
cpukeys = ['brand_raw', 'vendor_id_raw', 'arch_string_raw', 'arch', 'bits', 'count', 'model', 'hz_advertised_friendly',  'hz_actual_friendly', 'hz_actual', 'l2_cache_size', 'stepping', 'model',  'family', 'l3_cache_size' ]

for c in cpukeys:
    cpk = []
    for  i, (k, v) in enumerate(cpuinfo.get_cpu_info().items()):
        if (c ==  k):
          
            v = ("{}{}{}{}".format('CPU ', k, ': ', v))
            machine.append(v)

df1 = pd.DataFrame([machinejson])
df2 = pd.DataFrame([cpuinfojson])
df3 = pd.DataFrame([envinfojson])
df4 = pd.DataFrame([machine]) 

for filenamesyntax, fileext in machine_data_dict_obj.items():
    if (fileext == 'txt'):
        fe = 'csv'
    else:
        fe = fileext
    iafilelist = [filenamesyntax,uname.node]
    finfile = conliststr(myip = iafilelist,sep = ss, ff = fe)
    if (fileext == 'json'):
        fj = jsoning(fileext)
        print(fj)
        MergeJson = pd.concat([df4], axis=1)
        MergeJson.to_json(fj)
        
    if (fileext == 'csv'):
        fc = csving(fileext)
        print(fc)  
        MergeCSV = pd.concat([df1, df2], axis=1)
        mdhead = conliststr(myip = iafilelist,sep = ss, ff ='')
        cn = [re.sub(r"[^a-zA-Z0-9_-]+", '', mdhead)]
    
        machine_data_cvs = pd.DataFrame(machine, columns = cn)
        machine_data_cvs.to_csv(fc) 
    if (fileext == 'txt'):
        ft = txting(fileext)
        print(ft)  
        MergeTXT = pd.concat([df1, df2, df3], axis=1)
   
        mdhead = conliststr(myip = iafilelist,sep = ss, ff ='')
        ct = [re.sub(r"[^a-zA-Z0-9_-]+", '', mdhead)]
    
        machine_data_txt = pd.DataFrame(MergeTXT)
        machine_data_txt.to_csv(ft)
