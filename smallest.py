a=[2,4,411,4,1]
small=maxi=a[0]
for i in a:
    if i<=small:
        small=i
    if i>=maxi:
        maxi=i
print(small)
print(maxi)