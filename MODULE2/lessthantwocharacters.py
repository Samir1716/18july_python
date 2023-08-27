input=input("Enter Your Character:")
n=int

if input in ('a','A','E','e','I','i','O','o','u','U'):
    print("Vowel....")
elif input not in ('a','A','E','e','I','i','O','o','u','U') and input!=n  and len(input)<1:
    print("Constant.....")
elif len(input)>1:
    print("Error....")
else:
    print("Write Valid Input.!!!!")