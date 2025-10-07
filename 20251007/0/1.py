import decimal
import fractions

def multiplier(x, y, Type):
    return Type(x) * Type(y)

x = "3.2"
y = "2.5"
print(multiplier(x, y, decimal.Decimal))
    