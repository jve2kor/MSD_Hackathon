
#Link to MSD code Challenge
# http://marketing-ao.madstreetden.com/acton/media/25759/msd-coding-challenge
import pandas as pd
import time
import sys

""" code to check the arguments passed   """
if len(sys.argv) > 1:
    print "there are", len(sys.argv)-1, "arguments:"
    for arg in sys.argv[1:]:
        print arg
else:
    print "There are no arguments!,Provide Log and IPquery file"
    raise  ValueError('PLEASE PASS THE LOG FILE AND IPQUERY FILE AS INPUT TO SCRIPT') 
    
#extracting file names from command line
log_file_name=sys.argv[1]
query_file_name = sys.argv[2]



#extracting file names from command line
#log_file_name = "/Users/jvr605/Downloads/msd.log"
#query_file_name = "/Users/jvr605/Downloads/ip_query.log"

start = time.time()

#Reading the content from the log file into dataframe log_df
log_df = pd.read_csv(log_file_name," ",header=None ,names = ['DATE','TIME', 'IPADDR','URL','STATUS'],skip_blank_lines = True)

#Reading the content from the IPquery file into the data frame query_df
query_df = pd.read_csv(query_file_name," ",header=None,skip_blank_lines=True )

#Cheking if the IP address exists in the log file
Ipfound = query_df.isin(log_df.IPADDR).astype(int)

#print Ipfound[0].values.astype(int)

for items in Ipfound[0]:
    print items
    
 
    
#for everritem in     query_df[0]:
#    if everritem in log_df.IPADDR:
#        print 1
#    else:
 #       print 0
    

print "Execution Time of this script is  %f" %(time.time() - start)
