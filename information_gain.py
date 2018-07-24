import pandas as pd
import numpy as np
import scipy.stats
from math import log10


'''
reference-
Machine Learning in Automated Text Categorization-FABRIZIO SEBASTIANI

http://nmis.isti.cnr.it/sebastiani/Publications/ACMCS02.pdf

'''

dataset = pd.read_csv('merged_data_maline.csv')


#####creating the contingency table

n=len(dataset.columns)  #no of columns

X=dataset.iloc[:,1:n].values

l=len(X) #no or rows


score = []

for i in range(n-1):
    #print(i)
    
    X_column=X[:,i]
    neg_array,pos_array=np.hsplit(X_column,2)
    #print(pos_array.size)
    a=np.count_nonzero(pos_array)
    b=np.count_nonzero(neg_array)
    c= l/2-a
    d= l/2-b
    M=a+b
    tmp=0
    #temp_score=a*l
    #score.append(temp_score)
    list = [a,b,c,d]
    print(a,b,c,d)
    tmp1 = 0
    tmp2 = 0
    tmp3 = 0
    tmp4 = 0
    
    '''
    for i in list:
    
        if i==0:
            tmp= 0
            
        else:
            tmp += i*log((i/(M*n)))
            
     '''
    if a==0:
     
        tmp1 = 0
    else :
        tmp1= a*log(a/((a+b)*(a+c)))
        
    if b==0:
     
        tmp2 = 0
    else :
        tmp2= b*log(b/((a+b)*(b+d))) 

    if c==0:
     
        tmp3 = 0
    else :
        tmp3= c*log(c/((c+d)*(a+c)))

    if d==0:
     
        tmp4 = 0
    else :
    
        tmp4= d*log(d/((c+d)*(b+d)))        
        

      
    tmp = tmp1 + tmp2 + tmp3 + tmp4
    #print(((a*l)/((a+c)*(a+b))))
    
    
    score.append(tmp)
    
    '''
    if temp_score < 0.05:
        pscore.append(0)
    else:       
        pscore.append(temp_score)
    '''
    
    
np.savetxt("information_gain.csv",score, delimiter=",") 

##########################################################

dataset = pd.read_csv('merged_data_maline.csv') 

score = []

#Y = dataset['class']

#print(dataset)


###list =[(t,c) ,(t,c0),(t0,c),(t0,c0)]  ##representation of the combination of (t,c)
l=4289+8369 #152 is the number of files in malign and 1394 benign(change according to your files)


def information_gain(a,b,c,n):
    """Returns mutual_info(t,c) = log(A*N/((A+C)*(A+B)))"""
    if a == 0: 
        return 0
    print(a,b,c,n)    
    return log10((a * n) / ((a + c) * (a + b)))

for index, row in dataset.iterrows():
    a = row['file_frequency_M']
    b = row['file_frequency_B']
    c = 4289 - a   #change number of files malign     
    d = 8369 - b  #change number of files benign 

    tmp1 = mutual_info(a,b,c,l)
    tmp2 = mutual_info(b,a,d,l)
    tmp3 = mutual_info(c,d,a,l)
    tmp4 = mutual_info(d,c,b,l)
    temp_score = tmp1+tmp2+tmp3+tmp4
    score.append(temp_score)

np.savetxt("mutual_info.csv", score, delimiter=",")       
"""
#print(X)

#####creating the contingency table

n=len(dataset.columns)

X=dataset.iloc[:,1:n].values

l=len(X)



score = []

for i in range(n-1):
    
    X_column=X[:,i]
    neg_array,pos_array=np.hsplit(X_column,2)
    #df1 = df[df['Sales'] >= s]
    #print(pos_array.size)
    a=np.count_nonzero(pos_array)
    b=np.count_nonzero(neg_array)
    c= l/2-a
    d= l/2-b
    temp_score=0
    
    #temp_score=a*l
    #score.append(temp_score)
    
    if a==0:
        temp_score=0
    else:
        
        temp_score =  log10(((a*l)/(a+c)*(a+b)))
    #print(((a*l)/((a+c)*(a+b))))
    
    
    score.append(temp_score)
    
    
    if temp_score < 0.05:
        pscore.append(0)
    else:       
        pscore.append(temp_score)
    
    
    
np.savetxt("mutual_info2.csv",score, delimiter=",") 
    

"""    
    
    
   
    
    
    



    

    
    
    
    
    
    
    


