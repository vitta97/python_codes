port smtplib
import config
import pandas as pd
e = pd.read_csv("C:/Users/vchar/OneDrive/Documents/emails.txt")
emails = e["Emails"].values
server = stmplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login("vcharan957@gmail.com","9676647188")
msg = "hi this is charan"
subject = "hello! this mail is mail is for testing"
body = "Subject {}\n\n{}".format(subject,msg)
for email in emails:
    server.sendmail("vcharan957@gmail.com",email,body)
    print("Sucessfull")
server.quit()