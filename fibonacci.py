def fibonnaci(x):
    seq = []
    a, b = 0, 1
for n in range(x):
    seq.append(a)
    a, b = b, a+b
    return seq
  

