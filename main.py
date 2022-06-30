print("What message would you like to encode?")
message = input()
values = [letter for letter in message]

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

secret_alphabet = ["z", "y", "x", "w", "v", "u", "t", "s", "r", "q", "p", "o", "n", "m", "l", "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a", " "]

def encode(values):
  x = ""
  for letter in values:
    index = alphabet.index(letter)
    x += secret_alphabet[index]

  return x

  
secret_message = encode(values)
print(secret_message)

