
#Link to MSD code Challenge
# http://marketing-ao.madstreetden.com/acton/media/25759/msd-coding-challenge
import pandas as pd
import time
import sys

start = time.time()

#Reding the input files
log_file_name="msd.log"
query_file_name = "ip_query.log"
#if len(sys.argv) > 1:
#    print "there are", len(sys.argv)-1, "arguments:"
#    for arg in sys.argv[1:]:
#        print arg
#else:
#    print "there are no arguments!"
#    raise  ValueError('PLEASE PASS THE LOG FILE AND IPQUERY FILE AS INPUT TO SCRIPT') 
#    
#print sys.argv[1] ,sys.argv[2]
##log_file_name=sys.argv[1]
##query_file_name = sys.argv[2]


df = pd.read_csv(log_file_name," ",header=None,names = ['DATE','TIME', 'IPADDR','URL','STATUS'] )
query=pd.read_csv(query_file_name," ",header=None )
#cleaning the data by the time stamp and Date 
#Fromating the data helps to use Time series forcasting
#df[0]=df[0]+" "+df[1]
#del(df[1]) #Removing the unwanted time stamp data
#df.columns = ['DATE','TIME', 'IPADDR','URL','STATUS']
#
#
#
final_output=query.isin(df.IPADDR).astype(int)
print final_output
print "Execution Time of this script is  %f" %(time.time() - start)
