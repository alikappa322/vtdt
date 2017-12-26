    mas_max = 0
    for i in range(len(mas)):
        if mas[i]>=mas_max:
            mas_max = mas[i]
            i_max = i
    if k_d not in mas:
        mas[i_max] = k_d
        print(mas)
    else:
        print("число {} уже есть".format(k_d))
func(a1,k)
func(b1,des)