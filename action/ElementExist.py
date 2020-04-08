from selenium import webdriver

class ElementExist(object):
    @classmethod
    def isElementExist(cls,driver,elements):
        """
        :param driver:  浏览器驱动
        :param elements: 元素xpath定位方法
        :return:  type bool ，True or False
        """
        try:
            driver.find_element_by_xpath(elements)
            #print("True")
            return True
        except:
            #print("False")
            return False

    @classmethod
    def isexistAlter(cls,driver):
        """
        :param driver:  浏览器驱动
        :param alter: 弹窗
        :return:  type bool ，True or False
        """
        try:
            alter=driver.switch_to.alert
            alter.text
            return True
        except:
            #print("False")
            return False


if __name__=="__main__":
    driver = webdriver.Chrome(executable_path="C:\\Python37\chromedriver.exe")  # google驱动地址
    driver.get("https://www.baidu.com")
    ElementExist.isElementExist(driver, '//input[@id="su"]')
    # driver.get("https://zqhd.chainew.com/flowq/front/pay/homeIndex")
    # ElementExist.isElementExist(driver,'//div/span[text()="热销产品"]')
    #ElementExist.isexistAlter(driver)