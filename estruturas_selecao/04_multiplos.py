num_competidores, qtd_total_folhas, qtd_folhas_competidor = [int(w) for w in input().split()]

print('S' if num_competidores*qtd_folhas_competidor <= qtd_total_folhas else 'N')
