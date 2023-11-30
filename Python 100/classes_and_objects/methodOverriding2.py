class Aeroplane:
     def takeOff(self):
        print('Aeroplane is taking off')
     def landing(self):
        print('Aeroplane is landing')
    
class Cargoplane(Aeroplane):
    def takeOff(self):
        print('Cargoplane is taking off at medium pace')
    def landing(self):
        print('Cargoplane is landing at medium pace')
    def carryGoods(self):
        print('Cargoplane is carrying goods.')


class PassengerPlane(Aeroplane):
    def takeOff(self):
        print('PassengerPlane is taking off at slow pace')
    def landing(self):
        print('PassengerPlane is landing at slow pace')
    def carryPassenger(self):
        print('PassengerPlane is carrying passenger.')





ar =  Cargoplane()
ar.takeOff()
ar.landing()
ar.carryGoods()