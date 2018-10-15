#TE-B 67

def word_count(str):

    count=dict()
    w=str.split()

    for a in w:

        if a in count:
            
            count[a]=count[a]+1
        else:
            count[a]=1

    return count

str1=input("Enter a string : ")
c=word_count(str1)

print(c)

print('\n Sorted list : ')

for f in sorted(c):

    print(f)


