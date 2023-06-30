import requests
from selenium import webdriver
import time


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

def main():
    getUrlFromUser()

    driver.get(url)
    time.sleep(1000)
    driver.close
    
    
if __name__ == "__main__":
    main()