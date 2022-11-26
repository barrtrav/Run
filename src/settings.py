class Settings:
    def __init__(self):

        # Game setting
        self.game_active = True
        
        # Screen setting
        self.screen_caption = "Run"
        self.screen_size = (1600, 800)

        # Background setting
        self.background_scene = 0
        self.background_speed = 5

        # Warrior setting
        self.warrior_speed = 10
        self.warrior_count_jump = 48
        self.warrior_animation_speed = 4

        # Box setting
        self.box_wait_time = 20
        self.box_speed = self.background_speed

        # Coin setting
        self.coin_wait_time = 20
        self.coin_animation_speed = 4
        self.coin_speed = self.background_speed