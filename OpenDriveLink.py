import tkinter as tk
import webbrowser

def open_browser():
    # Text input ko get karna aur "search it" ke sath combine karna
    query = entry.get()
    url = f"https://www.google.com/search?q={query} site:drive.google.com"
    
    # Browser me URL open karna
    webbrowser.open(url)

# Tkinter window setup
root = tk.Tk()
root.title("Search Drive Links")
root.geometry("300x150")

# Text input field
label = tk.Label(root, text="Type your query:")
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Search button
search_button = tk.Button(root, text="Search", command=open_browser)
search_button.pack(pady=10)

root.mainloop()
