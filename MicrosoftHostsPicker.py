import ping3
fwrite=open(r"hosts",'w')
n=3
Time = []
result = []

def pingIP(result):
    Time.clear()
    TargetIP=fread.readline()
    while TargetIP:
        TotalTime=0.0
        for i in range(n):
            IPstrip=TargetIP.strip()
            PingTime=ping3.ping(IPstrip,timeout=1,unit='ms')
            if not PingTime:
                TotalTime=5000.0*n
                break
            TotalTime=TotalTime+PingTime
        print(IPstrip+','+str(int(TotalTime/n)))
        Time.append(int(TotalTime/n))
        Time.sort();
        if (int(TotalTime/n) == Time[0]): result.clear();result.append(IPstrip)
        TargetIP=fread.readline()
    fread.close()
    return

fread=open(r"./data/Microsoft_Login.txt",'r')
pingIP(result)
fwrite.writelines('#Microsoft Login '+'\n')
fwrite.writelines(result[0]+' '+'logincdn.msauth.net'+'\n')
fwrite.writelines(result[0]+' '+'login.live.com'+'\n')
fwrite.writelines(result[0]+' '+'acctcdn.msauth.net'+'\n')
fwrite.writelines(result[0]+' '+'account.live.com'+'\n')
print (result)
result.clear()
fwrite.writelines('\n')

fread=open(r"./data/Microsoft_Account.txt",'r')
pingIP(result)
fwrite.writelines('#Microsoft Account '+'\n')
fwrite.writelines(result[0]+' '+'account.microsoft.com'+'\n')
print (result)
result.clear()
fwrite.writelines('\n')

'''
fread=open(r"./data/OneNote.txt",'r')
pingIP(result)
fwrite.writelines('#OneNote '+'\n')
fwrite.writelines(result[0]+' '+'hierarchyapi.onenote.com'+'\n')
fwrite.writelines(result[0]+' '+'contentsync.onenote.com'+'\n')
fwrite.writelines(result[0]+' '+'d.docs.live.net'+'\n')
print (result)
result.clear()
fwrite.writelines('\n')
'''

fread=open(r"./data/Xbox_Live_CDN_1.txt",'r')
pingIP(result)
fwrite.writelines('#Xbox Live CDN '+'\n')
fwrite.writelines(result[0]+' '+'images-eds.xboxlive.com'+'\n')
fwrite.writelines(result[0]+' '+'xbl-smooth.xboxlive.com'+'\n')
fwrite.writelines(result[0]+' '+'gameclipscontent-d2009.xboxlive.com'+'\n')
fwrite.writelines(result[0]+' '+'titlehub.xboxlive.com'+'\n')
fwrite.writelines(result[0]+' '+'compass.xboxlive.com'+'\n')

fread=open(r"./data/Xbox_Live_CDN_2.txt",'r')
pingIP(result)
fwrite.writelines(result[0]+' '+'xnotify.xboxlive.com'+'\n')
fwrite.writelines(result[0]+' '+'activityhub.xboxlive.com'+'\n')
fwrite.writelines(result[0]+' '+'xboxcare.xboxlive.com'+'\n')
fwrite.writelines(result[0]+' '+'images-eds-ssl.xboxlive.com'+'\n')
fwrite.writelines(result[0]+' '+'rta.xboxlive.com'+'\n')
fwrite.writelines(result[0]+' '+'peoplehub.xboxlive.com'+'\n')
fwrite.writelines(result[0]+' '+'editorial.xboxlive.com'+'\n')
print (result)
result.clear()
fwrite.writelines('\n')

fread=open(r"./data/Xbox_Cloud_Sync.txt",'r')
pingIP(result)
fwrite.writelines('#Xbox Cloud Sync '+'\n')
fwrite.writelines(result[0]+' '+'titlestorage.xboxlive.com'+'\n')
print (result)
result.clear()
fwrite.writelines('\n')

fread=open(r"./data/Office_CDN.txt",'r')
pingIP(result)
fwrite.writelines('#Office CDN '+'\n')
fwrite.writelines(result[0]+' '+'officecdn.microsoft.com'+'\n')
print (result)
result.clear()
fwrite.writelines('\n')

fread=open(r"./data/Microsoft_Store_Images.txt",'r')
pingIP(result)
fwrite.writelines('#Microsoft Store Images '+'\n')
fwrite.writelines(result[0]+' '+'store-images.s-microsoft.com'+'\n')
print (result)
result.clear()
fwrite.writelines('\n')

fread=open(r"./data/Microsoft_Store_Pages.txt",'r')
pingIP(result)
fwrite.writelines('#Microsoft Store Pages '+'\n')
fwrite.writelines(result[0]+' '+'storeedgefd.dsx.mp.microsoft.com'+'\n')
print (result)
result.clear()
fwrite.writelines('\n')

fread=open(r"./data/Microsoft_Games_Download.txt",'r')
pingIP(result)
fwrite.writelines('#Microsoft Games Download '+'\n')
fwrite.writelines(result[0]+' '+'xvcf1.xboxlive.com'+'\n')
fwrite.writelines(result[0]+' '+'xvcf2.xboxlive.com'+'\n')
print (result)
result.clear()
fwrite.writelines('\n')

fread=open(r"./data/Windows_Update.txt",'r')
pingIP(result)
fwrite.writelines('#Windows Update '+'\n')
fwrite.writelines(result[0]+' '+'tlu.dl.delivery.mp.microsoft.com'+'\n')
fwrite.writelines(result[0]+' '+'dl.delivery.mp.microsoft.com'+'\n')
fwrite.writelines(result[0]+' '+'assets1.xboxlive.cn'+'\n')
fwrite.writelines(result[0]+' '+'assets2.xboxlive.cn'+'\n')
print (result)
result.clear()
fwrite.writelines('\n')

print ('All done. The output Hosts file is in the "hosts" file in the same directory as "MicrosoftHostsPicker.py". Please select the hosts you need to add to your system. ')
fwrite.close()
