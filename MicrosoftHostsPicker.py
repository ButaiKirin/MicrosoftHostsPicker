import concurrent.futures
from typing import List, Tuple
from ping3 import ping


def ping_ip(ip: str, attempts: int = 3, timeout: float = 1.0) -> float:
    total_time = 0.0
    for _ in range(attempts):
        ping_time = ping(ip, timeout=timeout, unit='ms')
        if ping_time is None:
            return float('inf')
        total_time += ping_time
    return total_time / attempts


def process_ip_list(file_path: str) -> Tuple[str, float]:
    best_ip = ''
    best_time = float('inf')
    with open(file_path, 'r') as file:
        for ip in file:
            ip = ip.strip()
            avg_time = ping_ip(ip)
            if avg_time < best_time:
                best_ip = ip
                best_time = avg_time
    return best_ip, best_time


def write_hosts_section(hosts_file, title: str, ip: str, domains: List[str]):
    hosts_file.write(f'# {title}\n')
    for domain in domains:
        hosts_file.write(f'{ip} {domain}\n')
    hosts_file.write('\n')


def main():
    ip_files = {
        'Microsoft_Account': './data/Microsoft_Account.txt',
        'Xbox_Live_CDN_1': './data/Xbox_Live_CDN_1.txt',
        'Xbox_Live_CDN_2': './data/Xbox_Live_CDN_2.txt',
        'Xbox_Cloud_Sync': './data/Xbox_Cloud_Sync.txt',
        'Office_CDN': './data/Office_CDN.txt',
        'Microsoft_Store_Images': './data/Microsoft_Store_Images.txt',
        'Microsoft_Store_Pages': './data/Microsoft_Store_Pages.txt',
        'Microsoft_Games_Download': './data/Microsoft_Games_Download.txt',
        'Windows_Update': './data/Windows_Update.txt',
    }

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_file = {executor.submit(process_ip_list, file_path): file_name 
                          for file_name, file_path in ip_files.items()}
        
        results = {}
        for future in concurrent.futures.as_completed(future_to_file):
            file_name = future_to_file[future]
            ip, time = future.result()
            results[file_name] = ip
            print(f"{file_name}: {ip} ({time:.2f}ms)")

    with open("hosts", 'w') as hosts:
        # OneDrive Hosts beta
        write_hosts_section(hosts, 'OneDrive (Beta, only for China)', '',
                            ['134.170.108.26 onedrive.live.com',
                             '134.170.109.48 skyapi.onedrive.live.com'])

        # Microsoft Login Hosts
        write_hosts_section(hosts, 'Microsoft Login', '13.107.42.22',
                            ['logincdn.msauth.net', 'login.live.com',
                             'acctcdn.msauth.net', 'account.live.com'])

        write_hosts_section(hosts, 'Microsoft Account', results['Microsoft_Account'],
                            ['account.microsoft.com'])

        # Xbox Live CDN
        xbox_live_cdn_domains = [
            'gameclipscontent-d2009.xboxlive.com', 'images-eds.xboxlive.com',
            'xbl-smooth.xboxlive.com', 'titlehub.xboxlive.com', 'compass.xboxlive.com',
            'xnotify.xboxlive.com', 'activityhub.xboxlive.com', 'xboxcare.xboxlive.com',
            'images-eds-ssl.xboxlive.com', 'rta.xboxlive.com', 'peoplehub.xboxlive.com',
            'editorial.xboxlive.com'
        ]
        write_hosts_section(hosts, 'Xbox Live CDN', results['Xbox_Live_CDN_1'], xbox_live_cdn_domains)

        write_hosts_section(hosts, 'Xbox Cloud Sync', results['Xbox_Cloud_Sync'],
                            ['titlestorage.xboxlive.com'])

        write_hosts_section(hosts, 'Office CDN', results['Office_CDN'],
                            ['officecdn.microsoft.com'])

        write_hosts_section(hosts, 'Microsoft Store Images', results['Microsoft_Store_Images'],
                            ['store-images.s-microsoft.com'])

        write_hosts_section(hosts, 'Microsoft Store Pages', results['Microsoft_Store_Pages'],
                            ['storeedgefd.dsx.mp.microsoft.com'])

        write_hosts_section(hosts, 'Microsoft Games Download', results['Microsoft_Games_Download'],
                            ['xvcf1.xboxlive.com', 'xvcf2.xboxlive.com'])

        write_hosts_section(hosts, 'Windows Update', results['Windows_Update'],
                            ['tlu.dl.delivery.mp.microsoft.com', 'dl.delivery.mp.microsoft.com',
                             'assets1.xboxlive.cn', 'assets2.xboxlive.cn'])

    print('All done.')
    print('The output Hosts file is in the "hosts" in the same directory as "MicrosoftHostsPicker.py".')
    print('Please select the hosts you need to add to your system.')
    input('Press Enter to exit...')

if __name__ == '__main__':
    main()
