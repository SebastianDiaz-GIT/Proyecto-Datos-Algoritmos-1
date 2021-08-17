import csv

def csvIt():
    with open('X:\Programacion\Python\csv\personas.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            print("Nombre : {0}, Apellido  : {1}, Edad : {2}, Departamento : {3}".format(row[0], row[1], row[2], row[3]))
csvIt()
#cvs1 = csv()
#cvs1.csvIt()
