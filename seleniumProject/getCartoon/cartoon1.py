#!/bin/usr/env python
#-*- coding:utf-8 -*-
from selenium import  webdriver
from myLog import MyLog as mylog
import os
import time

class GetCartoon(object):
    def __init__(self):
        self.startUrl = 'http://www.1kkk.com/ch31-499363/'
        self.log = mylog()
        self.browser = self.getBrowser()
        
        self.saveCartoon(self.browser)
        
    def getBrowser(self):
        browser = webdriver.PhantomJS()
        try:
            browser.get(self.startUrl)
        except:
            self.log.error('open %s failed' %self.startUrl)
        browser.implicitly_wait(20)
        return browser
    
    def saveCartoon(self,browser):
        cartoonTitle = 'CartoonPic'#browser.title.split('_')[0]
        self.createDir(cartoonTitle)
        os.chdir(cartoonTitle)
        sumPage = int(self.browser.find_element_by_xpath('//font[@class="zf40"]/span[2]').text)
        i = 1
        while i<sumPage:
            imgName = str(i) + '.png'
            browser.get_screenshot_as_file(imgName)
            self.log.info('save img %s' %imgName)
            i += 1
            NextTag = browser.find_element_by_id('next')
            NextTag.click()
            time.sleep(5)
        self.log.info('save img success')
        exit()
        
        
        
    def createDir(self,dirName):
        if os.path.exists(dirName):
            self.log.info('create dir %s failed,have a same name file or dir' %dirName)
        else:
            try:
                os.makedirs(dirName)
            except:
                self.log.error('create dir %s failed' %dirName)
            else:
                self.log.info('create dir %s success' %dirName)
                
if __name__ == '__main__':
    aa = GetCartoon()