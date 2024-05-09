#Program 1
#Name
#Manim Community v0.18.1

from manim import *

class TriangleToCircle(Scene):
    def construct(self):
        
        triangle = Polygon(
            np.array([-2, 0, 0]), 
            np.array([0, 2, 0]), 
            np.array([2, 0, 0]),
            color=BLUE
        )
        self.play(Create(triangle))

        circle = Circle(radius=1, color=RED)
        self.play(Transform(triangle, circle))

        self.wait(1)

if __name__ == "__main__":
    
    TriangleToCircle().render()
