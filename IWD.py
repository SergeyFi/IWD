I, E, S = 'IWD', '8', '     '
I2, I1 = I[:2], I[:1]
p, S0 = lambda a: print(a), E + I + I2 + E
LAll = lambda i: p(S0+S+S0) if i == 5 else p(S0+E*5+S0) if i == 4 else p(' '+E+I+I2+E*4+S0) if i == 7 else p(' '+E*2+I*4+I1+E*2) if i == 3 else p(' '*3+E*2+I*3+E*2) if i == 2 else p(' '*2 + E + I*4 + I1 + E) if i == 8 else p(' '*5+E*9) if i == 1 else p('F')
for a in [1, 2, 3, 4, 5, 5, 7, 8, 7, 5, 5, 5, 4, 3, 2, 1]: LAll(a)