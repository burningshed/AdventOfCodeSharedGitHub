from lib.autoloader import Autoloader

puz_data_url = 'https://adventofcode.com/2017/day/1/input'
al = Autoloader(puz_data_url)
al.connect()
data = al.fetch()
print(data)
