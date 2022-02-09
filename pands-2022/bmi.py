Weight = int(input("Enter weight(Kg): "))
Height = int(input("Enter height(cm): "))
bmi = Weight/((Height/100)**2)
print("The BMI is {} kg/m\N{SUPERSCRIPT TWO}".format(bmi))