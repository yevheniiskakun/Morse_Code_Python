''' Morse Code '''  
''' We will use 2 alphabets, first with Morse letters and second with English letters'''  
''' The algorithm works by comparing the letters of the English alphabet and characters from the Morse code and vice versa '''                                                                                                                                                                                                  #numbers  
morse_code = ["*-", "-***", "-*-*", "-**", "*", "**-*", "--*", "****", "**", "*---", "-*-", "*-**", "--", "-*", "---", "*--*", "--*-", "*-*", "***", "-", "**-", "***-", "*--", "-**-", "-*--", "--**", "*----", "**---", "***--", "****-", "*****", "-****", "--***", "---**", "----*", "-----", "~"]
alphabetEN = ['a',    'b',    'c',   'd',  'e',   'f',   'g',    'h',   'i',   'j',   'k',    'l',   'm',  'n',  'o',    'p',    'q',   'r',   's',  't',  'u',   'v',    'w',    'x',    'y',    'z',    '1',     '2',     '3',     '4',      '5',     '6',     '7',    '8',     '9',     '0',   ' ']
alphabetEN_length = len(alphabetEN) - 1

restart = 'yes'

''' Loop while to restart our program, you can stop this when entered "no" or something else except of "yes" or "1" '''
while restart == 'yes' or restart == '1':

    encrypted = []

    encode_decode_choose = input("You want encode or decode? ")
    if encode_decode_choose == "encode" or encode_decode_choose == "1":

        encoded_word = input("Enter word or sentence for encoding: ")
        ''' Put every letter to lowercase to simplify our work '''
        encoded_word = encoded_word.lower()             
        ''' Convert word to list so we can sort through and modify each element of the list and then we join encoded list in word or sentence '''
        encoded_list = list(encoded_word)
        encoded_list_length = len(encoded_list)

        ''' If programm see sos he immediately change our word for this "***---***" '''
        if(encoded_word == "sos"):
            print("***---***")
        else:
            for j in encoded_word:
                if j in alphabetEN:
                    ''' Checking every letter in our word and changing it with letters from Morse code'''
                    encrypted.append(morse_code[alphabetEN.index(j)])
                else:
                    pass    
            ''' Joining the letters of Morse code into word or sentence '''
            encrypted = ' '.join(encrypted)   
            print(encrypted)

    elif encode_decode_choose == "decode" or encode_decode_choose == "2":

        encoded_word = input("Enter word or sentence for decoding: ")
        ''' Splitting the Morse code letters '''
        encoded_list = encoded_word.split(" ")
        encoded_list_length = len(encoded_list)
        ''' Here we have SOS priority'''
        if(encoded_word == "***---***"):
            print ("sos")
        else:
            for j in range(encoded_list_length):
                if encoded_list[j] in morse_code:
                    try:
                        ''' Checking every letter in our word and changing it with normal letters '''
                        encrypted.append(alphabetEN[morse_code.index(encoded_list[j])])
                    except:
                        pass    
                else:
                    pass    
            ''' Joining the letters of English alphabet into word or sentence '''    
            encrypted = ''.join(encrypted)   
            print(encrypted)
    else:
        pass        
    ''' Asking the user to repeat the program or not '''
    restart = input("Do you want to restart? ")
