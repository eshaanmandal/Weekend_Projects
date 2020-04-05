morse_code={                                  'A':'.-', 'B':'-...', 
					'C':'-.-.', 'D':'-..', 'E':'.', 
					'F':'..-.', 'G':'--.', 'H':'....', 
					'I':'..', 'J':'.---', 'K':'-.-', 
					'L':'.-..', 'M':'--', 'N':'-.', 
					'O':'---', 'P':'.--.', 'Q':'--.-', 
					'R':'.-.', 'S':'...', 'T':'-', 
					'U':'..-', 'V':'...-', 'W':'.--', 
					'X':'-..-', 'Y':'-.--', 'Z':'--..', 
					'1':'.----', '2':'..---', '3':'...--', 
					'4':'....-', '5':'.....', '6':'-....', 
					'7':'--...', '8':'---..', '9':'----.', 
					'0':'-----', ', ':'--..--', '.':'.-.-.-', 
					'?':'..--..', '/':'-..-.', '-':'-....-', 
					'(':'-.--.', ')':'-.--.-'}

def decoder(code):
     code+=' '
     decipher = '' 
     citext = ''

     for letter in code:
          if letter != ' ':
               i=0
               citext +=letter
          else:
               i+=1
               if i==2:
                    decipher+=' '
               else:
                    decipher+=list(morse_code.keys())[list(morse_code.values()).index(citext)]
                    citext=''
     
     return decipher






def main():
     code=input('Enter morse code ')
     ans=decoder(code)
     print(ans)



if __name__ =="__main__":
     main()
