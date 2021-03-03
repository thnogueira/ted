# -*- coding: utf-8 -*-
# This code is used to cross all data extracted from 'instabot' in one matrix to create a relation between all extracted profiles. The purpose of doing this crossing is to verify the amount of mutual followers between two profiles or more.
"""
Created on Sun Jan 24 12:01:52 2021

@author: Thadeu Nogueira
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import os

import time
start_time = time.time()



# -------------------- listing your directory -----------------
path = r'input your path here'


arquivos = {'File': ['n']
             }
arq = pd.DataFrame(arquivos, columns = ['File'])

# read the entries

with os.scandir(path) as listOfEntries:
        for entry in listOfEntries:
        # print all entries that are files
            if entry.is_file():
                y = entry.name
                arq2 = pd.DataFrame({'File': [y]})
                arq = arq.append(arq2, ignore_index = True)
        

arq = arq.drop([0], axis = 0)
end_time = time.time() - start_time
print("arquivos:", end_time)
#----------------------------------------------------------
# -------------------- importing csv ---------------------

dados = {'Profile': ['n'],
             'Follower': ['n']
             }

#criação bd novo
df = pd.DataFrame(dados, columns = ['Profile', 'Follower'])
df1 = pd.DataFrame(dados, columns = ['Profile', 'Follower'])

a=0
b = len(arq)
k = 0
h = {}
p = {}
bdj = pd.DataFrame(p, columns = ['Profiles'])

while a < b:
    ori = arq['File'].values[a]
    a= a + 1
    final_path = r'input your final path here'.format(ori)
    
#--------------importing csv
    base123 = pd.read_csv(final_path, encoding = 'latin-1')

#--------- variable to serach for y
    z = 0

#---------- loop variables
    s = 1
    m = len(base123)

#------------------- removing '.csv' and creating more variables    
    ori = ori.replace('.csv','')
    x = ori
    key = k
    h[key] = ori
    k = k + 1

    
    bdj2 = pd.DataFrame({'Profiles': [ori]})
    bdj = bdj.append(bdj2, ignore_index = True)
    

#----------------------- loop to add itens
    while s < m:
        #---------- finding values
        y = base123['username'].values[z]
        #---------- creating lines and creating df2
        df2 = pd.DataFrame({'Profile': [x], 'Follower': [y]})
        df = df.append(df2, ignore_index=True)
        df1 = df1.append(df2, ignore_index=True)
        s = s + 1
        z = z + 1

end_time = time.time() - start_time
print("bases", end_time)


#--------------------- create df to guide matrix
dados2 = {}
#--------------------- the number of 'h[x]' are equal to the number of profiles extracted minus one. In this example, I used 36 profiles
df3 = pd.DataFrame(dados2, columns = [h[0], h[1], h[2], h[3], h[4], h[5], h[6], h[7], h[8], h[9], h[10], h[11], h[12], h[13], h[14], h[15], h[16], h[17], h[18], h[19], h[20], h[21], h[22], h[23], h[24], h[25], h[26], h[27], h[28], h[29], h[30], h[31],h[32],h[33],h[34],h[35]])
base_f = pd.concat([df1,df3], axis = 0)

#--------------------- joining data
base_f.insert(2, "Join", base_f["Profile"] + base_f["Follower"])
print(base_f)


#--------------------- crossing
for i, cc in df.iterrows():
    t = base_f["Profile"].values[i]
    r = base_f["Follower"].values[i]
    o = base_f["Join"].values[i]
    bdl = len(bdj)
    j = 0
    while j < bdl:
        bdk = bdj['Profiles'].values[j]
        cc1 = base_f[base_f['Join']== bdk + r]['Profile']
        if bdk == t:
            base_f.loc[i, bdk] = 0
        elif cc1.empty == True:
            base_f.loc[i,bdk] = 0
        else:
            base_f.loc[i,bdk] = 1
        j = j + 1   


print(base_f)
#-------------------- removing first lines
df = df.drop([0], axis = 0)
df1 = df1.drop([0], axis = 0)
base_f = base_f.drop([0], axis = 0)
df.to_csv(r'final path', index = False)
base_f.to_csv(r'final ath for crossing', index = False)
print(df)
print(df1)

end_time = time.time() - start_time
print("--- %s seconds ---" % end_time)
