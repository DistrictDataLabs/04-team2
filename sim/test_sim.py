
from similarity import file_text_similarity,text_similarity

arrays = [['sample0.txt','sample0.txt'],
          ['sample0.txt','sample1.txt'],
          ['similarity.py','sample1.txt'],
          ['similarity.py','sample0.txt','sample1.txt']
         ]


# test with text comparison
print 'similarity of file names'
for array in arrays:
    sim_score = text_similarity(array)
    print 'input:',array,'similarity:',sim_score
    
#test as file names
print 'similarity of file contents'
for array in arrays:
    sim_score = file_text_similarity(array)
    print 'input:',array,'similarity:',sim_score