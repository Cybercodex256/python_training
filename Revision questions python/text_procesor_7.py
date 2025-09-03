sentence=input("Input a sentence containg the word python:")
no_of_words=len(sentence.split())
print(f"\nThe sentence contains {no_of_words} words")
print(f"Lowercase version: {sentence.lower()}")
print(f"Reversed sentence:  {' '.join(sentence.split()[::-1])} ")
if "python" in sentence.lower():
   print("The sentence is about python")
else :
   pass


