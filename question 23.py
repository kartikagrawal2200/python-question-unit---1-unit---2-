word = input("Enter a word: ").lower()
vowels = "aeiou"
vowel_count = 0
for char in word:
   if char in vowels:
      vowel_count += 1 
print(f"Number of vowels: {vowel_count}")
