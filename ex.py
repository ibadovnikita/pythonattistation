import tkinter as tk

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Приложение заметок")

        self.notes_frame = tk.Frame(self.root)
        self.notes_frame.pack(pady=10)

        self.title_label = tk.Label(self.notes_frame, text="Заголовок:")
        self.title_label.grid(row=0, column=0, padx=10, pady=10)

        self.title_entry = tk.Entry(self.notes_frame, width=30)
        self.title_entry.grid(row=0, column=1, padx=10, pady=10)

        self.content_label = tk.Label(self.notes_frame, text="Содержание:")
        self.content_label.grid(row=1, column=0, padx=10, pady=10)

        self.content_entry = tk.Text(self.notes_frame, width=30, height=10)
        self.content_entry.grid(row=1, column=1, padx=10, pady=10)

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=10)

        self.create_button = tk.Button(self.buttons_frame, text="Создать заметку", command=self.create_note)
        self.create_button.grid(row=0, column=0, padx=10)

        self.display_button = tk.Button(self.buttons_frame, text="Отобразить заметки", command=self.display_notes)
        self.display_button.grid(row=0, column=1, padx=10)

        self.notes = []

    def create_note(self):
        title = self.title_entry.get()
        content = self.content_entry.get("1.0", tk.END)
        note = Note(title, content)
        self.notes.append(note)
        self.title_entry.delete(0, tk.END)
        self.content_entry.delete("1.0", tk.END)

    def display_notes(self):
        display_window = tk.Toplevel(self.root)
        display_window.title("Отображение заметок")

        notes_frame = tk.Frame(display_window)
        notes_frame.pack(pady=10)

        for index, note in enumerate(self.notes):
            title_label = tk.Label(notes_frame, text=f"Заметка #{index+1}")
            title_label.pack()

            content_label = tk.Label(notes_frame, text=note.title)
            content_label.pack()

            content_text = tk.Text(notes_frame, width=30, height=10)
            content_text.insert(tk.END, note.content)
            content_text.pack()

if __name__ == "__main__":
    root = tk.Tk()
    note_app = NoteApp(root)
    root.mainloop()