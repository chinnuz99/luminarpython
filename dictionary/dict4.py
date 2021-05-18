#enter hello hi hello
#{'hello':2,'hi'1}
dict={}                            #creating an empty dictionary
a=input("enter entry")             #entering the string "hello hi hello"
words=a.split(" ")                 #splitting the string with spaces,i.e hello, hi ,hello
for word in words:                 #iterating each element in a word
    if word not in dict:           #comparing each element with the empty dictionary, if the element
        dict.update({word:1})      #update the dictionary with the key(element) and value(count)
    else:                          #if the word is present ,[in cases where same elements are repeating]
        val=int(dict[word])        #val=the value of the key in the dictionary,i.e here value of word=1
        val+=1                     #if present increment the value by 1
        dict.update({word:val})    #updating/adding new key and value to the dictionary
print(dict)                        #printing new dictionary
