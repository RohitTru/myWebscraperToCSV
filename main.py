import requests

url = ''
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

        
        




def workingWithSelenium():
    import time
    from selenium import webdriver
    url = 'https://www.youtube.com/'

    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    driver.quit()




























def main():
    getUrlFromUser()
    print(url)

if __name__ == "__main__":
    main()