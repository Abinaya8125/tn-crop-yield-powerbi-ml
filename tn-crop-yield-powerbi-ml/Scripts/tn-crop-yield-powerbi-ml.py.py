import pandas as pd, numpy as np, sys
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import LeaveOneOut, cross_val_predict
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
src,out=sys.argv[1],sys.argv[2]
df0=pd.read_csv(src)
rain=['sw_monsoon_actual_mm','ne_monsoon_actual_mm','winter_actual_mm','hot_weather_actual_mm']
crops={'Rice':('rice_yield_t_ha','paddy_area_ha','paddy_irrigation_pct'),
 'Groundnut':('groundnut_yield_t_ha','groundnut_area_ha','foodgrains_irrigation_pct'),
 'Maize':('maize_yield_t_ha','maize_area_ha','foodgrains_irrigation_pct')}
P=[];I=[];S=[]
rng=np.random.RandomState(42)
for c,(yc,ac,ic) in crops.items():
    d=df0[df0[yc].notna()&(df0[ac]>=100)].reset_index(drop=True)
    groups={'Rainfall':rain,'Irrigation':[ic],'Crop area':[ac]}
    cols=rain+[ic,ac]; X=d[cols]; y=d[yc]
    m=RandomForestRegressor(300,min_samples_leaf=3,random_state=42)
    p=cross_val_predict(m,X,y,cv=LeaveOneOut())
    base=np.array([y.drop(i).mean() for i in range(len(y))])
    rm=mean_squared_error(y,p)**.5; rb=mean_squared_error(y,base)**.5; r2=r2_score(y,p)
    verdict='Weak model' if r2>=0.15 else 'No useful model'
    S.append(dict(Crop=c,Districts=len(y),RMSE=round(rm,3),MAE=round(mean_absolute_error(y,p),3),R2=round(r2,3),
      BaselineRMSE=round(rb,3),ErrorReductionPct=round((1-rm/rb)*100),Verdict=verdict))
    pr=pd.DataFrame(dict(Crop=c,District=d.District,Actual=y,Predicted=p.round(2)))
    pr['Error']=(pr.Predicted-pr.Actual).round(2); pr['AbsError']=pr.Error.abs(); P.append(pr)
    m.fit(X,y); base_rmse=mean_squared_error(y,m.predict(X))**.5; imp={}
    for g,gc in groups.items():
        inc=[]
        for _ in range(30):
            Xp=X.copy(); idx=rng.permutation(len(X)); Xp[gc]=X[gc].values[idx]
            inc.append(mean_squared_error(y,m.predict(Xp))**.5-base_rmse)
        imp[g]=max(np.mean(inc),0)
    t=sum(imp.values()) or 1
    for g,v in imp.items(): I.append(dict(Crop=c,Group=g,Importance=round(v/t*100)))
pd.concat(P).to_csv(out+'/ml_pred.csv',index=False)
pd.DataFrame(I).to_csv(out+'/ml_imp.csv',index=False)
s=pd.DataFrame(S); s.to_csv(out+'/ml_sum.csv',index=False)
print(s.to_string()); print(pd.DataFrame(I).pivot(index='Crop',columns='Group',values='Importance'))
