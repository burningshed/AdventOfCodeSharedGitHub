from lib.autoloader import Autoloader

al = Autoloader()
al.connect()
data = al.f_fetch(2020, 5)
print(data)

