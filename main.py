class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class NoteManager:
    def __init__(self):
        self.notes = []

    def create_note(self):
        title = input("Введите заголовок заметки: ")
        content = input("Введите содержимое заметки: ")
        note = Note(title, content)
        self.notes.append(note)
        print("Заметка создана.")

    def save_notes(self):
        # Здесь может быть код сохранения заметок в файл или базу данных
        print("Заметки сохранены.")

    def read_notes(self):
        if not self.notes:
            print("Список заметок пуст.")
            return

        print("Список заметок:")
        for i, note in enumerate(self.notes, 1):
            print(f"Заметка #{i}")
            print(f"Заголовок: {note.title}")
            print(f"Содержимое: {note.content}")
            print()

    def edit_note(self):
        if not self.notes:
            print("Список заметок пуст.")
            return

        note_index = int(input("Введите номер заметки для редактирования: "))
        if note_index < 1 or note_index > len(self.notes):
            print("Неверный номер заметки.")
            return

        new_title = input("Введите новый заголовок заметки: ")
        new_content = input("Введите новое содержимое заметки: ")

        note = self.notes[note_index - 1]
        note.title = new_title
        note.content = new_content

        print("Заметка отредактирована.")

    def delete_note(self):
        if not self.notes:
            print("Список заметок пуст.")
            return

        note_index = int(input("Введите номер заметки для удаления: "))
        if note_index < 1 or note_index > len(self.notes):
            print("Неверный номер заметки.")
            return

        del self.notes[note_index - 1]
        print("Заметка удалена.")

note_manager = NoteManager()

while True:
    print("Выберите действие:")
    print("1. Создать заметку")
    print("2. Сохранить заметки")
    print("3. Просмотреть список заметок")
    print("4. Редактировать заметку")
    print("5. Удалить заметку")
    print("0. Выход")

    choice = int(input())

    if choice == 1:
        note_manager.create_note()
    elif choice == 2:
        note_manager.save_notes()
    elif choice == 3:
        note_manager.read_notes()
    elif choice == 4:
        note_manager.edit_note()
    elif choice == 5:
        note_manager.delete_note()
    elif choice == 0:
        break
    else:
        print("Неверный выбор. Попробуйте еще раз.")
