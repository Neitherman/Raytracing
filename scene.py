import camera
import object

class Scene:

    def __init__(self, ambient_light):
        self.camera = None
        self.objects = []
        self.lights = []
        self.ambient = ambient_light
        self.image = None

    def add_camera(self, cam):
        self.camera = cam

    def add_object(self, object):
        self.objects.append(object)

    def add_light(self, light):
        self.lights.append(light)

    def radius_intersect(self):
        pass

    def render(self):
        pass


if __name__ == "__main__":
    pass
