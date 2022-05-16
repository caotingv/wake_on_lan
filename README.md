# wake_on_lan
网卡唤醒工具，主要实现在局域网内唤醒一台计算机

## 使用方法
运行python3 pywol.py -h，可以查看帮助。 
```
$ python3 pywol.py -h
usage: pywol.py [-h] [-i ip] [-n interface] mac address

Wake device using the wake on lan protocol.

positional arguments:
  mac address   The mac addresses of the computers you are trying to wake.

optional arguments:
  -h, --help    show this help message and exit
  -i ip         The ip address of the host to send the magic packet to. (default: 255.255.255.255)
  -n interface  The ip address of the network adapter to route the magic packet through. (default: None)

```

- mac address：mac地址为试图要启动的设备的mac地址，这个参数是必须要有的参数，
- -i ：可以通过"-i",来指定广播地址，这个地址可以是你当前网络的广播地址，也可以是想要启动的设备的具体的IP地址，默认是：255.255.255.255.
- -n：主要是用来指定用来发送广播包的网卡设备

## 通过mac地址唤醒一台计算机

```
python3 pywol.py 1A-2B-3c-4D-5E-6F
```

> mac地址可以是"-"连接，也可以是":"
