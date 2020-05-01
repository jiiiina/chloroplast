import os
import glob

for fastafile in glob.glob('./gene_fasta/*.fasta'):
    name = fastafile.split('/')[2].split('.')[0]
    os.system('prank -d='+fastafile+' -o=./gene_fasta_prank/'+name+'.nexus -f=nexus')
    
    
    