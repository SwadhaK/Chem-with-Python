
# Unit Converter By Swadha Kumari
# Instruction
# 1. Enter the type of unit ( Length, weight and Temperature)
# 2. Enter your unit and value to convert from
# 3. Enter you desired unit to convert for.

print ('''Unit Converter''')
typ= input ("\nEnter the type of unit,we accept LENGTH , WEIGHT , TEMPERATURE:  ")
type=typ.lower()


if type == ('length'):

    print('\nWe accept  only : mm, cm, m and km')
    unit1 = input (' Unit  convert from: ')
    unit2 = input (' Unit  convert to: ')
    num1 =  int(input(' Enter your value: ' ))

    def convert_unit(num1, unit1, unit2):
            unit = {'mm':0.001, 'cm':0.01, 'm':1.0, 'km':1000.}
            return num1*unit[unit1]/unit[unit2]
    answer=convert_unit(num1,unit1,unit2)
    print('\nYour value is {} {}'.format(answer,unit2))

elif type==('weight'):

    print('\nWe accept  only : microgram ,mg ,g, kg')
    unit1 = input (' Unit  convert from: ')
    unit2 = input (' Unit  convert to: ')
    num1 =  int(input(' Enter your value: ' ))

    def convert_unit(num1, unit1, unit2):
          unit = {'microgram':0.000001, 'mg':0.001, 'g':1.0, 'kg':1000}
          return num1*unit[unit1]/unit[unit2]
    answer=convert_unit(num1,unit1,unit2)
    print('\nYour value is {} {}'.format(answer,unit2))

elif type==('temperature'):

    print('\n We accept  only : K, C, F')
    unit1 = (input (' Unit  convert from: ')).upper()
    unit2 = (input (' Unit  convert to: ')).upper()
    num1 =  int(input(' Enter your value: ' ))

    if unit1 == "C" and unit2 == "K":
        answer = float(num1)+273.15
    elif unit1 == "K" and unit2 == "C":
        answer = float(num1)-273.15
    elif unit1 =="F" and unit2 == "C":
        answer = (float(num1)-32)*(5/9)
    elif unit1 == "C" and unit2 == "F":
        answer = (float(num1)*(9/5))+32
    print('\nYour value is {} {}'.format(answer,unit2))

else:
    print('\n Not a valid input')
