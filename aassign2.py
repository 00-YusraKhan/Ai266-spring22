#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
test_data_frame = pd.read_csv('C:\Users\MMC\Downloads\test.csv\test.csv');
id_data_frame = test_data_frame[['id']];
id_data_frame.insert(1,"target",0);
id_data_frame['target'] = np.random.rand(700000,1)
print(id_data_frame)
id_data_frame.to_csv('C:\Users\MMC\Downloads\test.csv\ma.csv',index=False);


# In[ ]:




