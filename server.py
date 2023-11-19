import socket
import mysql.connector


def main():
    PASSWORD = "ciccio"
    HOST = 'localhost'
    PORT = 50010
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
   # print("Server avviato, in ascolto...")
    conn, addr = s.accept()
   # print('Connesso da', addr)
   # 
    i = 0
    ins = ""
    
    while i < 3 and ins != PASSWORD:
        dati = "Inserisci la password, " + str(3 - i) + " tentativi rimasti"
        conn.send(dati.encode())
        i += 1
        ins = conn.recv(1024).decode()

    if ins == PASSWORD:
        conn.send("Password corretta, inizia la comunicazione".encode())
        handle_database_operations(conn)
    else:
        conn.send("Tentativi massimi raggiunti. Chiudo la connessione".encode())
        conn.close()

def handle_database_operations(conn):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",  # Inserisci il tuo nome utente MySQL
        password="",  # Inserisci la tua password MySQL
        database="progetto_tepsit"
    )

    curse = mydb.cursor()
    #print("Benvenuto\n")

    while True:
        val = ("Cosa desideri eseguire?\n1 per operazioni sui dipendenti\n2 per operazioni sulle zone di lavoro\n0 per terminare\nScelta: ")
        conn.send(val.encode())
        val = conn.recv(1024).decode()
        val = val.strip()
        
        if val == "1":
            # Operazioni sui dipendenti
            dipendenti_operations(conn, curse,mydb)
        elif val == "2":
            # Operazioni sulle zone di lavoro
            zone_di_lavoro_operations(conn, curse,mydb)
        elif val == "0":
            #print("Fine programma")
            break
        else:
            #print("Scelta non valida. Riprova.")
            pass
    conn.close()
def stampa(conn,cursor):
    cursor.execute("SELECT * FROM dipendenti_federico_ferretti")
    result = cursor.fetchall()
    results= ""
    for a in result:
        results  += str(a)
        #print("a",a)
    conn.send(results.encode())
    #print("risultatooooooooooooooooo",results)
   
    #print(results,"invio questo")
    #results = ', '.join(result)
    
def stampa_zone(conn,cursor):
    cursor.execute("SELECT * FROM zone_di_lavoro_federico_ferretti")
    result = cursor.fetchall()
    results= ""
    for a in result:
        results += str(a)
        print("a",a)
    conn.send(results.encode())
   # print(results,"resultsss")
    #print("inviato ")
    #print(results,"invio questo")
    #results = ', '.join(result)
    
def dipendenti_operations(conn, cursor,mydb):
    while True:
        operazione = ("Cosa desideri fare?\n"
                           "1 per visualizzare i dipendenti\n"
                           "2 per inserire un nuovo dipendente\n"
                           "3 per modificare i dati di un dipendente\n"
                           "4 per cancellare un dipendente\n"
                           "0 per tornare indietro\n"
                           "Scelta: ")
        conn.send(operazione.encode())
        operazione = conn.recv(1024).decode()
        operazione = operazione.strip()
        
        
        if operazione == "1":
            # Visualizza i dipendenti
            #print("entriamo in stampa dipendenti")
            stampa(conn,cursor)
            
            
        if operazione == "2":
            try:
                conn.send("-".encode())
                nome = conn.recv(1024).decode()

                conn.send("-".encode())
                indirizzo = conn.recv(1024).decode()

                conn.send("-".encode())
                telefono = conn.recv(1024).decode()

                conn.send("-".encode())
                cognome = conn.recv(1024).decode()

                conn.send("-".encode())
                mail = conn.recv(1024).decode()

                conn.send("-".encode())
                data_nascita = conn.recv(1024).decode()

                conn.send("-".encode())
                posizione = conn.recv(1024).decode()

                # Insert the new employee into the database
                query = "INSERT INTO dipendenti_federico_ferretti (nome, indirizzo, telefono, cognome, mail, data_nascita, posizione_lavorativa) " \
                        "VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (nome, indirizzo, telefono, cognome, mail, data_nascita, posizione))
                mydb.commit()

                conn.send("dai un'invio".encode())
                #print("Nuovo dipendente inserito con successo.")

            except Exception as e:
                conn.send(f"Si è verificato un errore durante l'inserimento: {str(e)}".encode())
               # print(f"Si è verificato un errore durante l'inserimento: {str(e)}")

        elif operazione == "3":
            stampa(conn,cursor)
            
            
            
            id_dipendente = conn.recv(1024).decode()
            
            
            operazione = ("Cosa desideri modificare?\n"
                           "1 per il nome di un dipendente\n"
                           "2 per il cognome di un dipendente\n"
                           "3 per la mail di un dipendente\n"
                           "4 per il telefono di un dipendente\n"
                           "5 per la data di nascita di un dipendente\n"
                           "6 per la posizione di un dipendente\n"
                           "7 per l'idirizzo di un dipendente\n"
                           "0 per tornare indietro\n"
                           "Scelta: ")
            conn.send(operazione.encode())
            operazione = conn.recv(1024).decode()
            operazione = operazione.strip()
            
            
            
            cursor.execute("SELECT * FROM dipendenti_federico_ferretti WHERE id_di = %s", (id_dipendente,))
            existing_dipendente = cursor.fetchone()
            if existing_dipendente:
                
                dip_trov="Dipendente trovato"
                conn.send(dip_trov.encode())
                if operazione == "1":
                    
                    
                    wer = conn.recv(1024).decode()
                    
                    
                    cursor.execute("UPDATE dipendenti_federico_ferretti SET nome = %s WHERE id_di = %s", (wer, id_dipendente))

                    mydb.commit()
                if operazione == "2":
                    wer = conn.recv(1024).decode()
                    cursor.execute("UPDATE dipendenti_federico_ferretti SET cognome = %s WHERE id_di = %s", (wer, id_dipendente))
                    mydb.commit()
                   
                    

                if operazione == "3":
                    wer = conn.recv(1024).decode()
                    cursor.execute("UPDATE dipendenti_federico_ferretti SET mail = %s WHERE id_di = %s", (wer, id_dipendente))
                    mydb.commit()
                   

                if operazione == "4":
                    wer = conn.recv(1024).decode()
                    cursor.execute("UPDATE dipendenti_federico_ferretti SET telefono = %s WHERE id_di = %s", (wer, id_dipendente))
                    mydb.commit()
                   

                if operazione == "5":
                    wer = conn.recv(1024).decode()
                    cursor.execute("UPDATE dipendenti_federico_ferretti SET data_nascita = %s WHERE id_di = %s", (wer, id_dipendente))
                    mydb.commit()
                   
                    

                if operazione == "6":
                    wer = conn.recv(1024).decode()
                    cursor.execute("UPDATE dipendenti_federico_ferretti SET posizione = %s WHERE id_di = %s", (wer, id_dipendente))
                    mydb.commit()
                   
                if operazione == "7":
                    wer = conn.recv(1024).decode()
                    cursor.execute("UPDATE dipendenti_federico_ferretti SET indirizzo = %s WHERE id_di = %s", (wer, id_dipendente))
                    mydb.commit()
                   
                
            else:
                #print("Dipendente non trovato.")
                pass
            messaggiomod="Dipendente modificato"
            conn.send(messaggiomod.encode())     
                
        elif operazione == "4":
            stampa(conn,cursor)
            
            cursor.execute("SELECT * FROM dipendenti_federico_ferretti")
            result = cursor.fetchall()
            results = "\n".join(f"ID: {row[0]}, Nome: {row[1]}" for row in result)
            conn.send(results.encode())

            id_to_delete = conn.recv(1024).decode()
            cursor.execute("SELECT * FROM dipendenti_federico_ferretti WHERE id_di = %s", (id_to_delete,))
            existing_employee = cursor.fetchone()

            if existing_employee:
                
                cursor.execute("DELETE FROM zone_di_lavoro_federico_ferretti WHERE cod_di = %s", (id_to_delete,))
                cursor.execute("DELETE FROM dipendenti_federico_ferretti WHERE id_di = %s", (id_to_delete,))
                mydb.commit()
                conn.send("dai un' invio".encode())
            else:
                conn.send("Dipendente non trovato.".encode())
            mess_canc="dai un'invio"
            #print(mess_canc)
            conn.send(mess_canc.encode())
            
        elif operazione == "0":
            #print("Tornando indietro.")
            break
        else:
           pass
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def zone_di_lavoro_operations(conn, cursor,mydb):
    

    while True:
        operazione = ("Cosa desideri fare?\n"
                           "1 per visualizzare le zone di lavoro\n"
                           "2 per inserire una nuova zona di lavoro\n"
                           "3 per modificare una zona di lavoro\n"
                           "4 per cancellare una zona di lavoro\n"
                           "0 per tornare indietro\n"
                           "Scelta: ")
        
        conn.send(operazione.encode())
        
        operazione = conn.recv(1024).decode()
    
        
        #print(operazione,"operazioneeeee")
        
        operazione = operazione.strip()
        
        
        if operazione == "1":
            # Visualizza i dipendenti
            #print("inizio stampa")
            stampa_zone(conn,cursor)
        elif operazione == "2":
            
            stampa(conn,cursor)
            # Inserimento di un nuovo dipendente
            try:
                conn.send("-".encode())
                nome = conn.recv(1024).decode()

                conn.send("-".encode())
                numero_zon = conn.recv(1024).decode()

                conn.send("-".encode())
                indirizzo_zon = conn.recv(1024).decode()

                conn.send("-".encode())
                id_dip = conn.recv(1024).decode()


                # Insert the new employee into the database
                query = "INSERT INTO zone_di_lavoro_federico_ferretti (nome_zona, numero_clienti, indirizzo, cod_di) " \
        "VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (nome,indirizzo_zon, numero_zon, id_dip))

                mydb.commit()

                conn.send("Premi invio".encode())
                
                #print("Nuova zona di lavoro inserita con successo.")

            except Exception as e:
                conn.send(f"Si è verificato un errore durante l'inserimento: {str(e)}".encode())
                #print(f"Si è verificato un errore durante l'inserimento: {str(e)}")


        elif operazione == "3":
            stampa_zone(conn,cursor)
            
            
            
            id_dipendente = conn.recv(1024).decode()
            
            
            operazione = ("Cosa desideri modificare?\n"
                           "1 per il nome di una zona\n"
                           "2 per l'indirizzo di una zona\n"
                           "3 per il numero di clienti di una zona\n"
                           "4 per il codice  di un dipendente\n"
                           "0 per tornare indietro\n"
                           "Scelta: ")
            conn.send(operazione.encode())
            operazione = conn.recv(1024).decode()
            operazione = operazione.strip()
            
            #print(id_dipendente,"debdeyfbefyegfuefyefyegye8")
            
            cursor.execute("SELECT * FROM zone_di_lavoro_federico_ferretti WHERE id_zo = %s", (id_dipendente,))
            existing_dipendente = cursor.fetchone()
            if existing_dipendente:
                
                dip_trov="Zona trovata"
                conn.send(dip_trov.encode())
                if operazione == "1":
                    
                    
                    wer = conn.recv(1024).decode()
                    
                    
                    cursor.execute("UPDATE zone_di_lavoro_federico_ferretti SET nome_zona = %s WHERE id_zo = %s", (wer, id_dipendente))

                    mydb.commit()
                if operazione == "2":
                    wer = conn.recv(1024).decode()
                    cursor.execute("UPDATE zone_di_lavoro_federico_ferretti SET cognome = %s WHERE id_zo = %s", (wer, id_dipendente))
                    mydb.commit()
                   
                    

                if operazione == "3":
                    wer = conn.recv(1024).decode()
                    cursor.execute("UPDATE zone_di_lavoro_federico_ferretti SET mail = %s WHERE id_zo = %s", (wer, id_dipendente))
                    mydb.commit()
                   

                if operazione == "4":
                    wer = conn.recv(1024).decode()
                    cursor.execute("UPDATE zone_di_lavoro_federico_ferretti SET telefono = %s WHERE id_zo = %s", (wer, id_dipendente))
                    mydb.commit()
                   

                   
               
                   
                
            else:
                #print("zona di lavoro non trovato.")
                pass
            messaggiomod="zona di lavoro modificato"
            conn.send(messaggiomod.encode())     
                
        elif operazione == "4":
            stampa_zone(conn,cursor)
            
            cursor.execute("SELECT * FROM zone_di_lavoro_federico_ferretti")
            result = cursor.fetchall()
            results = "\n".join(f"ID: {row[0]}, nome_zona: {row[1]}" for row in result)
            conn.send(results.encode())

            id_to_delete = conn.recv(1024).decode()
            cursor.execute("SELECT * FROM zone_di_lavoro_federico_ferretti WHERE id_zo = %s", (id_to_delete,))
            existing_employee = cursor.fetchone()

            if existing_employee:
                
                cursor.execute("DELETE FROM zone_di_lavoro_federico_ferretti WHERE id_zo = %s", (id_to_delete,))
                mydb.commit()
                conn.send("Premi invio".encode())
            else:
                conn.send("zona di lavoro non trovato.".encode())
            mess_canc="Premi invio"
            #print(mess_canc)
            conn.send(mess_canc.encode())
            
        elif operazione == "0":
            #print("Tornando indietro.")
            
            break
        else:
            #print("Scelta non valida. Riprova.")
            pass



if __name__ == "__main__":
    main()



