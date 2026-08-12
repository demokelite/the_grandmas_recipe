# ============================================================
# 尾声
# ============================================================

label epilogue:
    $ current_chapter = 8

    # 标题出现
    show text "{size=60}{font=fonts/handwrite.ttf}尾声{/font}{/size}" at truecenter with dissolve
    pause 10.0
    hide text with dissolve

    scene bg_dorm_kitchen with fade
    play music "audio/bgm/new_beginning.mp3" fadein 2.0

    narrator "回到学校后，我开始在宿舍里做菜。"
    narrator "宿舍的厨房很小，只有两个灶眼，锅铲还是跟室友借的。"
    narrator "可我每次站到灶台前，就觉得奶奶站在我旁边。"

    show qiu cooking at center with dissolve

    qiu_inner "先从最简单的西红柿炒鸡蛋开始。"
    qiu_inner "锅要先烧热，再倒油。油要等冒小烟了再下蛋液。"
    qiu_inner "蛋液下锅要'温柔'——这是奶奶的原话。"
    qiu_inner "室友说好吃，问我在哪学的。"
    qiu_inner "我说——是我奶奶教的。"
    qiu_inner "说这句话的时候，我特别骄傲。"

    # 视频通话
    scene bg_dorm_kitchen with dissolve

    narrator "手机支在灶台上，屏幕上奶奶正在看我炒菜。"
    narrator "屏幕有点小，奶奶的脸占了大半个画面。"
    narrator "她把手机举得很近，凑着眼睛看。"

    grandma "（电话里）小秋，你那边冷吗？多穿点。"
    grandma "我看你只穿了一件单衣。"

    qiu "(对着镜头)不冷。奶奶您记得穿毛衣了吗？"
    qiu "红色的那件。"

    grandma "穿了。你买的红色的那件。很暖和。"
    grandma "你二姨说我穿红色显气色。"

    # 解锁CG
    $ cg_gallery["cg09"] = True
    show cg09 with dissolve
    pause 3.0

    narrator "奶奶坐在沙发上，穿着红色毛衣。"
    narrator "毛衣的领口有点松了，但奶奶穿得很整齐。"
    narrator "茶几上摆着我的照片，相框擦得很干净。"
    narrator "那本菜谱放在电话旁边，翻到了最后一页。"
    narrator "那一页，是她写给我的信。"

    hide cg09 with dissolve

    grandma "小秋，我刚才看菜谱——最后一页写的是啥来着？"
    grandma "我看了半天，想不起来了。"

    narrator "我停了一下。手里的锅铲悬在半空。"
    narrator "锅里的油还在滋滋地响。"

    qiu_inner "她忘了。"
    qiu_inner "就像她忘掉怎么煮粥那样，她忘掉了自己写过什么。"

    qiu "(轻声)是您写给我的信。"

    grandma "我给你写信了？写的是什么？"
    grandma "是菜谱吗？"

    narrator "锅里的西红柿和鸡蛋在翻腾，红色的汁水咕嘟咕嘟冒着泡。"
    narrator "和奶奶家的厨房一样香。"

    qiu "(忍住眼泪，声音尽量平稳)您写的是——"
    qiu "'小秋，要做个善良的人。'"
    qiu "'不管走到哪，都要好好吃饭。'"
    qiu "'奶奶在你做的每一道菜里。'"

    grandma "(笑)是吗？写得挺好的。"
    grandma "我写的？我还挺会写的。"

    qiu "是很好。所以我每天都好好吃饭。"
    qiu "每天都做菜，每一道都按您教的来。"

    grandma "那你慢慢做，别急。火候到了才好吃。"

    narrator "我点点头，眼泪掉进了锅里。"
    narrator "锅里的西红柿炒鸡蛋又香了一点。"

    narrator "奶奶可能忘了自己写过什么。"
    narrator "可她没忘，菜要慢慢做，火候到了才好吃。"
    narrator "她没忘，要我好好吃饭。"
    narrator "她没忘的，都是最重要的。"

    scene black with dissolve

    $ recipes["letter"] = True
    $ game_completed = True

    return