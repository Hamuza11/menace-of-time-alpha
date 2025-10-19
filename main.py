@namespace
class SpriteKind:
    building = SpriteKind.create()
    NPC = SpriteKind.create()

def on_up_pressed():
    global lastDirection
    lastDirection = 0
    animation.run_image_animation(Hiro,
        [img("""
                . . . . . . f f f f . . . . . .
                . . . . f f e e e e f f . . . .
                . . . f e e e f f e e e f . . .
                . . f f f f f 2 2 f f f f f . .
                . . f f e 2 e 2 2 e 2 e f f . .
                . . f e 2 f 2 f f 2 f 2 e f . .
                . . f f f 2 2 e e 2 2 f f f . .
                . f f e f 2 f e e f 2 f e f f .
                . f e e f f e e e e f e e e f .
                . . f e e e e e e e e e e f . .
                . . . f e e e e e e e e f . . .
                . . e 4 f f f f f f f f 4 e . .
                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                . . 4 4 f 4 4 4 4 4 4 f 4 4 . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f e e e e f f . . . .
                . . . f e e e f f e e e f . . .
                . . . f f f f 2 2 f f f f . . .
                . . f f e 2 e 2 2 e 2 e f f . .
                . . f e 2 f 2 f f f 2 f e f . .
                . . f f f 2 f e e 2 2 f f f . .
                . . f e 2 f f e e 2 f e e f . .
                . f f e f f e e e f e e e f f .
                . f f e e e e e e e e e e f f .
                . . . f e e e e e e e e f . . .
                . . . e f f f f f f f f 4 e . .
                . . . 4 f 2 2 2 2 2 e d d 4 . .
                . . . e f f f f f f e e 4 . . .
                . . . . f f f . . . . . . . . .
                """),
            img("""
                . . . . . . f f f f . . . . . .
                . . . . f f e e e e f f . . . .
                . . . f e e e f f e e e f . . .
                . . f f f f f 2 2 f f f f f . .
                . . f f e 2 e 2 2 e 2 e f f . .
                . . f e 2 f 2 f f 2 f 2 e f . .
                . . f f f 2 2 e e 2 2 f f f . .
                . f f e f 2 f e e f 2 f e f f .
                . f e e f f e e e e f e e e f .
                . . f e e e e e e e e e e f . .
                . . . f e e e e e e e e f . . .
                . . e 4 f f f f f f f f 4 e . .
                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                . . 4 4 f 4 4 4 4 4 4 f 4 4 . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f e e e e f f . . . .
                . . . f e e e f f e e e f . . .
                . . . f f f f 2 2 f f f f . . .
                . . f f e 2 e 2 2 e 2 e f f . .
                . . f e f 2 f f f 2 f 2 e f . .
                . . f f f 2 2 e e f 2 f f f . .
                . . f e e f 2 e e f f 2 e f . .
                . f f e e e f e e e f f e f f .
                . f f e e e e e e e e e e f f .
                . . . f e e e e e e e e f . . .
                . . e 4 f f f f f f f f e . . .
                . . 4 d d e 2 2 2 2 2 f 4 . . .
                . . . 4 e e f f f f f f e . . .
                . . . . . . . . . f f f . . . .
                """)],
        100,
        True)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_map_loaded(overworldColumn, overworldRow, map2):
    global mySprite
    sprites.destroy_all_sprites_of_kind(SpriteKind.building)
    sprites.destroy_all_sprites_of_kind(SpriteKind.NPC)
    if len(tiles.get_tiles_by_type(sprites.dungeon.floor_dark_diamond)) > 0:
        for brick in tiles.get_tiles_by_type(sprites.dungeon.floor_dark_diamond):
            mySprite = sprites.create(assets.image("""
                houseRed
                """), SpriteKind.building)
            tiles.place_on_tile(mySprite, brick)
    elif len(tiles.get_tiles_by_type(assets.tile("""
        myTile
        """))) > 0:
        for grass in tiles.get_tiles_by_type(assets.tile("""
            myTile
            """)):
            mySprite = sprites.create(assets.image("""
                Mustafa
                """), SpriteKind.NPC)
            sprites.set_data_string(mySprite,
                "dialog",
                "Hey Hiro! Your sword and shield are ready!")
            sprites.set_data_string(mySprite, "name", "Mustafa")
            tiles.place_on_tile(mySprite, grass)
overworld.on_map_loaded(on_map_loaded)

def on_on_overlap(sprite, otherSprite):
    global hasTools
    if controller.B.is_pressed():
        game.show_long_text(sprites.read_data_string(otherSprite, "dialog"),
            DialogLayout.BOTTOM)
        if sprites.read_data_string(otherSprite, "name") == "Mustafa":
            hasTools = True
            music.play(music.melody_playable(music.power_up),
                music.PlaybackMode.UNTIL_DONE)
            game.show_long_text("You've got your sword and shield!", DialogLayout.BOTTOM)
sprites.on_overlap(SpriteKind.player, SpriteKind.NPC, on_on_overlap)

def initOverworld():
    scene.set_background_color(7)
    overworld.set_overworld16(overworld.create_map16(overworld.map_row16(overworld.tilemap16(tilemap("""
                    level0
                    """)),
                overworld.tilemap16(tilemap("""
                    level40
                    """)),
                overworld.tilemap16(tilemap("""
                    level3
                    """))),
            overworld.map_row16(overworld.tilemap16(tilemap("""
                    level42
                    """)),
                overworld.tilemap16(tilemap("""
                    level44
                    """)),
                overworld.tilemap16(tilemap("""
                    level9
                    """))),
            overworld.map_row16(overworld.tilemap16(tilemap("""
                    level46
                    """)),
                overworld.tilemap16(tilemap("""
                    level48
                    """)),
                overworld.tilemap16(tilemap("""
                    level15
                    """)))))
    overworld.set_animation_type(overworld.AnimationType.SCROLL)
    overworld.set_player_sprite(Hiro)
    overworld.load_map(0, 0)
    overworld.set_walls_block_transitions(True)
def endHiroAnim():
    animation.stop_animation(animation.AnimationTypes.IMAGE_ANIMATION, Hiro)
    if lastDirection == 0:
        Hiro.set_image(img("""
            . . . . . . f f f f . . . . . .
            . . . . f f e e e e f f . . . .
            . . . f e e e f f e e e f . . .
            . . f f f f f 2 2 f f f f f . .
            . . f f e 2 e 2 2 e 2 e f f . .
            . . f e 2 f 2 f f 2 f 2 e f . .
            . . f f f 2 2 e e 2 2 f f f . .
            . f f e f 2 f e e f 2 f e f f .
            . f e e f f e e e e f e e e f .
            . . f e e e e e e e e e e f . .
            . . . f e e e e e e e e f . . .
            . . e 4 f f f f f f f f 4 e . .
            . . 4 d f 2 2 2 2 2 2 f d 4 . .
            . . 4 4 f 4 4 4 4 4 4 f 4 4 . .
            . . . . . f f f f f f . . . . .
            . . . . . f f . . f f . . . . .
            """))
    elif lastDirection == 1:
        Hiro.set_image(img("""
            . . . . . . f f f f . . . . . .
            . . . . f f f 2 2 f f f . . . .
            . . . f f f 2 2 2 2 f f f . . .
            . . f f f e e e e e e f f f . .
            . . f f e 2 2 2 2 2 2 e e f . .
            . . f e 2 f f f f f f 2 e f . .
            . . f f f f e e e e f f f f . .
            . f f e f b f 4 4 f b f e f f .
            . f e e 4 1 f d d f 1 4 e e f .
            . . f e e d d d d d d e e f . .
            . . . f e e 4 4 4 4 e e f . . .
            . . e 4 f 2 2 2 2 2 2 f 4 e . .
            . . 4 d f 2 2 2 2 2 2 f d 4 . .
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
            . . . . . f f f f f f . . . . .
            . . . . . f f . . f f . . . . .
            """))
    elif lastDirection == 2:
        Hiro.set_image(img("""
            . . . . f f f f f f . . . . . .
            . . . f 2 f e e e e f f . . . .
            . . f 2 2 2 f e e e e f f . . .
            . . f e e e e f f e e e f . . .
            . f e 2 2 2 2 e e f f f f . . .
            . f 2 e f f f f 2 2 2 e f . . .
            . f f f e e e f f f f f f f . .
            . f e e 4 4 f b e 4 4 e f f . .
            . . f e d d f 1 4 d 4 e e f . .
            . . . f d d d d 4 e e e f . . .
            . . . f e 4 4 4 e e f f . . . .
            . . . f 2 2 2 e d d 4 . . . . .
            . . . f 2 2 2 e d d e . . . . .
            . . . f 5 5 4 f e e f . . . . .
            . . . . f f f f f f . . . . . .
            . . . . . . f f f . . . . . . .
            """))
    elif lastDirection == 3:
        Hiro.set_image(img("""
            . . . . . . f f f f f f . . . .
            . . . . f f e e e e f 2 f . . .
            . . . f f e e e e f 2 2 2 f . .
            . . . f e e e f f e e e e f . .
            . . . f f f f e e 2 2 2 2 e f .
            . . . f e 2 2 2 f f f f e 2 f .
            . . f f f f f f f e e e f f f .
            . . f f e 4 4 e b f 4 4 e e f .
            . . f e e 4 d 4 1 f d d e f . .
            . . . f e e e 4 d d d d f . . .
            . . . . f f e e 4 4 4 e f . . .
            . . . . . 4 d d e 2 2 2 f . . .
            . . . . . e d d e 2 2 2 f . . .
            . . . . . f e e f 4 5 5 f . . .
            . . . . . . f f f f f f . . . .
            . . . . . . . f f f . . . . . .
            """))

def on_button_released():
    endHiroAnim()
controller.any_button.on_event(ControllerButtonEvent.RELEASED, on_button_released)

def on_a_released():
    if hasTools:
        animation.stop_animation(animation.AnimationTypes.IMAGE_ANIMATION, Hiro)
        if lastDirection == 0:
            pass
        elif lastDirection == 1:
            animation.run_image_animation(Hiro,
                [img("""
                        ........................
                        .....ffff...............
                        ...fff22fff.............
                        ..fff2222fff............
                        .fffeeeeeefff...........
                        .ffe222222eef...........
                        .fe2ffffff2ef...........
                        .ffffeeeeffff...........
                        ffefbf44fbfeff..........
                        fee41fddf14eef..........
                        .ffffdddddeef...........
                        fddddf444eef............
                        fbbbbf2222f4e...........
                        fbbbbf2222fd4...........
                        .fccf45544f44...........
                        ..ffffffff..............
                        ....ff..ff..............
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        """),
                    img("""
                        ........................
                        ......ffff..............
                        ....fff22fff............
                        ...fff2222fff...........
                        ..fffeeeeeefff..........
                        ..ffe222222eef..........
                        ..fe2ffffff2ef..........
                        ..ffffeeeeffff..........
                        .ffefbf44fbfeff.........
                        .fee41fddf14eef.........
                        fdfeeddddd4eff..........
                        fbffee444edd4e..........
                        fbf4f2222edde...........
                        fcf.f22cccee............
                        .ff.f44cdc4f............
                        ....fffddcff............
                        .....fddcff.............
                        ....cddc................
                        ....cdc.................
                        ....cc..................
                        ........................
                        ........................
                        ........................
                        ........................
                        """),
                    img("""
                        ........................
                        ........................
                        .......ff...............
                        .....ff22ff.............
                        ...fff2222fff...........
                        ..fff222222fff..........
                        ..fff222222fff..........
                        ..feeeeeeeeeeff.........
                        .ffe22222222eff.........
                        .fffffeeeefffff.........
                        fdfefbf44fbfeff.........
                        fbfe41fddf14ef..........
                        fbffe4dddd4efe..........
                        fcfef22222f4e...........
                        .ff4f44554f4e...........
                        ....ffffffdde...........
                        .....ffffedde...........
                        ..........ee............
                        .........ccc............
                        ........cc1cc...........
                        .........c1c............
                        .........c1c............
                        .........c1c............
                        .........c1c............
                        """),
                    img("""
                        ......ffff..............
                        ....fff22fff............
                        ...fff2222fff...........
                        ..fffeeeeeefff..........
                        ..ffe222222eef..........
                        ..fe2ffffff2ef..........
                        ..ffffeeeeffff......ccc.
                        .ffefbf44fbfeff....cddc.
                        .ffefbf44fbfeff...cddc..
                        .fee4dddddd4eef.ccddc...
                        fdfeeddddd4eeffecddc....
                        fbffee4444ee4fddccc.....
                        fbf4f222222f1edde.......
                        fcf.f222222f44ee........
                        .ff.f445544f............
                        ....ffffffff............
                        .....ff..ff.............
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        """)],
                100,
                False)
        elif lastDirection == 2:
            animation.run_image_animation(Hiro,
                [img("""
                        ..............ffffff....
                        .............f2feeeeff..
                        ............f222feeeeff.
                        .......cc...feeeeffeeef.
                        .......cdc.fe2222eeffff.
                        .......cddcf2effff222ef.
                        ........cddcffeeefffffff
                        .........cddce44fbe44eff
                        ..........cdceddf14d4eef
                        ..........cccdeddd4eeef.
                        ...........edd4e44eeff..
                        ............ee442222f...
                        .............f2e2222f...
                        .............f554444f...
                        ..............ffffff....
                        ................fff.....
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        """),
                    img("""
                        ........................
                        ..............fff.......
                        .............f2fffff....
                        ...........ff22eeeeeff..
                        ..........ff222eeeeeeff.
                        ..........feeeefffeeeef.
                        .........fe2222eeefffff.
                        .........f2efffff222efff
                        ..cc.....fffeeefffffffff
                        ..cdcc...fee44fbbe44efef
                        ..ccddcc..feddfbb4d4eef.
                        ....cdddceefddddd4eeef..
                        .....ccdcddee2222222f...
                        ......cccdd44e544444f...
                        .........eeeeffffffff...
                        .............ff...fff...
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        """),
                    img("""
                        ...............ff.......
                        .............ff2ffff....
                        ............ff2feeeeff..
                        ...........ff22feeeeeff.
                        ...........feeeeffeeeef.
                        ..........fe2222eefffff.
                        ..........f2effff222efff
                        ..........fffeeeffffffff
                        ..........fee44fbe44efef
                        ...........feddfb4d4eef.
                        ..........c.eeddd4eeef..
                        ....ccccccceddee2222f...
                        .....dddddcedd44e444f...
                        ......ccccc.eeeefffff...
                        ..........c...ffffffff..
                        ...............ff..fff..
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        """),
                    img("""
                        ..............ffffff....
                        .............f2feeeeff..
                        ............f222feeeeff.
                        ............feeeeffeeef.
                        ...........fe2222eeffff.
                        ...........f2effff222ef.
                        ...........fffeeefffffff
                        ...........fee44fbe44eff
                        ............feddf14d4eef
                        .............fdddd4eeef.
                        .............fe444eddf..
                        .............ccc22eddf..
                        .............cdc22fee...
                        ............cddc4444f...
                        ...........cddcfffff....
                        ..........cddc..fff.....
                        ..........cdc...........
                        ..........cc............
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        """)],
                100,
                False)
        elif lastDirection == 3:
            animation.run_image_animation(Hiro,
                [img("""
                        ........................
                        ....ffffff..............
                        ..ffeeeef2f.............
                        .ffeeeef222f............
                        .feeeffeeeef...cc.......
                        .ffffee2222ef.cdc.......
                        .fe222ffffe2fcddc.......
                        fffffffeeeffcddc........
                        ffe44ebf44ecddc.........
                        fee4d41fddecdc..........
                        .feee4dddedccc..........
                        ..ffee44e4dde...........
                        ...f222244ee............
                        ...f2222e2f.............
                        ...f444455f.............
                        ....ffffff..............
                        .....fff................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        """),
                    img("""
                        ........................
                        .......fff..............
                        ....fffff2f.............
                        ..ffeeeee22ff...........
                        .ffeeeeee222ff..........
                        .feeeefffeeeef..........
                        .fffffeee2222ef.........
                        fffe222fffffe2f.........
                        fffffffffeeefff.....cc..
                        fefe44ebbf44eef...ccdc..
                        .fee4d4bbfddef..ccddcc..
                        ..feee4dddddfeecdddc....
                        ...f2222222eeddcdcc.....
                        ...f444445e44ddccc......
                        ...ffffffffeeee.........
                        ...fff...ff.............
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        """),
                    img("""
                        .......ff...............
                        ....ffff2ff.............
                        ..ffeeeef2ff............
                        .ffeeeeef22ff...........
                        .feeeeffeeeef...........
                        .fffffee2222ef..........
                        fffe222ffffe2f..........
                        ffffffffeeefff..........
                        fefe44ebf44eef..........
                        .fee4d4bfddef...........
                        ..feee4dddee.c..........
                        ...f2222eeddeccccccc....
                        ...f444e44ddecddddd.....
                        ...fffffeeee.ccccc......
                        ..ffffffff...c..........
                        ..fff..ff...............
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        """),
                    img("""
                        ....ffffff..............
                        ..ffeeeef2f.............
                        .ffeeeef222f............
                        .feeeffeeeef............
                        .ffffee2222ef...........
                        .fe222ffffe2f...........
                        fffffffeeefff...........
                        ffe44ebf44eef...........
                        fee4d41fddef............
                        .feee4ddddf.............
                        ..fdde444ef.............
                        ..fdde22ccc.............
                        ...eef22cdc.............
                        ...f4444cddc............
                        ....fffffcddc...........
                        .....fff..cddc..........
                        ...........cdc..........
                        ............cc..........
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        """)],
                100,
                False)
        pause(500)
        endHiroAnim()
    else:
        pass
controller.A.on_event(ControllerButtonEvent.RELEASED, on_a_released)

def on_left_pressed():
    global lastDirection
    lastDirection = 2
    animation.run_image_animation(Hiro,
        [img("""
                . . . . f f f f f f . . . . . .
                . . . f 2 f e e e e f f . . . .
                . . f 2 2 2 f e e e e f f . . .
                . . f e e e e f f e e e f . . .
                . f e 2 2 2 2 e e f f f f . . .
                . f 2 e f f f f 2 2 2 e f . . .
                . f f f e e e f f f f f f f . .
                . f e e 4 4 f b e 4 4 e f f . .
                . . f e d d f 1 4 d 4 e e f . .
                . . . f d d d d 4 e e e f . . .
                . . . f e 4 4 4 e e f f . . . .
                . . . f 2 2 2 e d d 4 . . . . .
                . . . f 2 2 2 e d d e . . . . .
                . . . f 5 5 4 f e e f . . . . .
                . . . . f f f f f f . . . . . .
                . . . . . . f f f . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . f f f f f f . . . . . .
                . . . f 2 f e e e e f f . . . .
                . . f 2 2 2 f e e e e f f . . .
                . . f e e e e f f e e e f . . .
                . f e 2 2 2 2 e e f f f f . . .
                . f 2 e f f f f 2 2 2 e f . . .
                . f f f e e e f f f f f f f . .
                . f e e 4 4 f b e 4 4 e f f . .
                . . f e d d f 1 4 d 4 e e f . .
                . . . f d d d e e e e e f . . .
                . . . f e 4 e d d 4 f . . . . .
                . . . f 2 2 e d d e f . . . . .
                . . f f 5 5 f e e f f f . . . .
                . . f f f f f f f f f f . . . .
                . . . f f f . . . f f . . . . .
                """),
            img("""
                . . . . f f f f f f . . . . . .
                . . . f 2 f e e e e f f . . . .
                . . f 2 2 2 f e e e e f f . . .
                . . f e e e e f f e e e f . . .
                . f e 2 2 2 2 e e f f f f . . .
                . f 2 e f f f f 2 2 2 e f . . .
                . f f f e e e f f f f f f f . .
                . f e e 4 4 f b e 4 4 e f f . .
                . . f e d d f 1 4 d 4 e e f . .
                . . . f d d d d 4 e e e f . . .
                . . . f e 4 4 4 e e f f . . . .
                . . . f 2 2 2 e d d 4 . . . . .
                . . . f 2 2 2 e d d e . . . . .
                . . . f 5 5 4 f e e f . . . . .
                . . . . f f f f f f . . . . . .
                . . . . . . f f f . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . f f f f f f . . . . . .
                . . . f 2 f e e e e f f . . . .
                . . f 2 2 2 f e e e e f f . . .
                . . f e e e e f f e e e f . . .
                . f e 2 2 2 2 e e f f f f . . .
                . f 2 e f f f f 2 2 2 e f . . .
                . f f f e e e f f f f f f f . .
                . f e e 4 4 f b e 4 4 e f f . .
                . . f e d d f 1 4 d 4 e e f . .
                . . . f d d d d 4 e e e f . . .
                . . . f e 4 4 4 e d d 4 . . . .
                . . . f 2 2 2 2 e d d e . . . .
                . . f f 5 5 4 4 f e e f . . . .
                . . f f f f f f f f f f . . . .
                . . . f f f . . . f f . . . . .
                """)],
        100,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    global lastDirection
    lastDirection = 3
    animation.run_image_animation(Hiro,
        [img("""
                . . . . . . f f f f f f . . . .
                . . . . f f e e e e f 2 f . . .
                . . . f f e e e e f 2 2 2 f . .
                . . . f e e e f f e e e e f . .
                . . . f f f f e e 2 2 2 2 e f .
                . . . f e 2 2 2 f f f f e 2 f .
                . . f f f f f f f e e e f f f .
                . . f f e 4 4 e b f 4 4 e e f .
                . . f e e 4 d 4 1 f d d e f . .
                . . . f e e e 4 d d d d f . . .
                . . . . f f e e 4 4 4 e f . . .
                . . . . . 4 d d e 2 2 2 f . . .
                . . . . . e d d e 2 2 2 f . . .
                . . . . . f e e f 4 5 5 f . . .
                . . . . . . f f f f f f . . . .
                . . . . . . . f f f . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f f f . . . .
                . . . . f f e e e e f 2 f . . .
                . . . f f e e e e f 2 2 2 f . .
                . . . f e e e f f e e e e f . .
                . . . f f f f e e 2 2 2 2 e f .
                . . . f e 2 2 2 f f f f e 2 f .
                . . f f f f f f f e e e f f f .
                . . f f e 4 4 e b f 4 4 e e f .
                . . f e e 4 d 4 1 f d d e f . .
                . . . f e e e e e d d d f . . .
                . . . . . f 4 d d e 4 e f . . .
                . . . . . f e d d e 2 2 f . . .
                . . . . f f f e e f 5 5 f f . .
                . . . . f f f f f f f f f f . .
                . . . . . f f . . . f f f . . .
                """),
            img("""
                . . . . . . f f f f f f . . . .
                . . . . f f e e e e f 2 f . . .
                . . . f f e e e e f 2 2 2 f . .
                . . . f e e e f f e e e e f . .
                . . . f f f f e e 2 2 2 2 e f .
                . . . f e 2 2 2 f f f f e 2 f .
                . . f f f f f f f e e e f f f .
                . . f f e 4 4 e b f 4 4 e e f .
                . . f e e 4 d 4 1 f d d e f . .
                . . . f e e e 4 d d d d f . . .
                . . . . f f e e 4 4 4 e f . . .
                . . . . . 4 d d e 2 2 2 f . . .
                . . . . . e d d e 2 2 2 f . . .
                . . . . . f e e f 4 5 5 f . . .
                . . . . . . f f f f f f . . . .
                . . . . . . . f f f . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f f f . . . .
                . . . . f f e e e e f 2 f . . .
                . . . f f e e e e f 2 2 2 f . .
                . . . f e e e f f e e e e f . .
                . . . f f f f e e 2 2 2 2 e f .
                . . . f e 2 2 2 f f f f e 2 f .
                . . f f f f f f f e e e f f f .
                . . f f e 4 4 e b f 4 4 e e f .
                . . f e e 4 d 4 1 f d d e f . .
                . . . f e e e 4 d d d d f . . .
                . . . . 4 d d e 4 4 4 e f . . .
                . . . . e d d e 2 2 2 2 f . . .
                . . . . f e e f 4 4 5 5 f f . .
                . . . . f f f f f f f f f f . .
                . . . . . f f . . . f f f . . .
                """)],
        100,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_down_pressed():
    global lastDirection
    lastDirection = 1
    animation.run_image_animation(Hiro,
        [img("""
                . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f f e 2 2 2 2 2 2 e e f . .
                . . f e 2 f f f f f f 2 e f . .
                . . f f f f e e e e f f f f . .
                . f f e f b f 4 4 f b f e f f .
                . f e e 4 1 f d d f 1 4 e e f .
                . . f e e d d d d d d e e f . .
                . . . f e e 4 4 4 4 e e f . . .
                . . e 4 f 2 2 2 2 2 2 f 4 e . .
                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f f e 2 2 2 2 2 2 e e f . .
                . f f e 2 f f f f f f 2 e f f .
                . f f f f f e e e e f f f f f .
                . . f e f b f 4 4 f b f e f . .
                . . f e 4 1 f d d f 1 4 e f . .
                . . . f e 4 d d d d 4 e f e . .
                . . f e f 2 2 2 2 e d d 4 e . .
                . . e 4 f 2 2 2 2 e d d e . . .
                . . . . f 4 4 5 5 f e e . . . .
                . . . . f f f f f f f . . . . .
                . . . . f f f . . . . . . . . .
                """),
            img("""
                . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f f e 2 2 2 2 2 2 e e f . .
                . . f e 2 f f f f f f 2 e f . .
                . . f f f f e e e e f f f f . .
                . f f e f b f 4 4 f b f e f f .
                . f e e 4 1 f d d f 1 4 e e f .
                . . f e e d d d d d d e e f . .
                . . . f e e 4 4 4 4 e e f . . .
                . . e 4 f 2 2 2 2 2 2 f 4 e . .
                . . 4 d f 2 2 2 2 2 2 f d 4 . .
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
                . . . . . f f f f f f . . . . .
                . . . . . f f . . f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f e e 2 2 2 2 2 2 e f f . .
                . f f e 2 f f f f f f 2 e f f .
                . f f f f f e e e e f f f f f .
                . . f e f b f 4 4 f b f e f . .
                . . f e 4 1 f d d f 1 4 e f . .
                . . e f e 4 d d d d 4 e f . . .
                . . e 4 d d e 2 2 2 2 f e f . .
                . . . e d d e 2 2 2 2 f 4 e . .
                . . . . e e f 5 5 4 4 f . . . .
                . . . . . f f f f f f f . . . .
                . . . . . . . . . f f f . . . .
                """)],
        100,
        True)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def initHiro():
    global Hiro, lastDirection, hasTools
    Hiro = sprites.create(assets.image("""
            HiroStandFront
            """),
        SpriteKind.player)
    controller.move_sprite(Hiro)
    lastDirection = 1
    hasTools = False
hasTools = False
mySprite: Sprite = None
Hiro: Sprite = None
lastDirection = 0
music.play(music.melody_playable(music.power_up),
    music.PlaybackMode.UNTIL_DONE)
game.splash("THE MENACE OF TIME", "Alpha 1.0.5.1")
initHiro()
initOverworld()