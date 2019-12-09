choice = int(input("Choose 1 or 2: "))
while choice != 1 or 2:
    if choice==1:
      text = input('Text: ')
      d = dict()
      for i in text:
          if i.isalpha():
            if i not in d:d[i] = 1
            else:
                d[i] += 1
      print (d)

    if choice==2:
         text = input('Text: ')
         words = sorted(set(text.split()))

         for word in words:
            print(word)



    choice = int(input("Choose 1 or 2: "))
