import time
from action.ElementExist import *
import traceback
from selenium import webdriver
from utils.log.excuteWriteLog import *
from conf.config import *
from utils.getDate import *
from utils.getRootPath import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class operateBrowser(object):
    @classmethod
    def openBrowser(cls,browserName):
        """
        :param browserName:     浏览器名字
        :return:
        """
        global driver
        if browserName.lower()=="google" or browserName.lower()=="chrome":
            driver=webdriver.Chrome(executable_path=chromeDriverPath)
        elif browserName.lower()=="ie":
            driver = webdriver.Ie(executable_path=ieDriverPath)
        elif browserName.lower()=="firefox":
            driver = webdriver.Firefox(executable_path=firefoxDriverPath)
        else:
            excutelog("info","not support the browserdriver open browser! please input parameter in method  'ie or chrome or firefox'")
            print("not support the browserdriver open browser! please input parameter in method  'ie or chrome or firefox'")
        return driver

    @classmethod
    def hideBrowse(cls,browserName):
        global driver
        try:
            if browserName.lower() == "google" or browserName.lower() == "chrome":
                option = webdriver.ChromeOptions()
                option.add_argument("--headless")
                driver = webdriver.Chrome(chrome_options=option)
            elif browserName.lower() == "ie":
                print("IE browser current not support headless mode")
            elif browserName.lower() == "firefox":
                option = webdriver.FirefoxOptions()
                option.add_argument("--headless")
                driver = webdriver.Firefox(firefox_options=option)
            else:
                excutelog("info","not support the browserdriver open browser! please input parameter in method  'ie or chrome or firefox'")
                print("not support the browserdriver open browser! please input parameter in method  'ie or chrome or firefox'")
        except:
            excutelog("error", traceback.format_exc())
            print("please copy %s webdriver input %s install root path"%(browserName,browserName))
            print(traceback.format_exc())

    @classmethod
    def visitUrl(cls,url):
        global driver
        try:
            driver.get(url)
        except:
            excutelog("error",traceback.format_exc())
            print(traceback.format_exc())

    @classmethod
    def findElement(cls,locateMethod,locateValue):
        """
        :param locateMethod:    (str)   定位方法，如"id","name","xpath" 等
        :param locateValue:     (str)   定位值,如"xpath"，"id","name","classname"的值
        :return:
        """
        global driver
        if isinstance(locateMethod,str) and isinstance(locateValue,str):
            if isinstance(locateMethod,str) and locateMethod.lower() in locateMethods.keys():
                locateValue=locateValue.strip("'")
                locateValue = locateValue.strip('"')
                locateValue=locateValue.replace("'", '"')
                locateValue="'"+locateValue+"'"
                try:
                    element=eval("driver." + locateMethods[locateMethod] % locateValue)
                    return element
                except:
                    print("element %s can't found"%locateValue)

    @classmethod
    def visitbleOfElement(cls, locateMethod, locateValue):
        """
        :param locateMethod:    (str)   定位方法，如"xpath"，"id","name","classname"等
        :param locateValue:     (str)   定位值,如"xpath"，"id","name","classname"的值
        :return:                        元素
        """
        global driver
        try:
            if locateMethod.lower() in shortLocateMethods.keys() and isinstance(locateValue, str):
                locateValue = locateValue.strip("'")
                locateValue = locateValue.strip('"')
                locateValue = locateValue.replace("'", '"')
                print(locateValue)
                locateMethod = shortLocateMethods[locateMethod.lower()]
                element = WebDriverWait(driver, 10, 0.2).until(
                    EC.visibility_of_element_located((eval(locateMethod), locateValue)))
                return element
            else:
                print("bad parameters")
        except Exception as err:
            print(err)
            excutelog("error", traceback.format_exc())

    @classmethod
    def clear(cls,locateMethod,locateValue):
        """
        :param locateMethod:    (str)   定位方法，如"id","name","xpath" 等
        :param locateValue:     (str)   定位值,如"xpath"，"id","name","classname"的值
        :return:
        """
        global driver
        try:
            operateBrowser.findElement(locateMethod,locateValue).clear()
            excutelog("info","succssful clearance,清空成功")
        except:
            print("element %s not located "%locateValue)

    @classmethod
    def input(cls,locateMethod,locateValue,content):
        """
        :param locateMethod:     (str)   定位方法，如"id","name","xpath" 等
        :param locateValue:      (str)   定位值,如"xpath"，"id","name","classname"的值
        :param content:                  输入内容
        :return:
        """
        global driver
        try:
            operateBrowser.findElement(locateMethod, locateValue).send_keys(content)
            excutelog("info","输入成功")
        except:
            print("element %s not located "%locateValue)

    @classmethod
    def click(cls,locateMethod,locateValue):
        """
        :param locateMethod:     (str)   定位方法，如"id","name","xpath" 等
        :param locateValue:      (str)   定位值,如"xpath"，"id","name","classname"的值,"//div/a[text()='个人中心']"
        :return:
        """
        global driver
        try:
            element=operateBrowser.findElement(locateMethod, locateValue)
            element.click()
        except:
            print("can't click to %s"%locateValue)

    @classmethod
    def switchWindow(cls):
        global driver
        #n = driver.window_handles  # 获取当前页面所有的句柄
        driver.switch_to.window(driver.window_handles[0])

    @classmethod
    def rollWindow(cls,element=None,position="底端"):
        """
        :param elements:        元素
        :param position:        （str）   平齐的位置元素，如"底端"，"顶端"
        :return:
        """
        global driver
        if element!=None:
            print(element)
            if position=="底端":
                driver.execute_script("arguments[0].scrollIntoView(false);", element)
            elif position=="顶端":
                driver.execute_script("arguments[0].scrollIntoView(true);", element)
        else:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    @classmethod
    def asserresult(cls,expected,result):
        global driver
        pass

    @classmethod
    def closeBrowser(cls):
        global driver
        driver.close()
        driver.quit()

    @classmethod
    def screntCapture(cls):
        """截取当前窗口"""
        global driver
        capturePath=getRootPath()+"\\screenCapture\\%s"%getDate.getDate()
        captureName="%s.png"%getDate.getTime().replace(":", "")
        print(capturePath)
        if os.path.exists(capturePath) and os.path.isdir(capturePath):
            driver.get_screenshot_as_file(capturePath+"\\%s.png"%getDate.getTime().replace(":",""))
            return (capturePath + "\\" + captureName)
        else:
            os.mkdir(capturePath)
            driver.get_screenshot_as_file(capturePath + "\\%s.png" % getDate.getTime().replace(":", ""))
            return (capturePath+"\\"+captureName)


if __name__=="__main__":
    operateBrowser.openBrowser('google')
    # driver.get("https://zqhd.chainew.com/flowq/front/pay/homeIndex")
    # # operateBrowser.hideBrowse("google")
    # # driver.get("https://www.baidu.com")
    # #operateBrowser.input("id","phone","13143683776")
    # # time.sleep(1)
    # #operateBrowser.clear("id","phone")
    # ele=operateBrowser.findElement("xpath","//div/span[text()='热销产品']")
    # #operateBrowser.click("xpath","//div/a[text()='个人中心']")
    # operateBrowser.screntCapture()
    #operateBrowser.rollWindow(element=ele,position="顶端")