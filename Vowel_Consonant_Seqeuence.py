def v_c_s(i_s):
    o_s = ""
    l_c_t = ""
    v=['a', 'e', 'i', 'o', 'u']
    for c in i_s:
        if c in v: 
            if l_c_t != 'v': 
                o_s += 'V' 
                l_c_t = 'v' 
        else: 
            if l_c_t != 'c': 
                o_s += 'C' 
                l_c_t = 'c'
    return o_s

i_s = input()
o_s = v_c_s(i_s)
print(o_s)
