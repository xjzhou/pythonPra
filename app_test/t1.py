# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import time

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "OD103"
caps["appPackage"] = "com.tencent.mm"
caps["appActivity"] = ".ui.LauncherUI"
caps["platformVersion"] = "7.1"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

el2 = driver.find_element_by_id("com.tencent.mm:id/d2z")
el2.click()
el3 = driver.find_element_by_id("com.tencent.mm:id/ht")
el3.send_keys("18538749356")
time.sleep(2)
el4 = driver.find_element_by_id("com.tencent.mm:id/ak_")
el4.click()
time.sleep(2)
el5 = driver.find_elements_by_class_name("android.widget.EditText")[1]
el5.send_keys("123")
el6 = driver.find_element_by_id("com.tencent.mm:id/ak_")
el6.click()
time.sleep(5)
driver.press_keycode('4')
time.sleep(30)
el8 = driver.find_element_by_xpath("//android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[contains(@index,2)]")
el8.click()
time.sleep(2)
el9 = driver.find_element_by_xpath("//android.widget.ListView/android.widget.LinearLayout")
el9.click()
time.sleep(2)
# 打印屏幕高和宽
print(driver.get_window_size())
#获取屏幕的高
x = driver.get_window_size()['width']
# 获取屏幕宽
y = driver.get_window_size()['height']
for i in range(10):
    try:
        time.sleep(5)
        data = driver.find_elements_by_xpath("//android.widget.ListView/android.widget.FrameLayout")[1:]
        try:
            for i in data:
                name = i.find_element_by_xpath("//android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView").get_attribute("text")
                words = i.find_element_by_xpath("//android.widget.LinearLayout/android.widget.LinearLayout").get_attribute("text")
                image = ""
                try:
                    image = i.find_element_by_xpath("//android.widget.LinearLayout/android.widget.LinearLayout[contains(@index,2)]/android.widget.FrameLayout/android.view.View").screenshot('/Screenshots/foo.png')
                except Exception as e:
                    print(e)
                print(name , words , image)
        except:
            pass
        # 向上滑
        driver.swipe(1 / 2 * x, 8 / 10 * y, 1 / 2 * x, 2 / 10 * y, 2000)
        time.sleep(5)
    except:
        pass
# driver.quit()


