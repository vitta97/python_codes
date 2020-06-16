import smtplib
import os
sender_email = "charanv@bbinsight.com"
rec_email = "vittajahnavi2000@gmail.com"
password = input(str("please enter your password: "))
message = "hey dis is charan"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("login sucess")
server.sendmail(sender_email,rec_email,message)
print("email has sent sucessfully to : ",rec_email)