while True:
    nota01 = float(input("Digite a primeira nota: "))
    nota02 = float(input("Digite a segunda nota: "))

    media06 = (nota01 + nota02 * 2) / 3

    if media06 >= 5:
        print(f"Aprovado no primeiro semestre com média: {media06:.1f}")

    elif media06 > 3 and media06 < 5:
        print(f"Recuperação no primeiro semestre com média: {media06:.1f}")

        media_recuperacao = float(input("Digite a nota da recuperação: "))
        media_final_primeiro_semestre = (media06 + media_recuperacao) / 2

        if media_final_primeiro_semestre >= 5:
            print(
                f"Aprovado no primeiro semestre com média: "
                f"{media_final_primeiro_semestre:.1f}"
            )
        else:
            print(
                f"Reprovado na recuperação do primeiro semestre com média: "
                f"{media_final_primeiro_semestre:.1f}"
            )

    else:
        print(f"Reprovado no primeiro semestre com média: {media06:.1f}")

    nota03 = float(input("Digite a terceira nota: "))
    nota04 = float(input("Digite a quarta nota: "))

    media712 = (nota03 + nota04 * 2) / 3

    if media712 >= 5:
        print(f"Aprovado no segundo semestre com média: {media712:.1f}")

    elif media712 > 3 and media712 < 5:
        print(f"Recuperação no segundo semestre com média: {media712:.1f}")

        media_recuperacao2 = float(input("Digite a nota da recuperação: "))
        media_final_segundo_semestre = (media712 + media_recuperacao2 * 2) / 3

        if media_final_segundo_semestre >= 5:
            print(
                f"Aprovado no segundo semestre com média: "
                f"{media_final_segundo_semestre:.1f}"
            )
        else:
            print(
                f"Reprovado na recuperação do segundo semestre com média: "
                f"{media_final_segundo_semestre:.1f}"
            )

    else:
        print(f"Reprovado no segundo semestre com média: {media712:.1f}")

    media_final = (media06 + media712) / 2

    if media_final >= 5:
        print(f"Aprovado no ano com média: {media_final:.1f}")

    elif media_final > 3 and media_final < 5:
        print(f"Recuperação no ano com média: {media_final:.1f}")

        media_recuperacao3 = float(input("Digite a nota da recuperação: "))
        media_final_recuperacao = (media_final + media_recuperacao3 * 2) / 3

        if media_final_recuperacao >= 5:
            print(f"Aprovado no ano com média: {media_final_recuperacao:.1f}")
        else:
            print(
                f"Reprovado na recuperação do ano com média: "
                f"{media_final_recuperacao:.1f}"
            )

    else:
        print(f"Reprovado no ano com média: {media_final:.1f}")