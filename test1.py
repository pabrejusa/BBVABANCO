from tkinter import *
from tkinter import messagebox
import mysql.connector
import os
import datetime
import time
from PIL import ImageTk, Image

#connecting to the database
db = mysql.connector.connect(host="localhost",user="root",passwd="Harveylinux77+",database="test1")
mycur = db.cursor()

def error_destroy():
    err.destroy()

def succ_destroy():
    succ.destroy()
    root1.destroy()

def succ_destroy2():
    succ.destroy()
    ingresarEfectivo.destroy()

def succ_destroy3():
    consultarSaldoWindow.destroy()

def succ_destroy4():
    succ.destroy()
    retirarEfectivo.destroy()

def succ_destroy5():
    succ.destroy()
    transferirEfectivo.destroy()

def succ_destroy6():
    consultarMovimientosWindows.destroy()


def error():
    global err
    err = Toplevel(root1)
    err.title("Error")
    err.geometry("500x500")
    Label(err,text="Por favor revisa los campos ingresados",fg="red",font="bold").pack()
    Label(err,text="").pack()
    Button(err,text="Ok",bg="#14549C", fg="white",width=8,height=1,command=error_destroy,font="bold").pack()

def error2():
    global err
    err = Toplevel(retirarEfectivo)
    err.title("Error")
    err.geometry("500x500")
    Label(err,text="Por favor revisa los campos ingresados",fg="red",font="bold").pack()
    Label(err,text="").pack()
    Button(err,text="Ok",bg="#14549C", fg="white",width=8,height=1,command=error_destroy,font="bold").pack()

def error3():
    global err
    err = Toplevel(transferirEfectivo)
    err.title("Error")
    err.geometry("500x500")
    Label(err,text="Por favor revisa los campos ingresados",fg="red",font="bold").pack()
    Label(err,text="").pack()
    Button(err,text="Ok",bg="#14549C", fg="white",width=8,height=1,command=error_destroy).pack()

def success():
    global succ
    succ = Toplevel(root1)
    succ.title("Success")
    succ.geometry("500x500")
    Label(succ, text="Operacion realizada correctamente", fg="green", font="bold").pack()
    Label(succ, text="").pack()
    Button(succ, text="Ok",bg="#14549C", fg="white", width=8, height=1, command=succ_destroy,font="bold").pack()

def success2():
    global succ
    succ = Toplevel(ingresarEfectivo)
    succ.title("Success")
    succ.geometry("500x500")
    Label(succ, text="Operacion realizada correctamente", fg="green", font="bold").pack()
    Label(succ, text="").pack()
    Button(succ, text="Ok",bg="#14549C", fg="white", width=8, height=1, command=succ_destroy2,font="bold").pack()

def success4():
    global succ
    succ = Toplevel(retirarEfectivo)
    succ.title("Success")
    succ.geometry("500x500")
    Label(succ, text="Operacion realizada correctamente", fg="green", font="bold").pack()
    Label(succ, text="").pack()
    Button(succ, text="Ok",bg="#14549C", fg="white", width=8, height=1, command=succ_destroy4).pack()

def success5():
    global succ
    succ = Toplevel(transferirEfectivo)
    succ.title("Success")
    succ.geometry("500x500")
    Label(succ, text="Operacion realizada correctamente", fg="green", font="bold").pack()
    Label(succ, text="").pack()
    Button(succ, text="Ok",bg="#14549C", fg="white", width=8, height=1, command=succ_destroy5).pack()

def register_user():
    id_info  = identificador.get()
    username_info = username.get()
    initial_balance = balance.get()
    if username_info == "":
        error()
    else:
        sql = "INSERT INTO cuentas VALUES(%s,%s,%s)"
        t = (id_info, username_info, initial_balance)
        mycur.execute(sql, t)
        db.commit()
        Label(root1, text="").pack()
        time.sleep(0.50)
        success()



def registration():
    global root1
    root1 = Toplevel(root)
    root1.title("Menu de registro")
    root1.geometry("500x500")
    root1.configure(bg='#14549C')
    global identificador
    global username
    global balance
    Label(root1,text="Registrate hoy mismo",bg="white",fg="black",font="bold",width=300).pack()
    identificador = StringVar()
    username = StringVar()
    balance = DoubleVar()
    balance.set(0)
    Label(root1,text="").pack()
    Label(root1,text="ID :",font="bold",bg="#14549C", fg="white").pack()
    Entry(root1,textvariable=identificador).pack()
    Label(root1, text="").pack()
    Label(root1,text="Username :",font="bold",bg="#14549C", fg="white").pack()
    Entry(root1,textvariable=username).pack()
    Label(root1, text="").pack()
    Label(root1, text="Saldo inicial :",font="bold",bg="#14549C", fg="white").pack()
    Entry(root1, textvariable=balance).pack()
    Label(root1, text="").pack()
    Button(root1,text="Registrate",bg="white", fg="#14549C",command=register_user,font="bold").pack()

def login():
    global root2
    root2 = Toplevel(root)
    root2.title("Ingresa a tu cuenta")
    root2.geometry("500x500")
    root2.configure(bg='#14549C')
    global username_varify
    Label(root2, text="Ingresa a tu cuenta", bg="white", fg="black", font="bold",width=300).pack()
    username_varify = StringVar()
    Label(root2, text="").pack()
    Label(root2, text="Nombre :", font="bold",bg="#14549C", fg="white").pack()
    Entry(root2, textvariable=username_varify).pack()
    Label(root2, text="").pack()
    Button(root2, text="Ingresa a tu cuenta",command=login_varify,font="bold",bg="white", fg="#14549C").pack()
    Label(root2, text="")

def logg_destroy():
    logg.destroy()
    root2.destroy()

def fail_destroy():
    fail.destroy()

def logged(data):
    global logg
    id = data[0]
    user = data[1]
    balance = data[2]
    print("data",user)
    logg = Toplevel(root2)
    logg.title("Bienvenido")
    logg.geometry("500x500")
    root2.configure(bg='#14549C')
    Label(logg, text="Bienvenido {} , tu numero de cuenta es: {}".format(user, id), fg="green", font="bold").pack()
    Label(logg, text="").pack()
    
    Label(logg, text="Que operacion deseas realizar el dia de hoy?", fg="green", font="bold").pack()
    Button(logg,text="Consultar saldo",width="20",height="1",bg="#14549C", fg="white",font="bold",command=lambda: consultarSaldo(id)).pack()
    Label(logg,text="").pack()

    Button(logg,text="Ingresar efectivo",width="20",height="1",bg="#14549C", fg="white",font="bold",command=lambda: ingresar_efectivo(id)).pack()
    Label(logg,text="").pack()

    Button(logg,text="Retirar efectivo",width="20",height="1",bg="#14549C", fg="white",font="bold",command=lambda: retirar_efectivo(id)).pack()
    Label(logg,text="").pack()

    Button(logg,text="Transferir efectivo",width="20",height="1",bg="#14549C", fg="white",font="bold",command=lambda: transferir_efectivo(id)).pack()
    Label(logg,text="").pack()

    Button(logg,text="Consultar movimientos",width="20",height="1",bg="#14549C", fg="white",font="bold",command=lambda: consultar_movimientos(id)).pack()
    Label(logg,text="").pack()
    
    Button(logg, text="Salir",bg="red", fg="white", width=20, height=1, command=logg_destroy,font="bold").pack()

def consultarSaldo(id):
    sql = "SELECT balance FROM cuentas WHERE id = %s"
    mycur.execute(sql,[(id)])
    results = mycur.fetchall()
    if results:
        balance = results[0][0]
    print("balance",balance)
    
    global consultarSaldoWindow
    consultarSaldoWindow = Toplevel(root)
    consultarSaldoWindow.title("consultarSaldo")
    consultarSaldoWindow.geometry("500x500")
    
    Label(consultarSaldoWindow, text="consultarSaldo", bg="white", fg="black", font="bold",width=300).pack()
    Label(consultarSaldoWindow, text="").pack()
    Label(consultarSaldoWindow, text="El balance de tu cuenta es de ${} ".format(balance), fg="green", font="bold").pack()
    Button(consultarSaldoWindow, text="Ok",bg="#14549C", fg="white", width=8, height=1, command=succ_destroy3).pack()
    Label(consultarSaldoWindow, text="")

def ingresar_efectivo(id):
    global ingresarEfectivo
    global saldo
    ingresarEfectivo = Toplevel(root)
    ingresarEfectivo.title("ingresarEfectivo")
    ingresarEfectivo.geometry("500x500")
    Label(ingresarEfectivo, text="ingresarEfectivo", bg="white", fg="black", font="bold",width=300).pack()
    saldo = IntVar()
    
    Entry(ingresarEfectivo, textvariable=saldo).pack()
    
    Button(ingresarEfectivo, text="ingresarEfectivo",bg="#14549C", fg="white",command=lambda: ejecutarIngresoEfectivo(id), font="bold").pack()

def ejecutarIngresoEfectivo(id):
    value = saldo.get()
    print(value)

    sql = "UPDATE cuentas SET balance = balance + %s WHERE id = %s"
    t = (int(value), id)
    mycur.execute(sql, t)
    db.commit()
    time.sleep(0.5)

    now = datetime.datetime.now()

    sql = "INSERT INTO transacciones VALUES(DEFAULT,%s,%s,%s,%s)"
    t = (id, "Ingreso", int(value), now)
    mycur.execute(sql, t)
    db.commit()
    time.sleep(0.50)


    success2()

def retirar_efectivo(id):
    global retirarEfectivo
    global saldo
    retirarEfectivo = Toplevel(root)
    retirarEfectivo.title("retirar_efectivo")
    retirarEfectivo.geometry("500x500")
    Label(retirarEfectivo, text="retirar_efectivo", bg="white", fg="black", font="bold",width=300).pack()
    saldo = IntVar()
    
    Entry(retirarEfectivo, textvariable=saldo).pack()
    
    Button(retirarEfectivo, text="retirar_efectivo",bg="#14549C", fg="white",command=lambda: ejecutarRetiroEfectivo(id),font="bold").pack()

def ejecutarRetiroEfectivo(id):

    sql = "SELECT balance FROM cuentas WHERE id = %s"
    mycur.execute(sql,[(id)])
    results = mycur.fetchall()
    if results:
        balance = results[0][0]
    print("balance",balance)


    value = saldo.get()
    print(value)
    if value <= balance:
        sql = "UPDATE cuentas SET balance = balance - %s WHERE id = %s"
        t = (int(value), id)
        mycur.execute(sql, t)
        db.commit()
        time.sleep(0.5)

        now = datetime.datetime.now()
        sql = "INSERT INTO transacciones VALUES(DEFAULT,%s,%s,%s,%s)"
        t = (id, "Retiro", int(value) * -1, now)
        mycur.execute(sql, t)
        db.commit()
        time.sleep(0.50)


        success4()
    else:
        error2()

def transferir_efectivo(id):
    global transferirEfectivo
    global saldoTransferencia
    global cuentaDestino
    transferirEfectivo = Toplevel(root)
    transferirEfectivo.title("transferir_efectivo")
    transferirEfectivo.geometry("500x500")
    Label(transferirEfectivo, text="transferir_efectivo", bg="white", fg="black", font="bold",width=300).pack()
    saldoTransferencia = IntVar()
    
    Entry(transferirEfectivo, textvariable=saldoTransferencia).pack()

    Label(transferirEfectivo, text="cuentaDestino", bg="white", fg="black", font="bold",width=300).pack()
    cuentaDestino = StringVar()
    
    Entry(transferirEfectivo, textvariable=cuentaDestino).pack()
    
    Button(transferirEfectivo, text="transferir_efectivo",font="bold",bg="#14549C", fg="white",command=lambda: ejecutarTransferencia(id)).pack()

def ejecutarTransferencia(id):
    sql = "SELECT balance FROM cuentas WHERE id = %s"
    mycur.execute(sql,[(id)])
    results = mycur.fetchall()
    if results:
        balance = results[0][0]
    print("balance",balance)
    
    value = saldoTransferencia.get()
    print(value)

    idDestino = cuentaDestino.get()
    print(idDestino)

    print(value)
    if value <= balance:

        sql = "UPDATE cuentas SET balance = balance - %s WHERE id = %s"
        t = (int(value), id)
        mycur.execute(sql, t)
        db.commit()
        time.sleep(0.1)

        sql = "UPDATE cuentas SET balance = balance + %s WHERE id = %s"
        t = (int(value), idDestino)
        mycur.execute(sql, t)
        db.commit()
        time.sleep(0.1)


        now = datetime.datetime.now()
        sql = "INSERT INTO transacciones VALUES(DEFAULT,%s,%s,%s,%s)"
        t = (id, "Transferencia", int(value) * -1, now)
        mycur.execute(sql, t)
        db.commit()
        time.sleep(0.1)

        sql = "INSERT INTO transacciones VALUES(DEFAULT,%s,%s,%s,%s)"
        t = (idDestino, "Transferencia", int(value) , now)
        mycur.execute(sql, t)
        db.commit()
        time.sleep(0.1)

        success5()
    else:
        error3()


def consultar_movimientos(id):
    sql = "SELECT * FROM transacciones WHERE idCuenta = %s"
    mycur.execute(sql,[(id)])
    results = mycur.fetchall()

    global consultarMovimientosWindows
    consultarMovimientosWindows = Toplevel(root)
    consultarMovimientosWindows.title("consultarMovimientosWindows")
    consultarMovimientosWindows.geometry("1000x800")
    Label(consultarMovimientosWindows, text="consultarMovimientosWindows", bg="white", fg="black", font="bold",width=300).pack()
    Label(consultarMovimientosWindows, text="").pack()

    if results:
        for row in results:
            print(row)
            Label(consultarMovimientosWindows, text="Movimiento {} ".format(str(row[0]) + ":" +str(row[2]) + " por $"+ str(row[3]) + " realizada el " + str(row[4]) ), fg="green", font="bold").pack()

    Button(consultarMovimientosWindows, text="Ok",bg="#14549C", fg="white", width=8, height=1, command=succ_destroy6,font="bold").pack()
    Label(consultarMovimientosWindows, text="")



def failed():
    global fail
    fail = Toplevel(root2)
    fail.title("Credenciales invalidas")
    fail.geometry("500x500")
    Label(fail, text="Credenciales invalidas", fg="red", font="bold").pack()
    Label(fail, text="").pack()
    Button(fail, text="Ok",bg="#14549C", fg="white", width=8, height=1, command=fail_destroy).pack()


def login_varify():
    user_varify = username_varify.get()
    sql = "SELECT * FROM cuentas WHERE user = %s"
    mycur.execute(sql,[(user_varify)])
    results = mycur.fetchall()
    results = results[0]
    if results:
        logged(results)

    else:
        failed()


def main_screen():
    global root
    root = Tk()
    root.configure(bg='#14549C')
    root.title("Banca en linea")
    root.geometry("500x500")
    # root.eval('tk::PlaceWindow . center')
    Label(root,text="Bienvenido a tu banca en linea",font="bold",bg="white",fg="black",width=300).pack()
    Label(root,text="").pack()

    Button(root,text="Ingresa a tu cuenta",width="20",height="1",bg="white",font="bold",command=login,fg="#14549C").pack()
    Label(root,text="").pack()
    Button(root, text="Registrate con nosotros",height="1",width="20",bg="white",font="bold",command=registration,fg="#14549C").pack()
    Label(root,text="").pack()
    Label(root,text="").pack()
    Label(root,text="Desarrollado por Equipo 5").pack()

main_screen()
root.mainloop()