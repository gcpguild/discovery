@echo off

set GH_TOKEN=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

echo "Git Hub Repository Key"

echo %GH_TOKEN%

:help
	echo %USERPROFILE%
	echo "Discovery is written in Python"
	
	echo "get init"
	echo "get discovery"
:init
	cd "C:\google\serpapi\indias\stratozone\discovery"
	git pull
	python "C:\google\serpapi\indias\stratozone\discovery\initialization.py"

:discovery
	echo "To collect the Machine Data the following program is executing"
	echo "Please wait for the program to generate the data"
	
	python "C:\google\serpapi\indias\stratozone\discovery\discovery.py"
:view
	%SystemRoot%\explorer.exe  "C:\google\serpapi\indias\stratozone\discovery\data"
	start excel "C:\google\serpapi\indias\stratozone\discovery\data\Machine_Data_System_Data_%computername%.csv"
	
:end