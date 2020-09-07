class Flight:
    def __init__(self,origin,destination,duration):
        self.origin=origin
        self.destination=destination
        self.duration=duration

    def print_info(self):
        print(f"Flight origin: {self.origin}")

def main():
    f1=Flight(origin="New York",destination="Paris",duration=540)
    f1.print_info()

if __name__ == "__main__":
    main()
