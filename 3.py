#مش عاوز اشغل التطبيق مباشره لا عاوز اشغله في متصفح 

#دي عشان اوصل بين الملفين 
import socket

from pywebio.input import input
from pywebio.output import put_text , put_buttons , put_html
from pywebio import start_server
#داله الاوامر 
def send_commands (msg):
    #امر af_inet ده ايبي فيرجن اربعه
    #sock_stream ده عباره عن تي سي بي
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client_socket:
        #السطر ده معناه انشئلي اتصال مع سيرفير الي بين علامه التنصيص  ولي جامبه البورت تقدر تحط اي رقم عادي 
        client_socket.connect (('localhost',77777))
        #معني السطر ده اني الي هكتب الاوامر
        client_socket.sendall(msg.encode('utf-8'))



def main ():
    put_html("<h1>cyber security learn<h1>")
    command = input("write commands : ",type='text')
    def send_command(e):
        send_commands(command)
        put_text(f"sended : {command}")
    put_buttons(['send'], onclick=send_command)

#عمل برمجيه بمجرد اني اشغلها ينذ الداله الي كتبتها وتشغيله كا وجهه اساسيه
if __name__ == '__main__' :
    #هنا هستدعي الداله الي بين قوسين الاوامر
    start_server (main , port=8080)