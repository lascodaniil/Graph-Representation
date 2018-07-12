# Introducere lista adiacenta
def list_adi():
    list = []
    for i in range(0, n):
        line = []
        y=int(input("Introdu cite legaturi are un virf "))
        for j in range(0, y):
            x = int(input())
            line.append(x)
        list.append(line)
    return list

# Introducere matrice adiacenta
def adi_matrix():
    matrice_adiacenta = []
    for i in range(0, n):
        print("Introducem valorile pentru matricea adiacenta")
        line = []
        for j in range(0, n):
            x = int(input())
            line.append(x)
        matrice_adiacenta.append(line)
    return matrice_adiacenta

# Introducere matrice incidenta
def incident_matrix():
    inc_mat=[]
    for i in range(m):
        aux=[]
        for j in range(n):
            x=int(input())
            aux.append(x)
        inc_mat.append(aux)
    return inc_mat


# Matrice adiacenta din lista adiacenta
def matrix_adj_from_list_adj(aux1):
    matrix=[]
    l = [x for x in range(0, n)]
    for line in aux1:

        aux = []
        for key in l:
    #   for key, value in enumerate(l):
            if key in line:
                aux.append(1)
            else:
                aux.append(0)
        matrix.append(aux)
    return matrix



# Lista adiacenta din matricea adiacenta
def list_adj_from_matrix_adj(aux2):
    list=[]

    for line in aux2:
        list1 = []
        for key,value in enumerate(line):
            if value==1:
                list1.append(key)
        list.append(list1)
    return list


# Lista adiacenta din matricea incidenta
def list_adj_from_matrix_incident(matrix):
    list_adiacenta=[]
    for j in range(n):
        list = []
        for i in range(m):
            if matrix[i][j]== -1:
                for x in range(n):
                    if matrix[i][x] == 1:
                        list.append(x)


                    if list in list_adiacenta:
                        continue
                    else:
                        list_adiacenta.append(list)

    if len(list_adiacenta)<n:
        x=len(list_adiacenta)
        l=[]
        for i in range (x,n):
            list_adiacenta.append(l)
    return list_adiacenta

# Matrice incidenta din lista adiacenta
def incident_matrix_from_adj_list(lista):
    matrice_de_incidenta = []
    n=len(lista)
    for i in range(n):
        for j in lista[i]:
            linie_noua = [-1 if k == i else (1 if k == j else 0) for k in range(n)]
            matrice_de_incidenta.append(linie_noua)

    return matrice_de_incidenta




print("\n")
print("\t\t*** MENIU ***\t\t\n")
print("1.Introducem matricea de adicenta\n")
print("2.Introducem matricea de incidenta\n")
print("3.Introducem lista de adicenta\n")

while True:
    case=int(input("Introdu cazul ales \n"))
    n = int(input("Introdu numarul de noduri\n"))
    m = int(input("Introdu numarul de arcuri\n"))
    if case==1:
        print("Ati ales cazul de a introduce matricea adiacenta\n")
        matrice_adiacenta=adi_matrix()
        for i in matrice_adiacenta:
            for elem in i:
                print(elem, end=" ")
            print("\n")
        print("Lista de adiacenta din matricea de adiacenta \n")
        lista_adiacenta_from_adi_mat=list_adj_from_matrix_adj(matrice_adiacenta)
        print("\n")
        for key,j in enumerate(lista_adiacenta_from_adi_mat):
            print(key, " -> ", end="")
            for elem1 in j:
                print(elem1, ",",end=" ")
            print("0")
            print("\n")

        print("Matricea de incidenta din matricea de adiacenta \n")
        x=incident_matrix_from_adj_list(lista_adiacenta_from_adi_mat)

        for a1 in x:
            for elem6 in a1:
                print(elem6, end=" ")
            print("\n")



    if case==2:
        print("Ati ales cazul de a introduce matricea de incidenta\n")
        matrice_incidenta = incident_matrix()
        for k in matrice_incidenta:
            for elem in k:
                print(elem, end=" ")
            print("\n")

        print("Lista de adiacenta din matricea de incidenta\n")
        lista_adiaceta_from_incid_mat=list_adj_from_matrix_incident(matrice_incidenta)
        print("\n")
        for key, h in enumerate(lista_adiaceta_from_incid_mat):
            print(key, " -> ", end=" ")
            for elem2 in h:
                print(elem2, end=" ")
            print("0")
            print("\n")

        print("Matrice de adiacenta din matricea de incidenta\n")
        h=matrix_adj_from_list_adj(lista_adiaceta_from_incid_mat)
        for a1 in h:
            for elem5 in a1:
                print(elem5, end=" ")
            print("\n")



    if case==3:
        print("Ati ales cazul de a introduce lista adiacenta\n")
        lista_adiacenta = list_adi()
        print("Lista de adiacenta este \n")
        print("\n")
        for key1, h1 in enumerate(lista_adiacenta):
            print(key1, " -> ", end=" ")
            for elem21 in h1:
                print(elem21, end=" ")
            print("0")
            print("\n")

        print("Matricea de adiacenta este\n")
        D=matrix_adj_from_list_adj(lista_adiacenta)
        for a in D:
            for elem3 in a:
                print(elem3, end=" ")
            print("\n")

        print("Matricea de incidenta din lista de adiacenta\n")
        m=incident_matrix_from_adj_list(lista_adiacenta)
        for n in m:
            for z in n:
                print(z, end=" ")
            print("\n")
