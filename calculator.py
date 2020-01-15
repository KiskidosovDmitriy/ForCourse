def calculate():
 number_1 = int(input ('pervoe chislo:'))
 number_2 = int(input ('vtoroe chislo:'))
 operation = input ('''viberite operasiy:
+ for plus
- for minus
* for multiplication
/ for division
Operasiya:''')
 if operation == '+':
  print (number_1 + number_2)
  again()
 elif operation == '-':
  print (number_1 - number_2)
  again()
 elif operation == '/':
  print (number_1 / number_2)
  again()
 elif operation == '*':
  print (number_1 * number_2)
  again()
 else:
  print('net takoy operasii,perezapolni normalno')
  calculate()
  
def again():
 calc_agn = input ('''
Eshe?
+ for Da
- for Net
''')
 if calc_agn == '+':
  calculate()
 elif calc_agn == '-':
  print ('Poka')
 else:
  print('vibiri + ili - ')
  again()
calculate()
