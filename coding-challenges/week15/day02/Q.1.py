
"""
Q-1 ) Validate IP Address
https://leetcode.com/problems/validate-ip-address/
(5 marks)
(Medium)
Given a string IP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid
IPv6 address or "Neither" if IP is not a correct IP of any type.
A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and
xi cannot contain leading zeros. For example, "192.168.1.1" and "192.168.1.0"
are valid IPv4 addresses but "192.168.01.1", while "192.168.1.00" and
"192.168@1.1" are invalid IPv4 addresses.
A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:
● 1 <= xi.length <= 4
● xi is a hexadecimal string which may contain digits, lower-case English
letter ('a' to 'f') and upper-case English letters ('A' to 'F').
● Leading zeros are allowed in xi.
For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and
"2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, while
"2001:0db8:85a3::8A2E:037j:7334" and
"02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.
Example 1:
Input: IP = "172.16.254.1"
Output: "IPv4"
Explanation: This is a valid IPv4 address, return "IPv4".
"""





class Solution:
    def validIPAddress(self, IP: str) -> str:
        
        result="IPv4"
        count=0
        for x in IP.split('.'):
            try:
                if int(x) > 255 or int(x)<0:
                    result="Neither"
                elif len(x)>3 or len(x)==0 or (int(x)<10 and len(x)!=1) or (100>int(x)>9  and len(x)!=2):
                    result="Neither"
            except: 
                 result="Neither"
            count+=1
            
        if count!=4: 
            result="Neither"

        IP=IP.split(':') 
        if len(IP)!=8:
            return result
        
        result="IPv6" 
        
        for x in IP:
            try:
                d=int(x, 16)
                if x[0]=="-"  or len(x)>4 or len(x)==0:
                    return "Neither"
            except:
                return "Neither"
            
        return result    


