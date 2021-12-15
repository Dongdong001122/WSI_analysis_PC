import pymannkendall as mk
import pandas as pd

# Data generation for analysis
data = list(range(360))
df=pd.read_csv(r"C:\Users\dell\Desktop\Yloutput.csv")
df_trend=pd.DataFrame(columns=['GDBDID'])
for i in range(len(df)):
    try:
        WSI=df.loc[i,["WSIrate"+str(year) for year in range(2000,2021)]]
        GDBDID=df.GDBD_ID[i]
        trend, h, p, z, Tau, s, var_s, slope, intercept=result = mk.original_test(WSI)
        # trend_dict={'GDBD_ID':GDBDID,'trend':trend,'h':h,'p':p,'Tau':Tau,'s':s,'var_s':var_s,'slope':slope,'intercept':intercept}
        # df_trend.append(trend_dict,ignore_index=False)
        df.loc[i,['trend','h','p','z','Tau','s','var_s','slope']]=[trend, h, p, z, Tau, s, var_s, slope]
        print(WSI)
        print(result.trend)
        print(result)
    except:
        pass
# show(df_trend)
'''
    trend: tells the trend (increasing, decreasing or no trend)
    h: True (if trend is present) or False (if the trend is absence)
    p: p-value of the significance test
    z: normalized test statistics
    Tau: Kendall Tau
    s: Mann-Kendal's score
    var_s: Variance S
    slope: Theil-Sen estimator/slope
    intercept: intercept of Kendall-Theil Robust Line, for seasonal test, full period cycle consider as unit time step
'''