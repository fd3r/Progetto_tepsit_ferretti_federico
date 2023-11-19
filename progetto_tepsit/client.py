import socket
from prettytable import PrettyTable
import datetime 
def main():
    HOST = 'localhost'
    PORT = 50010

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while True:
        response = s.recv(1024).decode()
        print(response)

        if "Password corretta" in response:
            handle_user_input(s)
            break
        elif "Tentativi massimi raggiunti" in response:
            print("Tentativi massimi raggiunti. Chiudo la connessione.")
            break
        else:
            password = input("Inserisci la password: ")
            s.send(password.encode())

    s.close()
    
    


def gestione_stampa_zone(result,s):

    result_senza_parentesi = result.strip('()')
    tuple_strings = result_senza_parentesi.split(')(')
    tuple_strings = ['(' + s + ')' for s in tuple_strings]

    lista_di_tuple = [eval(s) for s in tuple_strings]

    table = PrettyTable(['ID', 'Nome', 'Numero Clienti', 'Codice Dipendente', 'Indirizzo'])

    for row in lista_di_tuple:
        table.add_row(row)

    print(table)

def gestione_stampa_dipe(result,s):
    result_senza_parentesi = result.strip('()')
    tuple_strings = result_senza_parentesi.split(')(')
    tuple_strings = ['(' + s + ')' for s in tuple_strings]
    lista_di_tuple = [eval(s) for s in tuple_strings]

    table = PrettyTable(['ID', 'Nome', 'Indirizzo', 'Numero', 'Famiglia', 'Email', 'Data', 'Ruolo'])

    for row in lista_di_tuple:
        table.add_row(row)

    print(table)


    
    
    
def handle_user_input(s):
    while True:
        response = s.recv(1024).decode()
        choice = input(response)
        s.send(choice.encode())

        if choice == "1":
            handle_dipendenti_operations(s)
        elif choice == "2":
            handle_zone_di_lavoro_operations(s)
        elif choice == "0":
            print("Fine programma.")
            break
        else:
            print("Scelta non valida. Riprova.")

def handle_zone_di_lavoro_operations(s):
    
    
    while True:
        response = s.recv(1024).decode()
        choice = input(response)
        s.send(choice.encode())

        if choice == "1":
            result = s.recv(4096).decode()
            #print(result,"risultato")
            gestione_stampa_zone(result,s)
        elif choice == "2":
            handle_inserimento_zona(s)
        elif choice == "3":
            handle_modifica_zona(s)
        elif choice == "4":
            handle_cancellazione_zona(s)
        elif choice == "0":
            print("Tornando indietro.")
            break
        else:
            print("Scelta non valida. Riprova.")

def handle_inserimento_zona(s):
    inputs = s.recv(1024).decode()
    #print(inputs,"ef7rfrhfr8rh8grhh")
    gestione_stampa_dipe(inputs,s)

    nome = input("Inserisci il nome della zona: ")
    s.send(nome.encode())

    indirizzo = input("Inserisci l'indirizzo: ")
    s.send(indirizzo.encode())

    telefono = input("Inserisci il numero dei clienti: ")
    s.send(telefono.encode())

    cognome = input("Inserisci l'id del dipendente che si occupa della zona: ")
    s.send(cognome.encode())

 

    response = s.recv(1024).decode()
    print(response)

def handle_modifica_zona(s):
    
    result = s.recv(1024).decode()
    #print(result)
    gestione_stampa_zone(result,s)
    
    
    id_dipendente = input("Inserisci l'ID della zona da modificare: ")
    s.send(id_dipendente.encode())


    response = s.recv(1024).decode()
    print(response)
    
    n_oper=input("inserisci: ")
    s.send(n_oper.encode())
    operaz=n_oper
    
    result = s.recv(1024).decode()
    
    
    if result == "Zona trovata":
        #print("dipendente trovato lato client")
        #print(operaz,"operaz fgryfgrfgri")
        if operaz == "1":
            
            nome = input("Inserisci il nuovo nome della zona: ")
            s.send(nome.encode())
        if operaz == "2":
            
            nome = input("Inserisci il nuovo codice del dipendente di riferimento: ")
            s.send(nome.encode())

        if operaz == "3":
            
            nome = input("Inserisci il nuovo numero dei clienti: ")
            s.send(nome.encode())

        if operaz == "4":
            
            nome = input("Inserisci il nuovo indirizzo: ")
            s.send(nome.encode())

        
        response = s.recv(1024).decode()
        print(response)
    else:
        print("zona non trovata.")
    
    
    
def handle_cancellazione_zona(s):
    result = s.recv(1024).decode()
    #print(result)
    gestione_stampa_zone(result,s)

    id_dipendente = input("Inserisci l'ID della zona da cancellare: ")
    s.send(id_dipendente.encode())

    response = s.recv(1024).decode()
    print(response)
    
    
    
    
    
 
    
    
    
    
    
    
    
    
    
    
    
    
def handle_dipendenti_operations(s):
    while True:
        response = s.recv(1024).decode()
        choice = input(response)
        s.send(choice.encode())

        if choice == "1":
            result = s.recv(4096).decode()
            print(result)
            gestione_stampa_dipe(result,s)
        elif choice == "2":
            handle_inserimento_dipendente(s)
        elif choice == "3":
            handle_modifica_dipendente(s)
        elif choice == "4":
            handle_cancellazione_dipendente(s)
        elif choice == "0":
            print("Tornando indietro.")
            break
        else:
            print("Scelta non valida. Riprova.")

def handle_inserimento_dipendente(s):
    inputs = s.recv(1024).decode()
    print(inputs)
    #gestione_stampa_dipe(inputs,s)

    nome = input("Inserisci il nome: ")
    s.send(nome.encode())

    indirizzo = input("Inserisci l'indirizzo: ")
    s.send(indirizzo.encode())

    telefono = input("Inserisci il telefono: ")
    s.send(telefono.encode())

    cognome = input("Inserisci il cognome: ")
    s.send(cognome.encode())

    mail = input("Inserisci la mail: ")
    s.send(mail.encode())

    data_nascita = input("Inserisci la data di nascita (AAAA-MM-GG): ")
    s.send(data_nascita.encode())

    posizione = input("Inserisci la posizione: ")
    s.send(posizione.encode())

    response = s.recv(1024).decode()
    print(response)


def handle_modifica_dipendente(s):
    
    result = s.recv(1024).decode()
    print(result)
    gestione_stampa_dipe(result,s)
    
    id_dipendente = input("Inserisci l'ID del dipendente da modificare: ")
    s.send(id_dipendente.encode())


    response = s.recv(1024).decode()
    print(response)
    
    n_oper=input("inserisci: ")
    s.send(n_oper.encode())
    operaz=n_oper
    
    result = s.recv(1024).decode()
    
    
    if result == "Dipendente trovato":
        print("dipendente trovato lato client")
        print(operaz,"operaz fgryfgrfgri")
        if operaz == "1":
            
            nome = input("Inserisci il nuovo nome: ")
            s.send(nome.encode())
        if operaz == "2":
            
            nome = input("Inserisci il nuovo cognome: ")
            s.send(nome.encode())

        if operaz == "3":
            
            nome = input("Inserisci il nuovo mail: ")
            s.send(nome.encode())

        if operaz == "4":
            
            nome = input("Inserisci il nuovo telefono: ")
            s.send(nome.encode())

        if operaz == "5":
            
            nome = input("Inserisci la nuova data di nascita (AAAA-MM-GG): ")
            s.send(nome.encode())

        if operaz == "6":
            
            nome = input("Inserisci il nuovo posizione: ")
            s.send(nome.encode())
           
        if operaz == "7":
            
            nome = input("Inserisci il nuovo indirizzo: ")
            s.send(nome.encode())    
        
        response = s.recv(1024).decode()
        print(response)
    else:
        print("Dipendente non trovato.")

def handle_cancellazione_dipendente(s):
    result = s.recv(1024).decode()
    print(result)
    gestione_stampa_dipe(result,s)

    id_dipendente = input("Inserisci l'ID del dipendente da cancellare: ")
    s.send(id_dipendente.encode())

    response = s.recv(1024).decode()
    print(response)

if __name__ == "__main__":
    main()
