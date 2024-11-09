import tkinter as tk
from tkinter import ttk

def count_words():
    text = text_area.get("1.0", "end-1c")
    wordcount = len(text.split())
    result_label.config(text=f"Word Count: {wordcount}")

# Create main window
window = tk.Tk()
window.title("Word Counter")

# Create text area for user input
text_area = tk.Text(window, wrap=tk.WORD)
text_area.pack(padx=10, pady=10, fill="both", expand=True)

# Create button to trigger word count
count_button = ttk.Button(window, text="Count Words", command=count_words)
count_button.pack(pady=10)

# Create label to display result
result_label = ttk.Label(window, text="")
result_label.pack()

window.mainloop()