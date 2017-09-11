"""Simple script for converting short string into a longer"""
org = "Ala ma kota, kot ma 4nogi."
new = "Arek lubi psy, a najbardziej boksery!"


print(org)
print(new)

print(len(org))
print(len(new))



x = 0
while x < len(new):
    if x < len(org):
        old_char = ord(org[x])
        new_char = ord(new[x])
        if old_char > new_char:
            finnal_char = old_char - (old_char - new_char)
            print(chr(finnal_char), end="")
        elif old_char < new_char:
            finnal_char = old_char + (new_char - old_char)
            print(chr(finnal_char), end="")
        else:
            print(org[x], end="")
    else:
        old_char_from_begining = ord(org[x-len(org)])
        new_char = ord(new[x])
        if old_char_from_begining > new_char:
            finnal_char = old_char_from_begining - (old_char_from_begining - new_char)
            print(chr(finnal_char), end="")
        elif old_char_from_begining < new_char:
            finnal_char = old_char_from_begining + (new_char - old_char_from_begining)
            print(chr(finnal_char), end="")
        else:
            print(old_char_from_begining, end="")


    x += 1

