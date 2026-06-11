while True:
    linha = input().split()
    M = int(linha[0])
    N = int(linha[1])
    
    moedas = list(map(int, input().split()))
    
    if M == 0:
        break
    
    infinito = M + 1
    dp = [infinito] * (M + 1)
    dp[0] = 0
    
    for valor in range(1, M + 1):
        for moeda in moedas:
            if moeda <= valor:
                candidato = dp[valor - moeda] + 1
                if candidato < dp[valor]:
                    dp[valor] = candidato
    
    if dp[M] == infinito:
        print("impossivel")
    else:
        print(dp[M])
    
    print()
