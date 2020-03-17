def isPhoneNumber(text):
   if len(text) != 12:
         return False
     for i in range(0, 3):
       if not text[i].isdecimal():
             return False
   if text[3] != '-':
         return False
     for i in range 7):
       if not text[i].isdecimal():
             return False
   if text[7] != '-':
         return False
     for i in range(8, 12):
       if not text[i].isdecimal():
             return False
   return True
   
"""
First the code checks that the string is exactly 12 characters 
Then it checks that the area code (that is, the first three characters in text) consists of only numeric characters 
The rest of the function checks that the string follows the pattern of a phone number: 
the number must have the first hyphen after the area code , 
three more numeric characters , 
then another hyphen , 
and finally four more numbers . 
If the program execution manages to get past all the checks, it returns True.
The loop goes through the entire string, 
testing each 12-character piece and printing any chunk it finds that satisfies isPhoneNumber(). 
Once it's done going through message, print Done.
"""
message = 'I am unavailable now, please Call me at 444-555-8888 later'
for i in range(len(message)):
   chunk = message[i:i+12]
   if isPhoneNumber(chunk):
          print('Phone number found: ' + chunk)
print('Done')

"""
What If the input is "444-555-88 later88 99 00"
"""
