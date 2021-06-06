from datetime import datetime
import requests
from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]
credentials = ServiceAccountCredentials.from_json_keyfile_name(jsonFile, scopes) 
file = gspread.authorize(credentials) # authenticate the JSON key with gspread
sheet = file.open("pysheet").sheet1  #open sheet
data = [['','','','','','','']]
sheet.insert_rows(data, row=2, value_input_option='RAW')
sheet.update_cell(2,1,datetime.now().strftime("%d-%m-%Y"))

def get_price_info(url,x):
    page = requests.get(url)
    soup = BeautifulSoup(page.text) 

    try:
        input_tag = soup.find(attrs={"name": "lastPrice"})
        output = input_tag['value']
        print (output)
        sheet.update_cell(2,x,output)
    except:
        return "None, None, None"

def get_yahoo_info(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, features="lxml")
    values = []

    try:
        rows = soup.find_all('span')
        for row in rows:
            values.append(row.get_text()) 
        sheet.update_cell(2,4,"\n".join(values[3:6]) )
        sheet.update_cell(2,5,"\n".join(values[7:10]))
        sheet.update_cell(2,6,"\n".join(values[11:14]))
            
    except:
        return None, None, None
    
    
if __name__ == '__main__':
#     url = ""  # change to whatever your url is

    get_yahoo_info(url)
    for x in range(2,3):
        get_price_info(urlTD,x)     
        get_price_info(urlRBC,x+1)
      
      
        
