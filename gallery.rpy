# ============================================================
# 菜谱图鉴系统
# ============================================================

init python:
    # 菜谱数据结构
    class Recipe:
        def __init__(self, id, name, era, desc, cg_id=None):
            self.id = id
            self.name = name
            self.era = era
            self.desc = desc
            self.cg_id = cg_id

    recipe_data = [
        Recipe("tomato_egg", "西红柿炒鸡蛋", "1960s", "最简单也最难的一道菜。奶奶说，越简单的菜越看功夫。\n\n——你爷爷把家里老母鸡下的第一颗蛋留给了我。那颗蛋的味道，我记了一辈子。", "cg01"),
        Recipe("steamed_fish", "清蒸鲈鱼", "1970s", "爸爸生病时最馋的一口。鱼要新鲜，火候不能超过十分钟。\n\n——他考上大学那天，我蒸了一条鱼。他说饭盒里有家里的味道。", "cg02"),
        Recipe("braised_pork", "红烧肉", "1980s", "爸爸考上大学时全村庆祝的菜。炒糖色要小火，做人要舍得放料。\n\n——你爷爷把最后一头猪宰了，说儿子考上大学，杀一头猪算什么。", "cg03"),
        Recipe("shredded_potato", "酸辣土豆丝", "1990s", "妈妈第一次来家里学的菜。切了二十年才切得好。\n\n——你妈学不会，我说没关系，切不好就让你爸切。", "cg04"),
        Recipe("dumplings", "白菜猪肉馅饺子", "2000s", "小秋出生那天包的。包得丑没关系，都是好饺子。\n\n——你那么小，像一只剥了壳的虾米。从那天起我就想，要活久一点。", "cg05"),
        Recipe("millet_porridge", "小米粥", "现在", "水和米的比例是奶奶的温柔。慢慢熬，别着急。\n\n——我年轻的时候觉得人生好长，现在觉得不过是一碗粥的功夫。", "cg07"),
        Recipe("letter", "最后一页", "永远", "奶奶的告别。也是最长情的菜谱。\n\n——就算我什么都不记得了，我的心里也一定有一个位置，是留给你的。", "cg08"),
    ]

# ============================================================
# 菜谱图鉴界面
# ============================================================
screen recipe_gallery:
    tag menu
    predict False

    # 背景
    add "gui/gallery_bg.jpg"

    # 主布局
    frame:
        background None
        xfill True
        yfill True
        padding (40, 40)

        vbox:
            spacing 20

            # 标题
            text "菜 谱 图 鉴" size 48 color "#b5838d" xalign 0.5 font "fonts/handwrite.ttf"

            # 内容区
            hbox:
                spacing 30

                # 左侧：菜谱列表
                viewport:
                    xsize 300
                    ysize 500
                    scrollbars "vertical"
                    mousewheel True

                    vbox:
                        spacing 10
                        for r in recipe_data:
                            if recipes[r.id]:
                                textbutton r.name:
                                    xsize 280
                                    action SetScreenVariable("selected_recipe", r)
                                    style "recipe_button_unlocked"
                            else:
                                textbutton "？？？":
                                    xsize 280
                                    action None
                                    style "recipe_button_locked"

                # 右侧：菜谱详情
                if selected_recipe is not None:
                    viewport:
                        xsize 900
                        ysize 550
                        mousewheel True

                        vbox:
                            spacing 15

                            # 菜名和年代
                            hbox:
                                spacing 15
                                text selected_recipe.name size 36 color "#b5838d" font "fonts/handwrite.ttf"
                                text selected_recipe.era size 20 color "#999" yalign 0.5

                            # CG图片
                            if selected_recipe.cg_id and cg_gallery.get(selected_recipe.cg_id):
                                add selected_recipe.cg_id:
                                    xalign 0.5
                                    xsize 800
                                    ysize 350
                                    fit "contain"

                            # 描述文字
                            text selected_recipe.desc size 22 color "#666" line_spacing 8

                else:
                    vbox:
                        xsize 900
                        yalign 0.5
                        text "选择左侧已解锁的菜谱查看详情" size 24 color "#999" xalign 0.5

    # 返回按钮
    textbutton "返回":
        action Return()
        xalign 0.5
        yalign 0.95
        style "return_button"

# 图鉴界面样式
style recipe_button_unlocked:
    background "#ffe8d6"
    hover_background "#ffd4b8"
    padding (15, 10)
    text_align 0.5

style recipe_button_locked:
    background "#ddd"
    padding (15, 10)
    text_align 0.5

# 选中变量
default selected_recipe = None

# ============================================================
# CG画廊界面
# ============================================================
screen cg_gallery_screen:
    tag menu
    predict False

    add "gui/gallery_bg.jpg"

    frame:
        background None
        xfill True
        yfill True
        padding (40, 40)

        vbox:
            spacing 20

            text "C G 画 廊" size 48 color "#b5838d" xalign 0.5 font "fonts/handwrite.ttf"

            grid 5 2:
                spacing 15
                xalign 0.5

                for cg_id in ["cg01","cg02","cg03","cg04","cg05","cg06","cg07","cg08","cg09","cg10"]:
                    if cg_gallery.get(cg_id):
                        imagebutton:
                            idle cg_id
                            hover cg_id
                            xsize 200
                            ysize 120
                            action Show("cg_viewer", cg=cg_id)
                    else:
                        frame:
                            xsize 200
                            ysize 120
                            background "#333"
                            text "？？？" color "#666" align (0.5, 0.5)

    textbutton "返回":
        action Return()
        xalign 0.5
        yalign 0.95

# CG查看器
screen cg_viewer(cg):
    add "#000000e0"
    add cg:
        xalign 0.5
        yalign 0.5
        xsize 1200
        ysize 700
        fit "contain"
    textbutton "关闭":
        action Hide("cg_viewer")
        xalign 0.95
        yalign 0.05