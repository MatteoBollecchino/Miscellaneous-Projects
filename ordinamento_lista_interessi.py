# Programma per l'ordinamento della lista dei propri interessi

def conteggio_elementi_categoria(list,categoria):
    contatore = 0
    numero_elementi = 0

    for i in range(len(list)):
        numero_elementi += 1
        if(list[i] == "\n"):
            contatore += 1
            if(contatore == categoria):
                break
            else:
                numero_elementi = 0

    return numero_elementi

def ordinamento_scrittura_lista_in_file(f_sorted, list, title):
    list.sort()
    f_sorted.write(title)
    f_sorted.writelines(list)
    f_sorted.write("\n")

def scrittura_categorie(f_sorted, list):
    i = 1
    limite_inf = 0
    limite_sup = 0

    while True:
        limite_categoria = conteggio_elementi_categoria(list,i)
        limite_inf = limite_sup + 1
        limite_sup += limite_categoria
        sublist = list[limite_inf : limite_sup]

        if len(sublist) == 0:
            break
        else:
            categoria = input("Nome categoria "+ str(i) + ": ")
            ordinamento_scrittura_lista_in_file(f_sorted, sublist, categoria)
            
        i += 1
    
if __name__ == "__main__":

    nome_file = input("Inserire path relativo del file di input: ")
    f = open(nome_file,"r+")
    f_sorted = open("listaOrdinata.txt","w+")

    list = f.readlines()

    scrittura_categorie(f_sorted, list)
