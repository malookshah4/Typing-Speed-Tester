import time
import tkinter as tk


window = tk.Tk()
window.title("Typing Speed")
window.geometry("800x400")

text_for_speed = "Typing is a valuable skill in today's digital age. Whether you're writing emails, creating documents, or chatting with friends, the ability to type quickly and accurately can save you time and improve your productivity."
start_time = 0
TIME_REMAINING = 20


def count_down(second=TIME_REMAINING):
    global start_time
    start_time = time.time()
    if second > 0:
        time_text.config(text=f"Time Remaining: {second} seconds")
        window.after(1000, count_down, second - 1)
    else:
        time_text.config(text="Time Up")
        generate_typing_speed()


def generate_typing_speed():
    global start_time
    tt = entry.get()
    word = len(tt.split(" "))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(word)
    print(elapsed_time)
    typing_speed = (word / TIME_REMAINING) * 60
    time_text.config(text=str(f"Your typing speed is : {typing_speed}"))
    entry.config(state="disabled")


def restart():
    entry.config(state="normal")
    entry.delete(0, tk.END)
    time_text.config(text=f"Time: {TIME_REMAINING} seconds")


text_to_be_typed = tk.Label(
    text=text_for_speed,
    font=("Arial", 15), wraplength=600, borderwidth=2, relief="groove", height=5)
text_to_be_typed.pack(side="top", anchor="w", padx=20, pady=20, fill=tk.X)

time_text = tk.Label(text=f"{TIME_REMAINING} seconds")
time_text.pack()
btn = tk.Button(text="Start Typing", command=count_down)
btn.pack()

btn = tk.Button(text="ReStart", command=restart)
btn.pack()

entry = tk.Entry(borderwidth=2, relief="groove", font=('Arial', 12))
entry.pack(fill=tk.X, pady=20, padx=20)

window.mainloop()
