from ping3 import ping


def pingIP(file):
    Time = list()
    TargetIP = file.readline()
    while TargetIP:
        n = 3
        TotalTime = 0.0
        for i in range(n):
            IPstrip = TargetIP.strip()
            PingTime = ping(IPstrip, timeout=1, unit='ms')
            if not PingTime:
                TotalTime = 5000.0*n
                break
            TotalTime = TotalTime+PingTime
        print(IPstrip+'\t\t', int(TotalTime/n))
        Time.append(TotalTime/n)
        Time.sort()
        if (TotalTime/n == Time[0]):
            result_list = list()
            result_list.append(IPstrip)
        TargetIP = file.readline()
    return result_list


with open("hosts", 'w') as hosts:

    # OneDrive Hosts beta

    hosts.writelines('#OneDrive(Beta, only for China) \n')
    hosts.writelines('134.170.108.26 onedrive.live.com\n')
    hosts.writelines('134.170.109.48 skyapi.onedrive.live.com\n\n')

    # Microsoft Login Hosts
    Microsoft_Login_list = [
        'logincdn.msauth.ne',
        'login.live.com',
        'acctcdn.msauth.net',
        'account.live.com',
    ]
    hosts.writelines('#Microsoft Login \n')
    for url in Microsoft_Login_list:
        hosts.writelines('13.107.42.22'+' '+url+'\n')
    hosts.writelines('\n')

    with open("./data/Microsoft_Account.txt", 'r') as Microsoft_Account:
        result_list = pingIP(Microsoft_Account)
        hosts.writelines('#Microsoft Account \n')
        hosts.writelines(result_list[0]+' account.microsoft.com\n\n')
        print("Microsoft_Account")
        print(result_list)

    # with open("./data/OneNote.txt", 'r') as OneNote:
    #     result_list = pingIP(OneNote)
    #     hosts.writelines('#OneNote \n')
    #     hosts.writelines(result_list[0]+' hierarchyapi.onenote.com\n')
    #     hosts.writelines(result_list[0]+' contentsync.onenote.com\n')
    #     hosts.writelines(result_list[0]+' d.docs.live.net\n\n')
    #     print(result_list)

    Xbox_Live_CDN_1_list = [
        'gameclipscontent-d2009.xboxlive.com',
        'images-eds.xboxlive.com',
        'xbl-smooth.xboxlive.com',
        'titlehub.xboxlive.com',
        'compass.xboxlive.com'
    ]
    Xbox_Live_CDN_2_list = [
        'xnotify.xboxlive.com',
        'activityhub.xboxlive.com',
        'xboxcare.xboxlive.com',
        'images-eds-ssl.xboxlive.com',
        'rta.xboxlive.com',
        'peoplehub.xboxlive.com',
        'editorial.xboxlive.com'
    ]
    with open("./data/Xbox_Live_CDN_1.txt", 'r') as Xbox_Live_CDN_1:
        result_list = pingIP(Xbox_Live_CDN_1)
        hosts.writelines('#Xbox Live CDN\n')
        for url in Xbox_Live_CDN_1_list:
            hosts.writelines(result_list[0]+' '+url+'\n')
    with open("./data/Xbox_Live_CDN_2.txt", 'r') as Xbox_Live_CDN_2:
        result_list = pingIP(Xbox_Live_CDN_2)
        for url in Xbox_Live_CDN_2_list:
            hosts.writelines(result_list[0]+' '+url+'\n')
        hosts.writelines('\n')
        print("Xbox_Live_CDN")
        print(result_list)

    with open("./data/Xbox_Cloud_Sync.txt", 'r') as Xbox_Cloud_Sync:
        result_list = pingIP(Xbox_Cloud_Sync)
        hosts.writelines('#Xbox Cloud Sync \n')
        hosts.writelines(result_list[0]+' titlestorage.xboxlive.com\n\n')
        print("Xbox_Cloud_Sync")
        print(result_list)

    with open("./data/Office_CDN.txt", 'r') as Office_CDN:
        result_list = pingIP(Office_CDN)
        hosts.writelines('#Office CDN \n')
        hosts.writelines(result_list[0]+' officecdn.microsoft.com\n\n')
        print("Office_CDN")
        print(result_list)

    with open("./data/Microsoft_Store_Images.txt", 'r') as Microsoft_Store_Images:
        result_list = pingIP(Microsoft_Store_Images)
        hosts.writelines('#Microsoft Store Images \n')
        hosts.writelines(result_list[0]+' store-images.s-microsoft.com\n\n')
        print("Microsoft_Store_Images")
        print(result_list)

    with open("./data/Microsoft_Store_Pages.txt", 'r') as Microsoft_Store_Pages:
        result_list = pingIP(Microsoft_Store_Pages)
        hosts.writelines('#Microsoft Store Pages \n')
        hosts.writelines(
            result_list[0]+' storeedgefd.dsx.mp.microsoft.com\n\n')
        print("Microsoft_Store_Pages")
        print(result_list)

    with open("./data/Microsoft_Games_Download.txt", 'r') as Microsoft_Games_Download:
        result_list = pingIP(Microsoft_Games_Download)
        hosts.writelines('#Microsoft Games Download \n')
        hosts.writelines(result_list[0]+' xvcf1.xboxlive.com\n')
        hosts.writelines(result_list[0]+' xvcf2.xboxlive.com\n\n')
        print("Microsoft_Games_Download")
        print(result_list)

    Windows_Update_list = [
        'tlu.dl.delivery.mp.microsoft.com',
        'dl.delivery.mp.microsoft.com',
        'assets1.xboxlive.cn',
        'assets2.xboxlive.cn'
    ]
    with open("./data/Windows_Update.txt", 'r') as Windows_Update:
        result_list = pingIP(Windows_Update)
        hosts.writelines('#Windows Update \n')
        for url in Windows_Update_list:
            hosts.writelines(result_list[0]+' '+url+'\n')
        print("Windows_Update")
        print(result_list)

print('All done.')
print('The output Hosts file is in the "hosts" in the same directory as "MicrosoftHostsPicker.py".')
print('Please select the hosts you need to add to your system.')
input()
