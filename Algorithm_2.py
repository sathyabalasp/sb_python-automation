# Task 1. Reverse a negative integer and keep the negative sign at the beginning.
# Example: -189 -> -981

def reverse_integer(n: int):

      st1 = str(n)

      if st1[0] == '-':
         return int("-" + st1[:0:-1])
      else:
         return int(st1[::-1])


print(reverse_integer(-189))

# Task 2. Write a function that takes two strings as input and returns True if they are anagrams of each other, and False otherwise.
# The strings can contain uppercase and lowercase letters, and should be ignored during the comparison.


def are_anagrams(s1: str, s2: str):
    s1 = s1.lower()
    if len(s1) != len(s2):
        return False
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

print(are_anagrams('race', 'care'))
print(are_anagrams('hEArt', 'earth'))
print(are_anagrams('rattle', 'battle'))

# Task 3. Given a sentence, reverse the order of characters in each word.
def reverse_words(sentence: str):
    list_of_sentence = sentence.split()
    print(list_of_sentence)
    reverse_sentence = []
    for word in list_of_sentence:
        reverse_word = word[::-1]
        reverse_sentence.append(reverse_word)
        joined_reverse_sentence = " ".join(reverse_sentence)
    return (joined_reverse_sentence)

sentence = "Hello welcome to the python Algorithm"
print(reverse_words(sentence))

#Task 4. Given a string made of digits [0-9], return a string where each digit is repeated a number of times equals to its value.

def repeat_digits(s: str):
    result = ' '
    for m in s:
        result += m * int(m)

    return (result)


# Task 5. Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u) in a given string.
# “y” is not considered a vowel for this task. The input string is always in lowercase.

print(repeat_digits("234"))

def shortcut(s: str):
    result = ""
    for char in s:
        if( char not in ('a','e','i','o','u') ):
            result += char

    return(result)

print(shortcut("elephant"))