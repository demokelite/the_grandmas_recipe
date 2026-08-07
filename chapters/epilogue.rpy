# ============================================================
# 尾声
# ============================================================

label epilogue:
    $ current_chapter = 8

    scene bg_dorm_kitchen with fade
    play music "audio/bgm/new_beginning.mp3" fadein 2.0

    narrator "回到学校后，我开始在宿舍里做菜。"

    show qiu cooking at center with dissolve

    qiu_inner "先从最简单的西红柿炒鸡蛋开始。"
    qiu_inner "室友说好吃，问我在哪学的。"
    qiu_inner "我说——是我奶奶教的。"

    # 视频通话
    scene bg_dorm_kitchen with dissolve

    narrator "手机支在灶台上，屏幕上奶奶正在看我炒菜。"

    grandma "（电话里）小秋，你那边冷吗？多穿点。"

    qiu "(对着镜头)不冷。奶奶您记得穿毛衣了吗？"

    grandma "穿了。你买的红色的那件。很暖和。"

    # 解锁CG
    $ cg_gallery["cg09"] = True
    show cg09 with dissolve
    pause 3.0

    narrator "奶奶坐在沙发上，穿着红色毛衣。"
    narrator "茶几上摆着我的照片。那本菜谱放在电话旁边，翻到了最后一页。"

    hide cg09 with dissolve

    grandma "小秋，我刚才看菜谱——最后一页写的是啥来着？"

    narrator "我停了一下。"

    qiu "(轻声)是您写给我的信。"

    grandma "我给你写信了？写的是什么？"

    narrator "锅里的西红柿和鸡蛋在翻腾。"

    qiu "(忍住眼泪)您写的是——"
    qiu "'小秋，要做个善良的人。'"
    qiu "'不管走到哪，都要好好吃饭。'"

    grandma "(笑)是吗？写得挺好的。"

    qiu "是很好。所以我每天都好好吃饭。"

    scene black with dissolve

    $ recipes["letter"] = True
    $ game_completed = True

    return