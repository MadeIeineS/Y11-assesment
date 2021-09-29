# Currency types list
currency_types = """
The U.S. dollar (USD)
The Euro (EUR)
Japanese Yen (JPY)
The Pound Sterling (GBP)
Australian Dollar (AUD)
Canadian Dollar (CAD)
The Swiss Franc (CHF)
Chinese Renminbi (CNY)
South Korean Won (KRW)
Swedish Krona (SEK)
The Singapore dollar (SGD)
Norwegian Krone (NOK)
Mexican peso (MXN)
Indian rupee (INR)
Russian ruble (RUB)"""

# Finding name and capitalise, for user friendliness :)
name = input("What is your name? ")
name = name.capitalize()

# finding what currency they want
print(f"Hi {name}! We are able to convert the New Zealand dollar to any of the following currencies: {currency_types} ")
currency_type = input("What type of currency would you like to convert to? (please use the list above and enter the currency code e.g. USD) ")
currency_type = currency_type.upper()

# Setting a boundary for the amount the user can enter
amount = float(input("How much would you like to convert? $"))
# Calculating the total with if statements
def currency_calculator(currency_type , amount):
   while amount == float:
      if amount <= 100000000000000:
         if currency_type == "USD":
            print(f"That comes to ${amount * 0.73}")
         elif currency_type == "EUR":
            print(f"That comes to €{amount * 0.6}")
         elif currency_type == "JPY":
            print(f"That comes to ¥{amount * 79.78}")
         elif currency_type == "GBP":
            print(f"That comes to £{amount * 0.51}")
         elif currency_type == "AUD":
            print(f"That comes to ${amount * 0.94}")
         elif currency_type == "CAD":
            print(f"That comes to {amount * 0.88}")
         elif currency_type == "CHF":
            print(f"That comes to €{amount * 0.65}")
         elif currency_type == "CNY":
            print(f"That comes to €{amount * 4.62}")
         elif currency_type == "KRW":
            print(f"That comes to €{amount * 808.45}")
         elif currency_type == "SEK":
            print(f"That comes to {amount * 6.12} kr")
         elif currency_type == "SGD":
            print(f"That comes to s${amount * 0.96}")
         elif currency_type == "NOK":
            print(f"That comes to {amount * 6.18} kr")
         elif currency_type == "MXN":
            print(f"That comes to ${amount * 14.15}")
         elif currency_type == "INR":
            print(f"That comes to ₹{amount * 52.40}")
         elif currency_type == "RUB":
            print(f"That comes to ₽{amount * 51.99}")
         else:
            print("Please enter a valid code")
      else:
         print("Please enter a number less than 100,000,000,000,000")
   else:
      print("Please enter a valid number")
currency_calculator(currency_type, amount)

