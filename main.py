import customtkinter as ctk

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    window = ctk.CTk()
    window.title("Button Window")
    
    # Window Size:
    window.geometry("800x500")

    # Create a label widget in Tkinter
    label = ctk.CTkLabel(window, text="Hello World!", font=('Calibri', 15, 'bold'))
    label.pack(pady=20)

    window.mainloop()