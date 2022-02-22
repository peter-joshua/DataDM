# -*- coding: utf-8 -*-
# @作 者: 张帆
# @文件名: DataDM.py
# @创建时间    : 2022/2/11 13:18
import re
import time
from functools import update_wrapper
class DataWM:
    def __init__(self,func):
        self.data_list = []
        self.hiden2="*"
        # 身份证匹配表达式
        self.IDCARD = "[1-9][0-9]{17}"
        # 敏感关键字匹配规则
        self.keyword_list=["张","科技"]
        # # 匹配11位电话号码
        # self.partten4 = "([0-9]{3}-)[0-9]{8}"
        # 匹配密码
        self.passwd = "(password=|passwd=)[0-9]+"
        self.filterdata = []
        self.partten7 = "[0-9]+"
        self._func = func
        self._func_name = func.__name__
        update_wrapper(self, self._func)
    def __partten_passwd(self,value):
        value = value.split("=")[0] + "=" + value.split("=")[1][0:1] + self.hiden2 * (len(value.split("=")[1]) - 2) + \
                value.split("=")[1][-1]
        return value
    def __partten_number(self,value):
        value = value.replace(value[3:-1], (len(value)-4)*self.hiden2)
        return value
    def __partten_keyword(self,value,keyword):
        value = value.replace(keyword,len(keyword) * self.hiden2)
        return value
    def hitIDCARD(self,value):
        value=str(value)
        value=self.__partten_number(value)
        return value
    def hitPasswd(self,value):
        '''
        只取首位与最后一位
        '''
        value=str(value)
        if re.match(self.passwd, value):
            value=self.__partten_passwd(value)
            return value
    def hitPhone(self,value):
        value=str(value)
        if len(value)==11:
            value = self.__partten_number(value)
            return value
    def hitKeyWord(self,value):
        value=str(value)
        for item in self.keyword_list:
            if re.findall(item,value):
                value=self.__partten_keyword(value,item)
        return value

    def __call__(self,val):
        if self.hitPhone(val):
            return self.hitPhone(val)
        if self.hitPasswd(val):
            return self.hitPasswd(val)
        if self.hitIDCARD(val):
            return self.hitIDCARD(val)
        if self.hitKeyWord(val):
            return self.hitKeyWord(val)
        
       
if __name__ == '__main__':
    @DataWM
    def test(val):
        return val
    result=test("15189880763")
    print(result)
