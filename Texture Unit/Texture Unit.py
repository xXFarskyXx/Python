count = 0
for a in range(3):
    for b in range(3):
        for c in range(3):
            for d in range(3):
                for e in range(3):
                    for f in range(3):
                        for g in range(3):
                            for h in range(3):
                                count += 1
                                com_res = 0
                                com = [a , b , c , d , e , f , g , h]
                                for i in range(0 , 8):
                                    com_res += com[i] * pow(3 , i)
                                print(com , end = " ")
                                print("Result = " + str(com_res))
print(count)