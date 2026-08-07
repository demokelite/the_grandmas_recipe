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
    call prologue from _call_prologue

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

    # # 片尾字幕
    # call credits from _call_credits

    # 返回主菜单
    $ MainMenu(confirm=False)()
    return