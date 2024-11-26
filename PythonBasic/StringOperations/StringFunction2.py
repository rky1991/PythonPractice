#isalpha()
#isdigit()
#isalnum()

s="Welcome"

print(s.isalpha()) #true , space or special char present it will give false
print(s.isdigit()) #false
print(s.isalnum()) #True

s="Welcome123"
print(s.isalpha()) #false
print(s.isdigit()) #false
print(s.isalnum()) #True

s="12345"
print(s.isalpha()) #false
print(s.isdigit()) #True
print(s.isalnum()) #True

s="Welcome123@#$"
print(s.isalpha()) #false
print(s.isdigit()) #false
print(s.isalnum()) #false

