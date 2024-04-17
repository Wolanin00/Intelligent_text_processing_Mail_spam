import pickle
import tkinter as tk
from tkinter import messagebox
from pathlib import Path


class SpamClassifierApp:
    def __init__(self, master):
        self.master = master
        master.title("Spam classifier")
        master.minsize(500, 400)
        window_width = 800
        window_height = 600
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        master.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        self.title_label = tk.Label(master, text="Spam classifier", font=("Helvetica", 16))
        self.title_label.pack()

        self.text_frame = tk.Frame(master)
        self.text_frame.pack(pady=10)

        self.text_label = tk.Label(self.text_frame, text="Enter your email text:", font=("Helvetica", 12))
        self.text_label.pack()

        self.text_input = tk.Text(self.text_frame)
        self.text_input.pack()

        self.button_frame = tk.Frame(master)
        self.button_frame.pack(pady=10)

        self.classify_button = tk.Button(self.button_frame, text="Classify", command=self.classify_email)
        self.classify_button.pack(side=tk.LEFT, padx=10)

        self.exit_button = tk.Button(self.button_frame, text="Exit", command=self.exit_app)
        self.exit_button.pack(side=tk.RIGHT, padx=10)

        self.master.bind("<Configure>", self.resize_text_input)

        # Load the models
        with open(Path(__file__).resolve().parent / "best_model.pkl", "rb") as f:
            self.svm_classifier = pickle.load(f)

        with open(Path(__file__).resolve().parent / "vectorizer_model.pkl", "rb") as f:
            self.vectorizer = pickle.load(f)

    def exit_app(self):
        """
        Exit app
        """
        self.master.quit()

    def classify_email(self):
        """
        Classify email
        """
        email_text = self.text_input.get("1.0", tk.END)

        if not email_text.strip():
            messagebox.showwarning("Classification result", "Please enter your email text.")
            return

        email_vectorized = self.vectorizer.transform([email_text])
        prediction = self.svm_classifier.predict(email_vectorized)

        if prediction[0] == 1:
            messagebox.showinfo("Classification result", "The email is spam!")
        else:
            messagebox.showinfo("Classification result", "Email is not spam.")

    def resize_text_input(self, event):
        """
        Resize text input on live
        """
        new_height = int(self.master.winfo_height() * 0.05)
        new_width = int(self.master.winfo_width() * 0.14)
        self.text_input.config(height=new_height, width=new_width)


if __name__ == "__main__":
    root = tk.Tk()
    app = SpamClassifierApp(root)
    root.mainloop()
