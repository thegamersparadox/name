import os


print ('Hello, welcome to your phonebook.')

print('please inform me of your directory.')

directory = input()

isDir='true'

while isDir == "true":

  if os.path.isdir(directory):
    print ('what file would you like to save this to?')
    file = input()
    
    print ('what is the name?')
    name= input('')
    print ('what is the address?')
    address= input('')
    print ('what is the phone number?')
    number= input('')
  
    info= ((name), (address), (number))
  
    
    filename = ((directory)+'/'+(file))
  
    with open(filename, 'w') as file_object:
      file_object.write (str(info))
  
    with open (filename, 'r') as file_object:
      phonebook=file_object.read()
      print ('your phonebook contains', phonebook)
      print()

    print ('would you like to add another? (y/n)')
    again=input()
    print()
    if again == 'n':
      isDir ="false"
      print ('Thank you for using your phonebook, Goodbye.')
  else:
    isDir='false'
    print ('plese use a valid directory')
