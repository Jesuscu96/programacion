def pagada(cuota,n_anios):
    t_meses = 12*n_anios
    t_pagar = cuota*t_meses
    print(f"cantidad pagada total: {t_pagar}" )
    return(t_pagar)

cuota=1166.75
n_anios=15
c=150000
pagada(cuota,n_anios)