'''
import sys,os   
uniprotFile=open("UNIPROT-data.txt") #read original alignment file  
uniprotFileContent=uniprotFile.read() 
uniprotFileList=uniprotFileContent.split("//")
for items in uniprotFileList:
        seqInfoFile=open('%s.dat'%items[5:14],'w')
        seqInfoFile.write(str(items))



import re
myre = re.compile("(?<!:)//")
uniprotFileList = myre.split(uniprotFileContent)



import sys,os   
small_pgn=open("small_pgn.pgn") #read original alignment file  
pgn_content=small_pgn.read() 
pgn_list=pgn_content.split("\n\n")
for small_file in pgn_list:
        seqInfoFile=open('%s.dat'%items[5:14],'w')
        seqInfoFile.write(str(small_file))

import re
myre = re.compile("\n\n")
pgn_list = myre.split(pgn_content)
'''


import sys,os
import re
small_pgn=open("MagnusCarlsen.pgn") #read original alignment file  
pgn_content=small_pgn.read() 
myre = re.compile("\r\n\r\n\r\n")
pgn_list = myre.split(pgn_content)
i = 0
for small_file in pgn_list:
        name = str(i) + ".pgn"
        f = open(name, 'w')
        f.write(small_file)
        f.close()
        i += 1
        '''seqInfoFile=open('%s.dat'%small_file[5:14],'w')
        seqInfoFile.write(str(small_file))'''
