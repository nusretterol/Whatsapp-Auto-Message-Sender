import time , sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def new_chat(name):
    new_chat = driver.find_element_by_xpath('//div[@class="gQzdc"]')
    new_chat.click()

    new_user = driver.find_element_by_xpath('//div[@class="_2S1VP copyable-text selectable-text"]')
    new_user.send_keys(name)
    time.sleep(2)

    try:
            user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
            user.click()
    except NoSuchElementException:
        print('Girilen isim "{}" listede bulunamadı.'.format(name)) #the name is not find in list
    except Exception as e:
        driver.close()
        print(e)
        sys.exit()

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

user_name_list = ['Deneme','Deneme2'] #people to whom messages will be sent
#name = input('Gönderilecek Kişinin Adını Girin : ')
msg = input('Mesajı Girin : ') #Your message
count = int(input('Kaç Defa Gönderilecek : ')) #how many times it will be sent

input('Enter anything after scanning QR code')


for name in user_name_list:

    try:
        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        user.click()

    except NoSuchElementException as se:
        new_chat(name)

    msg_box = driver.find_element_by_class_name('_1Plpp')

    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_35EW6')
        button.click()