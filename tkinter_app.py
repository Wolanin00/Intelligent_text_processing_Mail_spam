import pickle
import tkinter as tk
from tkinter import messagebox


# Load the saved model
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
    # Get the email text entered by the user
    email_text = text_input.get("1.0", tk.END)

    if not email_text.strip():
        messagebox.showwarning("Wynik klasyfikacji", "Proszę wprowadzić tekst e-maila.")
        return

    # Vectorize the email text
    email_vectorized = vectorizer.transform([email_text])

    # Classify the email text
    prediction = svm_classifier.predict(email_vectorized)

    # Display the classification result
    if prediction[0] == 1:
        messagebox.showinfo("Wynik klasyfikacji", "E-mail jest spamem!")
    else:
        messagebox.showinfo("Wynik klasyfikacji", "E-mail nie jest spamem.")


def resize_text_input(event):
    """
    resize text input on live
    """
    new_height = int(root.winfo_height() * 0.05)
    new_width = int(root.winfo_width() * 0.14)
    text_input.config(height=new_height, width=new_width)


# Initialize main window
root = tk.Tk()
root.title("Klasyfikator Spam")

# Ustawienie minimalnych wymiarów okna
root.minsize(500, 400)

# Ustalenie położenia okna
window_width = 1000
window_height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Title label
title_label = tk.Label(root, text="Klasyfikator Spam", font=("Helvetica", 16))
title_label.pack()

# Frame for text input
text_frame = tk.Frame(root)
text_frame.pack(pady=10)

# Label for text input
text_label = tk.Label(text_frame, text="Wprowadź tekst e-maila:", font=("Helvetica", 12))
text_label.pack()

# Text input for email text
text_input = tk.Text(text_frame)
text_input.pack()

# Frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Classify button
classify_button = tk.Button(button_frame, text="Klasyfikuj", command=classify_email)
classify_button.pack(side=tk.LEFT, padx=10)

# Exit button
exit_button = tk.Button(button_frame, text="Wyjście", command=exit_app)
exit_button.pack(side=tk.RIGHT, padx=10)

root.bind("<Configure>", resize_text_input)

# Run the main GUI loop
root.mainloop()
