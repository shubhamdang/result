from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
import os


def getResult(regstart,regstop,rollstart,rollstop):
	cwd = os.getcwd()
	driver = webdriver.Firefox(executable_path=cwd+'/geckodriver')
	driver.get("http://result.mdurtk.in/postexam/result.aspx")
	correct =  True	
	for x in xrange(regstart,regstop+1):
		for y in xrange(rollstart,rollstop+1):

			reg =  driver.find_element_by_id("txtRegistrationNo")
			reg.clear()
			reg.send_keys(x)

			print str(x) + " " + str(y)
			rollno = driver.find_element_by_id("txtRollNo")
			rollno.clear()
			rollno.send_keys(y)


			proceed = driver.find_element_by_id("cmdbtnProceed")
			proceed.click()


			try:
			    WebDriverWait(driver, 3).until(EC.alert_is_present(),
			                                   'Timed out waiting for PA creation ' +
			                                   'confirmation popup to appear.')

			    alert = driver.switch_to.alert
			    alert.accept()
			    correct = False

			except TimeoutException:
				print "result added.."
				
			if correct ==  False:
			 	correct = True
			 	continue

			time.sleep(1)
			confirm = driver.find_element_by_id("imgComfirm")
			confirm.click()

			time.sleep(1)
			view = driver.find_element_by_xpath('.//*[@class="floatL"]/div/div/div/div/div/table/tbody/tr[2]/td[6]/a')
			view.click()
			time.sleep(2)
			page = driver.find_element_by_xpath('.//*[@id="divResult"]//div	')

			b = page.get_attribute('innerHTML').encode('utf-8')
			name_begin = b.find("lblStudentName")
			name_end = b.find("</span>",name_begin+3)
			a = "<!DOCTYPE html>\
			<html>\
			<head>\
				<title></title>\
			</head>\
			<body>"+ b+"</body>\
			</html>"

			with open(b[2991:name_end]+'.html','w') as fout:
				fout.write(a)

			back = driver.find_element_by_xpath('.//*[@id="btnBack"]')
			back.click()
			time.sleep(1)




if __name__ == '__main__':
	startreg = input('Enter the starting registration number:')
	endreg = input('Enter the starting registration number:')
	startroll = input('Enter the starting registration number:')
	endroll = input('Enter the starting registration number:')
	getResult(startreg,endreg,startroll,endroll)
