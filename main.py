import qrcode
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk, messagebox


class QRCodeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title('QR Code Generator')

        # Create widgets
        self.create_widgets()
    
    def create_widgets(self):
        label = ttk.Label(self.root, text="Enter text or URL:")
        label.grid(row=0, column=0, sticky='W', padx=10, pady=10)

        self.text_entry = ttk.Entry(self.root, width=40)
        self.text_entry.grid(row=0, column=1, sticky='WE', padx=10)

        generate_button = ttk.Button(self.root, text="Generate", command=self.generate_qrcode)
        generate_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.image_label = ttk.Label(self.root)
        self.image_label.grid(row=2, column=0, columnspan=2, pady=10)

    def generate_qrcode(self):
        text = self.text_entry.get()
        if not text:
            messagebox.showerror("Error", "The text field cannot be empty.")
            return

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img_tk = ImageTk.PhotoImage(img)

        self.image_label.configure(image=img_tk)
        self.image_label.image = img_tk  # Keep a reference!


if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGenerator(root)
    root.mainloop()
