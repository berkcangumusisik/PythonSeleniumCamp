""" 
AMAÇ:

Derste gösterilen konuların pekiştirilmesi.

ÖDEV TANIMI:

Aşağıda verilen test caselerin hepsini "https://www.saucedemo.com/" sitesinde gerçekleştirmeniz istenmektedir.

Yazacağınız tüm kodları oluşturduğunuz bir classda fonksiyonlar oluşturarak gerçekleştiriniz. Bu classın fonksiyonlarını çağırarak test ediniz.

Test Caseler;

Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır. Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır. (Tek test casede işleyiniz)
Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Test_Sauce:
    def username(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window() # pencereyi tam ekran yapar
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        input  = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID,"password")
        loginBtn = driver.find_element(By.ID,"login-button")
        sleep(5)
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print("Kullanıcı adı ve şifre boş geçilmiştir.")
        print(f"TEST SONUCU: {testResult}")
        
    
    def password(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        input  = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID,"password")
        loginBtn = driver.find_element(By.ID,"login-button")
        sleep(5)
        input.send_keys("1")
        passwordInput.send_keys("")
        sleep(2)
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print("Şifre alanı boş geçilmiştir.")
        print(f"TEST SONUCU: {testResult}")
    
    def kilit(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        input  = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID,"password")
        loginBtn = driver.find_element(By.ID,"login-button")
        sleep(5)
        input.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print("Kulanıcı adı ve şifresi kilitli.")
        print(f"TEST SONUCU: {testResult}")
        
        
    def icon_kontrol(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        input  = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID,"password")
        loginBtn = driver.find_element(By.ID,"login-button")
        sleep(5)
        input.send_keys("")
        passwordInput.send_keys("")
        sleep(2)
        loginBtn.click()
        errorButton = driver.find_element(By.CLASS_NAME,"svg-inline--fa fa-times-circle fa-w-16 error_icon")
        errorButton.click()
        print("Hata mesajı kapatıldı.")
        
    def login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        input  = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID,"password")
        loginBtn = driver.find_element(By.ID,"login-button")
        sleep(5)
        input.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn.click()
        sleep(5)
        print("Giriş yapıldı.")

    
    def product_control(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        input  = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID,"password")
        loginBtn = driver.find_element(By.ID,"login-button")
        sleep(5)
        input.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn.click()
        sleep(5)
        product_num = driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(f"Ürün sayısı: {len(product_num)}")
        
        sleep(3)
testClass = Test_Sauce()
#testClass.username()
#testClass.password()
#testClass.kilit()
# testClass.icon_kontrol()
# testClass.login()
testClass.product_control()
while True:
    continue


