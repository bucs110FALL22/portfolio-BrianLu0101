from airport_api import Airport

def main():
    airports = ["JFK","LGA","SWF","BUF","HPN","ISP","ALB","SYR","ROC","JRA","FRG","ITH","BGM","PBG","IAG","MGJ","FOK","CZG"]
    continuous = True
    while continuous:    
        print("\n---------------------------------------------------------------------------------------------------------")
        print("Availabe airports in New York:\n" + str(airports))
        code = input("Airport FAA or ICAO Identifier Code (or Quit to stop): ")
        if code.upper() in airports:
            Airport(code.upper()).update()
            print("---------------------------------------------------------------------------------------------------------")
        elif code.lower() == 'quit':
            continuous = False
        else:
            print("This code does not associate with any airport within New York State.")
            print("---------------------------------------------------------------------------------------------------------")

main()
