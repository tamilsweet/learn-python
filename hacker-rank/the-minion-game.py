def minion_game(string):
    # your code goes here
    kevin = 0
    stuart = 0
    vowel = "AEIOU"
    str_length = len(string)
    for char in string:
        if char in vowel:
            kevin += str_length
        else:
            stuart += str_length
        str_length -= 1
    
    if kevin > stuart:
      print(f"Kevin {kevin}")
    elif kevin < stuart:
      print(f"Stuart {stuart}")
    else:
      print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)