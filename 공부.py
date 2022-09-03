import pygame as pg, os, random

# 1. 게임 초기화
pg.init()

# 2. 게임창 옵션 설정
size = [600, 700]
screen = pg.display.set_mode(size)

title = "My Game"
pg.display.set_caption(title)

# 3. 게임 내 필요한 설정
fps = 60
clock = pg.time.Clock()
def resource_path(relative_path):
    basic_path = os.path.dirname(__file__)
    return os.path.join(basic_path, relative_path)
def img_load(a,b): return pg.image.load(os.path.join(a, b))
#dir
img_path = resource_path('assets')

class obj:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.move = 3
    def put_img(self,basic_path,address):
        self.img = img_load(basic_path,address)
        self.width, self.height = self.img.get_size()
        self.x, self.y = round(size[0]/2-self.width/2), round(size[1]-self.height-10)
    def draw(self):
        screen.blit(self.img, (self.x,self.y))
            
ss = obj()
ss.put_img(img_path,'spaceship.png')
black = (0,0,0)
white = (255,255,255)
k = 0
press_x_list = []
press_left, press_right = False, False

# 4. 메인 이벤트
done = False
while not done:

    # 4-1. FPS 설정
    clock.tick(fps)

    # 4-2. 각종 입력 감지
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
            
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                press_x_list.append(-ss.move)
                press_left = True
            if event.key == pg.K_RIGHT:
                press_x_list.append(ss.move)
                press_right = True
            
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                press_left = False
                if press_right == True:
                    press_x_list.append(ss.move)
            if event.key == pg.K_RIGHT:
                press_right = False
                if press_left == True:
                    press_x_list.append(-ss.move)
    if press_left == False and press_right == False:
        press_x_list.clear()
    if len(press_x_list) > 2:
        del press_x_list[0]

    try:
        ss.x += press_x_list[len(press_x_list)-1]
    except Exception:
        pass
    print(press_x_list)

    # 4-3. 입력, 시간에 따른 변화
    k+=1
    # 4-4. 그리기
    screen.fill(black)
    ss.draw()

    # 4-5. 업데이트
    pg.display.flip()

# 5. 게임 종료
pg.quit()