#运城学院
#张旭鹏
#时间:2022/3/14 7:04
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.get('https://cet-bm.neea.edu.cn/')
# options = Options()
# 隐藏 正在受到自动软件的控制 这几个字
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# options.add_experimental_option("debuggerAddress", "localhost:9222")
# driver=webdriver.Chrome(executable_path=r"D:\chromedriver_win32 (1)\chromedriver.exe", options=options)
# driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#     "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
# })
