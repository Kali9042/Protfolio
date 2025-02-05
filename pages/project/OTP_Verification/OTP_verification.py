import random
import smtplib
import tkinter as tk
from tkinter import messagebox

# Email and password for sending OTP
EMAIL_ADDRESS = "harvesthub99@gmail.com"
PASSWORD = "wexg hawf pidd fify"

# Function to send email with OTP
def send_email(receiver_email, otp):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL_ADDRESS, PASSWORD)

    body = f"Dear {name_entry.get()},\n\nYour OTP is {otp}."
    subject = "OTP verification"
    message = f'subject:{subject}\n\n{body}'
    
    server.sendmail(EMAIL_ADDRESS, receiver_email, message)
    server.quit()

# Function to validate email format
def email_verification(receiver_email):
    email_check1 = ["gmail", "hotmail", "yahoo", "outlook"]
    email_check2 = [".com", ".in", ".org", ".edu", ".co.in"]
    count = 0

    for domain in email_check1:
        if domain in receiver_email:
            count += 1
    for site in email_check2:
        if site in receiver_email:
            count += 1

    return "@" in receiver_email and count == 2

# Function to handle OTP generation and verification
def generate_otp():
    receiver_email = email_entry.get()
    if not email_verification(receiver_email):
        messagebox.showerror("Error", "Invalid email id. Please enter a valid email.")
        return

    global OTP
    OTP = random.randint(100000, 999999)
    send_email(receiver_email, OTP)
    messagebox.showinfo("Info", f"OTP has been sent to {receiver_email}")
    
    otp_window()

# Function to resend OTP
def resend_otp():
    generate_otp()

# Function to create the OTP entry window with individual boxes for each digit
def otp_window():
    otp_win = tk.Toplevel(root)
    otp_win.title("Enter OTP")
    
    tk.Label(otp_win, text="Enter OTP:").pack(pady=10)

    # Create a list to hold the entry boxes
    global otp_entries
    otp_entries = []

    # Create 6 entry boxes for a 6-digit OTP
    for i in range(6):
        entry = tk.Entry(otp_win, width=2, font=('Arial', 24), justify='center')
        entry.pack(side=tk.LEFT, padx=5)
        otp_entries.append(entry)

    # Set focus on the first entry box
    otp_entries[0].focus()

    # Bind the event to move to the next box on entry
    for i in range(6):
        otp_entries[i].bind("<KeyRelease>", lambda event, index=i: move_focus(event, index))

    tk.Button(otp_win, text="Verify OTP", command=verify_otp).pack(pady=20)
    tk.Button(otp_win, text="Resend OTP", command=resend_otp).pack(pady=5)  # Resend OTP button

# Function to handle focus movement
def move_focus(event, index):
    if event.char.isdigit() and index < 5:
        otp_entries[index + 1].focus()
    elif event.keysym == "BackSpace" and index > 0:
        otp_entries[index - 1].focus()

# Function to verify the OTP
def verify_otp():
    entered_otp = ''.join(entry.get() for entry in otp_entries)
    if entered_otp.isdigit() and int(entered_otp) == OTP:
        messagebox.showinfo("Success", "OTP verified successfully!")
    else:
        messagebox.showerror("Error", "Invalid OTP. Please try again.")

# Main UI setup
root = tk.Tk()
root.title("OTP Verification")

tk.Label(root, text="Enter Name:").pack(pady=10)
name_entry = tk.Entry(root)
name_entry.pack(pady=10)

tk.Label(root, text="Enter Email ID:").pack(pady=10)
email_entry = tk.Entry(root)
email_entry.pack(pady=10)

tk.Button(root, text="Send OTP", command=generate_otp).pack(pady=20)

root.mainloop()
