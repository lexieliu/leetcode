# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.bufptr = 0
        self.bufcnt = 0
        self.buf4 = [""]*4
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        if n == 0:
            return 0
        ptr = 0
        while ptr < n:
            if self.bufptr == 0:
                self.bufcnt = read4(self.buf4)
            if self.bufcnt == 0:
                break
            while ptr < n and self.bufptr < self.bufcnt:
                buf[ptr] = self.buf4[self.bufptr]
                ptr += 1
                self.bufptr += 1
            if self.bufptr == self.bufcnt:
                self.bufptr = 0
        return ptr
