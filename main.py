from ursina import *
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton
from object import *

FONT = "gui_asset/font/LuxuriousRoman-Regular.ttf"

class HomePage(Entity):
    def __init__(self):
        super().__init__()
        
        print("Page Loaded Succes")
        self.main_menu = Entity(
            parent=self,
            enabled=True
        ) 
        Entity(
            model = 'quad',
            parent=self.main_menu,
            position = (0, 0, 1),
            scale = (185/12, 105/12),
            texture = "gui_asset/home.jpg"
        )
        self.start_button = Button(
            text = "Play",
            color = color.rgba(1,1,1,0.8),
            scale = (4, 1),
            y = -0.1,
            parent = self.main_menu,
            radius = 0.25,
            highlight_color = color.gray
        )
        self.start_button.text_entity.font = FONT
        self.start_button.text_entity.color = color.black
        self.start_button._on_click = self.start_game
        
        self.setting_button = Button(
            text = "Settings",
            color = color.rgba(1,1,1,0.8),
            scale = (4, 1),
            y = -1.50,
            parent = self.main_menu,
            radius = 0.25,
            highlight_color = color.gray
        )
        self.setting_button.text_entity.font = FONT
        self.setting_button.text_entity.color = color.black
        self.setting_button._on_click = self.show_setting
        
        self.exit_button = Button(
            text = "Exit",
            color = color.rgba(1,1,1,0.8),
            scale = (4, 1),
            y = -2.90,
            parent = self.main_menu,
            radius = 0.25,
            highlight_color = color.gray
        )
        self.exit_button.text_entity.font = FONT
        self.exit_button.text_entity.color = color.black
        self.exit_button._on_click = application.quit
        
    def start_game(self):
        print("apalah")
        self.disable()
        game.enable()
        window.color = color.black
        window.fullscreen = True
            
    def show_setting(self):
        print("apalah")
        self.disable()
        #pengaturan.enable()
        
class SettingPage(Entity):
    def __init__(self):
        super().__init__()
        
        print("PageSetting Loaded Succes")
        self.game_setting = Entity(
            parent=self,
            enabled = True
        ) 
        Entity(
            model = 'quad',
            parent=self.game_setting,
            position = (0, 0, 1),
            scale = (185/12, 110/12),
            texture = "gui_asset/home.jpg"
        )
        
        self.back_button = Button(
            text = "Back",
            color = color.rgba(1,1,1,0.8),
            scale = (2, 1),
            position = (-6, 3.08, 0),
            parent = self.game_setting,
            radius = 0.25,
            highlight_color = color.gray,
            enabled = False
        )
        self.back_button.text_entity.font = FONT
        self.back_button.text_entity.color = color.black
        self.back_button._on_click = self.kembali
        
        self.container = Entity(
            model = 'quad',
            color = color.rgba(1,1,1,0.8),
            scale = (10, 5),
            position = (-0.15, -1.0, 0),
            parent = self.game_setting,
            enabled = False
        )
        
        self.music_dropdown = DropdownMenu(
            "Music",
            buttons = [DropdownMenuButton("On"), DropdownMenuButton("Off")],
            position = (-4, 1.0, -0.02),
            scale = (7, 0.7),
            parent = self.game_setting,
            enabled = False
        )
        
        self.volume_slide = Slider(
            text = "Volume",
            min = 0,
            max = 100,
            default = 50,
            position = (-3.2, -1.0, -0.01),
            scale = (10, 10),
            parent = self.game_setting,
            enabled = False
        )
        
    def enable(self):
        super().enable()
        self.back_button.enabled = True
        self.container.enabled = True
        self.music_dropdown.enabled = True
        self.volume_slide.enabled = True
        
    def disable(self):
        super().disable()
        self.back_button.enabled = False
        self.container.enabled = False
        self.music_dropdown.enabled = False
        self.volume_slide.enabled = False
        
    def kembali(self):
        self.disable()
        #home.enable()
        
class GamePlay(Entity):
    def __init__(self):
        super().__init__()
        
        print('Sukses Memulai Game')
        self.ambient_light = Entity(light=AmbientLight(color=color.rgba(0.5, 0.5, 0.5, 1)),)
        self.directional_light = Entity(light=DirectionalLight(color=color.rgba(0.5, 0.5, 0.5, 1), direction=(1, 1, 1)),)
        self.ukuran_map = 20
        self.game()
        camera.position = (self.ukuran_map // 2, 10, -50)
        
    def Map (self, ukuran_map):
        Entity(model = 'quad', scale = 50, position = (10, 10, 10), texture = "gameplay_asset/sand.jpg")
        Entity(model = 'quad', scale = ukuran_map, position = (ukuran_map // 2, ukuran_map // 2, 0), color = color.dark_gray,)
        
    def game (self):
        scene.clear()
        self.Map(self.ukuran_map)
        self.makanan = Makanan(self.ukuran_map, model = 'sphere', color = color.red)
        self.ulars = Ular(self.ukuran_map)
        
    def dimakan (self):
        if self.ulars.posisi_ular[-1] == self.makanan.position:
            self.ulars.tambah_ular()
            self.makanan.posisi_baru()
            
    def game_over (self):
        ular = self.ulars.posisi_ular
        if 0 < ular[-1][0] < self.ukuran_map and 0 < ular[-1][1] < self.ukuran_map and len(ular) == len(set(ular)):
            return
        print_on_screen('GAME OVER', position = (-0.7, 0.1), scale = 10, duration = 1)
        self.ulars.direction = Vec3(0, 0, 0)
        self.ulars.bisa = dict.fromkeys(self.ulars.bisa, 0)
        invoke (self.game, delay = 1)
        
    def updategame(self):
        print_on_screen(f'score: {self.ulars.score}', position = (-0.85, 0.45), scale = 3,)
        self.dimakan()
        self.game_over()
        self.ulars.main()
        self.ulars.control()
                   
app = Ursina()

#home = HomePage()
#pengaturan = SettingPage()
game = GamePlay()

#pengaturan.enabled = False
#game.enabled = False

def update():
    if GamePlay.enabled:
        game.updategame()

app.run()