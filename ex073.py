times = ('Sao Paulo','Palmeiras','Fluminence','Bahia','Flamengo','Coritiba','Gremio','Corinthians','Bragantino','Atletico-PR','Vitoria','Chapecoence','Mirassol','Santos','Vasco','Atletico-MG','Bota Fogo','Remo','Cruzeiro','Internacional')
print(f'Os primeiros colocados são {times[0:5]}')
print('*-_-*'*30)
print(f'Os 4 ultimos colocados são {times[-4:]}')
print('*-*'*30)
print(f'Na ordem alfabetica os times sao {sorted(times)}')
print('*-*'*30)
print(f'O time Chapecoence esta na {times.index('Chapecoence')+1} posição')


