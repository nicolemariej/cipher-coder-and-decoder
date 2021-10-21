plainText = input("Type your word here: ")
distance = int(input("Enter a distance here: "))
code = ""
aValue = ord('a')
zValue = ord('z')

for ch in plainText:
    ordValue = ord(ch)
    cipherValue = ordValue + distance

    if cipherValue > zValue:
        cipherValue = aValue + (cipherValue - ord('z') - 1)
    code += chr(cipherValue)
print("Ciphertext: " + code)
