import datetime
import numpy as np
import pandas as pd
import os.path
import os
from os import path, stat
from ftplib import FTP


# In[ ]:





# In[ ]:


years=['23']
#years=['10', '11', '12', '13', '14', '15','16', '17', '18', '19']
months = ['jan','feb','mar',  'apr',  'may', 'jun',
              'jul',  'aug', 'sep', 'oct', 'nov', 'dec']
#months=['apr','may',]
weeks=['w1','w2','w3','w4','w5']
for y in years:
    for m in months:
        for w in weeks:
            filename= 'gdas1.'+m+y+'.'+w
            print(filename)
            if(not(path.exists('datos/'+filename))):
                ftp = FTP('arlftp.arlhq.noaa.gov')
                ftp.login()
                ftp.cwd('/pub/archives/gdas1')
                try:
                    with open('datos/'+filename, 'wb') as fp:
                        ftp.retrbinary('RETR '+filename, fp.write)
                    ftp.quit()
                except:
                    pass
                ftp.close()
            elif (path.exists('datos/'+filename)):
                if (w!='w5' and stat('datos/'+filename).st_size<598888640):
                    print('Archivo '+ filename + ' incompleto')
                    os.remove('datos/'+filename)
                    ftp = FTP('arlftp.arlhq.noaa.gov')
                    ftp.login()
                    ftp.cwd('/pub/archives/gdas1')
                    try:
                        with open('datos/'+filename, 'wb') as fp:
                            ftp.retrbinary('RETR '+filename, fp.write)
                        ftp.quit()
                    except:
                        pass
                    ftp.close()

                elif (w=='w5'):
                    if(m=='jan' and stat('datos/'+filename).st_size<256666560):
                        print('Archivo '+ filename + ' incompleto')
                        os.remove('datos/'+filename)
                        ftp = FTP('arlftp.arlhq.noaa.gov')
                        ftp.login()
                        ftp.cwd('/pub/archives/gdas1')
                        try:
                            with open('datos/'+filename, 'wb') as fp:
                                ftp.retrbinary('RETR '+filename, fp.write)
                            ftp.quit()
                        except:
                            pass
                        ftp.close()
                    if(m=='feb' and (stat('datos/'+filename).st_size<256666560)):
                        print('Archivo '+ filename + ' incompleto')
                        os.remove('datos/'+filename)
                        ftp = FTP('arlftp.arlhq.noaa.gov')
                        ftp.login()
                        ftp.cwd('/pub/archives/gdas1')
                        try:
                            with open('datos/'+filename, 'wb') as fp:
                                ftp.retrbinary('RETR '+filename, fp.write)
                            ftp.quit()
                        except:
                            pass
                        ftp.close()


# In[ ]:





# In[ ]:


