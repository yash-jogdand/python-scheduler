import smtplib
import os

my_email = os.environ.get("EMAIL_USER")
my_password = os.environ.get("EMAIL_PASS")

with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs='22110059@pvgcoet.ac.in',
        msg="Subject:Test\n\nHello from GitHub Actions!"
    )
