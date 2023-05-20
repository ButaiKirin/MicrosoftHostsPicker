# !/usr/bin/env python
# -*-coding:utf-8 -*-

import re
import asyncio
import statistics
import time

from ping3 import ping


async def async_ping_ip(ip):
    """

    :param ip:
    :return:
    """
    delay = ping(ip, timeout=1, unit='ms')
    delay = delay if delay is not None else 5000
    return int(delay)


async def async_get_delay(ip, frequency=3):
    """

    :param ip:
    :param frequency:
    :return:
    """
    try:
        delay_list = await asyncio.gather(*[async_ping_ip(ip) for _ in range(frequency)])
        delay_list = [i for i in delay_list if i is not None]
        delay = statistics.harmonic_mean(delay_list)
        return int(delay)

    except Exception as e:
        print(e)
    return 5000


async def async_get_ips_delay(ips):
    """

    :param ips:
    :return:
    """
    try:
        delay_list = await asyncio.gather(*[async_get_delay(ip) for ip in ips])
        # print(delay_list)
        ip_delay_tup = zip(ips, delay_list)
        ip_delay_tup_sort = sorted(ip_delay_tup, key=lambda x: x[1])

        res = [f"{tup[0]:16}\t# delay: {tup[1]}" for tup in ip_delay_tup_sort]

        for i in res:
            print(i)

        return ip_delay_tup_sort[0][0]

    except Exception as e:
        print(e)


def get_ips(file_name):
    """

    :param file_name:
    :return:
    """
    pattern = re.compile(r"\s+")
    ips = []
    with open(file_name, 'r') as f:
        data = f.readlines()
        for s in data:
            ips.append(pattern.sub("", s))
    # return list(set(ips))[:3] # test
    return list(set(ips))


async def to_run(file_names):
    """
    For test, Not in main funciton
    :param file_names: string list
    :return: lick : [[host1_ip], [host2_ip], [host3_ip],...]
    """
    ips_list = []
    for file_name in file_names:
        ips_list.append(get_ips(file_name))
    # ips_list = [get_ips(file_names[0])[:3]]

    result = []
    tasks = []

    for ips in ips_list:
        task = asyncio.create_task(async_get_ips_delay(ips))
        tasks.append(task)

    for i in tasks:
        r = await i
        result.append(r)

    return result


async def main():
    h = {
        "Microsoft_Account": ["account.microsoft.com"],
        "Xbox_Live_CDN_1": [
            "gameclipscontent-d2009.xboxlive.com",
            "images-eds.xboxlive.com",
            "xbl-smooth.xboxlive.com",
            "titlehub.xboxlive.com",
            "compass.xboxlive.com"
        ],
        "Xbox_Live_CDN_2": [
            "xnotify.xboxlive.com",
            "activityhub.xboxlive.com",
            "xboxcare.xboxlive.com",
            "images-eds-ssl.xboxlive.com",
            "rta.xboxlive.com",
            "peoplehub.xboxlive.com",
            "editorial.xboxlive.com"
        ],
        "Xbox_Cloud_Sync": ["titlestorage.xboxlive.com"],
        "Office_CDN": ["officecdn.microsoft.com"],
        "Microsoft_Store_Images": ["store-images.s-microsoft.com"],
        "Microsoft_Store_Pages": ["storeedgefd.dsx.mp.microsoft.com"],
        "Microsoft_Games_Download": [
            "xvcf1.xboxlive.com",
            "xvcf2.xboxlive.com"
        ],
        "Windows_Update": [
            'tlu.dl.delivery.mp.microsoft.com',
            'dl.delivery.mp.microsoft.com',
            'assets1.xboxlive.cn',
            'assets2.xboxlive.cn'
        ],
    }

    with open("hosts", 'w') as f:
        # OneDrive Hosts beta
        f.writelines('#OneDrive(Beta, only for China) \n')
        f.writelines('134.170.108.26 onedrive.live.com\n')
        f.writelines('134.170.109.48 skyapi.onedrive.live.com\n\n')

        for k, v in h.items():
            info = k.replace('_', ' ')

            print(info)

            ip = await async_get_ips_delay(get_ips(f"./data/{k}.txt"))
            f.writelines(f'#{info} \n')

            for i in v:
                f.writelines(f'{ip} {i}\n')
            f.writelines('\n')

            print('')

    print('All done.')
    print('The output Hosts file is in the "hosts" in the same directory as "MicrosoftHostsPicker.py".')
    print('Please select the hosts you need to add to your system.')
    input()


if __name__ == '__main__':
    print(f"started at {time.strftime('%X')}")
    asyncio.run(main())
    print(f"finished at {time.strftime('%X')}")
