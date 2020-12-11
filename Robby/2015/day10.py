data=1113222113
class look_say():
    def __init__(self, starting_string):
        self.cur_string = str(starting_string)

    def one_time_err(self):
        ii = 0
        next_string = []
        str_len = len(self.cur_string)
        while ii < str_len:
            ii, cur_letter, num = self.look_err(ii, self.cur_string[ii], 0, str_len)
            next_string.extend((str(num), cur_letter))
        self.cur_string = ''.join(next_string)

    def look_err(self, ii, cur_letter, num, str_len):
        try: 
            if self.cur_string[ii] == cur_letter:
                return self.look_err(ii+1, cur_letter, num+1, str_len)
        except IndexError as err:
            return ii, cur_letter, num
        return ii, cur_letter, num

    def one_time_if(self):
        ii = 0
        next_string = []
        str_len = len(self.cur_string)
        while ii < str_len:
            ii, cur_letter, num = self.look_if(ii, self.cur_string[ii], 0, str_len)
            next_string.extend((str(num), cur_letter))
        self.cur_string = ''.join(next_string)

    def look_if(self, ii, cur_letter, num, str_len):
        if ii >= str_len:
            return ii, cur_letter, num
        if self.cur_string[ii] == cur_letter:
            return self.look_if(ii+1, cur_letter, num+1, str_len)
        return ii, cur_letter, num

    def look_iter(self, times=1):
        for _ in range(times):
            old_number = self.cur_string[0]
            count = 0
            counts = []
            numbers = []
            for letter in self.cur_string:
                if letter == old_number:
                    count += 1
                else:
                    counts.append(count)
                    numbers.append(old_number)
                    old_number = letter
                    count = 1
            counts.append(count)
            numbers.append(old_number)
            self.cur_string = ''.join(map(lambda x,y: ''.join((str(x), y)), counts, numbers))



ls = look_say(data)

data=1113222113
import time
t0 = time.time()

class look_say():
    def __init__(self, starting_string):
        self.cur_string = str(starting_string)

    def one_time_err(self):
        ii = 0
        next_string = []
        str_len = len(self.cur_string)
        while ii < str_len:
            ii, cur_letter, num = self.look_err(ii, self.cur_string[ii], 0, str_len)
            next_string.extend((str(num), cur_letter))
        self.cur_string = ''.join(next_string)

    def look_err(self, ii, cur_letter, num, str_len):
        try: 
            if self.cur_string[ii] == cur_letter:
                return self.look_err(ii+1, cur_letter, num+1, str_len)
        except IndexError as err:
            return ii, cur_letter, num
        return ii, cur_letter, num

    def one_time_if(self):
        ii = 0
        next_string = []
        str_len = len(self.cur_string)
        while ii < str_len:
            ii, cur_letter, num = self.look_if(ii, self.cur_string[ii], 0, str_len)
            next_string.extend((str(num), cur_letter))
        self.cur_string = ''.join(next_string)

    def look_if(self, ii, cur_letter, num, str_len):
        if ii >= str_len:
            return ii, cur_letter, num
        if self.cur_string[ii] == cur_letter:
            return self.look_if(ii+1, cur_letter, num+1, str_len)
        return ii, cur_letter, num

    def look_iter(self, times=1):
        for _ in range(times):
            old_number = self.cur_string[0]
            count = 0
            counts = []
            numbers = []
            for letter in self.cur_string:
                if letter == old_number:
                    count += 1
                else:
                    counts.append(count)
                    numbers.append(old_number)
                    old_number = letter
                    count = 1
            counts.append(count)
            numbers.append(old_number)
            self.cur_string = ''.join(map(lambda x,y: ''.join((str(x), y)), counts, numbers))



ls = look_say(data)

for ii in range(50):
    ls.one_time_err()
t1 = time.time()

print('using error:', t1-t0)
print(len(ls.cur_string))

t0 = time.time()

class look_say():
    def __init__(self, starting_string):
        self.cur_string = str(starting_string)

    def one_time_err(self):
        ii = 0
        next_string = []
        str_len = len(self.cur_string)
        while ii < str_len:
            ii, cur_letter, num = self.look_err(ii, self.cur_string[ii], 0, str_len)
            next_string.extend((str(num), cur_letter))
        self.cur_string = ''.join(next_string)

    def look_err(self, ii, cur_letter, num, str_len):
        try: 
            if self.cur_string[ii] == cur_letter:
                return self.look_err(ii+1, cur_letter, num+1, str_len)
        except IndexError as err:
            return ii, cur_letter, num
        return ii, cur_letter, num

    def one_time_if(self):
        ii = 0
        next_string = []
        str_len = len(self.cur_string)
        while ii < str_len:
            ii, cur_letter, num = self.look_if(ii, self.cur_string[ii], 0, str_len)
            next_string.extend((str(num), cur_letter))
        self.cur_string = ''.join(next_string)

    def look_if(self, ii, cur_letter, num, str_len):
        if ii >= str_len:
            return ii, cur_letter, num
        if self.cur_string[ii] == cur_letter:
            return self.look_if(ii+1, cur_letter, num+1, str_len)
        return ii, cur_letter, num

    def look_iter(self, times=1):
        for _ in range(times):
            old_number = self.cur_string[0]
            count = 0
            counts = []
            numbers = []
            for letter in self.cur_string:
                if letter == old_number:
                    count += 1
                else:
                    counts.append(count)
                    numbers.append(old_number)
                    old_number = letter
                    count = 1
            counts.append(count)
            numbers.append(old_number)
            self.cur_string = ''.join(map(lambda x,y: ''.join((str(x), y)), counts, numbers))



ls = look_say(data)

for ii in range(50):
    ls.one_time_if()
t1 = time.time()
print('using if:', t1-t0)
print(len(ls.cur_string))

t0 = time.time()

class look_say():
    def __init__(self, starting_string):
        self.cur_string = str(starting_string)

    def one_time_err(self):
        ii = 0
        next_string = []
        str_len = len(self.cur_string)
        while ii < str_len:
            ii, cur_letter, num = self.look_err(ii, self.cur_string[ii], 0, str_len)
            next_string.extend((str(num), cur_letter))
        self.cur_string = ''.join(next_string)

    def look_err(self, ii, cur_letter, num, str_len):
        try: 
            if self.cur_string[ii] == cur_letter:
                return self.look_err(ii+1, cur_letter, num+1, str_len)
        except IndexError as err:
            return ii, cur_letter, num
        return ii, cur_letter, num

    def one_time_if(self):
        ii = 0
        next_string = []
        str_len = len(self.cur_string)
        while ii < str_len:
            ii, cur_letter, num = self.look_if(ii, self.cur_string[ii], 0, str_len)
            next_string.extend((str(num), cur_letter))
        self.cur_string = ''.join(next_string)

    def look_if(self, ii, cur_letter, num, str_len):
        if ii >= str_len:
            return ii, cur_letter, num
        if self.cur_string[ii] == cur_letter:
            return self.look_if(ii+1, cur_letter, num+1, str_len)
        return ii, cur_letter, num

    def look_iter(self, times=1):
        for _ in range(times):
            old_number = self.cur_string[0]
            count = 0
            counts = []
            numbers = []
            for letter in self.cur_string:
                if letter == old_number:
                    count += 1
                else:
                    counts.append(count)
                    numbers.append(old_number)
                    old_number = letter
                    count = 1
            counts.append(count)
            numbers.append(old_number)
            self.cur_string = ''.join(map(lambda x,y: ''.join((str(x), y)), counts, numbers))



ls = look_say(data)

for ii in range(50):
    ls.look_iter()
t1 = time.time()
print('using iter:', t1-t0)
print(len(ls.cur_string))

t0 = time.time()

class look_say():
    def __init__(self, starting_string):
        self.cur_string = str(starting_string)

    def one_time_err(self):
        ii = 0
        next_string = []
        str_len = len(self.cur_string)
        while ii < str_len:
            ii, cur_letter, num = self.look_err(ii, self.cur_string[ii], 0, str_len)
            next_string.extend((str(num), cur_letter))
        self.cur_string = ''.join(next_string)

    def look_err(self, ii, cur_letter, num, str_len):
        try: 
            if self.cur_string[ii] == cur_letter:
                return self.look_err(ii+1, cur_letter, num+1, str_len)
        except IndexError as err:
            return ii, cur_letter, num
        return ii, cur_letter, num

    def one_time_if(self):
        ii = 0
        next_string = []
        str_len = len(self.cur_string)
        while ii < str_len:
            ii, cur_letter, num = self.look_if(ii, self.cur_string[ii], 0, str_len)
            next_string.extend((str(num), cur_letter))
        self.cur_string = ''.join(next_string)

    def look_if(self, ii, cur_letter, num, str_len):
        if ii >= str_len:
            return ii, cur_letter, num
        if self.cur_string[ii] == cur_letter:
            return self.look_if(ii+1, cur_letter, num+1, str_len)
        return ii, cur_letter, num

    def look_iter(self, times=1):
        for _ in range(times):
            old_number = self.cur_string[0]
            count = 0
            counts = []
            numbers = []
            for letter in self.cur_string:
                if letter == old_number:
                    count += 1
                else:
                    counts.append(count)
                    numbers.append(old_number)
                    old_number = letter
                    count = 1
            counts.append(count)
            numbers.append(old_number)
            self.cur_string = ''.join(map(lambda x,y: ''.join((str(x), y)), counts, numbers))



ls = look_say(data)

ls.look_iter(50)
t1 = time.time()
print('using iter:', t1-t0)
print(len(ls.cur_string))

data=1113222113

class look_say():
    def __init__(self, starting_string):
        self.cur_string = str(starting_string)

    def one_time_err(self):
        ii = 0
        next_string = []
        str_len = len(self.cur_string)
        while ii < str_len:
            ii, cur_letter, num = self.look_err(ii, self.cur_string[ii], 0, str_len)
            next_string.extend((str(num), cur_letter))
        self.cur_string = ''.join(next_string)

    def look_err(self, ii, cur_letter, num, str_len):
        try: 
            if self.cur_string[ii] == cur_letter:
                return self.look_err(ii+1, cur_letter, num+1, str_len)
        except IndexError as err:
            return ii, cur_letter, num
        return ii, cur_letter, num

    def one_time_if(self):
        ii = 0
        next_string = []
        str_len = len(self.cur_string)
        while ii < str_len:
            ii, cur_letter, num = self.look_if(ii, self.cur_string[ii], 0, str_len)
            next_string.extend((str(num), cur_letter))
        self.cur_string = ''.join(next_string)

    def look_if(self, ii, cur_letter, num, str_len):
        if ii >= str_len:
            return ii, cur_letter, num
        if self.cur_string[ii] == cur_letter:
            return self.look_if(ii+1, cur_letter, num+1, str_len)
        return ii, cur_letter, num

    def look_iter(self, times=1):
        for _ in range(times):
            old_number = self.cur_string[0]
            count = 0
            counts = []
            numbers = []
            for letter in self.cur_string:
                if letter == old_number:
                    count += 1
                else:
                    counts.append(count)
                    numbers.append(old_number)
                    old_number = letter
                    count = 1
            counts.append(count)
            numbers.append(old_number)
            self.cur_string = ''.join(map(lambda x,y: ''.join((str(x), y)), counts, numbers))



ls = look_say(data)
