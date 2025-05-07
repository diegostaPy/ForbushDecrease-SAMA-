import ARLreader as Ar
import datetime
import numpy as np
import pandas as pd
import os.path
from os import path
from ftplib import FTP
import datetime
#first period
start=[datetime.datetime(2024, 5, 6),datetime.datetime(2024, 9, 16)]
end=[datetime.datetime(2024, 6, 24, 23, 59),datetime.datetime(2024, 10, 31, 23, 59)]
folder=['first_period','second_period']
for dt,end in zip(start,end,folder):
    step = datetime.timedelta(hours=3)
    dates= []
    while dt <= end:
        dates.append(dt)
        dt += step
    months = {1: 'jan', 2: 'feb', 3: 'mar', 4:'apr', 5:'may', 6:'jun',
                7: 'jul', 8:'aug', 9:'sep', 10:'oct', 11:'nov', 12:'dec'}
    year='24'
    weeks=['w1','w2','w3', 'w4', 'w5']
    pos=( -25.331391,-57.516497)
    Tg=[]
    Pg=[]
    Hg=[]
    Tt=[]
    Pp=[]
    Hh=[]
    for date in dates:
        m = str(months[date.month])
        y = str(date.year)[2:4]
        if (date.day < 8):
            w='w1'
        elif (date.day < 15):
            w='w2'
        elif (date.day < 22):
            w='w3'
        elif (date.day < 29):
            w='w4'
        else:
            w='w5'
        filename= 'gdas1.'+m+y+'.'+w
        profile, sfcdata, indexinfo, ind = Ar.reader('datos/'+filename).load_profile(date.day, date.hour, pos,sfc=True, flag_interp=True)


        T=profile['TEMP']#- 273.15
        P=profile['PRSS']
        H=profile['HGTS']
        Ts=sfcdata['TMPS']
        Ps=sfcdata['PRSS']
        Tg.append(Ts)
        Pg.append(Ps)

        Tt.append(T)
        Hh.append(H)
        Pp.append(P)
    # Convertir perfiles a columnas expandidas
    T_cols = pd.DataFrame(Tt, columns=[f"T_{i}" for i in range(23)])
    P_cols = pd.DataFrame(Pp, columns=[f"P_{i}" for i in range(23)])
    H_cols = pd.DataFrame(Hh, columns=[f"H_{i}" for i in range(23)])

    # Crear DataFrame final
    df = pd.concat([
        pd.DataFrame({'timestamp': dates, 'Ts': Tg, 'Ps': Pg}),
        T_cols, P_cols, H_cols
    ], axis=1)

    # Guardar en CSV (legible por humanos, pero más pesado)
    df.to_csv("data/"+folder+"profileweather.csv", index=False)
