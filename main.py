import UHF

v1 = list([complex(real=1, imag=3)])
v2 = list([complex(real=1, imag=3)])
u = UHF.UHF(100)
print(u.hash_vct(v1) == u.hash_vct(v2))
