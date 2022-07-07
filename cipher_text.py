def encrypt(text,dataset,sugar):
   e_text = ''
   for i in range (len(text)):
      index = dataset.index(text[i]) + sugar
      
      if index > len(dataset):
         indexShift = index % len(dataset)
      else:
         indexShift = index

      e_text += dataset[indexShift]
   return e_text

def decrypt(text,dataset,sugar):
   c_text = ''
   for i in range (len(text)):

      indexShift = dataset.index(text[i]) - sugar
      c_text += dataset[indexShift]

   return c_text

def cipher(text,dataset,sugar):
   predict_text = ''
   for j in range(len(dataset)):
      predict_text = decrypt(text, dataset,j)
      print(predict_text)

choice = input("choose anyone (e) encrypt, (d) decrypt, (c) cipher ")
text = input("enter the text : ")
dataset = 'abcdefghijklmnopqrstuvwxyz'
sugar = 7

if choice == 'e' :
   choice = encrypt(text, dataset, sugar)
elif choice == 'd':
   choice = decrypt(text, dataset, sugar)
elif choice == 'c' :
   cipher(text, dataset, sugar)

print(choice)