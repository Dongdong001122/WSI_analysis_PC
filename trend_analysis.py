import numpy as np
import pandas as pd
import statsmodels.api as sm

x = [[0, 1], [5, 1], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35]]
y = [4, 5, 20, 14, 32, 22, 38, 43]
x, y = np.array(x), np.array(y)

df=pd.read_csv(r"C:\Users\dell\Desktop\Yloutput.csv")
df['trend']=None
for i in range(len(df)):
    y=np.array(df.loc[i,["WSIrate"+str(x) for x in range(2000,2021)]])
    # x=np.array([[1,x] for x in  range(2000,2021)])
    x=np.array(range(2000,2021))
    x=sm.add_constant(x)
    model = sm.OLS(y , x)
    result = model.fit()
    print(result.pvalues)
    try:

        if result.pvalues[1]<0.01:
            if result.params[1]>0:
                trend=2
            else:
                trend=-2
        elif result.pvalues[1]<0.05:
            if result.params[1]>0:
                trend=1
            else:
                trend=-1
        else:
            trend=0
        df['trend'][i]=trend
        print(i,trend)
    except:
        print(i,'failed')
df.to_excel(r"C:\Users\dell\Desktop\Yloutput.xlsx")