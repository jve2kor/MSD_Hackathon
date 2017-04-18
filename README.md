# MSD_Hackathon
This repo is used to  submit the code challenge

This is the Mad Street Den Online coding challenge, which will establish basic eligibility to participate in the Hackathon.

Follow the instructions as below and send your submissions to careers@madstreeden.com with Subject line: Hackathon Coding Challenge


Submissions by 23:59 hours, 21st April 2017 (Friday). 

 

Don't forget to attach a 1-page pdf resume with your submission 

 

The Challenge:

You have a log file where each line is of the following format 

 

date ipaddr url status

 

Here is an example file: 

2017-03-02 13:02:43 123.123.123.123 /index.html 200

2017-03-02 13:02:46 123.123.123.124 /index.html 200

2017-03-02 13:02:47 123.123.123.125 /about1.html 404

2017-03-02 13:02:49 123.123.123.123 /about.html 200

 

The log file can have maximum of 1 million lines with upto 1 million unique IP addresses. 

 

You also have a query file which is a list of IP addresses. One IP address per line.

Example file: 

123.123.123.123

123.123.123.124

123.123.123.125

123.123.123.126

 

What you need to do:

Write a program that takes in 2 inputs (log file and ip_query file) and outputs to stdout

1) read and parse the log files

2) load the IP addresses in memory

3) for every IP in the ip_query file, print to stdout if the IP was seen in the log file. 

Print 1 if IP was found and 0 if IP was not found. In the same order as the query file.

 

For the above example input files, the output will be:

$ python program.py log_file query_file 

1

1

1

0




Note:

Make sure the program takes in the files in the same order as in the example. log file first and query file second.
Your program will be evaluated on the following criteria in order: correctness, clean and modular code, test cases, time taken to run, and the memory required.
If your code needs external dependencies, make sure to track them in the requirements.txt file. Also have a README file if there are any special instructions to make your program run.
