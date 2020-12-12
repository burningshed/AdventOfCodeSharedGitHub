from autoloader import Autoloader
import reader

testurl = 'https://adventofcode.com/2017/day/1/input'
altest = Autoloader(testurl)

altest.connect()
print(altest.fetch())
# password
# login
