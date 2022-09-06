import random
import string
length=int(input('Enter the length of Password:'))
all=string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
temp=random.sample(all,length)

password="".join(temp)
print(f'Password is:{password}')