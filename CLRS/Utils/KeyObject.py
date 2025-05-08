class KeyObject:
    def __init__(self, string: str, key: int):
        self.string = string
        self.key = key
    
    @staticmethod
    def get_key(x) -> int:
        return x.key

    @staticmethod
    def set_key(key: int):
        self.key = key

    def __gt__(self, other: "KeyObject"):
        return self.key > other.key
    
    def __str__(self):
        return self.string + ":" + str(self.key)


#Testing
if __name__=="__main__":
    obja = KeyObject("a", 1)
    objb = KeyObject("b", 2)
    print(obja > objb)
    print(obja < objb)




