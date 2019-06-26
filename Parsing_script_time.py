from selenium import webdriver
from time import sleep
from tqdm import tqdm


try:
    driver = webdriver.Chrome(executable_path='./chromedriver')
except:
    print('chromedriver not found')

try:
    driver.get("http://proxylibrary.hse.ru:2048/login?url=http://isiknowledge.com/wos")
except:
    print('hse proxylibrary page not available: http://proxylibrary.hse.ru:2048/login?url=http://isiknowledge.com/wos')


def OpenWoSandSearch(driver):

    print('Please input you hse library login:')
    email = input()
    print('Please input you hse library password:')
    password = input()

    inputElement = driver.find_element_by_xpath(
        "/html/body/center/table/tbody/tr/td/div[2]/form/table/tbody/tr[1]/td[2]/input")
    inputElement.send_keys(email)

    inputElement = driver.find_element_by_xpath(
        "/html/body/center/table/tbody/tr/td/div[2]/form/table/tbody/tr[2]/td[2]/input")
    inputElement.send_keys(password)

    inputElement.submit()

    print('Please input you WoS search to parse:')
    search = input()

    inputElement = driver.find_element_by_xpath('//*[@id="value(input1)"]')
    inputElement.send_keys(search)
    inputElement.submit()

    print('Please input number of articles you want to scrape:')
    number = int(input())

    return number


def OneFileLoader(startPage, endPage):

    driver.find_element_by_xpath('//*[@id="exportTypeName"]').click()
    try:
        driver.find_element_by_xpath('//*[@id="saveToMenu"]/li[3]/a').click()
    except:
        pass

    driver.find_element_by_xpath('//*[@id="numberOfRecordsRange"]').click()

    driver.find_element_by_xpath('//*[@id="markFrom"]').clear()
    driver.find_element_by_xpath('//*[@id="markTo"]').clear()

    input1 = driver.find_element_by_xpath('//*[@id="markFrom"]')
    input2 = driver.find_element_by_xpath('//*[@id="markTo"]')

    input1.send_keys(str(startPage))
    input2.send_keys(str(endPage))

    driver.find_element_by_xpath('//*[@id="select2-saveOptions-container"]').click()
    driver.find_element_by_xpath("//li[contains(text(),'HTML')]").click()

    driver.find_element_by_xpath('//*[@id="select2-bib_fields-container"]').click()
    driver.find_element_by_xpath("//li[contains(text(),'Full Record and Cited References')]").click()

    driver.find_element_by_xpath('//*[@id="exportButton"]').click()
    return -1


def WoSArticlesLoader(driver, articlesNumber):

    if articlesNumber > 99000:
        return ('articlesNumber should not be more than 99000. Please restart with lover ammount.')

    loadsNumber = articlesNumber // 500
    residualNumber = articlesNumber % 500

    for load in tqdm(range(loadsNumber)):
        try:
            driver.refresh()
            OneFileLoader(1+load*500, (1 + load)*500)
            sleep(10)
        except:
            print('Some issue appeared and articles from {0} to {1} not downloaded'.format(load*500, (load+1)*500))

    try:
        driver.refresh()
        OneFileLoader(loadsNumber*500, loadsNumber*500 + residualNumber)
    except:
        print('Some issue appeared and articles from {0} to {1} not downloaded'.format(load * 500, (load + 1) * 500))

    return print('Success (files are in your downloads folder)')


if __name__ == '__main__':
    articlesNumber = OpenWoSandSearch(driver)
    print('Waht time need to sleep after download untill another? Please, specify in seconds:')
    t = int(input())
    while True:
        WoSArticlesLoader(driver, articlesNumber)
        sleep(t)
