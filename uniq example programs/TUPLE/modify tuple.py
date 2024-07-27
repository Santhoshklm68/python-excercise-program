tuple1 = (11,[22,33],44,55)
tuple2 = list(tuple1)
print(tuple2)
tuple2[1][0]=222
ans = tuple(tuple2)
print(ans)