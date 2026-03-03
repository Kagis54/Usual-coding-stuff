# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#Day 1 of Pyhton coding exercise GitHub

print("Welcome to mini unit converter")
print("press 1 to enter celcius degrees and convert to fahrenheit")
print("press 2 to enter fahrenheit and convert to celcius")
print("press 3 to enter kilometers and convert to meters")
print("press 4 to enter meters and convert to kilometers")

controlentry = int(input("enter your choice:"))  #option entered by user

value_entry = float(input("enter your value:"))  #value entered by user
if controlentry == 1:
   f=(value_entry*9/5)+32
   print(f"fahrenheit degrees: {f}")
elif controlentry == 2:
    c=(value_entry-32)*5/9
    print(f"celcius degrees: {c}")
elif controlentry == 3:
    m=value_entry*1000
    print(f"meters:{m}")
elif controlentry == 4:
    print(value_entry/1000)
else:
    print('you existed the program')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
