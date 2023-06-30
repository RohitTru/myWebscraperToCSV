
from selenium import webdriver
import time

url = 'https://www.youtube.com/watch?v=lTypMlVBFM4'
driver = webdriver.Chrome()
driver.get(url)

time.sleep(5)

fieldNames = []
xPathList = []


def getFieldAndXPath():
    global fieldNames
    global xPathList
    
    i=0
    while True:
        # Exit message
        exitMessage = ""
        if i >= 1:
            exitMessage = "or type 'done' to move on "
        
        # Gather field name
        userInputFieldName = input('Please input a name of a field you would like to scrape ' + exitMessage)
        fieldNames.append(userInputFieldName)
        i+=1
        
        # Exit loop
        if userInputFieldName == 'done':
            break
        
        # Gather and validate XPath
        userInputXpath = input("Please input an xpath: ")
        try:
            driver.find_element('xpath', userInputXpath )
            
            # Append to list if program checks out
            xPathList.append(userInputXpath)

            # Toss out the error and try again
        except Exception as e:
            print(f'invalid Xpath: ')
    
            

getFieldAndXPath()     
print(fieldNames)
print(xPathList)
time.sleep(50)


