from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

class Test_Sauce:
    def __init__(self) :
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
    
    def test_invalid_login(self):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name"))) #  WebDriverWait(driver,5) 5 saniye boyunca bekler.
        usernameInput =self.driver.find_element(By.ID, "user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password"))) 
        passwordInput = self.driver.find_element(By.ID,"password")
    
        usernameInput.send_keys("1")
        passwordInput.send_keys("1")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"TEST SONUCU: {testResult}")

    def test_valid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name"))) #  WebDriverWait(driver,5) 5 saniye boyunca bekler.
        usernameInput = self.driver.find_element(By.ID, "user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password"))) 
        passwordInput = self.driver.find_element(By.ID,"password")
        
    
        # Action Chains => Birden fazla işlemi tek seferde yapmak için kullanılır.
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,"standard_user") # usernameInput'a standard_user yazdırır.
        actions.send_keys_to_element(passwordInput, "secret_sauce") # passwordInput'a secret_sauce yazdırır.
        actions.perform() # perform() => Birden fazla işlemi tek seferde yapar.
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(2)
        self.execute_script("window.scroolTo(0,600)") # execute_script => Javascript kodlarını çalıştırmak için kullanılır. 
        sleep(2)
        



testClass = Test_Sauce()
testClass.test_invalid_login()
testClass.test_valid_login()