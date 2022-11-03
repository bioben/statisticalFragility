#!/usr/bin/env python
# coding: utf-8

# In[19]:


import scipy.stats as stats
import pandas as pd
import math


# ### Data import and number crunching

# In[33]:


#import sample df;
sampleData = pd.read_csv('sampleData.csv');


# In[34]:


sampleData


# In[35]:


#add information!!

#find total number of participants
only2x2TableData = sampleData[['a', 'b', 'c', 'd']];
sumAcrossRows = only2x2TableData.sum(axis = 1);
sampleData['totalPop'] = sumAcrossRows;

sampleData


# In[36]:


#given abcd values, what is the p-value using fishers test?
def myFishersTestFunction(abcdDataRow):
    indivTable = abcdDataRow.values
    organizedTable = [
        [indivTable[0], indivTable[1]],
        [indivTable[2], indivTable[3]]
    ]
    [oddsRatio, pValue] = stats.fisher_exact(organizedTable)

    return pValue


# In[37]:


#determine p-value from Fisher's Exact Test
only2x2TableData = sampleData[['a', 'b', 'c', 'd']];

myPValuesOriginal = []

for index, rows in only2x2TableData.iterrows():
    pValue = myFishersTestFunction(only2x2TableData.iloc[index])
    myPValuesOriginal.append(pValue)
    
sampleData['pValuesOriginal'] = myPValuesOriginal


# In[38]:


sampleData


# In[39]:


#find the fragility index and fragility quotient
only2x2TableData = sampleData[['a', 'b', 'c', 'd']];

myFIValues = []
newPValues = []

for index, rows in only2x2TableData.iterrows():
    currentStudy = only2x2TableData.iloc[index]
    pValue = myFishersTestFunction(currentStudy)
    
    counter = 0
    # is the pValue insig?
    while (pValue < 0.05):
        currentStudy['a'] = currentStudy['a'] + 1
        currentStudy['b'] = currentStudy['b'] - 1
        counter = counter + 1
        pValue = myFishersTestFunction(currentStudy)
        
    myFIValues.append(counter)
    newPValues.append(pValue)


# In[40]:


myFIValues


# In[41]:


#add these new FI and p values to main table
sampleData['FI'] = myFIValues;
sampleData['FQ'] = sampleData['FI'] / sampleData['totalPop']
sampleData['newPValue'] = newPValues;


# In[42]:


sampleData


# ### Descriptive Stats

# In[1]:


import matplotlib as plt


# ### Multivariate Stats

# In[ ]:




