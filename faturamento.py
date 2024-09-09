# variavel armazenando o valor de cada estado
sp = float(67.83643) 
rj = float(36.67866)
mg = float (29.22988)
es = float(27.16548)
ot = float(19.84953)
soma = float(sp+rj+mg+es+ot) # soma para calcular o percentual

# calculo do percentual
percentual_sp = float(sp/soma)
percentual_rj = float(rj/soma)
percentual_mg = float(mg/soma)
percentual_es = float(es/soma)
percentual_ot = float(ot/soma)


# resultado de acordo com cada estado
print (f'O percentual do estado de São paulo é : {percentual_sp:.2%} ')
print (f'O percentual do estado de Rio de Janeiro é : {percentual_rj:.2%} ')
print (f'O percentual do estado de Minas Gerais é : {percentual_mg:.2%} ')
print (f'O percentual do estado de Espírito Santo é : {percentual_es:.2%} ')
print (f'O percentual de outros estados é : {percentual_ot:.2%} ')

