class Animal:

    def __init__(self, typeAnimal):
        self.typeAnimal = typeAnimal


    def sounds(self, noise=None):

        if noise is not None:
            print('Sound: ' + noise)
        else:
            print('Sound: !!!!!')

obj_an1 = Animal('Dog')
obj_an2 = Animal('Cat')
obj_an3 = Animal('Bird')

obj_an1.sounds('Rowf rowf')
obj_an2.sounds('Meooown')
obj_an3.sounds()
