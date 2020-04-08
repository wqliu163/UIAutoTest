from utils.handleExcel import *
from conf.config import *
from action.operateBrowser import *

def runningCase():
    for index, cell in enumerate(handleExcel.getColumnsObject(getRootPath() + "\\data\\case.xlsx", "CASES", columnNo=caseIsexecuted)[1:], 2):
        #print(index)
        if cell.value=="y" or cell.value=="Y":
            caseSheetName=handleExcel.getValueOfCell(getRootPath() + "\\data\\case.xlsx", "CASES",rowNo=index,columnNo=caseStepSheetName)
            #print(caseSheetName)
            columnMax=handleExcel.getMaxRowNO(getRootPath()+"\\data\\case.xlsx",caseSheetName)
            #print("columnMax=",columnMax)
            caseStatus =0
            for i in range(2,columnMax+1):
                print("i=",i)
                parameterList=[]
                methodValue=handleExcel.getValueOfCell(getRootPath()+"\\data\\case.xlsx",caseSheetName,rowNo=i,columnNo=action)
                locateMethodValueNew=handleExcel.getValueOfCell(getRootPath()+"\\data\\case.xlsx",caseSheetName,rowNo=i,columnNo=locateMethod)
                locateValueNew=handleExcel.getValueOfCell(getRootPath()+"\\data\\case.xlsx",caseSheetName,rowNo=i,columnNo=locateValue)
                actionValueNew=handleExcel.getValueOfCell(getRootPath()+"\\data\\case.xlsx",caseSheetName,rowNo=i,columnNo=actionValue)
                print(methodValue,locateMethodValueNew,locateValueNew,actionValueNew)
                if methodValue and isinstance(methodValue,str):
                    methodValue=methodValue.strip()
                if locateMethodValueNew and isinstance(locateMethodValueNew,str):
                    locateMethodValueNew = locateMethodValueNew.strip()
                    locateMethodValueNew = locateMethodValueNew.strip("'")
                    locateMethodValueNew = locateMethodValueNew.strip('"')
                    print(locateMethodValueNew)
                    if "'" not in locateMethodValueNew:
                        locateMethodValueNew = "'" + locateMethodValueNew + "'"
                    else:
                        locateMethodValueNew = '"' + locateMethodValueNew + '"'
                if locateValueNew and isinstance(locateValueNew,str):
                    locateValueNew=locateValueNew.strip()
                    locateValueNew = locateValueNew.strip("'")
                    locateValueNew = locateValueNew.strip('"')
                    if "'" not in locateValueNew:
                        locateValueNew="'"+locateValueNew+"'"
                    else:
                        locateValueNew='"'+locateValueNew+'"'
                if actionValueNew and isinstance(actionValueNew,str):
                    actionValueNew=actionValueNew.strip()
                if methodValue!=None:
                    if locateMethodValueNew!=None and locateValueNew!=None and actionValueNew!=None:
                        parameterList.append(locateMethodValueNew)
                        parameterList.append(locateValueNew)
                        if isinstance(actionValueNew,int):
                            parameterList.append(str(actionValueNew))
                        else:
                            parameterList.append("'"+actionValueNew+"'")
                        parameter=",".join(parameterList)
                        value="operateBrowser."+methodValue+"("+parameter+")"
                        print(value)
                        try:
                            eval(value)
                            handleExcel.writeValueInCell(getRootPath()+"\\data\\case.xlsx",caseSheetName,"pass",rowNo=i,columnNo=executedResult)
                            handleExcel.writeValueInCell(getRootPath() + "\\data\\case.xlsx", caseSheetName,getDate.getDate()+" "+getDate.getTime(),rowNo=i, columnNo=executedTime)
                        except:
                            caseStatus =1
                            handleExcel.writeValueInCell(getRootPath() + "\\data\\case.xlsx", caseSheetName, "fail",rowNo=i, columnNo=executedResult,colour="red")
                            handleExcel.writeValueInCell(getRootPath() + "\\data\\case.xlsx", caseSheetName,getDate.getDate() + " " + getDate.getTime(), rowNo=i,columnNo=executedTime,colour="red")
                    elif locateMethodValueNew!=None and locateValueNew!=None and actionValueNew==None:
                        value ="operateBrowser." + methodValue + "(" + locateMethodValueNew +","+ locateValueNew + ")"
                        print(value)
                        try:
                            eval(value)
                            handleExcel.writeValueInCell(getRootPath()+"\\data\\case.xlsx",caseSheetName,"pass",rowNo=i,columnNo=executedResult)
                            handleExcel.writeValueInCell(getRootPath() + "\\data\\case.xlsx", caseSheetName,getDate.getDate()+" "+getDate.getTime(),rowNo=i, columnNo=executedTime)
                        except:
                            caseStatus = 1
                            handleExcel.writeValueInCell(getRootPath() + "\\data\\case.xlsx", caseSheetName, "fail",rowNo=i, columnNo=executedResult,colour="red")
                            handleExcel.writeValueInCell(getRootPath() + "\\data\\case.xlsx", caseSheetName,getDate.getDate() + " " + getDate.getTime(), rowNo=i,columnNo=executedTime,colour="red")
                    elif locateMethodValueNew==None and locateValueNew==None and actionValueNew==None:
                        value ="operateBrowser." + methodValue + "("+")"
                        print(value)
                        try:
                            result=eval(value)
                            handleExcel.writeValueInCell(getRootPath()+"\\data\\case.xlsx",caseSheetName,"pass",rowNo=i,columnNo=executedResult)
                            handleExcel.writeValueInCell(getRootPath() + "\\data\\case.xlsx", caseSheetName,getDate.getDate()+" "+getDate.getTime(),rowNo=i, columnNo=executedTime)
                            if methodValue=="screntCapture":
                                handleExcel.writeValueInCell(getRootPath() + "\\data\\case.xlsx", caseSheetName, result,rowNo=i, columnNo=capturePath)
                        except:
                            caseStatus = 1
                            handleExcel.writeValueInCell(getRootPath() + "\\data\\case.xlsx", caseSheetName, "fail",rowNo=i, columnNo=executedResult,colour="red")
                            handleExcel.writeValueInCell(getRootPath() + "\\data\\case.xlsx", caseSheetName,getDate.getDate() + " " + getDate.getTime(), rowNo=i,columnNo=executedTime,colour="red")
                    elif locateMethodValueNew==None and locateValueNew==None and actionValueNew!=None:
                        if isinstance(actionValueNew,int):
                            actionValueNew=str(actionValueNew)
                        else:
                            actionValueNew=actionValueNew.strip("'")
                            actionValueNew = actionValueNew.strip('"')
                            actionValueNew="'"+actionValueNew+"'"
                        value="operateBrowser." + methodValue + "(" + actionValueNew +")"
                        print(value)
                        try:
                            eval(value)
                            handleExcel.writeValueInCell(getRootPath()+"\\data\\case.xlsx",caseSheetName,"pass",rowNo=i,columnNo=executedResult)
                            handleExcel.writeValueInCell(getRootPath() + "\\data\\case.xlsx", caseSheetName,getDate.getDate()+" "+getDate.getTime(),rowNo=i, columnNo=executedTime)
                        except:
                            caseStatus = 1
                            handleExcel.writeValueInCell(getRootPath() + "\\data\\case.xlsx", caseSheetName, "fail",rowNo=i, columnNo=executedResult,colour="red")
                            handleExcel.writeValueInCell(getRootPath() + "\\data\\case.xlsx", caseSheetName,getDate.getDate() + " " + getDate.getTime(), rowNo=i,columnNo=executedTime,colour="red")
            if caseStatus==0:
                handleExcel.writeValueInCell(getRootPath() + "\\data\\case.xlsx", "CASES", "pass", rowNo=index,columnNo=caseExecutedResult)
                handleExcel.writeValueInCell(getRootPath() + "\\data\\case.xlsx", "CASES",getDate.getDate() + " " + getDate.getTime(), rowNo=index,columnNo=caseExecutedTime)
            else:
                handleExcel.writeValueInCell(getRootPath() + "\\data\\case.xlsx", "CASES", "fail", rowNo=index,columnNo=caseExecutedResult,colour="red")
                handleExcel.writeValueInCell(getRootPath() + "\\data\\case.xlsx", "CASES",getDate.getDate() + " " + getDate.getTime(), rowNo=index,columnNo=caseExecutedTime)


if __name__=="__main__":
    runningCase()