def leap_year():
        year=int(input("Ingrese un año: "))
        if year>=100 and year%400==0:
                print(f"El año {year} es bisiesto")
        elif year<100 and year%4==0:
                print(f"El año {year} es bisiesto")
        else:
                print(f"El año {year} no es bisiesto")        

