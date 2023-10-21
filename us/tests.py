from datetime import datetime
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Hosttest(TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.live_server_url = 'http://127.0.0.1:8000/'
    def tearDown(self):
        self.driver.quit()
        
    def test_01_login_page(self):
        driver = self.driver
        driver.get(self.live_server_url)
        driver.maximize_window()
        time.sleep(1)
        login = driver.find_element(By.CSS_SELECTOR, 'a[href="/login/"]')
        login.click()
        time.sleep(2)
        email = driver.find_element(By.CSS_SELECTOR, 'input[type="text"][name="email"]')
        email.send_keys("midhunkrishnan2024@mca.ajce.in")
        password = driver.find_element(By.CSS_SELECTOR, 'input[type="password"][name="password"]#id_password')
        password.send_keys("Romeo!0481")
        time.sleep(2)
        submit = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-outline-primary.text-light.p-2.w-50.mt-3')
        submit.click()
        time.sleep(2)
        post = driver.find_element(By.CSS_SELECTOR, 'textarea.form-control[name="feed"]')
        post.send_keys("Testing on progress")
        time.sleep(2)
        testbtn = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-warning")
        testbtn.click()
        time.sleep(2)
        profile = driver.find_element(By.CSS_SELECTOR, 'a[href="/edit-player-profile"]')
        profile.click()
        time.sleep(2)
        post = driver.find_element(By.CSS_SELECTOR, 'input.form-control[name="loc"]')
        post.send_keys("Meenadom")
        time.sleep(2)
        sub = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-success")
        sub.click()
        time.sleep(2)
        feeds = driver.find_element(By.CSS_SELECTOR, 'a[href="/following_feeds"]')
        feeds.click()
        time.sleep(2)
        like = driver.find_element(By.CSS_SELECTOR, 'button[data-feed-id="24"]')
        like.click()
        time.sleep(2)
        logout = driver.find_element(By.CSS_SELECTOR, 'a[href="/logout/"]')
        logout.click()
        time.sleep(2)


if __name__ == '__main__':
    import unittest
    unittest.main()