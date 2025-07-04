from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, TimeoutException
import time
import json
import os
from fake_useragent import UserAgent

# إعدادات متقدمة للمتصفح
CHROME_OPTIONS = [
    "--headless",  # تشغيل المتصفح في الخلفية
    "--disable-gpu",
    "--no-sandbox",
    "--disable-dev-shm-usage",
    "--disable-extensions",
    "--disable-infobars",
    "--disable-notifications",
    "--ignore-certificate-errors",
    "--log-level=3",
    "--disable-blink-features=AutomationControlled"
]

# إعدادات الانتظار
WAIT_TIMEOUT = 15
LOAD_TIMEOUT = 60  # زيادة وقت الانتظار

class EnhancedWebScraper:
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.service = Service(driver_path)
        self.options = webdriver.ChromeOptions()
        for opt in CHROME_OPTIONS:
            self.options.add_argument(opt)
        
        # إعدادات وكيل المستخدم
        user_agent = UserAgent().random
        self.options.add_argument(f"user-agent={user_agent}")

    def init_driver(self):
        try:
            driver = webdriver.Chrome(service=self.service, options=self.options)
            driver.set_page_load_timeout(LOAD_TIMEOUT)
            return driver
        except WebDriverException as e:
            print(f"فشل تهيئة المتصفح: {e}")
            return None

    def wait_for_page_ready(self, driver):
        try:
            WebDriverWait(driver, WAIT_TIMEOUT).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            WebDriverWait(driver, WAIT_TIMEOUT).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
        except TimeoutException:
            print("تحذير: تم تجاوز وقت الانتظار لتحميل الصفحة")

    def dynamic_scroll(self, driver):
        try:
            last_height = driver.execute_script("return document.body.scrollHeight")
            while True:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
        except Exception as e:
            print(f"خطأ أثناء التمرير: {e}")

    def extract_data_safely(self, driver, selector_type, selector, attribute=None):
        try:
            elements = driver.find_elements(selector_type, selector)
            return [elem.get_attribute(attribute).strip() if attribute else elem.text.strip() 
                    for elem in elements if elem.is_displayed()]
        except Exception as e:
            print(f"خطأ في استخراج البيانات: {e}")
            return []

    def extract_advanced_data(self, driver):
        data = {
            "titles": self.extract_data_safely(driver, By.TAG_NAME, "h1") +
                     self.extract_data_safely(driver, By.TAG_NAME, "h2") +
                     self.extract_data_safely(driver, By.TAG_NAME, "h3"),
            "links": self.extract_data_safely(driver, By.TAG_NAME, "a", "href"),
            "images": self.extract_data_safely(driver, By.TAG_NAME, "img", "src"),
            "meta": self.extract_metadata(driver),
            "articles": self.extract_data_safely(driver, By.TAG_NAME, "article")
        }
        return {k: v for k, v in data.items() if v}

    def extract_metadata(self, driver):
        try:
            return {
                "title": driver.title,
                "description": driver.find_element(By.XPATH, "//meta[@name='description']").get_attribute("content") if driver.find_elements(By.XPATH, "//meta[@name='description']") else None,
                "keywords": driver.find_element(By.XPATH, "//meta[@name='keywords']").get_attribute("content") if driver.find_elements(By.XPATH, "//meta[@name='keywords']") else None
            }
        except Exception as e:
            print(f"خطأ في استخراج الميتادات: {e}")
            return {}

    def get_content(self, url):
        driver = self.init_driver()
        if not driver:
            return None, None
            
        try:
            driver.get(url)
            self.wait_for_page_ready(driver)
            self.dynamic_scroll(driver)
            return driver.page_source, self.extract_advanced_data(driver)
        except Exception as e:
            print(f"حدث خطأ: {e}")
            return None, None
        finally:
            driver.quit()

def validate_url(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    return url

def save_content(content, filename, ext="html"):
    try:
        os.makedirs("scraped_data", exist_ok=True)
        full_path = os.path.join("scraped_data", f"{filename}.{ext}")
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content if ext == "html" else json.dumps(content, ensure_ascii=False, indent=2))
        print(f"تم الحفظ في: {os.path.abspath(full_path)}")
    except Exception as e:
        print(f"خطأ في الحفظ: {e}")

if __name__ == "__main__":
    DRIVER_PATH = "E:/chromdriver/chromedriver-win64/chromedriver-win64/chromedriver.exe"
    
    scraper = EnhancedWebScraper(DRIVER_PATH)
    
    url_input = input("أدخل رابط الموقع: ").strip()
    validated_url = validate_url(url_input)
    
    html_content, extracted_data = scraper.get_content(validated_url)
    
    if html_content and extracted_data:
        print("\n[جزء من محتوى الصفحة]:")
        print(html_content[:500] + "\n..." if len(html_content) > 500 else html_content)
        
        base_name = validated_url.split("//")[-1].replace("/", "_").replace(".", "_")[:50]
        save_content(html_content, f"{base_name}_content", "html")
        save_content(extracted_data, f"{base_name}_data", "json")