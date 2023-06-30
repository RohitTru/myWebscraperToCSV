import lxml.etree
from selenium import webdriver

url = 'https://www.youtube.com/watch?v=lTypMlVBFM4'
driver = webdriver.Chrome()
driver.get(url)

xPathList = []
def validateXpath():
    global xPathList
    i=0
    
    while True:
        exitMessage = ''
        if i >= 1:
            exitMessage = 'or type done to move on '
        
        userInputXpath = input("Please input an xpath " + exitMessage)
        i+=1
        
        if userInputXpath == 'done':
            break
        try:
            driver.find_element('xpath', userInputXpath )
            xPathList.append(userInputXpath)

        except Exception as e:
            print(f'invalid Xpath: ')
    
    print('List of valid XPaths:')
    for xpath in xPathList:
        print(xpath)        
        
validateXpath()
