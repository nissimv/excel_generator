from pydbgen import pydbgen

myDB = pydbgen.pydb()

print('This generator creates the fields name, phone, time and country')
num = input('how many rows do you want? :')

test_df = myDB.gen_excel(num=num, fields=['name', 'phone', 'time', 'country'],
 phone_simple = False, filename='customer_details.xlsx')


print('file was created ...')



