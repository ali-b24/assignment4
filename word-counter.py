def countWords(string): 
    state = 0 
    wc = 0
  
    for i in range(len(string)): 
  
        if (string[i] == ' ' or string[i] == '\n' or string[i] == '\t'): 
            state = 0
  
        elif state == 0: 
            state = 1
            wc += 1
  
    return wc 
  
string = input("enter your string:\n")
print("Number of words :" , str(countWords(string))) 