# Test Network Connection

import subprocess

with open('host.txt') as f:
    ip_addresses = f.read().splitlines()
    # print(ip_addresses)
    for ip in ip_addresses:
        try:
            command = 'ping -n 1 8.8.8.3'
            output = subprocess.check_output(command.split())
            print(output.decode())
        except Exception as e:
            print(f'Host {ip} is down => {e}')
        print('#' * 50)