from manim import *
import operator as op
class Example2Scene(Scene):
    def construct(self):
        box=self.get_box()
        dots=self.get_dots()
        self.add(
            box,
            dots,
        )
        self.wait(8)
    def get_box(self):
        box=self.box=Rectangle(width=6,height=4)
        return box
    def get_dots(self):
        points=np.array([
            [
                np.random.uniform(-3,3),
                np.random.uniform(-2,2),
                0
            ] for _ in range(2)
        ])
        dots=VGroup(*[
            Dot(radius=0.08).move_to(point) for point in points
        ])
        for dot in dots:
            dot.center=dot.get_center()
            dot.velocity=rotate_vector(
                np.random.uniform(0,5)*RIGHT,
                np.random.uniform(0,TAU)
            )
        dots.add_updater(self.update_particles)
        return dots
    def update_particles(self,particles,dt):
        for p1 in particles:
            p1.center+=p1.velocity*dt
            if(abs(p1.center[0])+0.08)>self.box.width/2:
                p1.center[0]=np.sign(p1.center[0])*(self.box.width/2-0.08)
                p1.velocity[0]*=-1*op.mul(np.sign(p1.velocity[0]),np.sign(p1.center[0]))
            elif (abs(p1.center[1])+0.08)>self.box.height/2:
                p1.center[1]=np.sign(p1.center[1])*(self.box.height/2-0.08)
                p1.velocity[1]*=-1*op.mul(np.sign(p1.velocity[1]),np.sign(p1.center[1]))
        for p in particles:
            p.move_to(p.center)