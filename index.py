
###################### Index.py ######################
################## Python Exercises ##################

###### Imports ######

import math



######### String & Int types ##########

x = 0

hex(x) # Prints 0x...

bin(x) # Prints 0b...

int('0xadfebb', 0)
int('010111010', 2)

#######################################



############## Functions ##############


# Vowel Count
# Input a string, output the number of vowels
def vls(strng = ''):
    vowels = 'aeiouy'
    vowelCount = 0
    for i in strng:
        if i in vowels:
            vowelCount += 1
    print(str(vowelCount) + ' vowels in that string')


# String Split
# Separates vowels and consonants
def strSplit(defstring):
    vowels = 'aeiouy'
    for i in defstring:
        if i == ' ':
            break
        elif i not in vowels:
            print(i)

    for i in defstring:
        if i in vowels:
            print(i)


# String Analyser
# Advanced string analysing
def strAnalyse(strng, action, value):
    
    if action == 'remove':
        letterCount = 0
        for i in strng:
            if not i in value:
                letterCount+=1
        return letterCount
    elif action == 'find':
        wordCount = 0
        wordCount = strng.find(value)
        if wordCount != -1:
            return wordCount
        else:
            return 0

    elif action == 'delete':
        removed = strng.split(value)
        return removed
    
    elif action == 'split':
        s1 = ''
        s2 = ''
        for i in strng:
            if i in value:
                s2 += i
            else:
                s1 += i
        reslt = 'The sentence without given cahrs: %s (%s chars), and the unwanted chars: %s (%s). Total %s chars'%(s1, len(s1), s2, len(s2), len(strng))
        return reslt


# .Split
# Splits the Arg from the String
def splitEx(strng, arg):
    S = strng.split(arg)
    print(S[-1])


# Second Converter
# Converts seconds into a readable string
def timeConvrt(scnds):
    seconds = int(scnds)
    hours = seconds // 3600
    seconds1 = seconds - (hours * 3600)
    minutes = seconds1 // 60 
    seconds2 = seconds1 - (minutes * 60) 
    print('%sh:%sm:%ss'%(hours, minutes, seconds2))


# Coordinates Analyser
# Input command x & y Output final coordinates
def move(command = '.', x = 0, y = 0):
    steps = 1
    xpos = x
    ypos = y
    for i in command:
        if i == 'e': 
            xpos += steps
        elif i == 'w':
            xpos -= steps
        elif i == 'n':
            ypos += steps
        elif i == 's':
            ypos -= steps
        elif i == '.':
            pass
        elif i == 'd':
            steps *= 2
        elif i == 'h':
            steps /= 2
        elif i == 'r':
            ypos *= -1
        elif i == 'R':
            xpos *= -1
        else:
            pass
    coords = [xpos, ypos]
    return coords


# Days Analyser
# Converts a number of days to a readable format
def days(arg):
    days = int(arg)
    weeks = days // 7
    remnd = days % 7
    if remnd == 1:
        print('%s days is %s weeks and %s day'%(days, weeks, remnd))
    elif remnd == 0:
        print('%s days is %s weeks'%(days, weeks))
    else:
        print('%s days is %s weeks and %s days'%(days, weeks, remnd))


# Password Validation
# Validates the strength as a password of a given string
def acceptPass(password):
    chars = '!&%#@$*'
    charnum = 0
    for i in chars:
        charnum += strAnalyse(password, 'find', i)
    if charnum < 3:
        print('Invalid Password')
        return False
    if len(password) < 12:
        print('Invalid Password')
        return False
    charnum = 0
    chars = 'zxcvbnm'
    for i in chars:
        charnum += strAnalyse(password, 'find', i)
    if charnum > 3:
        print('Invalid Password')
        return False
    charnum = 0
    chars = '0123456789'
    for i in chars:
        charnum += strAnalyse(password, 'find', i)
    if charnum < 2:
        print('Invalid Password')
        return False
    charnum = 0
    chars = 'aeiouy'
    for i in chars:
        charnum += strAnalyse(password, 'find', i)
    if charnum < 2:
        print('Invalid Password')
        return False
    print('Success')
    return True
    

#######################################



############### Classes ###############


class car(object):
    def __init__(self, model, color, age):
        self.model = model
        self.color = color
        self.age = age

    def hsp(self, x):
        return x**2 + self.age * math.sqrt(x)

    def __str__(self):
        return "%s %s %syrs"%(self.color, self.model, self.age)


class color(object):
    def __init__ (self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def lightness(self):
        r = self.red / 255
        g = self.green / 255
        b = self.blue / 255
        light = (r + g + b) / 3
        return '%s%%'%(round(light * 100))

    def __str__(self):
        return 'rgb(%s, %s, %s)'%(self.red, self.green, self.blue)

    def __add__(self, other):
        nr = ((self.red + other.red) / 2)
        ng = ((self.green + other.green) / 2)
        nb = ((self.blue + other.blue) / 2)
        return color(nr, ng, nb)
        # if blendmode == 'darken':
        #     nr = ((self.red + r) / 2)
        #     ng = ((self.green + g) / 2)
        #     nb = ((self.blue + b) / 2)
        #     return 'rgb(%s, %s, %s)'%(nr, ng, nb)
        # elif blendmode == 'lighten':
        #     nr = self.red + r
        #     ng = self.green + g
        #     nb = self.blue + b
        #     return 'rgb(%s, %s, %s)'%(nr, ng, nb)
        # else:
        #     return 'Please specify a blend mode'
    
    def __eq__(self, other):
        if other.red == self.red and other.green == self.green and other.blue == self.blue:
            return True
        else:
            return False

    
    

class fraction(object):
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator

    def __str__(self):
        return '%s/%s'%(self.num, self.den)

    def __add__(self, other):
        newnum = (self.num * other.den) + (other.num * self.den)
        newden = other.den * self.den
        rounder = fraction(int(newnum), int(newden))
        return rounder.rounding()

    def __sub__(self, other):
        newnum = (self.num * other.den) - (other.num * self.den)
        newden = other.den * self.den
        rounder = fraction(int(newnum), int(newden))
        return rounder.rounding()

    def __mul__(self, other):
        newnum = self.num * other.den
        newden = other.den * self.num
        rounder = fraction(int(newnum), int(newden))
        return rounder.rounding()

    def __truediv__(self, other):
        newnum = self.num * other.num
        newden = other.den * self.den
        rounder = fraction(int(newnum), int(newden))
        return rounder.rounding()

    def rounding(self):
        if self.num == self.den:
            return 1
        elif self.den%self.num == 0:
            return fraction(1, int(self.den / self.num))
        for i in range(1, abs(min(self.den, self.num))):
            if round(self.num / i) == self.num / i and round(self.den / i) == self.den / i:
                self.den /= i
                self.num /= i
        return fraction(int(self.num), int(self.den))



class universityMember(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'Name: %s, Surname: %s, %syrs old'%(self.name.split(' ')[0], self.name.split(' ')[1], self.age)


class universityStudent(universityMember):
    def __init__(self, name, age, classes):
        universityMember.__init__(self, name, age)
        self.classes = classes

    def __str__(self):
        return 'Name: %s, %syrs old, %s'%(self.name, self.age, self.classes)



#######################################








