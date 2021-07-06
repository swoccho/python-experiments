from file_imports.addition import Addition

class Calculator:
    @classmethod
    def add(cls,num1,num2):
        return Addition.add(num1, num2)

    @classmethod
    def multiply(cls,num1,num2):
        return Addition.multiply(num1,num2)

    @classmethod
    def divide(cls,num1,num2):
        return Addition.divide(num1,num2)

    @classmethod
    def subtract(cls,num1,num2):
        return Addition.subtract(num1,num2)



