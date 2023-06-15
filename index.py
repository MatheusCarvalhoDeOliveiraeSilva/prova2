def eliminar_recursao_esquerda_direta(gramatica):
    for nao_terminal in gramatica:
        regras = gramatica[nao_terminal]
        novas_regras = []
        recursao = []
        for regra in regras:
            if regra[0] == nao_terminal:
                recursao.append(regra[1:])
            else:
                novas_regras.append(regra)
        if len(recursao) > 0:
            novo_nao_terminal = nao_terminal + "'"
            novas_regras.append(novo_nao_terminal)
            for regra in recursao:
                novas_regras.append(regra + novo_nao_terminal)
            gramatica[novo_nao_terminal] = recursao
        gramatica[nao_terminal] = novas_regras

def eliminar_recursao_esquerda_indireta(gramatica):
    nao_terminais = list(gramatica.keys())
    for i in range(len(nao_terminais)):
        for j in range(i):
            A = nao_terminais[i]
            B = nao_terminais[j]
            regras_A = gramatica[A]
            regras_B = gramatica[B]
            novas_regras = []
            for regra_A in regras_A:
                if regra_A[0] == B:
                    for regra_B in regras_B:
                        novas_regras.append(regra_B + regra_A[1:])
                else:
                    novas_regras.append(regra_A)
            gramatica[A] = novas_regras

def converter_regras_unitarias(gramatica):
    for nao_terminal in gramatica:
        regras = gramatica[nao_terminal]
        novas_regras = []
        regras_unitarias = []
        for regra in regras:
            if len(regra) == 1 and regra[0] in gramatica:
                regras_unitarias.append((nao_terminal, regra[0]))
            else:
                novas_regras.append(regra)
        while regras_unitarias:
            A, B = regras_unitarias.pop()
            for regra in gramatica[B]:
                if len(regra) == 1 and regra[0] in gramatica:
                    regras_unitarias.append((A, regra[0]))
                else:
                    novas_regras.append(regra)
        gramatica[nao_terminal] = novas_regras

def converter_para_forma_normal(gramatica):
    eliminar_recursao_esquerda_direta(gramatica)
    eliminar_recursao_esquerda_indireta(gramatica)
    converter_regras_unitarias(gramatica)