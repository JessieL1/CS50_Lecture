class Flight:
    counter = 1
    def __init__(self,origin,destination,duration):
        self.id=Flight.counter
        Flight.counter+=1

        self.passengers=[]

        self.origin=origin
        self.destination=destination
        self.duration=duration
    
    def print_info(self):
        print(f"Flight origin: {self.origin}.")
        print(f"Flight destination: {self.destination}.")
        print(f"Flight duration: {self.duration}.")
        print()
        print("Pssengers:")
        for passenger in self.passengers:
            print(f"{passenger.name}")
        
    def dalay(self,amount):
        self.duration +=amount

    
    def add_passenger(self,p):
        #self：Filght object p: Passenger object
        self.passengers.append(p)
        #p.filght_id=self.id
class Passenger:
    def __init__(self,name):
        self.name=name

def main():
    f1=Flight(origin="New York",destination="Paris",duration=540)
    
    alice=Passenger("Alice")
    bob=Passenger("Bob")

    f1.add_passenger(alice)
    f1.add_passenger(bob)

    f1.print_info()

if __name__ == "__main__":
    main() 