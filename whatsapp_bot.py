from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 

from argparse import ArgumentParser

#function to return the number of child nodos given a node path
def getNumOfChilds(path = '//*[@id="main"]/div[3]/div/div[2]/div[3]'):
    path = driver.find_element(By.XPATH,path)
    num_childs = path.find_elements(By.XPATH, './child::*')
    return len(num_childs)

try:
    parser = ArgumentParser(prog='whatsapp_bot.py') 
    #group or contact name (target)
    parser.add_argument('-t', nargs='?', action='store', type = str, required=True, help='TARGET (User or group) name')	
    #message that will be sent
    parser.add_argument('-m', nargs='?', action='store', type = str, required=True, help='MESSAGE that will be sent')
    #number of messages that will be sent
    parser.add_argument('-n', nargs='?', action='store', type = int, default = 1, help='NUMBER of messages to send')	

    #process parameters
    args = parser.parse_args()   

    #Firefox driver
    driver =webdriver.Firefox()
    #Whatsapp Web URL
    driver.get("https://web.whatsapp.com/")
    print('\033[93mConecting to WhatsApp Web...\033[00m')

    #Find "Keep my signed in" checkbox and set it to non-selected
    driver.find_element(By.XPATH, '//*[@class="landing-main"]/div/div[3]/label/input').click()
    print('\033[1;32mUnselect \"Keep my signed in\" checkbox\033[00m')

    #set 5 minutes maximun of waiting
    wait = WebDriverWait(driver,timeout = 300) 

    #Contact or group name 
    target ='"Pruebas"'
    #message that will be sent to target
    string = args.m
    #number of messages that will be sent to target
    num_msg = int(args.n)
    print('\033[1;32mMessage, count and target defined\033[00m')

    #find contact item on list of conversations
    x_arg='//span[contains(@title,'+ target +')]' 
    conv_title = wait.until(EC.presence_of_element_located((By.XPATH,x_arg))) 
    #select conversation
    conv_title.click()
    print('\033[1;32mTarget conversation selected\033[00m')

    #get number of messages loaded after sending any
    init = getNumOfChilds()

    #get message input box
    msg_input = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    print('\033[1;32mGet message input box\033[00m')

    print('\033[93mSending message (or messages)...\033[00m')
    # send N times message
    for i in range(num_msg):
        msg_input.send_keys(string) #write message
        send_button=driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button') #send button
        send_button.click() #click send button
    print('\033[1;32mMessage (or messages) sent\033[00m')


    #last message sent's path 
    msg_path = '//*[@id="main"]/div[3]/div/div[2]/div[3]/div['+ str(init+num_msg)+']'
    print('\033[93mWaiting for message (or messages) to appear...\033[00m')
    #wait until last message appears on screen
    wait.until(EC.element_to_be_clickable((By.XPATH,msg_path)))
    print('\033[1;32mMessage (or messages) written\033[00m')

    #get last message sent's icon (clock, check or double check)
    icon_path = msg_path + '/div/div/div/div[2]/div/div/span'
    print('\033[93mWaiting for message (or messages) to be sent, delivered or viewed ...\033[00m')
    # wait until this icon is not a clock
    wait.until(EC.presence_of_element_located((By.XPATH, icon_path + '[@data-icon="msg-check" or  @data-icon="msg-dblcheck"]')))
    print('\033[1;32mMessage (or messages) sent, delivered or viewed\033[00m')

    #deploy menu icon's path
    menu_path = '//*[@id="side"]/header/div[2]/div/span/div[3]'
    #click on menu's icon
    driver.find_element(By.XPATH, menu_path + '/div').click()
    print('\033[93mDeploying menu...\033[00m')

    #wait until menu is showed
    wait.until(EC.presence_of_element_located((By.XPATH, menu_path + '/span/div[1]')))
    #select "Log out" option
    driver.find_element(By.XPATH, menu_path + '/span/div[1]/ul/li[5]/div[1]').click()
    print('\033[93mLogging out...\033[00m')

    #close driver and browser
    driver.close()
    print('\033[1;32mBrowser and session closed. Bye!\033[00m')

except Exception as e:
    print('\033[91mAn error ocurred :/\033[00m')




