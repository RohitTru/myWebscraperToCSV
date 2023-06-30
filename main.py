import requests
from selenium import webdriver
import time

fieldNames = []
xPathList = []

url = None
driver = webdriver.Chrome()
def getUrlFromUser():
    global url
    while True:
        
        # Url Validation
        try: 
            userInput = input("Please enter the URL of the website you would like to scrape:\n")
            page = requests.get(userInput)
            statusCode = page.status_code
            
            if page.status_code == 200:
                print(f'Status code: {statusCode} connection secured.') 
                url = userInput
                return url

        except Exception:
            print("Your url did not work")

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


def main():
    
    getUrlFromUser()

    driver.get(url)
    getFieldAndXPath()
    print(fieldNames)
    print(xPathList)
    time.sleep(800)
    driver.close
    

if __name__ == "__main__":
    main()