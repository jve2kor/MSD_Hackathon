
#Link to MSD code Challenge
# http://marketing-ao.madstreetden.com/acton/media/25759/msd-coding-challenge
import pandas as pd
import time

start = time.time()
df = pd.read_csv("/Users/jvr605/Downloads/msd.log"," ",header=None )
df[0]=df[0]+" "+df[1]
del(df[1])
df.columns = ['DATE', 'IPADDR','URL','STATUS']

query=pd.read_csv("/Users/jvr605/Downloads/ip_query.log"," ",header=None )

final_output=query.isin(df.IPADDR).astype(int)
print final_output
print time.time() - start
