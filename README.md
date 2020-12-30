Sometimes you wanna **ACCEPT** more than one ip addresses (as a list) to **iptables** on your Linux Server (for **CDN** or etc. useage),\
This may help you by
1.  **put** all ips as a list (each ip in a line) named `input_list`
2.  **run** the `iptables_reformater.py` for Reformatting the ips to Linux Terminal Commands named `output_list`
3.  **zip** `output_list.txt` & `iptables_runable.py` (make sure you've installed **zip** and **unzip**)
4.  then **upload** it to the Server
5.  **unzip** it 
6.  **run** the `iptables_runable.py` with `(sudo) python iptables_runable.py`
7.  **Done**

And, as you know, you're able to change the Terminal Command or the file's name or develope it further

> requirements: (sudo) apt install python zip unzip iptables

Thanks to:\
[Executing Shell Commands with Python](https://stackabuse.com/executing-shell-commands-with-python/)\
[How To: Whitelist An IP Address In IPTables](https://help.serversaustralia.com.au/s/article/How-To-Whitelist-An-IP-Address-In-IPTables)\

Used [ArvanCloud](https://www.arvancloud.com/)'s CDN and here is the ips list: [ArvanCloud IP Ranges](https://www.arvancloud.com/en/ips)
