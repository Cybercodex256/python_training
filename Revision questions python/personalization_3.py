def personalize(email):
   username=email[:email.index("@")]
   domain_name=email[email.index("@")+1 :]
   return username ,domain_name

print(personalize("Edwjn@gmail.com"))
print(personalize("Kamugishaedwin256@gmail.com"))
print(personalize("anorld107@gmail.com"))
print(personalize("yasal367dn@gmail.com"))
