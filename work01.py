
# Python Testcode.

print("## リストの要素[一部書き換え]")
foods = ['apple','curry','sushi','tenpura']
foods[1] = 'pizza'
print(foods)

print("")
print("## リストの要素[選択して表示]")
cliches = [
"At the end of the day",

"Having said that",
"The fact of the matter is",
"Be that as it may",
"The bottom line is",
"If you will",
]
print(cliches[2])

quotes = {
"Moe": "A wise guy, huh?",
"Larry": "Ow!", 
"Curly": "Nyuk nyuk!", 
}
stooge = "Curly"
print(stooge, "says:", quotes[stooge])

language = 7
print("Language %s: I am Python. What's for supper?" % language)
print("(日本語訳：言語 7： 私がPythonです。晩御飯はなんですか？)")

print("")
print("## classの定義")

class person():
    def __init__(self, name):
        self.name = name
hunter = person('Elmer Fudd')
print('The mighty hunter: ', hunter.name)

print("")
print("## Classの継承")

class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    pass

give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()

print("")
print("## 親Classのオーバーライド")

class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo[; Much like a Car, but more Yugo-ish.")

give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()

print("")
print("## Classのオーバーライド __init__メソッド編")

class Person():
    def __init__(self, name):
        self.name = name

class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name

class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"

person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')
print(person.name)
print(doctor.name)
print(lawyer.name)

print("")
print("## これでもいける？親classを継承しなくても単体でnameを変えられるかどうか検証")

class MDPerson():
    def __init__(self, name):
        self.name = "Doctor " + name
        
doctor = MDPerson('Fudd')
print(doctor.name)

print()
print("## import sysモジュールを使ってみる")

import sys
print('Program arguments:', sys.argv)
