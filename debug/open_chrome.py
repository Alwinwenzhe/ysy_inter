

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import selenium


if __name__ == '__main__':

	PROXY = ""
	chrome_options = webdriver.ChromeOptions()
	prefs = {
		"profile.default_content_setting_values":
			{
				"notifications": 2
			},
		"profile.managed_default_content_settings.images": 2
	}
	#chrome_options.add_argument('--proxy-server={0}'.format(PROXY))  # 设置代理
	chrome_options.add_experimental_option("prefs", prefs)  # 设置浏览器不出现通知
	driver = webdriver.Chrome(chrome_options=chrome_options)
	driver.get('http://www.baidu.com')
	time.sleep(20)
	driver.quit()



