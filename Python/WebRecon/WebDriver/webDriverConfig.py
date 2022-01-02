import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # pip install webdriver-manager


def webdriverCfg():
    try:
        chromeOp = Options()
        chromeOp.add_argument("--headless")
        chromeOp.add_argument("--mute-audio")
        chromeOp.add_argument("--no-sandbox")
        chromeOp.add_argument("--log-level=3")
        chromeOp.add_argument("--disable-gpu")
        chromeOp.add_argument("disable-extensions")
        chromeOp.add_experimental_option("useAutomationExtension", False)
        chromeOp.add_argument("disable-blink-features=AutomationControlled")
        chromeOp.add_experimental_option("excludeSwitches", ["enable-automation"])
        chromeOp.add_experimental_option('excludeSwitches', ['enable-logging'])
        os.environ["WDM_LOG_LEVEL"] = "0"
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s, options=chromeOp)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        driver.maximize_window()
        return driver
    except Exception as ex:
        raise ex
