

#   match 正则match匹配的几个用法
import requests
import re

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}',content)
print(result)
print(result.group())
print(result.span())

import re
content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\sWorld',content)
print(result)
print(result.group())
print(result.group())
print(result.span())

##贪婪与非贪婪
import re
content ='Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*(\d+).*Demo$',content)
print(result)
print(result.group(1))
#非贪婪匹配

import re
content ='Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*?(\d+).*Demo$',content)
print(result)
print(result.group(1))

import re
content = '(百度)www.baidu.com'
result = re.match('\(百度\)www\.baidu.com',content)
print(result)


