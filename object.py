from ursina import *
from random import randrange

class Makanan(Entity):
    def __init__(self, ukuran_map, **kwargs):
        super().__init__(**kwargs)
        self.ukuran_map = ukuran_map
        self.posisi_baru()
        
    def posisi_baru (self):
        self.position = (randrange(self.ukuran_map) + 0.5, randrange(self.ukuran_map) + 0.5, -0.5)
        
class Ular(Entity):
    def __init__(self, ukuran_map,):
        super().__init__()
        self.ukuran_map = ukuran_map
        self.panjang_ular = 1
        self.posisi = self.panjang_ular = 1
        self.posisi_ular = [Vec3(randrange(ukuran_map) + 0.5, randrange(ukuran_map) + 0.5, -0.5)]
        self.ular = []
        self.textures = [
            "gameplay_asset/head.jpeg",
            "gameplay_asset/body2.png","gameplay_asset/body2.png","gameplay_asset/body2.png","gameplay_asset/body2.png","gameplay_asset/body2.png","gameplay_asset/body2.png","gameplay_asset/body2.png","gameplay_asset/body2.png","gameplay_asset/body2.png","gameplay_asset/body2.png",
            "gameplay_asset/body.jpeg","gameplay_asset/body.jpeg","gameplay_asset/body.jpeg","gameplay_asset/body.jpeg","gameplay_asset/body.jpeg","gameplay_asset/body.jpeg","gameplay_asset/body.jpeg","gameplay_asset/body.jpeg","gameplay_asset/body.jpeg","gameplay_asset/body.jpeg",
            "gameplay_asset/body3.png","gameplay_asset/body3.png","gameplay_asset/body3.png","gameplay_asset/body3.png","gameplay_asset/body3.png","gameplay_asset/body3.png","gameplay_asset/body3.png","gameplay_asset/body3.png","gameplay_asset/body3.png","gameplay_asset/body3.png",
            "gameplay_asset/body7.png","gameplay_asset/body7.png","gameplay_asset/body7.png","gameplay_asset/body7.png","gameplay_asset/body7.png","gameplay_asset/body7.png","gameplay_asset/body7.png","gameplay_asset/body7.png","gameplay_asset/body7.png","gameplay_asset/body7.png",
            "gameplay_asset/body4.jpg","gameplay_asset/body4.jpg","gameplay_asset/body4.jpg","gameplay_asset/body4.jpg","gameplay_asset/body4.jpg","gameplay_asset/body4.jpg","gameplay_asset/body4.jpg","gameplay_asset/body4.jpg","gameplay_asset/body4.jpg","gameplay_asset/body4.jpg",
            "gameplay_asset/body8.jpeg","gameplay_asset/body8.jpeg","gameplay_asset/body8.jpeg","gameplay_asset/body8.jpeg","gameplay_asset/body8.jpeg","gameplay_asset/body8.jpeg","gameplay_asset/body8.jpeg","gameplay_asset/body8.jpeg","gameplay_asset/body8.jpeg","gameplay_asset/body8.jpeg",
            "gameplay_asset/body6.jpg","gameplay_asset/body6.jpg","gameplay_asset/body6.jpg","gameplay_asset/body6.jpg","gameplay_asset/body6.jpg","gameplay_asset/body6.jpg","gameplay_asset/body6.jpg","gameplay_asset/body6.jpg","gameplay_asset/body6.jpg","gameplay_asset/body6.jpg",
            "gameplay_asset/body5.jpeg","gameplay_asset/body5.jpeg","gameplay_asset/body5.jpeg","gameplay_asset/body5.jpeg","gameplay_asset/body5.jpeg","gameplay_asset/body5.jpeg","gameplay_asset/body5.jpeg","gameplay_asset/body5.jpeg","gameplay_asset/body5.jpeg","gameplay_asset/body5.jpeg",
            
        ]
        self.buat_ular(self.posisi_ular[0])
        self.directions = {'w': Vec3(0, 1, 0), 's': Vec3(0, -1, 0), 'a': Vec3(-1, 0, 0), 'd': Vec3(1, 0, 0),}
        self.direction = Vec3(0, 0, 0)
        self.bisa = {'a': 1, 'd': 1, 'w': 1, 's': 1,}
        self.tidak_bisa = {'a': 'd', 'd': 'a', 'w': 's', 's': 'w',}
        self.speed = 12
        self.score = 0
        self.frame = 0
        
    def buat_ular (self, position):
        orai = Entity(position=position,)
        texture = self.textures[len(self.ular) % len(self.textures)]
        Entity(model = 'quad', texture = texture, position = position,).add_script(
            SmoothFollow(speed = 12, target = orai, offset = (0, 0, 0))
        )
        self.ular.insert(0, orai)
        
    def tambah_ular (self):
        self.panjang_ular += 1
        self.posisi += 1
        self.score += 1
        self.speed = max(self.speed -1, 5)
        self.buat_ular(self.posisi_ular[0])    
        
    def main (self):
        self.frame += 1
        if not self.frame % self.speed:
            self.control()
            self.posisi_ular.append(self.posisi_ular[-1] + self.direction)
            self.posisi_ular = self.posisi_ular[-self.panjang_ular:]
            for ular, posisi_ulars in zip (self.ular, self.posisi_ular):
                ular.position = posisi_ulars
    
    def control (self):
        for key in 'wasd':
            if held_keys[key] and self.bisa[key]:
                self.direction = self.directions[key]
                self.bisa = dict.fromkeys(self.bisa, 1)
                self.bisa[self.tidak_bisa[key]] = 0
                break
            elif held_keys['escape']:
                application.quit()
        