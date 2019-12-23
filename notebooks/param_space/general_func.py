import numpy as np

def read_my_npy_all(pth, name, pref):
    a = np.load(pth+pref[0]+name)[0]
    
    for i in range(1,len(pref)):
        try:
            b = np.load(pth+pref[i]+name)[0]
            for k in a.keys():
                a[k] = np.concatenate((a[k],b[k]))
        except:
            print 'file', pref[i]+name, 'doesn`t exists '
            
    return a

def read_my_npy(pth, name, pref):
    a = {'dis':[],'cc':[], 'nc':[],'neu':[],'hitnuc':[],'A':[],'hitqrk':[],
         'Ev':[], 'x':[],'y':[], 'Q2':[], 'W':[], 
         'xsec':[], 'sea':[], 'neut_code':[], 'nik0':[], 'niother':[], 'charm':[]}
    for i in range(len(pref)):
        try:
            b = np.load(pth+pref[i]+name)[0]
            for k in a.keys():
                a[k] = np.concatenate((a[k],b[k]))
        except:
            print 'file', pref[i]+name, 'doesn`t exists '
            
    return a

