""";; This buffer is for notes you don't want to save, and for Lisp evaluation.
;; If you want to create a file, visit that file with C-x C-f,
;; then enter the text in that file's own buffer."""
import re, mmap

with open('small_pgn.pgn', 'r+') as f:
  data = mmap.mmap(f.fileno(), 0)
  reg1 = re.search('WhiteElo (.*)', data)
  final_string1 = reg1.group(1)
  reg2 = re.search('BlackElo (.*)', data)
  final_string2 = reg2.group(1)
  reg3 = re.search('Result (.*)', data)
  final_string3 = reg3.group(1)
  
  WhiteElo = int(final_string1[1:-2])
  BlackElo = int(final_string2[1:-2])

  print "%d \n%d" %(WhiteElo, BlackElo) 
  
  if int(final_string3[1]) == 0:
    print 'Black'
  elif int(final_string3[3]) == 2:
    print 'Tie'
  else:
    print "White"
  
f.close()


