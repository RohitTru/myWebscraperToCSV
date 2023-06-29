


def workingWithSelenium():
    import time
    from selenium import webdriver
    url = 'https://www.youtube.com/'

    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    driver.quit()




























def main():
    workingWithSelenium()

if __name__ == "__main__":
    main()