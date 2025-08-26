# class car, method contans car detials , creting obejct and access details 
class car: 
    def __init__(self, car_model, car_variant, engine):
        self.model = car_model
        self.variant = car_variant
        self.eng_ine = engine

object1 = car("verna", "sx", "2cc")
print(object1.model) #print with var name tht is uses with self keyword 
print(object1.variant)
print(object1.eng_ine)


        