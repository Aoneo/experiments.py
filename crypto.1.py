clear = "RIQSRQUEZWLIQZWLBDARQLCNLERCBNQQGQCNLIBSTBSWRWNLIWLLIQELIQCYQCESKSUQCALWSUAQGQCNLISJWPRWNARCBLQDPQWSWSUWPRWNAHQDWCQTYPRBLINEKCWCBLIZQLBD"
key = 5

def encrypt(letter, key):
    "Κρυπτογραφεί ένα γράμμα letter με κλειδί key, έναν αριθμό από 0 έως 127"
    return chr( (ord(letter)+key) % 128 )

def decrypt(encletter, key):
    "Αποκρυπτογραφεί ένα γράμμα letter με κλειδί key, έναν αριθμό από 0 έως 127"
    return chr( (ord(encletter)-key) % 128 )

enc = ""
for x in clear:
    y = encrypt(x, key)
    enc += y

print ("The encrypted text is [{e}], with key={k}".format(e=enc, k=key))

decr = ""
for x in enc:
    decr += decrypt(x, key)

print ("The decrypted text is [{e}], with key={k}".format(e=decr, k=key))

s = "RIQSRQUEZWLIQZWLBDARQLCNLERCBNQQGQCNLIBSTBSWRWNLIWLLIQELIQCYQCESKSUQCALWSUAQGQCNLISJWPRWNARCBLQDPQWSWSUWPRWNAHQDWCQTYPRBLINEKCWCBLIZQLBD"
def decode(s):
    ab=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in s:
        newname = ""
        for k in ab:
            newname+=
