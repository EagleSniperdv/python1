#Program 2
#Name
#Manim Community v0.18.1

from manim import *

class AnimatedText(Scene):
    def construct(self):
        text1 = Text("MassBay is a good place to start!", font="Arial", color=BLUE).scale(0.8)
        self.play(Write(text1))
        self.wait(1)

        text2 = Text("I love college life", font="Times New Roman", color=RED).scale(1.2)
        self.play(Transform(text1, text2))
        self.wait(1)

        text3 = Text("Python is fantastic!", font="Comic Sans MS", color=GREEN).scale(1.0)
        self.play(Transform(text1, text3))
        self.wait(1)

        self.play(FadeOut(text1))  

if __name__ == "__main__":
    
    AnimatedText().render()
