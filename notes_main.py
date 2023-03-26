#запомним одну фразу все будет но не сразу
import os

import json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit,QVBoxLayout,QMessageBox,QHBoxLayout,QTextEdit, QListWidget, QInputDialog


if not os.path.exists('note.json'):

    note = {
        "Пир":{
            'text':'Сидела девочка на трубе и думала о суюциде,труба взрывается ,газпром мечты збываются',
            'teg':["хихи"]
        },
        "Попка муровья":{
            'text':'Как дела',
            'teg':[]
        }
    }

    with open('note.json','w', encoding="utf-8") as file:
        json.dump(note, file)


#создание экрана1
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Умные заметки')
#левая часть
large_text_screen = QTextEdit('Это самое лучшее приложение для заметок в мире!')

#правая верхняя часть
list_of_notes = QLabel('Список заметок')
small_screen_note_list = QListWidget()
NSeve = QPushButton ('Cоздать заметку')
NDelit = QPushButton ('Удалить Заметку')
NCreate = QPushButton ('Сохранитьть Заметку')
#правая нижняя часть
tag_list = QLabel('Список тегов')
small_screen_tag_list = QListWidget()
screen_for_entering_tags =QLineEdit('Введите тег')
FSeve = QPushButton ('Добавить к Заметки')
FDelit = QPushButton ('Откреиь от Заметки')
FCreate = QPushButton ('Искать заметки по тегу')
#создание экрана2
left_layout_teg = QHBoxLayout()
left_layout_teg.addWidget(large_text_screen, alignment = Qt.AlignLeft)
right_layout_teg = QVBoxLayout()

right_layout_teg.addWidget(list_of_notes)
right_layout_teg.addWidget(small_screen_note_list)
upper_layout_teg = QHBoxLayout()

upper_layout_teg.addWidget(NDelit)
right_layout_teg.addWidget(NCreate)
upper_layout_teg.addWidget(NSeve)

right_layout_teg.addLayout(upper_layout_teg)
right_layout_teg.addWidget(tag_list)
right_layout_teg.addWidget(small_screen_tag_list)
right_layout_teg.addWidget(screen_for_entering_tags)

lower_layout_teg = QHBoxLayout()
lower_layout_teg.addWidget(FSeve)
lower_layout_teg.addWidget(FDelit)
right_layout_teg.addLayout(lower_layout_teg)
right_layout_teg.addWidget(FCreate)

left_layout_teg.addLayout(right_layout_teg)
main_win.setLayout(left_layout_teg)

def add_note():
    pass

def show_note():
    with open('note.json','r', encoding="utf-8") as file:
        note = json.load(file)
#получение название заметки из виджета Список заметок по которому кликнули
    name = small_screen_note_list.selectedItems()[0].text()
#отоброжение текста из заметок по которому кликнули
    large_text_screen.setText(note[name]["text"])
#удоление тегов
    small_screen_tag_list.clear()
#теги выброной заметки
    small_screen_tag_list.addItems(note[name]["teg"])

def create():
    note_name, result = QInputDialog.getText(
        main_win, "Добавить заметку","Название заметки:"
    )
    with open('note.json','r', encoding="utf-8") as file:
        note = json.load(file)
    note[note_name] = {
        'text':'',
        'teg':[]
    }
    with open('note.json','w', encoding="utf-8") as file:
        json.dump(note, file)
        small_screen_note_list.addItem(note_name)
NSeve.clicked.connect(create)

def delit():
    name = small_screen_note_list.selectedItems()[0].text()
    with open('note.json','r', encoding="utf-8") as file:
        note = json.load(file)
    del note [name]
    with open('note.json','w', encoding="utf-8") as file:
        json.dump(note, file)
    small_screen_note_list.clear()
    small_screen_note_list.addItems(note)
NDelit.clicked.connect(delit)

def seve():
    name = small_screen_note_list.selectedItems()[0].text()
    with open('note.json','r', encoding="utf-8") as file:
        note = json.load(file)
        note[name]['text'] = large_text_screen.toPlainText()
    with open('note.json','w', encoding="utf-8") as file:
        json.dump(note, file)

small_screen_note_list.itemClicked.connect(show_note)
NCreate.clicked.connect(seve)

with open('note.json','r', encoding="utf-8") as file:
    note = json.load(file)
def add_teg():
    name = small_screen_note_list.selectedItems()[0].text()
    with open('note.json','r', encoding="utf-8") as file:
        note = json.load(file)
        teg = screen_for_entering_tags.text()
        note[name]['teg'].append(teg)

    with open('note.json','w', encoding="utf-8") as file:
        json.dump(note, file)
    screen_for_entering_tags.clear()
    show_note()

FSeve.clicked.connect(add_teg)

def del_teg():
    name = small_screen_note_list.selectedItems()[0].text()
    with open('note.json','r', encoding="utf-8") as file:
        note = json.load(file)
    teg = small_screen_tag_list.selectedItems()[0].text()
    note[name]['teg'].remove(teg)

    with open('note.json','w', encoding="utf-8") as file:
        json.dump(note, file)
    screen_for_entering_tags.clear()
    show_note()

def search_teg():
    teg = screen_for_entering_tags.text()
    with open('note.json','r', encoding="utf-8") as file:
        notes = json.load(file)
    if FCreate.text() == "Искать заметки по тегу" and teg:
        note_filtered = {}
        for note in notes:
            if teg in notes[note]['teg']:
                note_filtered[note]=notes[note]
        FCreate.setText('Сбросить поиск')
        list_of_notes.clear()
        teg_list.clear()
        list_of_notes.addItems(note_filtered)
    elif FCreate.text() == "Сбросить поиск":
        screen_for_entering_tags.clear()
        list_of_notes.clear()
        teg_list.clear()
        list_of_notes.addItems(note)
        FCreate.setItems("Искать заметки по тегу")
    else:
        pass
FCreate.clicked.connect(search_teg)
FDelit.clicked.connect(del_teg)

small_screen_note_list.addItems(note)
#чтобы работоло все
main_win.show()
app.exec_()
#запомним одну фразу все будет но не сразу
