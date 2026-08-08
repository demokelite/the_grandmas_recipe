# ============================================================
# 《奶奶的菜谱》 - 主脚本入口
# 小红花赛道参赛作品
# ============================================================

# ---------- 角色定义 ----------
define narrator = Character(
    None,
    what_italic=True,
    what_color="#777",
    what_prefix="（",
    what_suffix="）"
)

define qiu = Character(
    "小秋",
    color="#d4a373",
    who_outlines=[(1, "#8b6914")],
    what_outlines=[(1, "#5c4a3a")],
    image="qiu"
)

define grandma = Character(
    "奶奶",
    color="#b5838d",
    who_outlines=[(1, "#6d4c5e")],
    what_outlines=[(1, "#5c3d4a")],
    image="grandma"
)

define qiu_inner = Character(
    None,
    color="#c9a87c",
    what_italic=True,
    what_prefix="（",
    what_suffix="）"
)

# ---------- 立绘缩放 transform ----------
# 统一缩放置绘，避免原图过大覆盖屏幕
transform char_scale:
    zoom 0.32

# ---------- 立绘定义 ----------
# 小秋 - 有真实立绘的表情
image qiu neutral:
    "images/characters/qiu_neutral.png"
    zoom 0.75
image qiu happy:
    "images/characters/qiu_happy.png"
    zoom 0.75
image qiu sad:
    "images/characters/qiu_sad.png"
    zoom 0.75
image qiu surprised:
    "images/characters/qiu_surprised.png"
    zoom 0.75
image qiu touched:
    "images/characters/qiu_touched.png"
    zoom 0.75
image qiu worried:
    "images/characters/qiu_worried.png"
    zoom 0.75
image qiu calm:
    "images/characters/qiu_calm.png"
    zoom 0.75
image qiu focused:
    "images/characters/qiu_focused.png"
    zoom 0.75
image qiu thoughtful:
    "images/characters/qiu_thoughtful.png"
    zoom 0.75
image qiu crying:
    "images/characters/qiu_crying.png"
    zoom 0.75
image qiu cooking:
    "images/characters/qiu_cooking.png"
    zoom 0.75

# 奶奶 - 仅 neutral 有真实立绘，其余用 neutral 占位
image grandma neutral:
    "images/characters/grandma_neutral.png"
    zoom 0.65
image grandma happy:
    "images/characters/grandma_neutral.png"
    zoom 0.65
image grandma calm:
    "images/characters/grandma_neutral.png"
    zoom 0.65
image grandma worried:
    "images/characters/grandma_neutral.png"
    zoom 0.65
image grandma teach:
    "images/characters/grandma_neutral.png"
    zoom 0.65
image grandma laugh:
    "images/characters/grandma_neutral.png"
    zoom 0.65
image grandma reminisce:
    "images/characters/grandma_neutral.png"
    zoom 0.65
image grandma energetic:
    "images/characters/grandma_neutral.png"
    zoom 0.65
image grandma confused:
    "images/characters/grandma_neutral.png"
    zoom 0.65
image grandma relieved:
    "images/characters/grandma_neutral.png"
    zoom 0.65
image grandma crying:
    "images/characters/grandma_neutral.png"
    zoom 0.65
image grandma dressed:
    "images/characters/grandma_neutral.png"
    zoom 0.65

# ---------- 缺失背景图占位定义 ----------
# 以下背景资源尚未制作，暂用现有相近图片占位，制作好后替换路径即可
image bg_kitchen_morning = "images/bg_kitchen_morning.png"      
image bg_diningtable = "images/bg_diningtable.png"        
image bg_kitchen_stools = "images/bg_kitchen.png"         # 厨房凳子 → 厨房
image bg_letter = "images/old_paper_texture.jpg"          # 信件 → 旧纸张纹理

# ---------- CG 图占位定义 ----------
# 所有 CG 图资源尚未制作，暂用现有相近图片占位，制作好后替换路径即可
image cg01 = "images/cg01.png"   # 奶奶的结婚照 (1965) → 旧照片纹理
image cg02 = "images/old_photo_texture.jpg"   # 奶奶抱着年幼的父亲 (1970s)
image cg03 = "images/old_photo_texture.jpg"   # 父亲上大学前的照片 (1982)
image cg04 = "images/old_photo_texture.jpg"   # 母亲第一次来学做菜 (1995)
image cg05 = "images/old_photo_texture.jpg"   # 奶奶抱着刚出生的小秋 (2003)
image cg06 = "images/old_photo_texture.jpg"   # 奶奶教小秋做菜 (主线)
image cg07 = "images/bg_balcony.jpg"          # 阳台上喝粥 → 阳台背景
image cg08 = "images/old_paper_texture.jpg"   # 小秋读信 → 旧纸张纹理
image cg09 = "images/bg_dorm_kitchen.jpg"     # 宿舍做菜 (尾声) → 宿舍厨房
image cg10 = "images/handwritten_recipe.jpg"  # 菜谱封面 (主视觉) → 手写菜谱

# ---------- 道具图定义 ----------
image item_recipe_first = "images/handwritten_recipe.jpg"
image item_rice = "images/item_rice.png"

# ---------- 米饭左右位置 ----------
# 用于菜品两侧对称摆放米饭
transform rice_left:
    xalign 0.20
    yalign 0.55
transform rice_right:
    xalign 0.80
    yalign 0.55

# ---------- 全局变量 ----------
default companionship = 0          # 陪伴感 0-100
default ending_type = ""           # 结局标识: good/normal/sad
default current_chapter = 0        # 当前章节

# 菜谱解锁状态
default recipes = {
    "tomato_egg": False,
    "steamed_fish": False,
    "braised_pork": False,
    "shredded_potato": False,
    "dumplings": False,
    "millet_porridge": False,
    "letter": False
}

# CG解锁状态
default cg_gallery = {
    "cg01": False,  # 奶奶的结婚照 (1965)
    "cg02": False,  # 奶奶抱着年幼的父亲 (1970s)
    "cg03": False,  # 父亲上大学前的照片 (1982)
    "cg04": False,  # 母亲第一次来学做菜 (1995)
    "cg05": False,  # 奶奶抱着刚出生的小秋 (2003)
    "cg06": False,  # 奶奶教小秋做菜 (主线)
    "cg07": False,  # 阳台上喝粥
    "cg08": False,  # 小秋读信
    "cg09": False,  # 宿舍做菜 (尾声)
    "cg10": False   # 菜谱封面 (主视觉)
}

# 是否已通关（用于解锁全部功能）
default game_completed = False

# ---------- 游戏开始 ----------
label start:
    # 初始设置
    $ quick_menu = True
    $ _game_menu_screen = "game_menu_selector"

    # 播放背景音乐
    play music "audio/bgm/morning_dew.mp3" fadein 2.0 volume 0.6

    # 序章
    # call prologue from _call_prologue

    # 第一章
    call chapter1 from _call_chapter1

    # # 第二章
    # call chapter2 from _call_chapter2

    # # 第三章
    # call chapter3 from _call_chapter3

    # # 第四章
    # call chapter4 from _call_chapter4

    # # 第五章
    # call chapter5 from _call_chapter5

    # # 第六章
    # call chapter6 from _call_chapter6

    # # 第七章
    # call chapter7 from _call_chapter7

    # # 尾声
    # call epilogue from _call_epilogue

    # # 结局判定
    # call ending_judgment from _call_ending_judgment

    # 片尾字幕
    # call credits from _call_credits

    # 返回主菜单
    $ MainMenu(confirm=False)()
    return