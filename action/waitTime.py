import time
import traceback
from conf.config import *
from utils.log.excuteWriteLog import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

class waitTime(object):

    @classmethod
    def sureSleep(cls,second):
        if isinstance(second,(int,float)):
            time.sleep(int(second))
        else:
            print("sleep time must be int type !")

    @classmethod
    def visitbleOfElement(cls,locateMethod,locateValue):
        """
        :param locateMethod:    (str)   定位方法，如"xpath"，"id","name","classname"等
        :param locateValue:     (str)   定位值,如"xpath"，"id","name","classname"的值
        :return:                        元素
        """
        global driver
        try:
            if locateMethod.lower() in shortLocateMethods.keys() and isinstance(locateValue,str):
                locateValue=locateValue.strip("'")
                locateValue = locateValue.strip('"')
                locateValue = locateValue.replace("'",'"')
                print(locateValue)
                locateMethod=shortLocateMethods[locateMethod.lower()]
                element=WebDriverWait(driver, 10, 0.2).until(EC.visibility_of_element_located((eval(locateMethod),locateValue)))
                return  element
            else:
                print("bad parameters")
        except Exception as err:
            print(err)
            excutelog("error",traceback.format_exc())

    @classmethod
    def swithToFrame(cls,locateMethod,locateValue):
        """
        :param locateMethod:
        :param locateValue:
        :return:
        """
        global driver
        try:
            if locateMethod.lower() in shortLocateMethods.keys() and isinstance(locateValue,str):
                locateValue=locateValue.strip("'")
                locateValue = locateValue.strip('"')
                locateValue = locateValue.replace("'",'"')
                print(locateValue)
                locateMethod=shortLocateMethods[locateMethod.lower()]
                WebDriverWait(driver, 10, 0.2).until(EC.visibility_of_element_located((eval(locateMethod),locateValue)))
            else:
                print("bad parameters")
        except Exception as err:
            print(err)
            excutelog("error",traceback.format_exc())



if __name__=="__main__":
    driver = webdriver.Chrome(executable_path=chromeDriverPath)
    driver.get("https://zqhd.chainew.com/flowq/front/pay/homeIndex")
    waitTime.visitbleOfElement("id","phone")

