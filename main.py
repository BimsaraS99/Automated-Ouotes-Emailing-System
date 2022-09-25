import smtplib
import datetime
import random

last_send_date = None
MSG_SEND_HOUR = 4


def send_email(quote):
    if len(quote) != 0:
        my_email = "pythonworks.bimsara@gmail.com"  # email and password of sender's e-mail
        my_email_pw = "mamaDoggy@99"

        sender_email = "ideapacklk@gmail.com"

        with smtplib.SMTP("smtp.gmail.com") as connection:  # connect with the Google email server
            connection.starttls()  # this secure our e-mail by encrypting the email
            connection.login(user=my_email, password=my_email_pw)  # loging to my email address
            connection.sendmail(from_addr=my_email, to_addrs=sender_email,
                                msg=f"Subject:Morning Motivation \n\n {quote}")


def get_quote():
    global last_send_date
    weekday = 0

    if weekday == 0:
        with open("quotes.txt") as quote_file:
            all_quotes = quote_file.readlines()
            quote = random.choice(all_quotes)
            quote_split = quote.split('-')
            send = quote_split[0] + "\n\n" + "- " + quote_split[1].strip('"')
            print(send)
            return send
    return ""


text = get_quote()
send_email(text)
