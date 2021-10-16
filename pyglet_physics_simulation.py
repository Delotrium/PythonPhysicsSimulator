import pyglet
from pyglet import *
from pyglet.window import key
import pymunk
import pymunk.pyglet_util
import time

#Import Settings
from settings import *
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
space.gravity = 0, gravityValue

mass = ballMass
radius = ballRadius
sprites = []

sound = pyglet.resource.media(SoundPath, streaming=False)

label = pyglet.text.Label('',font_name='Times New Roman',font_size=36,x=window.width//2, y=window.height//2,anchor_x='center', anchor_y='center', color=(128,128,128,128))


segment_shape1 = pymunk.Segment(space.static_body, (0,0), (200*SegmentOneXMultiplier,60*SegmentOneYMultiplier), StrokeThickness)
segment_shape1.body.position = 350 * WindowsSizeFactorX, 300 * WindowsSizeFactorY
segment_shape1.elasticity = 0.8 * ElasticityMultiplier
segment_shape1.friction = 1.0 * FrictionMultiplier
space.add(segment_shape1)

segment_shape2 = pymunk.Segment(space.static_body, (1*WindowsSizeFactorX,80 *WindowsSizeFactorY), (400 *SegmentTwoXMultiplier,20 * SegmentTwoYMultiplier), StrokeThickness)
segment_shape2.body.position = 50 *WindowsSizeFactorX, 100 * WindowsSizeFactorY
segment_shape2.elasticity = 0.8 * ElasticityMultiplier
segment_shape2.friction = 1.0 * FrictionMultiplier
space.add(segment_shape2)

@window.event
def on_draw():
    window.clear()
    label.draw()
    space.debug_draw(options)

@window.event
def on_mouse_press(x, y, button, modifiers):
    sound.play()
    circle_moment = pymunk.moment_for_circle(mass, 0, radius)
    circle_body = pymunk.Body(mass, circle_moment)
    circle_body.position = x, y
    circle_shape = pymunk.Circle(circle_body,radius)
    circle_shape.elasticity = 0.8 * ElasticityMultiplier
    circle_shape.friction = 1.0 * FrictionMultiplier
    #sprites.append(pyglet.sprite.Sprite(img, x=circle_body.position.x, y=circle_body.position.y, batch=batch))
    space.add(circle_body, circle_shape)

@window.event
def on_deactivate():
    pyglet.app.exit

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
    pyglet.clock.schedule_interval(update, 1.0/60)
    pyglet.app.run()
