class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return '{0:b}'.format(int(a, 2) + int(b, 2))

'''
int(a, 2)           means convert a to int from base 2 (binary)
int(a, 6)           means convert a to int from base 6 (hexa)  

so it will convert the two binaries to int, add them and create a 'value'
'value' will be sent to template to be formated acc. to template

'{0}{1}{2}'.format('foo', 'bar', 'baz') -> 'foobarbaz'

Template = {0:b},   here b means convert to binary
So the 'value' is sent to {0} and in binary format

But after a certain length of a,b the integer will not support value
'''