#Program 4
#Name
#Manim Community v0.18.1


from manim import *
class Transformations(Scene):
    def construct(self):
        
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 5, 1],
            x_length=6,
            y_length=6,
            axis_config={"color": BLUE},
        )
        self.play(Create(axes))

        # Create the quadratic curve f(x) = x^2
        graph_curve = self.get_graph_curve()
        graph = ParametricFunction(lambda t: [t, t**2, 0], t_range=[-3, 3], color=GREEN)
        self.play(Create(graph))

        
        transformations = [
            lambda x: (x - 1, (x - 1)**2),  
            lambda x: (x + 2, (x + 2)**2 + 1),  
            lambda x: (x, x**2 + 3),  
        ]
        transformed_graphs = [
            self.get_transformed_graph(graph_curve, transform)
            for transform in transformations
        ]
        self.play(*[Create(g) for g in transformed_graphs])

        
        labels = [
            Text("Shift left by 1", font_size=24).shift(UP * 3),
            Text("Shift right by 2 and up by 1", font_size=24).shift(UP * 1),
            Text("Shift up by 3", font_size=24).shift(DOWN * 2),
        ]
        self.play(*[Write(label) for label in labels])

        self.wait(2)  

    def get_graph_curve(self):
        graph_points = [(x, x**2, 0) for x in np.linspace(-3, 3, 100)]
        graph_curve = VMobject()
        graph_curve.set_points_smoothly([*graph_points, graph_points[0]])
        return graph_curve

    def get_transformed_graph(self, graph_curve, transform):
        transformed_points = [(*transform(point[0]), point[1]) for point in graph_curve.points]
        transformed_graph = VMobject()
        transformed_graph.set_points_smoothly([*transformed_points, transformed_points[0]])
        return ParametricFunction(lambda t: [t, t**2, 0], t_range=[-3, 3])

if __name__ == "__main__":
    Transformations().render()
