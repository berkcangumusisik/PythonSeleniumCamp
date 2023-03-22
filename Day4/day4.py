from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By # By sınıfını kullanmak için import ediyoruz.
""" 
Selenium ile web sayfalarını kontrol edebiliriz.
Farklı diller ile de kullanılabilir.
pip install selenium ile selenium kütüphanesini indirebiliriz.
pip install webdriver-manager ile tarayıcı sürücülerini indirebiliriz.
"""

driver = webdriver.Chrome(ChromeDriverManager().install()) # Chrome tarayıcısını açar.
driver.get("https://www.google.com") # Google sayfasını açar.
input = driver.find_element(By.NAME , "q") # find_element() metodu ile arama kutusunu bulur. By.NAME ile name değerine göre arama yapar. q değeri arama kutusunun name değeridir.
input.send_keys("kodlama.io") # send_keys() metodu ile arama kutusuna yazı yazdırır.
searchButton = driver.find_element(By.NAME , "btnK") # find_element() metodu ile arama butonunu bulur. By.NAME ile name değerine göre arama yapar. btnK değeri arama butonunun name değeridir.
sleep(2) # Seleniumda butona tıklamadan önce 2 saniye bekletmeliyiz. Diğer durumlarda arama ypamayacaktır.
searchButton.click() # click() metodu ile arama butonuna tıklar.
sleep(3)
firstResult = driver.find_element(By.XPATH ,"/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a" ) # find_element() metodu ile ilk sonucu bulur. By.XPATH ile xpath değerine göre arama yapar. 
firstResult.click()

listOfCourses = driver.find_elements(By.CLASS_NAME , "course-listing") # find_elements() metodu ile tüm sonuçları bulur. By.CLASS_NAME ile class değerine göre arama yapar. course-listing değeri kodlamaio sitesindeki tüm kursların class değeridir.
print(f" Kodlamaio sitesinde şu anda {len(listOfCourses)} kurs var") # len() metodu ile sonuçların sayısını bulur.
# sleep(10) # 10 saniye bekler.
while True:
    continue


