class Solution:
    def validIPAddress(self, IP: str) -> str:
        reg_v6 = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
        r_v4 = r'(([2][0-5][0-5])|([1][0-9][0-9])|([1-9][0-9])|([0-9]))'
        reg_v4 = re.compile(r'^(' + r_v4 + r'\.){3}' + r_v4 + r'$')
        if re.search(reg_v6, IP): return 'IPv6'
        if re.search(reg_v4, IP): return 'IPv4'
        return 'Neither'