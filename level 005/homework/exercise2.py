# and - это логический оператор который возвращает (True), если только оба его операнда истинны, если нет то будет ложь (False)

# мешок картошки и мешок свеклы

print (True and True) # правильно
print (False and True) # не правильно
print (True and False) # не правильно
print (False and False) # не правильно

#print(5 > 4 and 150 < 200) # правильно

# or - возвращает (True), если хотя бы одно из двух или более логических выражений ложны. И ложь если только все вырожения ложныe.

# лимонад или сок

print (False or True) # правильно
print (True or False) # правильно
print (False or False) # не правильно
print (True or True) # правильно

#print(5 > 15 or 50 < 100) # правильно

# not - оператор переворачивает значение, если оно было True то станет False или наоборот

print (not True)
print (not False)