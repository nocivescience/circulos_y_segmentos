from manim import *
class CircleSegmentScene(Scene):
    CONFIG={
        'radio':3
    }
    def construct(self):
        dots=self.get_point_mobs()
        lines=self.getting_lines()
        triangles=self.get_triangle()
        for mob in [
            dots,
            lines,
        ]:
            self.play(Create(mob))
        triangle_anims=self.get_triangle_update(
            np.array(list(map(Mobject.get_center,dots))),triangles
        )
        self.play(triangle_anims)
        self.wait()
    def get_point_mobs(self):
        points=self.points=np.array([
            ORIGIN+rotate_vector(self.CONFIG['radio']*RIGHT,theta) for theta in np.random.random(size=3)*TAU
        ])
        dots=VGroup(*[
            Dot().move_to(point).set_z_index(3) for point in points
        ])
        self.dots=dots
        return dots
    def getting_lines(self):
        angles=self.get_point_mob_angles()
        lines=VGroup()
        for angle in angles:
            line=Line(
                self.CONFIG['radio']*RIGHT,self.CONFIG['radio']*LEFT
            )
            line.rotate(angle)
            line.shift(ORIGIN)
            line.set_color(RED)
            line.set_z_index(-1)
            lines.add(line)
        self.lines=lines
        return lines
    def get_point_mob_angles(self):
        points_mob=self.dots
        points=[pm.get_center() for pm in points_mob]
        return np.array(list(map(angle_of_vector,points)))
    def get_triangle(self):
        triangle=self.triengle=RegularPolygon(n=3)
        triangle.set_stroke(BLUE)
        return triangle
    def get_triangle_update(self,points_mob,triangle):
        def update_triangle(triangle):
            points=[pm for pm in points_mob]
            triangle.set_points_as_corners(points)
            return triangle
        return UpdateFromFunc(triangle,update_triangle)