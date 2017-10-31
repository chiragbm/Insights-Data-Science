'''
Created on Oct 29, 2017

@author: chiragm
'''
from _collections import defaultdict
import datetime

from Contributor import Receiver
import sys


def getDate(dt):
    m = int(dt[:2])
    d = int(dt[2:4])
    y = int(dt[4:])
    return datetime.datetime(y,m,d)

def isDateValid(dt):
    ## Transaction Date(MMDDYYYY)
#     print dt
    
    if len(dt) != 8:
        return False
    
    m = int(dt[:2])
    d = int(dt[2:4])
    y = int(dt[4:])
    try:
        datetime.datetime(y,m,d)
        return True
    except ValueError:
        return False

def sortUserData(a, b):
    
    u1 = a.split("-")[0]
    d1 = getDate(a.split("-")[1])
    
    u2 = b.split("-")[0]
    d2 = getDate(b.split("-")[1])
    
    if(u1 != u2):
        if u1 > u2:
            return 1
        else: 
            return -1
    else:
        if d1 > d2:
            return 1
        else:
            return -1
    


donorsFile = open(sys.argv[1], 'r')
index_dict = {'id':0, 'zipcode':10, 'td': 13, 'ta' : 14, 'other':15}

user_zipcode_dict = defaultdict(lambda : {})
user_date_dict = defaultdict(lambda : {})
user_date_set = set()
user_date_list = list()

median_date_file = open(sys.argv[3],'w')
median_zip_file = open(sys.argv[2], 'w')

for line in donorsFile.readlines():
    values = line.split('|')
    
    if values[index_dict['id']] is None or values[index_dict['id']] == "":  continue
    if values[index_dict['other']] != "":  continue
    if values[index_dict['ta']] is None or values[index_dict['ta']] == "":  continue
    
    
    usr = values[index_dict['id']]
    contri = int(values[index_dict['ta']])
    date = values[index_dict['td']]
    
    if len(values[index_dict['zipcode']]) >= 5:
        
        zp  = values[index_dict['zipcode']][:5]
        if user_zipcode_dict[usr].__contains__(zp):
            user_zipcode_dict[usr][zp].insertVal(contri)
        else:
            recipient = Receiver()
            recipient.insertVal(contri)
            user_zipcode_dict[usr][zp] = recipient
    
        
        median_zip_file.write("%s|%s|%s|%s|%s\n"%(usr, zp, user_zipcode_dict[usr][zp].median, user_zipcode_dict[usr][zp].total_transactions, user_zipcode_dict[usr][zp].total_contributions))
        #print usr, zp, user_zipcode_dict[usr][zp].median, user_zipcode_dict[usr][zp].total_transactions, user_zipcode_dict[usr][zp].total_contributions
    
    if isDateValid(date):
        
        if user_date_dict[usr].__contains__(date):
            user_date_dict[usr][date].insertVal(contri)
        else:
            recipient = Receiver()
            recipient.insertVal(contri)
            user_date_dict[usr][date] = recipient
            
        user_date_set.add(usr+"-"+date)


user_date_list = list(user_date_set)
user_date_list.sort(sortUserData)       
# print user_date_list

# print user_date_dict

for u_d in user_date_list:
    usr = u_d.split("-")[0]
    date = u_d.split("-")[1]
    
    median_date_file.write("%s|%s|%s|%s|%s\n"%(usr, date, user_date_dict[usr][date].median, user_date_dict[usr][date].total_transactions, user_date_dict[usr][date].total_contributions))
    #print usr, date, user_date_dict[usr][date].median, user_date_dict[usr][date].total_transactions, user_date_dict[usr][date].total_contributions
                                             
    
    