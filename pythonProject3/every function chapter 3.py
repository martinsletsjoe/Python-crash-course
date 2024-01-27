drit = ["istind", "blåtind", "lågen", "lysakerelva", "larvik", "svensk"]
print(len(drit))
drit.reverse()
print(drit)
print(sorted(drit))
drit.sort(reverse=True)
print(drit)
drit.append("sandefjord")
print(drit)
drit[0] = "croatia"
print(drit)
del drit[0]
print(drit)
drit.insert(0,"croatia")
print(drit)
drit_pop = drit.pop()
print(drit)
print(drit_pop)
mokka_by = "larvik"
drit.remove(mokka_by)
print(sorted(drit))
