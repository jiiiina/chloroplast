import os
import glob

for file in glob.glob('./gene_fasta_prank_bras/*.nex'):
    gene = file.split('/')[2].split('.')[0]
    os.system('java -jar /mnt/c/Users/PJH/Desktop/prottest-3.4.2/prottest-3.4.2.jar -i '+file+' -all-matrices -all-distributions -threads 2 > ./prottest_bras/'+gene+'.txt')
    
    
    