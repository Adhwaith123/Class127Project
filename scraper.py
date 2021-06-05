from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
starturl="https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser=webdriver.Chrome("/Users/LENOVO/Downloads/chromedriver_win32/chromedriver")
browser.get(starturl)
time.sleep(10)

def scrape():
    headers=["Proper_name","Distance","Mass","Radius"]
    planetData=[]
    soup=BeautifulSoup(browser.page_source,"html.parser")
    for trtag in soup.find_all("ul",attrs={"class"," brighteststars"}):
        thtags=trtag.find_all("li")
        templist=[]
        for index,thtags in enumerate(thtags):
            if index==0:
                templist.append(thtags.find_all("a")[0].contents[0])

            else:
                try:
                    templist.append(thtags.contents[0])

                except:
                    templist.append("")

         starsData.append(templist)   

   with open("scrper.csv","w")as f:
        csvWriter=csv.writer(f)
        csvWriter.writerow(headers)
        csvWriter.writerows(starsData)                  

scrape()



        
