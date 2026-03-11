import smtplib

print("Testing SMTP connection...")

try:
    server = smtplib.SMTP("smtp.gmail.com", 587, timeout=10)
    server.starttls()
    print("SMTP Connected Successfully")
    server.quit()
except Exception as e:
    print("Error:", e)

print("Test Finished")