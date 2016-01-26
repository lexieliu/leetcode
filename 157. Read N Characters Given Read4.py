# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
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
            buf4 = [""]*4
            l = read4(buf4)
            if l == 0:
                break
            size = min(l,n-ptr)
            for i in xrange(size):
                buf[ptr] = buf4[i]
                ptr += 1
        return ptr
