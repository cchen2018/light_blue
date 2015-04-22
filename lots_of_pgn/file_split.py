import sys,os
import re
small_pgn=open("WesleySo.pgn") #read original alignment file  
pgn_content=small_pgn.read() 
myre = re.compile("\r\n\r\n\r\n")
pgn_list = myre.split(pgn_content)
i = 15791
for small_file in pgn_list:
        name = str(i) + ".pgn"
        f = open(name, 'w')
        f.write(small_file)
        f.close()
        i += 1

