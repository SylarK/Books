class Orc():
    def __init__(self, name, age, element):
        self.name       = name
        self.age        = age
        self.element    = element
    
    def sounds(self):
        print('AWRRRG!')
    
    def weapon(self):
        print('Take the axe.')

class Human():
    def __init__(self, name, age, element):
        self.name       = name
        self.age        = age
        self.element    = element
    
    def sounds(self):
        print('OUCH!')

    def weapon(self):
        print('Take the bow.')

obj_orc = Orc('Max', 35, 'Fire')
obj_hum = Human('Charles', 32, 'Water')

for char in (obj_hum, obj_orc):
    char.sounds()
    char.weapon()
