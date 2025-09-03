

def formatNumber(phone):
 
    section1=phone[:3]
    section2=phone[3:][:3]
    section3=phone[3:][3:]
    print(f"({section1}) {section2}-{section3}")

#formatNumber(phone_number)
while True:
 phone_number=input("Enter your phone number:")
 if len(phone_number)==10:
       formatNumber(phone_number)
       break
 else :
       print(f"Ivalid phone number length({len(phone_number)}) . Phone number should have 10 digits\n\n")
