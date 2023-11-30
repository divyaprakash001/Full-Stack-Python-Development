letter = 'Hey my name is {name} and my country name is {country}'
name='Harry'
country = 'India'
# print(letter.format(country=country,name=name))

print(f"Hey my name is {{name}} and my country name is {{country}}")
print(f"Hey my name is {name} and my country name is {country}")

price = 'for only price {price:.2f} rupee'
print(price.format(price=43.3422))