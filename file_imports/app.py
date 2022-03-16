from file_imports.addition import Addition

class Calculator:
    @classmethod
    def add(cls,num1,num2):
        return Addition.add(num1, num2)

    @classmethod
    def subtract(cls,num1,num2):

        return cls.add(num1,-num2)

    @classmethod
    def multiply(cls,num1,num2):
        result = 0
        for x in range(0, num2):
            result = cls.add(result,num1)
        return result

    @classmethod
    def divide(cls,num1,num2):
        result = 0
        while num1 >= num2:
            num1 = cls.subtract(num1,num2)
            result = cls.add(result,1)

        return result






