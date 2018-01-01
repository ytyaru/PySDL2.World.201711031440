import sys
import sdl2
import sdl2.ext

def run():
    sdl2.ext.init()
    window = sdl2.ext.Window("こんにちは sdl2.ext.World() !!", size=(640, 480))
    window.show()

    factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
    spriterenderer = factory.create_sprite_render_system(window)
    world = sdl2.ext.World()
    world.add_system(spriterenderer)

    WHITE = sdl2.ext.Color(255, 255, 255)   
    sp_paddle = factory.from_color(WHITE, size=(20, 100))
    
    entity = sdl2.ext.Entity(world, sp_paddle)
    entity.splite = sp_paddle
    entity.position = 50, 250

    running = True
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
        world.process()
    return 0

if __name__ == "__main__":
    sys.exit(run())
