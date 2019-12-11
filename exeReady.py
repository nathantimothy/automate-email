from tkinter import *
from tkinter import filedialog
import pandas as pd  # Load the Pandas libraries with alias 'pd'
import numpy as np  # Load the Numpy libraries with alias 'np'
import smtplib  # Load the smtplib (Simple Mail Transfer Protocol) libraries
import time  # Load the time libraries

root = Tk()  # Initialize window
root.geometry('260x210+500+250')  # Set size and position of window
root.title('Automate Emails')  # Set title of window
#root.iconbitmap(r'Email.ico')  # Set icon of window THIS STEP WILL BREAK IF YOU TRY AND CONVERT TO .EXE


def get_file_name():
    root.filename = filedialog.askopenfilename(initialdir="C:/", title="Select Automate Emails File")
    entry_filename.insert(0, root.filename)
    return root.filename # #


def send_emails():
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)  # Configure smtp_obj to Gmail server, connected on port 587 (TLS encryption)
    smtp_obj.ehlo()  # Establish a connection with the server
    smtp_obj.starttls()  # Enable TLS encryption for the connection
    smtp_obj.login(entry_email_address.get(), entry_app_password.get())  # Login to the Gmail SMTP server using your personal credentials
    data = pd.read_csv(entry_filename.get())  # Read Email list data from file
    data = np.array(data)  # Convert Data into an array
    numrows = len(data)  # Obtains length (in rows) of the array
    numspam = scale_spam.get()

    # Send Emails
    for j in range(numspam):
        if numspam>1:
            time.sleep(864/5)
        for i in range(numrows):
            ToName = data[i][0].split(" ")
            ToEmail = data[i][1]
            FromName = data[i][2].split(" ")
            FromEmail = data[i][3]
            Subject = data[i][4]
            Message = data[i][5]

            smtp_obj.sendmail('{0}'.format(FromEmail), '{0}'.format(ToEmail), 'Subject: {0}\n' 'Dear {1},\n\n''{2}\n\n' 'Love,\n\n' '{3}'.format(Subject,ToName[0],Message,FromName[0]))

    root.destroy()


label_email_address = Label(root, text='Email:', padx=10, pady=5)  # Create Widgets - email address label
label_app_password = Label(root, text='App Password:', padx=10, pady=5)  # Create Widgets - app password label
label_spam = Label(root, text='Select number of times you want to send:', padx=10, pady= 5)  # Create Widgets - spam label
entry_email_address = Entry(root)  # Create Widgets - email address entry
entry_app_password = Entry(root)  # Create Widgets - app password entry
entry_filename = Entry(root)  # Create Widgets - filename entry
button_go = Button(root, text='Go', command=send_emails)  # Create Widgets - go button
button_cancel = Button(root, text='Cancel', command=root.destroy)  # Create Widgets - cancel button
button_filename = Button(root, text='Browse to File...', command=get_file_name)  # Create Widgets - filename button
scale_spam = Scale(root, from_=1, to=500, orient=HORIZONTAL, length=200)  # Create Widgets - scale for spamming

button_go.config(height=1, width=10)  # Configure Widgets - go button
button_cancel.config(height=1, width=10)  # Configure Widgets - cancel button

label_email_address.grid(row=0, sticky=E)  # Place Widgets - email address label
label_app_password.grid(row=1, sticky=E)  # Place Widgets - app password label
label_spam.grid(row=3, columnspan=2)  # Place Widgets - spam label
entry_email_address.grid(row=0,column=1)  # Place Widgets - email address entry
entry_app_password.grid(row=1, column=1)  # Place Widgets - app password entry
entry_filename.grid(row=2, column=1)  # Place Widgets - filename entry
button_cancel.grid(row=5, column=1, padx=10, pady=10)  # Place Widgets - cancel button
button_go.grid(row=5, column=0, padx=10, pady=10)  # Place Widgets - go button
button_filename.grid(row=2, column=0, padx=10, pady=5)  # Place Widgets - filename button
scale_spam.grid(row=4, columnspan=2, padx=5)


root.mainloop()