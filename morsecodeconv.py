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
def convert_to_morse(script):
     op = ''
     for a in script:
          if a !=' ':
               op+=morse_code[a]
               op+=' ' 
          elif a== ' ':
               op+='  '
     return op


'''def morse_to_normal(output):
     output+= ' '
     decipher = '' 
     citext = ''
     for letter in output:
          if (letter != ' '):
               i=0
               citext += letter
          else:
               i+=1
               if i==2:
                    decipher+=' '
               else:
                    decipher+=list(morse_code.keys())[list(morse_code.values()).index(citext)]
                    citext=''
     return decipher
'''               
def main():
     script = input('Enter the string :').upper()
     output=convert_to_morse(script)
     print(output)
 #    answer=morse_to_normal(output)
  #   print(answer)

if __name__=="__main__":
     main()

