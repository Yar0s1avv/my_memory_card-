from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QGroupBox,
    QButtonGroup,
    QRadioButton,
    QPushButton,
    QLabel,
)
from random import *



#Класс для хранения данных о вопросе
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3



questions_list = list()

q1 = Question("Какой самый лучший язык программирования?", "python", "javascript", "c++", "pascal")
q2 = Question("Какой цвет кожи больше всего принежали?", "Чёрный", "Белый", "Жёлтый", "Крсный")

questions_list.append(q1)
questions_list.append(q2)


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Memory Card")
main_win.resize(300, 300)

main_win.totol = 0
main_win.scor = 0

text_question = QLabel("Какой цвет кожи больше всего принежали?")
btn_answer = QPushButton("Ответить")

# Начало Группы вопроса
RadioGroupBox = QGroupBox("Варианты ответов")


rbtn1 = QRadioButton("Чёрный")
rbtn2 = QRadioButton("Белый")
rbtn3 = QRadioButton("Жёлтый")
rbtn4 = QRadioButton("Крсный")

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

group_vline1 = QVBoxLayout()
group_vline2 = QVBoxLayout()
group_main = QHBoxLayout()

group_vline1.addWidget(rbtn1, alignment=Qt.AlignLeft)
group_vline1.setSpacing(50)
group_vline1.addWidget(rbtn2, alignment=Qt.AlignLeft)
group_vline2.addWidget(rbtn3, alignment=Qt.AlignRight)
group_vline2.setSpacing(50)
group_vline2.addWidget(rbtn4, alignment=Qt.AlignRight)

group_main.addLayout(group_vline1)
group_main.setSpacing(50)
group_main.addLayout(group_vline2)

RadioGroupBox.setLayout(group_main)
# Конец группы вопроса
AnsGroupBox = QGroupBox("Результат теста")
text_answer = QLabel("Правильно/Неправильно")
right_answer = QLabel("")

ans_main_line = QVBoxLayout()
ans_main_line.addWidget(text_answer, alignment=Qt.AlignLeft)
ans_main_line.setSpacing(30)
ans_main_line.addWidget(right_answer, stretch=10)

AnsGroupBox.setLayout(ans_main_line)
AnsGroupBox.hide()

layout_main = QVBoxLayout()
layout_main.addSpacing(10)

layout_main.addWidget(text_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_main.addSpacing(20)
layout_main.addWidget(RadioGroupBox, alignment=Qt.AlignCenter)
layout_main.addWidget(AnsGroupBox, alignment=Qt.AlignCenter)
layout_main.addSpacing(50)
layout_main.addWidget(btn_answer, stretch=2)

answers = [rbtn1, rbtn2, rbtn3, rbtn4]

cur_question = ''

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_answer.setText("Ответить")

    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_answer.setText("Следующий вопрос")


def ask(q):
    shuffle(answers)  # [rbtn2, rbtn3, rbtn1, rbtn4]
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    text_question.setText(q.question)
    show_question()


def show_correct(result):
    print('Статистика:')
    print('Количество вопросов', main_win.totol)
    print('Количество правельных ответов', main_win.scor)
    print('Рейтинг:', (main_win.scor/main_win.totol) * 100)

    text_answer.setText(result)
    right_answer.setText(questions_list[cur_question].right_answer)
    show_result()

def next_question():
    main_win.totol += 1
    global cur_question
    cur_question = randint(0, len(questions_list) -1)
    ask(questions_list[cur_question])

def check_answer():
    if answers[0].isChecked() == True:
        main_win.scor += 1
        show_correct("Правильно!")
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            # неправильный ответ!
            show_correct("Неверно!")

def click_ok():
    if btn_answer.text() == "Ответить":
        check_answer()
    else:
        next_question()


btn_answer.clicked.connect(click_ok)


main_win.setLayout(layout_main)

next_question()

main_win.show()
app.exec_()
