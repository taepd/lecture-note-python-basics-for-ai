from stage.main import game_start
from stage.sub import set_stage_level
from image.character import show_character
from sound.bgm import bgm_play

if __name__ == "__main__":
    game_start()
    set_stage_level(5)
    bgm_play(10)
    show_character()
