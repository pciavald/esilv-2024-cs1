import sys

def usage():
  print('python3 cyprher.py [cyper|decipher] key message')

if (len(sys.argv) != 4):
  usage()
  sys.exit(0)

if (sys.argv[1] == "cypher"):
  key = int(sys.argv[2]) % 26
elif (sys.argv[1] == "decypher"):
  key = -(int(sys.argv[2]) % 26)
else:
  print(f"commande non supportee: {sys.argv[1]}")
  usage()
  sys.exit(0)

response = ''
for current_character in sys.argv[3]:
  dec = ord(current_character) + key
  if (dec > ord('z')):
    dec -= 26
  elif (dec < ord('a')):
    dec += 26
  response += chr(dec)

print(response)
