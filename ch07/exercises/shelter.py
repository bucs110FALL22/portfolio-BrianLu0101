import time

class Animal:
    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.id = time.strftime("%d/%m/%Y")
        self.arrived = time.strftime("%d/%m/%Y")
        self.adopted = None
    
    def setAdopt(self):
        self.adopt = time.strftime("%d/%m/%Y")

    def __str__(self):
        result_str = f"{self.name}[{self.type}]"
        result_str += f"\narrived: {self.arrived}"
        result_str += f"\nadopted: {self.adopted}"
        return result_str

def main():
    fido = Animal('Fido','Cat')
    fido.setAdopt()
    print(fido)

main()