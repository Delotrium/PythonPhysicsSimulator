import pyglet
from pyglet import *
from pyglet.window import key
from pyglet.window import mouse
import pymunk
import pymunk.pyglet_util
import time

#Import Settings
from settings import *
from environment import *

music = Music

pyglet.options['audio'] = ('openal', 'pulse', 'directsound', 'silent')
pyglet.options['search_local_libs'] = True
window = pyglet.window.Window(windowSizeX, windowSizeY, "Physics Simulation", resizable=True, visible=False)
#window.set_icon(pyglet.image.load("icon.png"))
options = pymunk.pyglet_util.DrawOptions()
batch = pyglet.graphics.Batch()

if music:
    music = pyglet.resource.media(MusicPath)
    music.play()

space = pymunk.Space()
if gravityFlip == True:
    gravityValue = -gravityValue
space.gravity = 1, gravityValue

mass = ballMass
radius = ballRadius
sprites = []

sound = pyglet.resource.media(SoundPath, streaming=False)

label = pyglet.text.Label('',font_name='Times New Roman',font_size=36,x=window.width//2, y=window.height//2,anchor_x='center', anchor_y='center', color=(128,128,128,128))

window.set_mouse_visible(True)
cursor = window.get_system_mouse_cursor(window.CURSOR_DEFAULT)
window.set_mouse_cursor(cursor)

i = 0

while i < Shape_Amount:
    segment_shape = pymunk.Segment(space.static_body, (ShapeList[i][0] ,ShapeList[i][1]), (ShapeList[i][2],ShapeList[i][3]), StrokeThickness)
    segment_shape.body.position = 100  , 100  
    segment_shape.elasticity = 1 * ElasticityMultiplier
    segment_shape.friction = 1.0 * FrictionMultiplier
    space.add(segment_shape)
    i += 1

@window.event
def on_draw():
    window.clear()
    #label.draw()
    space.debug_draw(options)

@window.event
def on_mouse_press(x, y, button, modifiers):
        sound.play()
        if Shape == "circle":
            circle_moment = pymunk.moment_for_circle(mass, 1, radius)
            circle_body = pymunk.Body(mass, circle_moment)
            circle_body.position = x, y
            circle_shape = pymunk.Circle(circle_body,radius)
            circle_shape.elasticity = psi * ElasticityMultiplier
            circle_shape.friction = 1.0
            #sprites.append(pyglet.sprite.Sprite(img, x=circle_body.position.x, y=circle_body.position.y, batch=batch))
            space.add(circle_body, circle_shape)

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.Q:
        music.pause()
    if symbol == key.S:
        music.play()

def update(dt):
    space.step(dt)
    for shape in space.shapes:
        if shape.body.position.y < -100:
            space.remove(shape.body, shape)

event_logger = pyglet.window.event.WindowEventLogger()
window.push_handlers(event_logger)

window.set_visible()

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, RefreshRate)
    pyglet.app.run()
