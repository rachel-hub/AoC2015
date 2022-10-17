import hashlib

input_text = "ckczppom"

hash_start = ""
k = 0
while hash_start != "00000":
    a = input_text + str(k)
    hash_start = hashlib.md5(a.encode("latin1")).hexdigest()[0:5]
    k += 1
    if k % 1000 == 0:
        print(k, hash_start)

print(k - 1)

hash_start = ""
k = 0
while hash_start != "000000":
    a = input_text + str(k)
    hash_start = hashlib.md5(a.encode("latin1")).hexdigest()[0:6]
    k += 1
    if k % 1000 == 0:
        print(k, hash_start)

print(k - 1)
