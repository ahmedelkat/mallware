#دي عشان اوصل بين الملفين 
import socket

#داله الاوامر 
def send_commands (msg):
    #امر af_inet ده ايبي فيرجن اربعه
    #sock_stream ده عباره عن تي سي بي
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client_socket:
        #السطر ده معناه انشئلي اتصال مع سيرفير الي بين علامه التنصيص  ولي جامبه البورت تقدر تحط اي رقم عادي 
        client_socket.connect (('localhost',12345))
        #معني السطر ده اني الي هكتب الاوامر
        client_socket.sendall(msg.encode('utf-8'))

#عمل برمجيه بمجرد اني اشغلها ينذ الداله الي كتبتها وتشغيله كا وجهه اساسيه
if __name__ == '__main__' :
    #هنا هستدعي الداله الي بين قوسين الاوامر
    send_commands ('update')