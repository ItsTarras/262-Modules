def lcs(s1, s2):
    cache = {}
    def recursive(s1, s2):

        if s1 == '' or s2 == '':
            return ""
        if (s1, s2) in cache:
            return cache[(s1, s2)]
        elif s1[-1] == s2[-1]:
            cache[(s1, s2)] = recursive(s1[:-1], s2[:-1]) + s1[-1]
        else:
            soln1 = recursive(s1[:-1], s2)
            soln2 = recursive(s1, s2[:-1])
            if len(soln1) > len(soln2):
                cache[(s1, s2)] = soln1
                return soln1
            else:
                cache[(s1, s2)] = soln2
                return soln2
            

        return cache[(s1, s2)]

    a = recursive(s1, s2)
    return a


# A simple test that should run without caching
s1 = "abcde"
s2 = "qbxxd"
lcs_string = lcs(s1, s2)
print(lcs_string)

s1 = "Look at me, I can fly!"
s2 = "Look at that, it's a fly"
print(lcs(s1, s2))

s1 = "abcdefghijklmnopqrstuvwxyz"
s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYS"
print(lcs(s1, s2))


s1 = "balderdash!"
s2 = "balderdash!"
print(lcs(s1, s2))

s1 = "Solidandkeen\nSolidandkeen\nSolidandkeen\n"
s2 = "Whoisn'tsick\nWhoisn'tsick\nWhoisn'tsick"
lcs_string = lcs(s1, s2)
print(lcs_string)
print(repr(lcs_string))