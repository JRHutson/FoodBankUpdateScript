import csv
import logging

def initialize_logger(output_dir):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
     
    # create console handler and set level to info
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

#open CSV as read only
with open(r"/Users/Regan/Documents/Repositories/FoodBankUpdateScript/StartingList/AgencyList.csv","rb") as csvfile:

    #instantiate csv reader variable
    reader = csv.reader(csvfile,delimiter=',', quotechar='"')
    
    
    #loop through each row in the csv
    firstline = True
for row in reader:
    if firstline:    #skip first line
        firstline = False
        continue
        