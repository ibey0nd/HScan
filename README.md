# HScan
超精简的POC扫描框架

# Usage
```
python hscan.py
 _    _   _____
| |  | | / ____|
| |__| || (___    ___  __ _  _ __
|  __  | \___ \  / __|/ _` || '_ \
| |  | | ____) || (__| (_| || | | |
|_|  |_||_____/  \___|\__,_||_| |_|
                                plugins weB vulnerability Scanner
                          bey0nd [at] (https://www.beysec.com)

usage: HScan.py [options]

* A plugins weB vulnerability Scanner. *
Author : bey0nd [at] (https://www.beysec.com)

optional arguments:
  -h, --help            show this help message and exit
  -u [HOST [HOST2 HOST3 ...] [HOST [HOST2 HOST3 ...] ...]]
                        Scan several url from command line
  -f TargetFile         Load new line delimited targets from TargetFile
  -p , --plugins        Load plugins from TargetDirectory
  -cookie name=value    HTTP cookies for Target
```

```
python hscan.py -u 172.16.32.97
 _    _   _____
| |  | | / ____|
| |__| || (___    ___  __ _  _ __
|  __  | \___ \  / __|/ _` || '_ \
| |  | | ____) || (__| (_| || | | |
|_|  |_||_____/  \___|\__,_||_| |_|
                                plugins weB vulnerability Scanner
                          bey0nd [at] (https://www.beysec.com)

[-] 11:39:05 [INFO] check target [172.16.32.97] with plugins [redis-remote]
[-] 11:39:05 [INFO] check target [172.16.32.97] with plugins [redis-unauth]
[-] 11:39:05 [INFO] all target[s] is done , check result with output

success : 0
```
