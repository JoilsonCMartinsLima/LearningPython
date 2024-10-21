# comentario
print("ola")

print("oi", "meu", "nome", "é", "oi")
print("oi", "meu", "nome", "é", "oi", sep="-")  # separa as strings com o -

# por padrão, a função print termina com quebra de linha, esse comando end vazio, retira isso
print("oi", "meu", "nome", "é", "oi", end="")
print("oi", "meu", "nome", "é", "oi", sep=".", end="-\n")

# esse \" faz com que o interpretador veja o proximo caractere, que nesse caso é ", como caractere de escape, nao como aspas para fechar a string
print("teste \"teste\"")
# esse R, faz com que tanto os caracteres de escape quanto a contrabarra como caractere normal
print(r"teste \"teste\"", "oi\"")

print("'ola'")  # imprime apenas com as as aspas de dentro
print('"ola"')
