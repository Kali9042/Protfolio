import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import messagebox
import schedule
import time
import threading

# Email Configuration
sender_email = "your_email@gmail.com"
password = "your_password"

def send_email():
    receiver_email = receiver_entry.get()
    subject = subject_entry.get()
    body = body_entry.get("1.0", tk.END)

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email. Error: {str(e)}")

def schedule_email():
    time_str = time_entry.get()
    schedule.every().day.at(time_str).do(send_email)
    threading.Thread(target=run_schedule).start()
    messagebox.showinfo("Success", f"Email scheduled for {time_str} daily")

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Create GUI
root = tk.Tk()
root.title("Email Automation")

tk.Label(root, text="Receiver Email:").grid(row=0, column=0)
receiver_entry = tk.Entry(root, width=40)
receiver_entry.grid(row=0, column=1)

tk.Label(root, text="Subject:").grid(row=1, column=0)
subject_entry = tk.Entry(root, width=40)
subject_entry.grid(row=1, column=1)

tk.Label(root, text="Body:").grid(row=2, column=0)
body_entry = tk.Text(root, height=10, width=30)
body_entry.grid(row=2, column=1)

tk.Label(root, text="Send Time (HH:MM):").grid(row=3, column=0)
time_entry = tk.Entry(root, width=10)
time_entry.grid(row=3, column=1)

send_button = tk.Button(root, text="Send Email Now", command=send_email)
send_button.grid(row=4, column=0)

schedule_button = tk.Button(root, text="Schedule Email", command=schedule_email)
schedule_button.grid(row=4, column=1)

root.mainloop()
