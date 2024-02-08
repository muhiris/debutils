from tkinter import *

def clicked(state, name):
    if state.get():
        print("Checked", name)
    else:
        print("Unchecked", name)

def checkbox(frame, text, row, column):
    chk_state = BooleanVar()
    chk_state.set(False)  # set check state
    chk = Checkbutton(
        frame,
        bg="#2E3436",  # Background color
        fg="#FFFFFF",  # Text color
        activebackground="#2E3436",  # No hover change
        activeforeground="#FFFFFF",
        font=("monospace", 11, "normal"),
        selectcolor="#2E3436",  # No focus/selection change
        text=text,
        var=chk_state,
        command=lambda: clicked(chk_state, name=text)
    )
    chk.grid(row=row, column=column, sticky=W, padx=5, pady=5)
    chk.config(highlightthickness=0, bd=0)

# create window and config
window = Tk()
window.title("Linux Utils - Muhiris")
window.configure(background='#2E3436')
window.geometry('500x300')

# Create a frame for checkboxes
checkbox_frame = Frame(window, bg="#2E3436")
checkbox_frame.pack(pady=10)

# Show checkboxes
columns_per_row = 4
for i, text in enumerate(["Alacritty", "Vim", "Alacritty", "Vim", "Alacritty", "Vim", "Alacritty", "Vim", "Alacritty", "Vim", "Alacritty", "Vim", "Alacritty", "sadsadas"]):
    checkbox(checkbox_frame, text, i // columns_per_row, i % columns_per_row)

# Add submit button at the end, bottom center
submit_button = Button(
    window,
    text="Submit",
    bg="#2E3436",
    fg="#FFFFFF",
    font=("monospace", 11, "normal"),
    command=window.quit  # Change this to your submit function
)
submit_button.pack(side="bottom", pady=10)

# Run main loop
window.mainloop()
