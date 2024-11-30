import tkinter as tk
from tkinter import messagebox
import random


quotes = [
    "The best way to get started is to quit talking and begin doing. - Walt Disney",
    "The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty. - Winston Churchill",
    "Don't let yesterday take up too much of today. - Will Rogers",
    "You learn more from failure than from success. Don't let it stop you. Failure builds character. - Unknown",
    "It's not whether you get knocked down, it's whether you get up. - Vince Lombardi",
]


favorites = []

def display_random_quote():
    """Display a random quote on the screen."""
    global current_quote
    current_quote = random.choice(quotes)
    quote_label.config(text=current_quote)

def save_to_favorites():
    """Save the current quote to the favorites list."""
    if current_quote not in favorites:
        favorites.append(current_quote)
        messagebox.showinfo("Saved", "Quote added to favorites!")
    else:
        messagebox.showinfo("Info", "This quote is already in your favorites.")

def view_favorites():
    """Display all saved favorite quotes."""
    if favorites:
        favorites_window = tk.Toplevel(app)
        favorites_window.title("Favorite Quotes")
        favorites_window.geometry("400x300")

        tk.Label(favorites_window, text="Your Favorite Quotes:", font=("Helvetica", 14, "bold")).pack(pady=10)
        for quote in favorites:
            tk.Label(favorites_window, text=quote, wraplength=350, justify="left", font=("Helvetica", 10)).pack(pady=5)
    else:
        messagebox.showinfo("No Favorites", "You haven't saved any quotes yet.")

def share_quote():
    """Simulate sharing the quote."""
    messagebox.showinfo("Share", f"Sharing this quote:\n\n{current_quote}")


app = tk.Tk()
app.title("Quote of the Day")
app.geometry("500x400")


current_quote = random.choice(quotes)
quote_label = tk.Label(app, text=current_quote, wraplength=400, justify="center", font=("Helvetica", 12), pady=20)
quote_label.pack()


tk.Button(app, text="New Quote", command=display_random_quote, width=15, bg="#4CAF50", fg="white", font=("Helvetica", 10)).pack(pady=10)
tk.Button(app, text="Save to Favorites", command=save_to_favorites, width=15, bg="#2196F3", fg="white", font=("Helvetica", 10)).pack(pady=10)
tk.Button(app, text="View Favorites", command=view_favorites, width=15, bg="#FFC107", fg="white", font=("Helvetica", 10)).pack(pady=10)
tk.Button(app, text="Share Quote", command=share_quote, width=15, bg="#F44336", fg="white", font=("Helvetica", 10)).pack(pady=10)


app.mainloop()
