srtings=input()
for char in srtings:
    if char=='A':
        if 'AB' in srtings :
            x=srtings.replace('AB','-',1)
            if 'BA' in srtings:
                print('YES')
                break
            else:
                print('NO')
                break
        else:
            print('NO')
            break
    elif char=='B':
        if 'BA' in srtings :
            srtings=srtings.replace('BA','-',1)
            if 'AB' in srtings:
                print('YES')
                break
            else:
                print('NO')
                break
        else:
            print('NO')
            break