#!/usr/bin/python3

print("Content-type:text/html; charset=utf-8\r\n\r\n")

import cgi
import datetime
#import pytz

# Dictionary for Tamil translations of numbers
tamil_numbers_cardinals = {
    0: 'பூஜ்யம்',
    1: 'ஒன்று',
    2: 'இரண்டு',
    3: 'மூன்று',
    4: 'நான்கு',
    5: 'ஐந்து',
    6: 'ஆறு',
    7: 'ஏழு',
    8: 'எட்டு',
    9: 'ஒன்பது',
    10: 'பத்து',
    20: 'இருபது',
    30: 'முப்பது',
    40: 'நாற்பது',
    50: 'ஐம்பது',
    60: 'அறுபது',
    70: 'எழுபது',
    80: 'எண்பது',
    90: 'தொண்ணூறு',
    100: 'நூறு',
    200: 'இருநூறு',
    300: 'முந்நூறு',
    400: 'நானூறு',
    500: 'ஐநூறு',
    600: 'அறுநூறு',
    700: 'எழுநூறு',
    800: 'எண்ணூறு',
    900: 'தொள்ளாயிரம்',
    1000: 'ஆயிரம்',
    2000: 'இரண்டாயிரம்',
    3000: 'மூவாயிரம்',
    4000: 'நாலாயிரம்',
    5000: 'ஐயாயிரம்',
    6000: 'ஆறாயிரம்',
    7000: 'ஏழாயிரம்',
    8000: 'எட்டாயிரம்',
    9000: 'ஒன்பதாயிரம்',
    10000: 'பத்தாயிரம்',
    20000: 'இருபதாயிரம்',
    30000: 'முப்பதாயிரம்',
    40000: 'நாற்பதாயிரம்',
    50000: 'ஐம்பதாயிரம்',
    60000: 'அறுபதாயிரம்',
    70000: 'எழுபதாயிரம்',
    80000: 'எண்பதாயிரம்',
    90000: 'தொண்ணூறாயிரம்',
    100000: 'லட்சம்',
    10000000: 'கோடி',
    # Add translations for other numbers as needed
}

tamil_numbers_adj = {
     1: 'ஒரு',
     2: 'இரண்டு',
     3: 'மூன்று',
     4: 'நான்கு',
     5: 'ஐந்து',
     6: 'ஆறு',
     7: 'ஏழு',
     8: 'எட்டு',
     9: 'ஒன்பது',
    10: 'பதின்',
    20: 'இருபத்து',
    30: 'முப்பத்து',
    40: 'நாற்பத்து',
    50: 'ஐம்பத்து',
    60: 'அறுபத்து',
    70: 'எழுபத்து',
    80: 'எண்பத்து',
    90: 'தொண்ணூற்று',
    100: 'நூற்று',
    200: 'இருநூற்று',
    300: 'முன்னூற்று',
    400: 'நானூற்று',
    500: 'ஐநூற்று',
    600: 'அறுநூற்று',
    700: 'எழுநூற்று',
    800: 'எண்ணூற்று',
    900: 'தொள்ளாயிரத்து',
    1000: 'ஆயிரத்து',
    2000: 'இரண்டாயிரத்து',
    3000: 'மூவாயிரத்து',
    4000: 'நாலாயிரத்து',
    5000: 'ஐயாயிரத்து',
    6000: 'ஆறாயிரத்து',
    7000: 'ஏழாயிரத்து',
    8000: 'எட்டாயிரத்து',
    9000: 'ஒன்பதாயிரத்து',
    10000: 'பத்தாயிரத்து',
    20000: 'இருபதாயிரத்து',
    30000: 'முப்பதாயிரத்து',
    40000: 'நாற்பதாயிரத்து',
    50000: 'ஐம்பதாயிரத்து',
    60000: 'அறுபதாயிரத்து',
    70000: 'எழுபதாயிரத்து',
    80000: 'எண்பதாயிரத்து',
    90000: 'தொண்ணூறாயிரத்து',
    100000: 'லட்சத்து',
    10000000: 'கோடியே',
}

# Dictionary for Tamil translations of time units
tamil_units = {
    'year': 'ஆண்டு',
    'month': 'மாதம்',
    'day': 'நாள்',
    'hour': 'மணி',
    'minute': 'நிமிடம்',
    'second': 'விநாடி',
}

def convert_tamil_numbers_tens(n):
     n1 = divmod(n,10)
     #(8,6) 86
     if(n1[1] == 0):
        n2 = str(n1[0]) + "0" #10,20,30,40...
        return f"{tamil_numbers_cardinals[int(n2)]}"
     else:   
      n1a = str(n1[0]) + "0"
      n1adj = f"{tamil_numbers_adj[int(n1a)]}"
      double_digit = n1adj + " " + f"{tamil_numbers_cardinals[n1[1]]}"
      if(double_digit == "பதின் இரண்டு"):
         return "பன்னிரண்டு"
      else:
         return double_digit

def convert_tamil_numbers_hundreds(n):
        n1 = divmod(n,100)
        if(n1[1] == 0):
           n1_100 = str(n1[0]) + "00" #100,200,300...
           return f"{tamil_numbers_cardinals[int(n1_100)]}"
        elif(n1[1] <= 9):
           n1a = str(n1[0]) + "00"
           return f"{tamil_numbers_adj[int(n1a)]}" + " " + f"{tamil_numbers_cardinals[n1[1]]}"
        else: # (8,61) 861 or (0,84) 804
           n2a = str(n1[0]) + "00"
           return f"{tamil_numbers_adj[int(n2a)]}" + " " + convert_tamil_numbers_tens(n1[1]) 

def convert_tamil_numbers_thousands(n):    
        n1 = divmod(n,1000)
        if(n1[1] == 0): #1000,2000,3000,4000...
           n1_1000 = str(n1[0]) + "000"
           return f"{tamil_numbers_cardinals[int(n1_1000)]}"
        elif(n1[1] <= 9):
           n1a = str(n1[0]) + "000"
           return f"{tamil_numbers_adj[int(n1a)]}" + " " + f"{tamil_numbers_cardinals[n1[1]]}"
        elif(n1[1] <= 99):
           n1a = str(n1[0]) + "000"
           return f"{tamil_numbers_adj[int(n1a)]}" + " " + convert_tamil_numbers_tens(n1[1])
        else: # (8,61) 861 or (0,84) 804
           n2a = str(n1[0]) + "000"
           return f"{tamil_numbers_adj[int(n2a)]}" + " " + convert_tamil_numbers_hundreds(n1[1]) 

def convert_tamil_numbers_tenthousands(n):   
        n1 = divmod(n,10000)
        if(n1[1] == 0):
            n1_10000 = str(n1[0]) + "0000" #10000,20000...
            return f"{tamil_numbers_cardinals[int(n1_10000)]}"
        elif(n1[1] <= 9):
           n1a = str(n1[0]) + "0000"
           return f"{tamil_numbers_adj[int(n1a)]}" + " " + f"{tamil_numbers_cardinals[n1[1]]}"
        elif(n1[1] <= 99):
           n1a = str(n1[0]) + "0000"
           return f"{tamil_numbers_adj[int(n1a)]}" + " " + convert_tamil_numbers_tens(n1[1])
        elif(n1[1] <= 999):
           n1a = str(n1[0]) + "0000"
           return f"{tamil_numbers_adj[int(n1a)]}" + " " + convert_tamil_numbers_hundreds(n1[1])
        elif(n1[1] <= 9999):
            n2 = divmod(n1[1],1000)
            if(n2[1] <=9):  #2005 - 2,5
               n1a = str(n1[0]) + str(n2[0])
               return convert_tamil_numbers_tens(int(n1a)) + " ஆயிரத்து " + f"{tamil_numbers_cardinals[n2[1]]}" 
            elif(n2[1] <= 99): #2034 - 2,34
               n1a = str(n1[0]) + str(n2[0]) 
               return convert_tamil_numbers_tens(int(n1a)) + " ஆயிரத்து " + convert_tamil_numbers_tens(n2[1])
            else:
               n1a = str(n1[0]) + str(n2[0])
               return convert_tamil_numbers_tens(int(n1a)) + " ஆயிரத்து " + convert_tamil_numbers_hundreds(n2[1]) 

def convert_tamil_numbers_lakhs(n):   
        n1 = divmod(n,100000)
        if(n1[1] == 0):
            return f"{tamil_numbers_adj[n1[0]]}" + " " + "லட்சம்"
        elif(n1[1] <= 9):
           return f"{tamil_numbers_adj[n1[0]]}" + " " + "லட்சத்து" + " " + f"{tamil_numbers_cardinals[n1[1]]}"
        elif(n1[1] <= 99):
           return f"{tamil_numbers_adj[int(n1[0])]}" + " லட்சத்து " + convert_tamil_numbers_tens(n1[1])
        elif(n1[1] <= 999):
           return f"{tamil_numbers_adj[int(n1[0])]}" + " லட்சத்து " + convert_tamil_numbers_hundreds(n1[1])
        elif(n1[1] <= 9999):  
           return f"{tamil_numbers_adj[int(n1[0])]}" + " லட்சத்து " + convert_tamil_numbers_thousands(n1[1]) 
        elif(n1[1] <= 99999 and n1[0] <=9 ): #999999
           return f"{tamil_numbers_adj[int(n1[0])]}" + " லட்சத்து " + convert_tamil_numbers_tenthousands(n1[1])        
        else: #9999999 (99,99999)
           return convert_tamil_numbers_tens(n1[0]) + " லட்சத்து " + convert_tamil_numbers_tenthousands(n1[1])


def convert_tamil_numbers_crores(n):   
        n1 = divmod(n,10000000)
        if(n1[1] == 0):
            return f"{tamil_numbers_cardinals[n1[0]]}" + " " + " கோடி "
        elif(n1[0] <= 9):
          return  f"{tamil_numbers_adj[n1[0]]}" + " " + " கோடியே " + convert_tamil_numbers_lakhs(n1[1])   
        elif(n1[0] <= 99):
           return convert_tamil_numbers_tens(n1[0]) + " " + " கோடியே " + convert_tamil_numbers_lakhs(n1[1])
        elif(n1[0] <= 999): 
           return  convert_tamil_numbers_hundreds(n1[0]) + " கோடியே " + convert_tamil_numbers_lakhs(n1[1])
        elif(n1[0] <= 9999):
            return  convert_tamil_numbers_thousands(n1[0]) + " கோடியே " + convert_tamil_numbers_lakhs(n1[1])
        elif(n1[0] <= 99999):
            return  convert_tamil_numbers_tenthousands(n1[0]) + " கோடியே " + convert_tamil_numbers_lakhs(n1[1])
        elif(n1[0] <= 999999):
            return  convert_tamil_numbers_lakhs(n1[0]) + " கோடியே " + convert_tamil_numbers_lakhs(n1[1])
        
def current_date():
  # Get the current time
  current_time = datetime.datetime.now()

  # Extract the components of the current time
  year = current_time.year
  month = current_time.month
  day = current_time.day
 
  # Convert the components into Tamil strings
  tamil_date = convert_tamil_numbers(year) + "ஆம் வருடம் " + convert_tamil_numbers(month) + "ஆம் மாதம் " + convert_tamil_numbers(day) + "ஆம் நாள் " + "\n"
  # Print the Tamil time
  return "இன்று " + tamil_date

def current_time():
  # Get the current time
  current_time = datetime.datetime.now()

  # Extract the components of the current time
  year = current_time.year
  month = current_time.month
  day = current_time.day
  hour = current_time.hour
  minute = current_time.minute
  second = current_time.second
  if(hour >=12):
     ampm = 'மாலை'
     hour = hour - 12
     if(hour == 0):
        hour = 12
  else:
      ampm = 'காலை'
  # Convert the components into Tamil strings
  #tamil_time = f"{tamil_numbers[hour]} {tamil_units['hour']} {tamil_numbers[minute]} {tamil_units['minute']} {tamil_numbers[second]} {tamil_units['second']}"
  tamil_time = convert_tamil_numbers(hour) + " மணி " + convert_tamil_numbers(minute) + " நிமிடம் " + convert_tamil_numbers(second) + " வினாடி " + "\n"
  # Print the Tamil time
  return "இப்பொழுது அமெரிக்கக் கிழக்கு நேரம் " + ampm + " " + tamil_time

def convert_tamil_numbers(n):
    if(n <= 10):
       return f"{tamil_numbers_cardinals[n]}" 
    elif(n >= 11 and n <= 99):
        return convert_tamil_numbers_tens(n)
    elif(n >= 100 and n <= 999):
        return convert_tamil_numbers_hundreds(n)
    elif(n >= 1000 and n <=9999):
        return convert_tamil_numbers_thousands(n)
    elif(n >= 10000 and n <= 99999):
        return convert_tamil_numbers_tenthousands(n)
    elif(n >= 100000 and n <= 9999999):
        return convert_tamil_numbers_lakhs(n)    
    else:
        return convert_tamil_numbers_crores(n)


form = cgi.FieldStorage()
rnumber = ""
print("<ul><ul><br><br><a href=http://text2speech.tamilnlp.com/>Back to Tamil NLP site</a>")
print("<br><br>Enter a number in the field below and it will be converted to corresponding Tamil version of it:<br>")    
if(form):
  rnumber=form["roman_number"].value
  if(rnumber.isdigit):
     print("<font color=red>" + str(rnumber) + ": " + convert_tamil_numbers(int(rnumber)) + "</font>")
     print("<br><br><br>")
     print(current_time())
     print("<br>")
     print(current_date())
  else:
  	 print("Enter only digits in this field.")
  
    
print("<form name=f1 method=post action=convert_tamil_number.py>")
print("<table>")
print("<tr><td>Enter a roman number </td><td><input type=text name=roman_number><td></tr>")
print(" </td></tr>")
print(" <tr><td><input type=submit value=Submit></td><td> </td></tr>")
print("</table>")
print("</form>")
print("Examples:<br>")
print("9: ஒன்பது <br>")
print("99: தொண்ணூற்று ஒன்பது <br>")
print("999: தொள்ளாயிரத்து தொண்ணூற்று ஒன்பது <br>")
print("9999: ஒன்பதாயிரத்து தொள்ளாயிரத்து தொண்ணூற்று ஒன்பது<br>")
print("99999: தொண்ணூற்று ஒன்பது ஆயிரத்து தொள்ளாயிரத்து தொண்ணூற்று ஒன்பது <br>")
print("999999: ஒன்பது லட்சத்து தொண்ணூற்று ஒன்பது ஆயிரத்து தொள்ளாயிரத்து தொண்ணூற்று ஒன்பது <br>")
print("9999999: தொண்ணூற்று ஒன்பது லட்சத்து தொண்ணூற்று ஒன்பது ஆயிரத்து தொள்ளாயிரத்து தொண்ணூற்று ஒன்பது <br>")
print("99999999: ஒன்பது கோடியே தொண்ணூற்று ஒன்பது லட்சத்து தொண்ணூற்று ஒன்பது ஆயிரத்து தொள்ளாயிரத்து தொண்ணூற்று ஒன்பது <br>")
print("999999999: தொண்ணூற்று ஒன்பது கோடியே தொண்ணூற்று ஒன்பது லட்சத்து தொண்ணூற்று ஒன்பது ஆயிரத்து தொள்ளாயிரத்து தொண்ணூற்று ஒன்பது <br>")
print("9999999999: தொள்ளாயிரத்து தொண்ணூற்று ஒன்பது கோடியே தொண்ணூற்று ஒன்பது லட்சத்து தொண்ணூற்று ஒன்பது ஆயிரத்து தொள்ளாயிரத்து தொண்ணூற்று ஒன்பது <br>")
print("99999999999: ஒன்பதாயிரத்து தொள்ளாயிரத்து தொண்ணூற்று ஒன்பது கோடியே தொண்ணூற்று ஒன்பது லட்சத்து தொண்ணூற்று ஒன்பது ஆயிரத்து தொள்ளாயிரத்து தொண்ணூற்று ஒன்பது <br>")
print("999999999999: தொண்ணூற்று ஒன்பது ஆயிரத்து தொள்ளாயிரத்து தொண்ணூற்று ஒன்பது கோடியே தொண்ணூற்று ஒன்பது லட்சத்து தொண்ணூற்று ஒன்பது ஆயிரத்து தொள்ளாயிரத்து தொண்ணூற்று ஒன்பது <br>")
print("9999999999999: ஒன்பது லட்சத்து தொண்ணூற்று ஒன்பது ஆயிரத்து தொள்ளாயிரத்து தொண்ணூற்று ஒன்பது கோடியே தொண்ணூற்று ஒன்பது லட்சத்து தொண்ணூற்று ஒன்பது ஆயிரத்து தொள்ளாயிரத்து தொண்ணூற்று ஒன்பது <br>")

