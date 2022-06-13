from products import * 

class Cart():
    def __init__(self):
        self.__productList = []
        self.__cartValue = 0

    def addProduct(self,product):
       #if isinstance(product, Phone) or isinstance(product, TV):
       if isinstance(product, Product):
        if product not in self.__productList:
            self.__productList.append(product)
            self.calculateCart()


    def calculateCart(self):
        self.__cartValue = 0
        for el in self.__productList:
            self.__cartValue += el.price

    def __str__(self):
        strData = "\nCart Info, products list:"
        for el in self.__productList:
            strData += "\n - " + str(el.name) + " " + str(el.price)
            strData += "\n cart value:" + str(self.__cartValue)
        return strData

