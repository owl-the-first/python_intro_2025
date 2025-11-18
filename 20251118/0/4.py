import locale

print('Привет'.encode())
print('Привет'.encode('CP1251'))
print('Привет'.encode('CP1251').decode('KOI8-R'))

print('----------------')

print("Вопрос: ", 'Вопрос'.encode('CP1251').decode('KOI8-R'))
print("бМХЛЮМХЕ: ", 'бМХЛЮМХЕ'.encode('KOI8-R').decode('CP1251'))
print("ОХРЮМХЕ: ", 'ОХРЮМХЕ'.encode('KOI8-R').decode('CP1251'))
