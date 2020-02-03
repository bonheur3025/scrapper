from selenium import webdriver
import time
 
driver = webdriver.Chrome('/Users/smkwon/Downloads/chromedriver')

# 암묵적으로 웹 자원 로드를 위해 3초까지 기다리기
# driver.implicitly_wait(3)
driver.get('http://www.iros.go.kr/PMainJ.jsp')
 
# driver.maximize_window()
 
# driver.find_element_by_class_name('lg_local_btn').click()
driver.find_element_by_id('id_user_id').send_keys('dovmf30')
driver.find_element_by_id('password').send_keys('Sull!0@0')
driver.find_element_by_xpath("//a[contains(@onclick, 'javascript:f_gosubmit();return false;')]").click()
# driver.find_element_by_class_name('btn_global').click()
 
# time.sleep(3)
# driver.close()