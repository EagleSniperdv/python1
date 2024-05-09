#Program 3
#Name
#Manim Community v0.18.1

from manim import *

class AnimatedFormulas(Scene):
    def construct(self):
        
        formula1 = Text("a² + b² = c²", font_size=48).shift(UP*1)
        self.play(Write(formula1))
        self.wait(1)

        formula2 = Text("E = mc²", font_size=48).shift(DOWN*1)
        self.play(Transform(formula1, formula2))
        self.wait(1)

        
        self.play(formula1.animate.scale(1.2).shift(LEFT*2), run_time=2)
        self.play(formula1.animate.scale(0.8).shift(RIGHT*4), run_time=2)
        self.play(formula1.animate.scale(1.0).shift(UP*2 + LEFT*2), run_time=2)
        self.wait(1)

        self.play(FadeOut(formula1))  

if __name__ == "__main__":
    

    AnimatedFormulas().render()
