# Microsoft Hosts Picker - M$💊

A lightweight Python script to help you select the fastest IP addresses for Microsoft services.

## Why This Tool?

In certain regions, Microsoft services may not function optimally due to DNS resolving to suboptimal IP addresses. This script aims to address that issue by finding the most responsive IPs for various Microsoft services.

## Getting Started

1. Install dependencies:

```sh
pip install -r requirements.txt
```

2. Download the latest [ZIP](https://github.com/ButaiKirin/MicrosoftHostsPicker/archive/refs/heads/main.zip) from this repository.

3. Extract the contents to your preferred location.

4. Run the script:

```sh
python MicrosoftHostsPicker.py
```

## How It Works

The script automatically selects the best IP addresses for various Microsoft services. Results are saved in a "hosts" file in the same directory as "MicrosoftHostsPicker.py".

## Usage Tips

- Only replace the problematic IP addresses in your system's hosts file.
- Avoid overwriting all entries, as this may cause unintended issues.
- Some services (e.g., Office Download and Windows Update) use global CDN nodes and may not require manual configuration unless your DNS is resolving incorrectly.


Enjoy faster and more reliable access to Microsoft services!
