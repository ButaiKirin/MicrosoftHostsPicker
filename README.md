# Microsoft Hosts Picker - M$💊

A simple Python scrip for you to select the fastest IP for Microsoft services. 

As you know, Microsoft services often don't work properly in a mysterious country (a big country west of North Korea, north of Vietnam, and south of Russia). Thanks to the powerful network technology of this country, DNS often resolves Microsoft services to inappropriate IPs. This script was created to solve this problem.

So, enjoy it! 

## Get Started

You need install [ping3](https://github.com/kyan001/ping3) at first. 

* If you met "permission denied", you may need to run this as root.

```sh
pip install ping3
```

Download the latest [ZIP](https://github.com/ZeroSimple/MicrosoftHostsPicker/archive/refs/heads/main.zip) from the repo, unzip the ZIP archive to your preferred location and run the following command: 

```sh
.\MicrosoftHostsPicker.py
```

Next, all processes are automated. The script will automatically pick the best IP. The output results is in the "hosts" file in the same directory as "MicrosoftHostsPicker.py". Please select the hosts you need to add to your system. 

You only need to replace the original abnormal IPs without overwriting them all, otherwise it may be counterproductive (after all, my collection of IPs is not complete). For example, Office downloads and Windows updates have CDN nodes all over the world, so you don't need to manually configure Hosts unless your DNS resolves incorrectly. 

