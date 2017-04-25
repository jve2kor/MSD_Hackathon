#!/usr/bin/env python2
# -*- coding: utf-8 -*-
""" This code is used to read the log file into the memory  and convert into the data frame
    Once the log file is loaded ,every item in the IPQuery file checked if exist and result is print onto the console"""


#importing  python modules required for this script to perform operations

import time
import sys



start = time.time()#capturing time instance


class IpQuery:
    """Below methods contain the functionality to read file paths ,import log and query data 
       and provide the result to the console """    
    def __init__(self):
        self.log_file_name= ""
        self.query_file_name = ""
        self.logset = {}
        self.IPlist= []
        
    def Inputfiles(self):
        """code to check the arguments passed  and throw an error  """
        if len(sys.argv)!= 3:
            raise  ValueError(""" PLEASE PASS THE BOTH LOG FILE AND IPQUERY FILE AS INPUT TO SCRIPT
                              ex: python program.py log_file query_file """) 
       # extracting file names from command line
        self.log_file_name=sys.argv[1]
        self.query_file_name = sys.argv[2]
        
    def read_logfile(self):
        #Reading the log data
        with open(self.log_file_name,'r') as f:
            self.logset = {line.split(' ')[2] for line in f}


    def read_Queryfile(self):
        #Reading the query file into the  dataframe"""
        with open(self.query_file_name,'r') as f:
            self.IPlist = [line.rstrip('\n') for line in f]
            

    def CheckIpAdress(self):
        #Ip address from query file ae checked against the log file """ 
        dummy= self.logset.intersection(set(self.IPlist))
    
        for element in self.IPlist:
            if element in dummy:
                print "1"
            else :
                print "0"
                



#Create an instance of the IpQuery file
msd=IpQuery()
#Extacting the input file information 
msd.Inputfiles()
#Importing the Ip informatin from the log files
msd.read_logfile()
#Importing the Ipquery information from the quer file
msd.read_Queryfile()
#Serching for the Ip in log file
msd.CheckIpAdress()



            
    
                
print "Execution Time of this script is  %f" %(time.time() - start)
                
