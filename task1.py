import tkinter as tk
from tkinter import messagebox


def encrypt(text, shift):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


def encrypt_callback():
    text = txtMessage.get("1.0", "end-1c")
    shift = int(txtShift.get())
    result = encrypt(text, shift)
    txtResult.delete("1.0", "end")
    txtResult.insert("1.0", result)


def decrypt_callback():
    text = txtMessage.get("1.0", "end-1c")
    shift = int(txtShift.get())
    result = decrypt(text, shift)
    txtResult.delete("1.0", "end")
    txtResult.insert("1.0", result)


def reset_callback():
    txtMessage.delete("1.0", "end")
    txtShift.delete("0", "end")
    txtResult.delete("1.0", "end")


def exit_callback():
    root.destroy()


root = tk.Tk()
root.title("Encryption and Decryption Tool")
root.geometry("400x300")
root.configure(background="#f0f0f0")  # Light gray background

lblMessage = tk.Label(root, text="Message:", bg="#f0f0f0")
lblMessage.pack()

txtMessage = tk.Text(root, height=5, width=40, bg="#ffffff")  # White text box
txtMessage.pack()

lblShift = tk.Label(root, text="Shift:", bg="#f0f0f0")
lblShift.pack()

txtShift = tk.Entry(root, width=40, bg="#ffffff")  # White entry box
txtShift.pack()

btnEncrypt = tk.Button(root, text="Encrypt", command=encrypt_callback, bg="#007bff",
                       fg="#ffffff")  # Blue button with white text
btnEncrypt.pack(pady=10)

btnDecrypt = tk.Button(root, text="Decrypt", command=decrypt_callback, bg="#007bff",
                       fg="#ffffff")  # Blue button with white text
btnDecrypt.pack(pady=10)

lblResult = tk.Label(root, text="Result:", bg="#f0f0f0")
lblResult.pack()

txtResult = tk.Text(root, height=5, width=40, bg="#ffffff")  # White text box
txtResult.pack()

btnReset = tk.Button(root, text="Reset", command=reset_callback, bg="#007bff",
                     fg="#ffffff")  # Blue button with white text
btnReset.pack(pady=10)

btnExit = tk.Button(root, text="Exit", command=exit_callback, bg="#007bff", fg="#ffffff")  # Blue button with white text
btnExit.pack(pady=10)

root.mainloop()
