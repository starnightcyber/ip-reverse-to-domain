# ip-reverse-to-domain
reverse ip to domain, find domains reverse to the same ip. <br>
ip反向解析,找出解析到该ip的所有域名.

### Declaration
The original work was done by Joinse7en, you can get more information by visiting his github page. </br>
https://github.com/JoinSe7en/reverseip  

这个脚本是基于Joinse7en的工作,更详细的信息请访问其Github主页,如上.</br>

### reverse_ip_batch.py

I add a batch script based on his work to reverse a list of ip at a time and save the reversed domains to a file for further exploitation.</br>

在他的工作的基础上,我增加了一个可以解析一批ip列表到域名的脚本,并保存在一个文件中以备日后之用.</br>

### Sample

![image](https://github.com/starnightcyber/ip-reverse-to-domain/blob/master/reverse_ip_batch.py_usage.png)

reverse_ip_batch.py: 用法很简单,可以简单看下如上的示例,只需要提供一个保存ip的列表的文件名即可,脚本会自动解析.</br>
reverseip.py: 解析单个ip地址到域名,用法可以直接使用reverseip.py -h查看帮助.</br>
