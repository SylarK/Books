    # Hipotenusa² = Cateto oposto² + Cateto adj²
import math

def hipotenusa(catOposto, catAdj): 
    x = int(math.pow(catOposto, 2)) + int(math.pow(catAdj, 2))
    return 'Value: ' + str(x)

print(hipotenusa(5,2))