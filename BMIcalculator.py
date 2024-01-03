def bmi(weight, height):
    return weight / height ** 2


weight = float(input("Podaj swoją wagę w kg: "))
height = float(input("Podaj swój wzrot w m: "))

print(bmi(weight, height))

