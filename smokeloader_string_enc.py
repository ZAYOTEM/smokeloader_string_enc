def ROL(data, shift, size=32):
    shift %= size
    remains = data >> (size - shift)
    body = (data << shift) - (remains << size )
    return (body + remains)

def encoder(nname):
    key = 0
    for i in nname:
        buyuk = ord(i) & 0xdf
        result = buyuk ^ key
        aa = ROL(result,8)
        key = aa + buyuk
    return hex(key ^ 0x15C08A54)[2:] 