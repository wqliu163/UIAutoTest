#浏览器驱动地址
chromeDriverPath="C:\\Python37\\chromedriver.exe"
ieDriverPath="C:\\Python37\\IEDriverServer.exe"
firefoxDriverPath="C:\\Python37\\geckodriver.exe"
locateMethods={"id":"find_element_by_id(%s)","name":"find_element_by_name(%s)","xpath":"find_element_by_xpath(%s)",
              "classname":"find_element_by_class_name(%s)","tagname":"find_element_by_tag_name(%s)","linktext":"find_element_by_link_text(%s)"}

shortLocateMethods={"id":"By.ID","name":"By.NAME","xpath":"By.XPATH","classname":"By.CLASS_NAME","tagname":"By.TAG_NAME","linktext":"By.LINK_TEXT"}


#映射关系
test_case_sheet = "CASES"
caseStepSheetName = 3       #用例操作表sheet
caseIsexecuted = 4          #用例是否执行
caseExecutedTime = 5        #用例执行时间
caseExecutedResult = 6      #用例执行结果


action = 2          #执行动作，即调用函数
locateMethod = 3    #定位方式
locateValue = 4     #定位表达式的值
actionValue = 5     #操作值，及函数输入的参数
executedTime = 6    #执行时间
executedResult = 7  #执行结果
exceptionInfo = 8   #异常信息
capturePath = 9     #截图保存位置