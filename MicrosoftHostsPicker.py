import ping3
fwrite=open(r"hosts",'w')
n=5
Time = []

fread=open(r"./data/Microsoft_Login.txt",'r')
Time.clear()
Best_IP = ''
TargetIP=fread.readline()
while TargetIP:
    TotalTime=0.0
    for i in range(n):
        IPstrip=TargetIP.strip()
        PingTime=ping3.ping(IPstrip,timeout=1,unit='ms')
        if not PingTime:
            PingTime=5000.0
        TotalTime=TotalTime+PingTime
    print(IPstrip+','+str(int(TotalTime/n)))
    Time.append(int(TotalTime/n))
    Time.sort();
    if (int(TotalTime/n) == Time[0]): Best_IP=str(IPstrip)
    TargetIP=fread.readline()
fread.close()
print (Best_IP)
fwrite.writelines('#Microsoft Login '+'\n')
fwrite.writelines(Best_IP+' '+'logincdn.msauth.net'+'\n')
fwrite.writelines(Best_IP+' '+'login.live.com'+'\n')
fwrite.writelines(Best_IP+' '+'acctcdn.msauth.net'+'\n')
fwrite.writelines(Best_IP+' '+'account.live.com'+'\n')
fwrite.writelines('\n')


fread=open(r"./data/OneNote.txt",'r')
Time.clear()
Best_IP = ''
TargetIP=fread.readline()
while TargetIP:
    TotalTime=0.0
    for i in range(n):
        IPstrip=TargetIP.strip()
        PingTime=ping3.ping(IPstrip,timeout=1,unit='ms')
        if not PingTime:
            PingTime=5000.0
        TotalTime=TotalTime+PingTime
    print(IPstrip+','+str(int(TotalTime/n)))
    Time.append(int(TotalTime/n))
    Time.sort();
    if (int(TotalTime/n) == Time[0]): Best_IP=str(IPstrip)
    TargetIP=fread.readline()
fread.close()
print (Best_IP)
fwrite.writelines('#OneNote '+'\n')
fwrite.writelines(Best_IP+' '+'hierarchyapi.onenote.com'+'\n')
fwrite.writelines(Best_IP+' '+'contentsync.onenote.com'+'\n')
fwrite.writelines('\n')


fread=open(r"./data/Xbox_Live_CDN_1.txt",'r')
Time.clear()
Best_IP = ''
TargetIP=fread.readline()
while TargetIP:
    TotalTime=0.0
    for i in range(n):
        IPstrip=TargetIP.strip()
        PingTime=ping3.ping(IPstrip,timeout=1,unit='ms')
        if not PingTime:
            PingTime=5000.0
        TotalTime=TotalTime+PingTime
    print(IPstrip+','+str(int(TotalTime/n)))
    Time.append(int(TotalTime/n))
    Time.sort();
    if (int(TotalTime/n) == Time[0]): Best_IP=str(IPstrip)
    TargetIP=fread.readline()
fread.close()
print (Best_IP)
fwrite.writelines('#Xbox Live CDN '+'\n')
fwrite.writelines(Best_IP+' '+'images-eds.xboxlive.com'+'\n')
fwrite.writelines(Best_IP+' '+'xbl-smooth.xboxlive.com'+'\n')
fwrite.writelines(Best_IP+' '+'gameclipscontent-d2009.xboxlive.com'+'\n')
fwrite.writelines(Best_IP+' '+'titlehub.xboxlive.com'+'\n')
fwrite.writelines(Best_IP+' '+'compass.xboxlive.com'+'\n')


fread=open(r"./data/Xbox_Live_CDN_2.txt",'r')
Time.clear()
Best_IP = ''
TargetIP=fread.readline()
while TargetIP:
    TotalTime=0.0
    for i in range(n):
        IPstrip=TargetIP.strip()
        PingTime=ping3.ping(IPstrip,timeout=1,unit='ms')
        if not PingTime:
            PingTime=5000.0
        TotalTime=TotalTime+PingTime
    print(IPstrip+','+str(int(TotalTime/n)))
    Time.append(int(TotalTime/n))
    Time.sort();
    if (int(TotalTime/n) == Time[0]): Best_IP=str(IPstrip)
    TargetIP=fread.readline()
fread.close()
print (Best_IP)
fwrite.writelines(Best_IP+' '+'xnotify.xboxlive.com'+'\n')
fwrite.writelines(Best_IP+' '+'activityhub.xboxlive.com'+'\n')
fwrite.writelines(Best_IP+' '+'xboxcare.xboxlive.com'+'\n')
fwrite.writelines(Best_IP+' '+'images-eds-ssl.xboxlive.com'+'\n')
fwrite.writelines(Best_IP+' '+'rta.xboxlive.com'+'\n')
fwrite.writelines(Best_IP+' '+'peoplehub.xboxlive.com'+'\n')
fwrite.writelines(Best_IP+' '+'editorial.xboxlive.com'+'\n')
fwrite.writelines('\n')


fread=open(r"./data/Xbox_Cloud_Sync.txt",'r')
Time.clear()
Best_IP = ''
TargetIP=fread.readline()
while TargetIP:
    TotalTime=0.0
    for i in range(n):
        IPstrip=TargetIP.strip()
        PingTime=ping3.ping(IPstrip,timeout=1,unit='ms')
        if not PingTime:
            PingTime=5000.0
        TotalTime=TotalTime+PingTime
    print(IPstrip+','+str(int(TotalTime/n)))
    Time.append(int(TotalTime/n))
    Time.sort();
    if (int(TotalTime/n) == Time[0]): Best_IP=str(IPstrip)
    TargetIP=fread.readline()
fread.close()
print (Best_IP)
fwrite.writelines('#Xbox Cloud Sync '+'\n')
fwrite.writelines(Best_IP+' '+'titlestorage.xboxlive.com'+'\n')
fwrite.writelines('\n')


fread=open(r"./data/Office_CDN.txt",'r')
Time.clear()
Best_IP = ''
TargetIP=fread.readline()
while TargetIP:
    TotalTime=0.0
    for i in range(n):
        IPstrip=TargetIP.strip()
        PingTime=ping3.ping(IPstrip,timeout=1,unit='ms')
        if not PingTime:
            PingTime=5000.0
        TotalTime=TotalTime+PingTime
    print(IPstrip+','+str(int(TotalTime/n)))
    Time.append(int(TotalTime/n))
    Time.sort();
    if (int(TotalTime/n) == Time[0]): Best_IP=str(IPstrip)
    TargetIP=fread.readline()
fread.close()
print (Best_IP)
fwrite.writelines('#Office CDN '+'\n')
fwrite.writelines(Best_IP+' '+'officecdn.microsoft.com'+'\n')
fwrite.writelines('\n')


fread=open(r"./data/Microsoft_Store_Images.txt",'r')
Time.clear()
Best_IP = ''
TargetIP=fread.readline()
while TargetIP:
    TotalTime=0.0
    for i in range(n):
        IPstrip=TargetIP.strip()
        PingTime=ping3.ping(IPstrip,timeout=1,unit='ms')
        if not PingTime:
            PingTime=5000.0
        TotalTime=TotalTime+PingTime
    print(IPstrip+','+str(int(TotalTime/n)))
    Time.append(int(TotalTime/n))
    Time.sort();
    if (int(TotalTime/n) == Time[0]): Best_IP=str(IPstrip)
    TargetIP=fread.readline()
fread.close()
print (Best_IP)
fwrite.writelines('#Microsoft Store Images '+'\n')
fwrite.writelines(Best_IP+' '+'store-images.s-microsoft.com'+'\n')
fwrite.writelines('\n')


fread=open(r"./data/Microsoft_Store_Pages.txt",'r')
Time.clear()
Best_IP = ''
TargetIP=fread.readline()
while TargetIP:
    TotalTime=0.0
    for i in range(n):
        IPstrip=TargetIP.strip()
        PingTime=ping3.ping(IPstrip,timeout=1,unit='ms')
        if not PingTime:
            PingTime=5000.0
        TotalTime=TotalTime+PingTime
    print(IPstrip+','+str(int(TotalTime/n)))
    Time.append(int(TotalTime/n))
    Time.sort();
    if (int(TotalTime/n) == Time[0]): Best_IP=str(IPstrip)
    TargetIP=fread.readline()
fread.close()
print (Best_IP)
fwrite.writelines('#Microsoft Store Pages '+'\n')
fwrite.writelines(Best_IP+' '+'storeedgefd.dsx.mp.microsoft.com'+'\n')
fwrite.writelines('\n')


fread=open(r"./data/Microsoft_Games_Download.txt",'r')
Time.clear()
Best_IP = ''
TargetIP=fread.readline()
while TargetIP:
    TotalTime=0.0
    for i in range(n):
        IPstrip=TargetIP.strip()
        PingTime=ping3.ping(IPstrip,timeout=1,unit='ms')
        if not PingTime:
            PingTime=5000.0
        TotalTime=TotalTime+PingTime
    print(IPstrip+','+str(int(TotalTime/n)))
    Time.append(int(TotalTime/n))
    Time.sort();
    if (int(TotalTime/n) == Time[0]): Best_IP=str(IPstrip)
    TargetIP=fread.readline()
fread.close()
print (Best_IP)
fwrite.writelines('#Microsoft Games Download '+'\n')
fwrite.writelines(Best_IP+' '+'xvcf1.xboxlive.com'+'\n')
fwrite.writelines(Best_IP+' '+'xvcf2.xboxlive.com'+'\n')
fwrite.writelines('\n')


fread=open(r"./data/Windows_Update.txt",'r')
Time.clear()
Best_IP = ''
TargetIP=fread.readline()
while TargetIP:
    TotalTime=0.0
    for i in range(n):
        IPstrip=TargetIP.strip()
        PingTime=ping3.ping(IPstrip,timeout=1,unit='ms')
        if not PingTime:
            PingTime=5000.0
        TotalTime=TotalTime+PingTime
    print(IPstrip+','+str(int(TotalTime/n)))
    Time.append(int(TotalTime/n))
    Time.sort();
    if (int(TotalTime/n) == Time[0]): Best_IP=str(IPstrip)
    TargetIP=fread.readline()
fread.close()
print (Best_IP)
fwrite.writelines('#Windows Update '+'\n')
fwrite.writelines(Best_IP+' '+'tlu.dl.delivery.mp.microsoft.com'+'\n')
fwrite.writelines(Best_IP+' '+'dl.delivery.mp.microsoft.com'+'\n')
fwrite.writelines(Best_IP+' '+'assets1.xboxlive.cn'+'\n')
fwrite.writelines(Best_IP+' '+'assets2.xboxlive.cn'+'\n')
fwrite.writelines('\n')

print ('All done. The output Hosts file is in the "hosts" file in the same directory as "MicrosoftHostsPicker.py". Please select the hosts you need to add to your system. ')
fwrite.close()

