#
import inflect     #importing inflect library which convert word to no.
p=inflect.engine() #define a object for it

def convert_str(text): #define a function for convertion
  temp=text.split()  #split a text and store it in temp
  new_string=[] #create a empty string to store
  for word in temp: #traverse a word one by one
    if word.isdigit():  # if it found to be a number then convert it to word using inflect
      temp=p.number_to_words(word)
      new_string.append(temp) #then append the converted word in temp to new string array
    else:
      new_string.append(word) #if no number is found then just append the word in new string
  temp=' '.join(new_string) #just join the string and store in temp
  return temp
  
#main function
input_str=input('Enter the String:') #input the string
convert_str(input_str) #call the function
    

