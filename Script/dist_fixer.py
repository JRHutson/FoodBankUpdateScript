import csv
import xlrd
from os.path import join, dirname, abspath

fname = join(dirname(dirname(abspath(__file__))), 'StartingList', 'Agency List Dec 2015.xls')

xl_workbook = xlrd.open_workbook(fname)

    #instantiate csv reader variable
    reader = csv.reader(csvfile,delimiter=',', quotechar='"')

    #loop through each row in the csv
    for row in reader:

        #grab value for DistributionSchedule column and split into 2 list strings based on period
        split_values = row[9].split(".")        

        #this if statements tests to make sure there are only 2 items in that list. some of the values have more than 2, and should be cleansed
        if len(split_values) == 2:
            
            #split the list into a 2 item list- open and close time
            open_close_times = split_values[1].split("-")

            #try printing out the open and close time
            try:
                #declare open and close times as variables
                open_time = open_close_times[0]
                closing_time = open_close_times[1]

                #print open and close times
                print "Open Time: ", open_time, " | Close Time: ", closing_time
            except:
                #if there are more than 2 items in the resulting mess of splits, this error will display
                print ""
                print "ERROR: ", split_values
                print ""
