jef = {"swift", "picpay", "original", "jbs", "friboi", "J&F"}
jbs = {"swift", "friboi", "seara", "rezende", "delícia", "primor", "doriana", "massaleve", "marba"}
empresas_iguais = set()
empresas_diferentes = set()
print(f'O Instituto J&F tem {len(jef)} empresas, já a JBS tem {len(jbs)} marcas')

for empresas_jef in jef:
    for marcas_jbs in jbs:
        if marcas_jbs == empresas_jef:
            empresas_iguais.add(empresas_jef)
            
for empresas_jef in jef:
    for marcas_jbs in jbs:
        if marcas_jbs in empresas_iguais or empresas_jef in empresas_iguais:
            continue
        else:
            empresas_diferentes.add(empresas_jef)
            empresas_diferentes.add(marcas_jbs)
print(f'As marcas que se interseção são {empresas_iguais} e as diferentes são {empresas_diferentes}')