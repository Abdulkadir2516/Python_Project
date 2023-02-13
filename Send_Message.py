import pywhatkit
import datetime as dt
import time

# bu uygulama whatsapp web üserinden mesaj göndermektedir bu proje kapsamında ilerleyen zamanlarda api ile göndermesinin planlıyorum

to_number = "+905555555555" # gönderilmek istenen tel number
send_time = "21:00" # gönderim zamanı
msg = "Günaydın" # gönderilen mesaj

send_hour = int(send_time.split(":")[0])
send_minute = int(send_time.split(":")[1])

send_time_ = dt.datetime.now().replace(hour=send_hour, minute = send_minute, second=0, microsecond=0 )

if send_time_ < dt.datetime.now():
    tomorrow = dt.date.today() + dt.timedelta(days = 1)
    send_time_ = dt.datetime.combine(tomorrow, dt.time(send_hour,send_minute))


later_1min = send_time_ + dt.timedelta(minutes=1)

while True:
    
    now = dt.datetime.now()
    
    if now.hour == send_hour and now.minute == send_minute and now.day == send_time_.day:
        
        pywhatkit.sendwhatmsg(to_number, msg, send_hour, send_minute+1)
        
        print("Message Gönderildi")
        
        tomorrow = dt.date.today() + dt.timedelta(days = 1)
        send_time_ = dt.datetime.combine(tomorrow, dt.time(send_hour,send_minute))
        later_1min = send_time_ + dt.timedelta(minutes=1)
    
    
    time.sleep(10)


input()
