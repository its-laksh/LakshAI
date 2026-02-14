import tkinter as tk

class AssistantGUI:
    def __init__(self, callback):
        self.callback = callback
        self.root = tk.Tk()
        self.root.title("Laksh - Offline Assistant")

        self.chat_area = tk.Text(self.root, height=20, width=60)
        self.chat_area.pack()

        self.input_field = tk.Entry(self.root, width=50)
        self.input_field.pack()

        self.send_button = tk.Button(self.root, text="Send",
                                     command=self.send_query)
        self.send_button.pack()

    def send_query(self):
        query = self.input_field.get()
        self.chat_area.insert(tk.END, f"\nYou: {query}")
        self.callback(query)
        self.input_field.delete(0, tk.END)

    def display_response(self, response):
        self.chat_area.insert(tk.END, f"\nLaksh: {response}")

    def run(self):
        self.root.mainloop()
