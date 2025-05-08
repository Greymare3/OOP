class dog:
    def speak(self):
        return 'woof!'

class cat:
    def speak(self):
        return 'meow!'
#polysoysim in action
for animal in (dog(),cat()):
    print(animal.speak())