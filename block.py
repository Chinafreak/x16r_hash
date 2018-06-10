import x16r_hash, os, sys, time, binascii

def gennonce(decnonce):
  hexnonce = str(hex(decnonce)).replace('0x','')
  while len(hexnonce) < 8:
    hexnonce = '0' + hexnonce
  return str(hexnonce)

#doesnt matter what this is, as long as nonce changes
header = ''
while len(header) < 152:
  header = '00' + header

#main
target = "000000ffff000000000000000000000000000000000000000000000000000000"
targetbin = binascii.unhexlify(target)
nonce = 0
while True:
  
  complete_header = str(header) + str(gennonce(nonce))
  hashbin = x16r_hash.getPoWHash(binascii.unhexlify(complete_header))[::-1]

  if hashbin < targetbin:
     print 'block ' + str(binascii.hexlify(hashbin))
     print 'nonce was ' + str(nonce)
     sys.exit(0)

  if (nonce % 4096 == 0):
     print str(nonce)

  nonce += 1

