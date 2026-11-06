# Are you ready to tell your marks to the AI Asian Dad?
# Do it only if you are ready

import sys, os
import random
from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit, QLabel, QPushButton, QGridLayout, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFontDatabase

# THE INSULTS and "PRAISES"
PRAISE = [
    "{mark}%! I am so proud of you. Actually, I am so disappointed you didn't get 100, but the pride is bigger. Slightly.",
    "Wow, {mark}%! You know what this calls for? Nothing. Go back to studying.",
    "{mark}%! That's amazing! That's incredible! That's... still not as good as Athena's, but amazing!",
    "{mark}%? Okay. Okay! I'm not mad. I'm actually mad, but a different, quieter mad.",
    "{mark}%! I'm going to tell your uncle. He's going to be so happy for you. He's lying, but he'll say it.",
]

MILD_INSULTS = [
    "{mark}%?! WHAT. Actually, you know what, it's fine. It's FINE. (It is not fine.)",
    "{mark}%! Oh my goodness. Oh my goodness gracious. I'm calling the school. Actually I'm calling a different, better school.",
    "{mark}%?! Timmy got a 96 and he has THREE part-time jobs and he's also curing a disease!",
    "{mark}%! You know what this is? This is a scam. You scammed me out of {gap}%.",
    "{mark}%?! I didn't raise a {mark}-percent kid! I raised a NINETY-SEVEN percent kid, minimum!",
    "{mark}%! Interesting. Very interesting. You know who else got {mark}%? Nobody. Because everybody else got higher.",
    "{mark}%?! Okay so here's what's going to happen. Nothing good. That's what's going to happen.",
    "{mark}%! I'm not yelling. THIS is not yelling. You'll KNOW when I'm yelling.",
]

SEVERE_INSULTS = [
    "{mark}%?! WHAT DID YOU SAY? {mark}?! I heard 97 in my head just now because my brain refuses to accept this!",
    "{mark}%! Okay. OKAY. I'm calm. I'm very calm. I am SO calm that I already called your future employer to cancel your job. That's how calm I am.",
    "{mark}%?! You know what, forget medical school. Forget ALL school. Go be a street performer. At least THAT requires a skill you have.",
    "{mark}%! Timmy is eight years old and he just got accepted into a university that doesn't exist yet, and you got {mark}%!",
    "{mark}%?! I'm not upset. I'm actually SO not upset that I've already rewritten the will. Twice.",
    "{mark}%! You know what this number reminds me of? Nothing. Because I've never seen a number this low. Ever. In my life.",
    "{mark}%?! Okay, that's it. THAT. IS. IT. I'm not saying what 'it' is, but it's happening, and it's happening TONIGHT.",
    "{mark}%! I'm going to need you to say the number again, slower, so I can be disappointed at the correct speed.",
    "{mark}%?! You know how I know this is bad? I'm not even yelling. I've moved PAST yelling. I'm in a new emotion. It doesn't have a name yet.",
    "{mark}%! Congratulations! You've invented a new grade! It's called 'the grade that ends careers'!",
    "{mark}%?! I already emailed Athena's mom to apologize on your behalf. She said 'wow.' Just 'wow.' That's worse than yelling.",
    "{mark}%! You know what, I'm proud of you! I'm proud you found a way to score LOWER than I thought was mathematically possible!",
    "{mark}%?! That's it, we're moving. Not countries — just far enough that nobody at the reunion can find us.",
    "{mark}%! I want you to look me in the eyes and explain this number. Actually, no, I can't look at it OR you right now.",
    "{mark}%?! I'm not disappointed. Disappointed is for {gap} percent gaps I can FORGIVE. This is a different feeling. A historic feeling.",
    "{mark}%?! You are such a failure!!!! Even my shit can score more than that you moron!",
    "{mark}%? Look at Timmy your uncle's son he is a genius with 20 years of experience and he is 9!",
    "{mark}%? You are a total failure it is good that the founder of the subject you studied died way before you were born otherwise they would have died with disappointmnet in you r grades.",
    "{mark}%? You are Asian not Bsian, BOY" 
    "Why are you so STOOBID?"
]

# Window and Marks anaylser
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        current_dir = os.path.dirname(os.path.abspath(__file__))
        image = os.path.join(current_dir, "images.jpg")

        self.setWindowTitle("AI Asian Dad")
        self.setFixedSize(420, 260)
        self.setWindowIcon(QIcon(image)) # Get any image from google

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.grid = QGridLayout()
        central_widget.setLayout(self.grid)

        # Adding the Creepster Font to the font database 
        self.font_id = QFontDatabase.addApplicationFont("Creepster-Regular.ttf")
        self.family_name = QFontDatabase.applicationFontFamilies(self.font_id)[0]

        self.Label = QLabel("😈 TELL ME YOUR MARKS BOY 😈", self)
        self.Label.setStyleSheet("color:#0D0D0D;"
                                 "background-color:#FF0000;"
                                 "font-weight:bold;"
                                 f"font-family:'{self.family_name}';"
                                 "font-size:28px;")

        self.get_marks = QLineEdit()
        self.get_marks.setPlaceholderText("Marks Go Here")
        self.get_marks.setStyleSheet("color:black;"
                                     "background-color:white;"
                                     "font-family:Arial;"
                                     "font-size:18px;"
                                     "font-weight:bold;")
        
        self.tell = QPushButton("Say")
        self.tell.setStyleSheet("color:black;"
                               "background-color:red;"
                               f"font-family:'{self.family_name}';"
                               "font-weight:bold;"
                               "font-size:16px;")
        self.tell.clicked.connect(self.load_roast)

        self.roaster = QLabel("\t\tRemarks", self)
        self.roaster.setWordWrap(True)
        self.roaster.setFixedHeight(100)
        self.roaster.setFixedWidth(400)
        self.roaster.setStyleSheet("color:black;"
                                   "background-color:white;"
                                   f"font-family:'{self.family_name}';"
                                   "font-size:22px;")

        self.grid.addWidget(self.Label, 0, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)
        self.grid.addWidget(self.get_marks, 1, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)        
        self.grid.addWidget(self.tell, 2, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)
        self.grid.addWidget(self.roaster, 3, 0, 3, 3, Qt.AlignmentFlag.AlignCenter)

    # Getting the Roast and putting it in the roaster label
    def load_roast(self):
        try:         
            marks = self.get_marks.text()
            mark = float(marks)
            gap = round(100 - mark)

            if mark > 100:
                roast = f"Are you Timmy???😮😮Coz only Timmy can do {marks}%!!!"
                color = 'white'

                self.roaster.setText(roast)
                self.roaster.setStyleSheet(f"color: {color};"
                                           "background-color:black;"
                                           f"font-family:Arial;"
                                           "font-size:24px;"
                                           "font-weight:bold;")
                
            elif mark > 90 and mark <= 100:
                roast = random.choice(PRAISE).format(mark = marks, gap = gap)
                color = 'blue'
                
                self.roaster.setText(roast)
                self.roaster.setStyleSheet(f"color: {color};"
                                           "background-color:white;"
                                           f"font-family:Arial;"
                                           "font-size:20px;"
                                           "font-weight:bold;")
                
            elif mark <= 90 and mark > 50:
                roast = random.choice(MILD_INSULTS).format(mark = marks, gap = gap)
                color = 'green'

                self.roaster.setText(roast)
                self.roaster.setStyleSheet(f"color: {color};"
                                           "background-color:white;"
                                           "font-family:Arial;"
                                           "font-size:20px;"
                                           "font-weight:bold;")

            elif mark <= 50 and mark > 33.33:
                roast = random.choice(SEVERE_INSULTS).format(mark = marks, gap = gap)
                color = 'orange'

                self.roaster.setText(roast)
                self.roaster.setStyleSheet(f"color: {color};"
                                           "background-color:red;"
                                           f"font-family:'{self.family_name}';"
                                           "font-size:20px;"
                                           "font-weight:bold;")

            elif mark <= 33.33:
                roast = random.choice(SEVERE_INSULTS).format(mark = marks, gap = gap)
                color = 'black'

                self.roaster.setText(roast)
                self.roaster.setStyleSheet(f"color: {color};"
                                           "background-color:red;"
                                           f"font-family:'{self.family_name}';"
                                           "font-size:20px;"
                                           "font-weight:bold;")

        except:
            roast = "Hello Uncle Roger, this kid is so stoobid that he enters random shit when asked for marks 🤣🤣🤣🤣🤣"
            color = 'black'

            self.roaster.setText(roast)
            self.roaster.setStyleSheet(f"color: {color};"
                                       "background-color:white;"
                                       f"font-family:Arial;"
                                       "font-size:20px;"
                                       "font-weight:bold;")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()