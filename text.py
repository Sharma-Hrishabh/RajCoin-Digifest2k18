



# https://apitest.sewadwaar.rajasthan.gov.in/app/live/Service/family/details/1067-7PVQ-28383?client_id=ad7288a4-7764-436d-a727-783a977f1fe1



import urllib2
import json
# 1207-CN0V-24567
# 1207-HOTX-20756
# WDBBCCK
# WDBFUUK
bhama = "https://apitest.sewadwaar.rajasthan.gov.in/app/live/Service/family/details/1067-7PVQ-28383?client_id=ad7288a4-7764-436d-a727-783a977f1fe1"

page = urllib2.urlopen(bhama)

from bs4 import BeautifulSoup


soup = BeautifulSoup(page)

data  = str(soup)



def returnBhama():
    index = data.find("BHAMASHAH_ID")
    print(data[index+15:index+30])
    
def returnFirstLastName():
    indexName = data.find('"NAME_ENG"')
    string = data[indexName + 12:]
    indexQuote = string.find('"')
    name = data[indexName + 12 : indexQuote + indexName + 12] 
    
    print(name)
    
    nameComp = name.split()
    return nameComp[0] , nameComp[-1]           # firstName , lastName = returnFirstLastName()0
    
returnFirstLastName()
# 




https://docs.google.com/document/d/10SO9OnNO-MErc0aP8LcunPftvpbexlVXSWsjeJ2yW3c/edit?usp=sharing