#!/usr/local/bin/python3.3
import os,subprocess,time,sys,random
#需要檔案或資訊：usercode,problemID,problemInput,problemOutput
#file_name=input() #usercode
#file_ID=10400
#file_ID=input()
os.system('python3.3 /home/coding/FL/del.py')
abpath='/home/coding/FL'
file_name=sys.argv[1]
file_ID=int(sys.argv[2]) #problemID
timelimit=5
testround=6
totalline = 0
D=1
Nus=[0]
Ncs=[0]
Nuf=[0]
Ncf=[0]
result=[0]
resultt=[0]
resulttt=[0]
wrong_answer=[]
f = open(abpath+'/ucodes/'+ file_name, 'r')
while True :
    line = f.readline()
    if line=='': break
    totalline+=1
    Nus.append(0)
    Ncs.append(0)
    Nuf.append(0)
    Ncf.append(0)
    result.append(0)
    resultt.append(0)
    resulttt.append(0)
f.close()

pathlist=os.listdir(abpath+'/problemIO/'+sys.argv[2])
promaxlen=len(pathlist)/2
problemlist=[]

name=os.path.splitext(file_name)
#path=os.getcwd()
os.system('mkdir %s/ufiles'%abpath)
os.system('chmod 1777 %s/ufiles'%abpath)
os.chdir(abpath+'/ufiles')
os.system('mkdir %s'%name[0])
os.system('chmod 1777 %s'%name[0])
os.system('cp -p ../ucodes/%s %s'%(file_name,name[0]))
os.chdir(abpath+'/ufiles/'+name[0])

#print('開始跑user code...')
for i in range(1,testround):
    ###
    ###  STEP 1 跑USER的CODE並用GCOV指令來產生GCOV檔
    ###
    #compile with gcov
    whilelimit=0
    while True:
        pronum=random.randint(1,promaxlen)
        if pronum not in problemlist:
            problemlist.append(pronum)
            break
        whilelimit+=1
        if whilelimit==1000: 
            problemlist.append(pronum)
            break
    #print(problemlist)
    if name[1]=='.c':os.system('gcc -fprofile-arcs -ftest-coverage %s %s/mystart.c -o %s\n'%(file_name,abpath,name[0]))
    elif name[1]=='.cpp':os.system('g++ -fprofile-arcs -ftest-coverage %s %s/mystart.cpp -o %s\n'%(file_name,abpath,name[0]))
    elif name[1]=='.java':
        print('not support yet\n')
        break
    else :
        print('not c|cpp|java file\n')
        break
    #'/usr/bin/sudo /bin/su penobody -c '
    #p = subprocess.Popen('/home/coding/FL/ufiles/%s/%s'%(name[0],name[0]), stdin = subprocess.PIPE, 
    p = subprocess.Popen('/usr/bin/sudo /bin/su penobody -c /home/coding/FL/ufiles/%s/%s'%(name[0],name[0]), stdin = subprocess.PIPE, 
            stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
    #get input
    f = open('%s/problemIO/%d/%d_input%d.txt'%(abpath,file_ID,file_ID,problemlist[i-1]), 'r')
    data = f.read()
    f.close()
    #feed the input
    #p.stdin.write(data.encode('utf-8'))
    #p.stdin.close()
    time_out=0
    try:
        s = p.communicate(input =data.encode('utf-8'),timeout = timelimit)
    except:
        time_out=1
        print("hi")
        print(name)
        tpid = subprocess.check_output('pgrep -u penobody %s'%name[0][0:10], shell=True)
        print(tpid)
        ppid = tpid.decode("utf-8").split('\n')
        print(ppid)
        '''f = open('pid.txt', 'a')
        f.write(ppid+'\n')
        f.close()'''
        print('user time out')
        #print(s[0])
        wrong_answer.append('t%d'%problemlist[i-1])
        f = open('%d_useroutput%d.txt'%(file_ID,problemlist[i-1]), 'w')
        f.write('user time out')
        f.close()
        #if name[1]=='.c':p.send_signal('SIGUSR1')
        if name[1]=='.c' or name[1]=='.cpp':
            #os.system("/usr/bin/sudo /bin/su penobody -c '/bin/kill -s SIGUSR1 %i'" %p.pid)
            os.system("/usr/bin/sudo /bin/su penobody -c '/bin/kill -s SIGUSR1 %s'" %ppid[-2])
            #os.system("bash -c 'kill -s SIGUSR1 %i'" %p.pid)
            #os.system("/usr/bin/sudo /bin/su penobody -c '/bin/kill %i'" %p.pid)
            os.system("/usr/bin/sudo /bin/su penobody -c '/bin/kill %s'" %ppid[-2])
            #os.system('kill %i' %p.pid)
            p.terminate()
            p.kill()
            '''if p.returncode !='' :
                f = open(abpath+'/unkill/%s.txt'%name[0], 'w')
                f.write('program pid %d not kill'%p.pid)
                #f.write('program pid %s not kill'%pid.decode("utf-8"))
                f.close()'''
        else:
            continue
    #驗證結果(correct/wrong)
    if time_out ==0:
        f = open('%d_useroutput%d.txt'%(file_ID,problemlist[i-1]), 'w')
        f.write((s[0].decode('utf-8','ignore')).replace('\r\n','\n'))
        f.close()
    #cmd gcov
    os.system('gcov %s\n'%(file_name))
    file_gcov=file_name+'.gcov'
    os.system('cp -p %s g%d.txt'%(file_gcov,problemlist[i-1]))
    ###
    ###  STEP 2 記下.gcov內容稍後來分析哪一行最可能錯
    ###
    os.system('diff %d_useroutput%d.txt %s/problemIO/%d/%d_output%d.txt >output_same%d.txt'%(file_ID,problemlist[i-1],abpath,file_ID,file_ID,problemlist[i-1],problemlist[i-1]))
    os.system('diff -w -B %d_useroutput%d.txt %s/problemIO/%d/%d_output%d.txt >output_same_ignore%d.txt'%(file_ID,problemlist[i-1],abpath,file_ID,file_ID,problemlist[i-1],problemlist[i-1]))
    f = open('output_same%d.txt'%problemlist[i-1], 'r')
    line=f.read()
    f.close()
    f = open('output_same_ignore%d.txt'%problemlist[i-1], 'r')
    line_g=f.read()
    f.close()
    output_same=0
    #if answer==data: output_same=1
    if line=='':output_same=1
    else:
        if line_g=='':
            print('presentation error\n')
            wrong_answer.append('p%d'%problemlist[i-1])
        else:
            if time_out==0:wrong_answer.append('w%d'%problemlist[i-1])
    f = open(file_gcov, 'r')
    if output_same==1:
        for line in f:
            LOC=line.split(':')
            if int(LOC[1])==0:continue
            if line.find('-:')==-1 and line.find('#:')==-1:
                #correct and pass
                Ncs[int(LOC[1])]+=int(LOC[0])
            else:
                #correct not pass
                Nus[int(LOC[1])]+=1        
    else:
        #if time_out==0:wrong_answer.append('w%d'%i)
        for line in f:
            LOC=line.split(':')
            if int(LOC[1])==0:continue
            if line.find('-:')==-1 and line.find('#:')==-1:
                #wrong and pass
                Ncf[int(LOC[1])]+=int(LOC[0])
            else:
                #wrong not pass
                Nuf[int(LOC[1])]+=1
        #os.system('lcov -c -o converge%d.info -d .'%i)
        #os.system('genhtml converge%d.info -o w%d'%(i,i))
    f.close()
###
###  STEP 4 分析 (  (Ncf)*D/(Ncs+Nuf)  )
###  correct-0:Nus #correct-1:Ncs #wrong-0:Nuf #wrong-1:Ncf
i=0
for i in range(0,totalline):
    if Ncf[i]==0: continue
    elif (Ncs[i]+Nuf[i] == 0): 
        result[i]=Ncf[i]
        resultt[i]=Ncf[i]
        resulttt[i]=Ncf[i]
    else : 
        result[i] = round((Ncf[i])*D/(Ncs[i]+Nuf[i]),3)
        resultt[i] = round((Ncf[i])*(Ncf[i])/(Ncs[i]+Nuf[i]),3)
        resulttt[i] = round((Ncf[i])*(Ncf[i])*(Ncf[i])/(Ncs[i]+Nuf[i]),3)
m=[]
m=m+result
mm=[]
mm=mm+resultt
mmm=[]
mmm=mmm+resulttt
m.sort()
mm.sort()
mmm.sort()
#print('result\n',result)
#print('sort\n',m)
possible_txt = open('fault.txt', 'w')
if not wrong_answer:
    possible_txt.write('correct')
else:
    for i in wrong_answer:
        possible_txt.write('%s;'%i)
possible_txt.write('\nD1:\n')
i=10
while i!=0:
    if m[i-11]==0: break
    j=result.index(m[i-11])
    possible_txt.write('possible line:%d\n'%j)
    result[j]=0
    i-=1
possible_txt.write('D2:\n')
i=10
while i!=0:
    if mm[i-11]==0: break
    j=resultt.index(mm[i-11])
    possible_txt.write('possible line:%d\n'%j)
    resultt[j]=0
    i-=1
possible_txt.write('D3:\n')
i=10
while i!=0:
    if mmm[i-11]==0: break
    j=resulttt.index(mmm[i-11])
    possible_txt.write('possible line:%d\n'%j)
    resulttt[j]=0
    i-=1
possible_txt.close()
