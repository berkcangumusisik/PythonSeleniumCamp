import matematik as m   # import <module_name> as <alias_name>
import random
from day3 import Human # from <module_name> import <class_name>
import  selenium

print(m.topla(5,3)) # 8
print(random.randint(1,10)) # 1 ile 10 arasında rastgele bir sayı üretir.

human1 = Human("Berkcan")
human1.talk("Merhaba")

selenium.webdriver.Chrome()