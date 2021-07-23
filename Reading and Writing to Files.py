with open ('ekNBk9X.jpg','rb') as rf:
    with open('aaa.jpg','wb') as wf:
        size = 1
        rff = rf.read(size)
        while len(rff) > 0:
            wf.write(rff)
            rff = rf.read(size)
