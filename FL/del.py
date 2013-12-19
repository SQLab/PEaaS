

import os
import time
import datetime

def checktime(yourpath):
	pathlist=os.listdir(yourpath)
	#print(pathlist);
	#extlist=['zip','7z','csv','txt','jpg','rar','jpeg','log']
	for i in range(len(pathlist)):
		source=yourpath+pathlist[i]
		m=time.localtime(os.stat(source).st_ctime)
		startime=datetime.datetime.now()
		endtime=datetime.datetime(m.tm_year,m.tm_mon,m.tm_mday,m.tm_hour,m.tm_min,m.tm_sec)
		mydays=(startime-endtime).days
		mysecs=(startime-endtime).seconds
		ext=os.path.splitext(source)[1][1:].lower()
		#print(source,mydays)
		if mydays>=7 and ext!='py':
			#7 days
			#if ext!='':os.remove(source)
			#else : os.rmdir(source) 
			os.system('rm -rf %s'%source)
			print ('remove',source)
				

if __name__ == '__main__': 
    try: 
        checktime('/home/coding/FL/ucodes/')   
        checktime('/home/coding/FL/ufiles/')
    except Exception as se: 
        print (str(se));
