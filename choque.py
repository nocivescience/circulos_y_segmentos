from manim import *
class CrushScene(Scene):
    CONFIG={
        'starting':0
    }
    def construct(self):
        dots=self.get_points()
        self.add(dots)
        self.wait(4)
    def get_points(self):
        points=[3*RIGHT,5*LEFT]
        dots=VGroup(*[Dot().move_to(point) for point in points])
        dots[0].is_coloring=False
        def update_color(mob):
            dist=np.linalg.norm(mob.get_center()-dots[1].get_center())
            mob.will_coloring=(dist<1 and dist>-1)
            if  mob.will_coloring:
                mob.set_color(RED)
            else:
                mob.set_color(BLUE)

        def update_move(mob,dt):
            self.CONFIG['starting']+=3*dt
            mob.move_to(self.CONFIG['starting']*LEFT)
        dots[0].add_updater(update_color)
        dots[0].add_updater(update_move)
        return dots