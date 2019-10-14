
# Python Testcode.

# ```Python
foods = ['apple','curry','sushi','tenpura']
foods[1] = 'pizza'
print(foods)
# ```

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

## classの定義
class person():
    def __init__(self, name):
        self.name = name
hunter = person('Elmer Fudd')
print('The mighty hunter: ', hunter.name)

## Classの継承
class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    pass

give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()
