magazine = {'apple': 4, 'cherry': 10}
magazine['apple']
print(magazine['cherry'])
magazine['fruit'] = 14

print(magazine['fruit'])
print(magazine.get('', 10))

try:
    print(magazine['orange'])
except:
    magazine['orange'] = 111
    print(magazine.get('orange'))

magazine.pop('orange')

print(magazine)