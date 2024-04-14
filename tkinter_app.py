import pickle
import tkinter as tk
from tkinter import messagebox

with open('best_model.pkl', 'rb') as f:
    svm_classifier = pickle.load(f)

with open('vectorizer_model.pkl', 'rb') as f:
    vectorizer = pickle.load(f)


def exit_app():
    """
    Exit app
    """
    root.quit()


def classify_email():
    """
    classify email
    """
    email_text = text_input.get("1.0", tk.END)

    if not email_text.strip():
        messagebox.showwarning("Classification result", "Please enter your email text.")
        return

    email_vectorized = vectorizer.transform([email_text])
    prediction = svm_classifier.predict(email_vectorized)

    if prediction[0] == 1:
        messagebox.showinfo("Classification result", "The email is spam!")
    else:
        messagebox.showinfo("Classification result", "Email is not spam.")


def resize_text_input(event):
    """
    resize text input on live
    """
    new_height = int(root.winfo_height() * 0.05)
    new_width = int(root.winfo_width() * 0.14)
    text_input.config(height=new_height, width=new_width)

root = tk.Tk()
root.title("Spam classifier")

root.minsize(500, 400)
window_width = 1000
window_height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

title_label = tk.Label(root, text="Spam classifier", font=("Helvetica", 16))
title_label.pack()

text_frame = tk.Frame(root)
text_frame.pack(pady=10)

text_label = tk.Label(text_frame, text="Enter your email text:", font=("Helvetica", 12))
text_label.pack()

text_input = tk.Text(text_frame)
text_input.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

classify_button = tk.Button(button_frame, text="Classify", command=classify_email)
classify_button.pack(side=tk.LEFT, padx=10)

exit_button = tk.Button(button_frame, text="Exit", command=exit_app)
exit_button.pack(side=tk.RIGHT, padx=10)

root.bind("<Configure>", resize_text_input)

root.mainloop()
