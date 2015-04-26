""";; This buffer is for notes you don't want to save, and for Lisp evaluation.
;; If you want to create a file, visit that file with C-x C-f,
;; then enter the text in that file's own buffer."""
import re, mmap
#opens the file to read 
with open('small_pgn.pgn', 'r+') as f:
  data = mmap.mmap(f.fileno(), 0)
  #searches for the specified string combination 
  reg1 = re.search('WhiteElo (.*)', data)
  #grabs the string right after the flag and stores it in a variable
  final_string1 = reg1.group(1)
  reg2 = re.search('BlackElo (.*)', data)
  final_string2 = reg2.group(1)
  reg3 = re.search('Result (.*)', data)
  final_string3 = reg3.group(1)
  
  #strips the quotation marks and ending bracket and returns an int
  WhiteElo = int(final_string1[1:-3])
  BlackElo = int(final_string2[1:-3])
 
  #displays Elo
  print "%d \n%d" %(WhiteElo, BlackElo) 
  
  #displays who won the game
  if int(final_string3[1]) == 0:
    print 'Black'
  elif int(final_string3[3]) == 2:
    print 'Tie'
  else:
    print "White"
  
f.close()


