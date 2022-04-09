import requests
from bs4 import BeautifulSoup
import mysql.connector as c 
con=c.connect(host="localhost",user="root",passwd="12345",database="scrape_data") #connecting to database
if con.is_connected():
    print("Database connected!")
else:
    print("connectivity issue ")
cursor =con.cursor()
try:
    url="https://www.flipkart.com/search?q=Iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off" #hitting url to get the data
    r=requests.get(url)
    print("Getting data from flipkart..... ")
    content_=r.content
    soup= BeautifulSoup(content_,"html.parser")
except:
    print("error!")
try:
    
    for i,j  in zip( (soup.findAll('div', {'class': '_4rR01T'})) , (soup.findAll('div',{'class': '_30jeq3 _1_WHN1'}))): #extracting data from the webpage
        strr="insert into scrapedata(Modelname,Price)values('{}','{}')".format((str(i.text)),(j.text[1:]))  #inserting the data into the sql database
        cursor.execute(strr)
except:
    print("Data not updated. there is some issue")

print("data updated in the database succesfully!")  
con.commit()    #saving the data in the database 


