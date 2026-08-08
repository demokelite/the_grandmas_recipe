# ============================================================
# 序章：回家
# ============================================================

label prologue:
    $ current_chapter = 0

    # 标题出现
    show text "{size=60}{font=fonts/handwrite.ttf}序章{/font}{/size}" at truecenter with dissolve
    pause 10.0
    hide text with dissolve

    # 场景：楼下
    scene bg_building with fade
    stop music fadeout 1.0
    play music "audio/bgm/nostalgia.mp3" fadein 2.0

    narrator "从学校到家，坐了四个小时的大巴。"
    narrator "楼还是那栋楼，只是比记忆里更旧了一些。"
    narrator "奶奶家在五楼，没有电梯。"

    # 场景：楼梯间
    scene bg_stairwell with dissolve
    play sound "audio/sfx/footsteps_rolling.mp3"

    narrator "行李箱的轮子磕在台阶上，发出单调的声响。"
    narrator "声控灯忽明忽暗，照得墙壁上的裂纹更深了。"
    narrator "小时候觉得这楼梯很高，每一步都像冒险。"
    narrator "现在我不觉得高了——只是奶奶还能爬得动吗？"

    # 场景：门口
    scene bg_door with dissolve
    play sound "audio/sfx/knocking.mp3"

    narrator "暗红色的铁门，新贴的春联已经翘了边。"
    narrator "我敲了三下。没有人应。"

    play sound "audio/sfx/door_open.mp3"
    narrator "用钥匙开了门。"

    # 场景：客厅
    scene bg_livingroom with fade
    narrator "客厅里，电视开着却没有声音，画面是戏曲频道。"
    narrator "茶几上散着几个药瓶。沙发扶手上搭着洗得发白的毛毯。"

    # 场景：厨房
    scene bg_kitchen with wipeleft
    play sound "audio/sfx/boiling.mp3"

    narrator "厨房里有咕嘟咕嘟的声响。"
    narrator "奶奶背对着我，系着那条蓝布围裙，站在灶台前。"

    show grandma neutral at center with dissolve

    grandma "你……你是？"

    narrator "她的眼神隔着一层雾。"

    qiu_inner "小时候我总觉得，不管我走多远，奶奶都会在原地等我。"
    qiu_inner "她记得我喜欢吃什么，记得我怕打雷，记得我所有的事。"
    qiu_inner "可是现在，她看着我的眼神，像是在努力拼起一幅打乱的拼图。"

    # 关键选择
    menu:
        "“奶奶，我是小秋啊，您的孙女。”":
            $ companionship += 5
            show grandma happy
            grandma "小秋！哎呀，你看我这脑子……"
            grandma "小秋回来了！快让奶奶看看，瘦了没有？"
            grandma "怎么晒黑了？大学食堂不好吃吧？"
            grandma "你想吃什么？奶奶给你做。"

        "“我回来啦。好香啊，锅里在煮什么？”":
            $ companionship += 10
            show grandma calm
            grandma "煮粥呢。你最爱喝的小米粥。"
            grandma "放了红枣和枸杞，补血。"
            grandma "你小时候啊，一生病就想喝这个粥。"
            grandma "有次你发烧，我喂你喝了一碗，你烧就退了。"

    show grandma neutral

    narrator "奶奶最终认出了我。"
    narrator "但我瞥了一眼灶台。"

    # 盐罐糖罐细节
    show item_salt_sugar at truecenter with dissolve
    pause 2.0
    hide item_salt_sugar with dissolve

    qiu_inner "盐罐里放着糖，糖罐里放着盐。"

    grandma "你先去放行李，你房间我上周就收拾好了。"
    grandma "就是你小时候那些东西，我没舍得扔。"

    # 场景：小秋的房间
    scene bg_xiaoqiu_room with fade

    narrator "我的房间还是老样子。"
    narrator "单人床铺着碎花床单，墙上还贴着我初中的奖状。"
    narrator "床头柜上放着一本泛黄的旧本子。"

    # 菜谱第一页
    show item_recipe_first at truecenter with dissolve
    play sound "audio/sfx/page_turn.mp3"

    narrator "我拿起本子，翻开第一页。"

    # 展示奶奶的手写文字
    "{i}{size=28}给我的小秋——{/size}{/i}"
    "{i}{size=28}等你长大，奶奶教你做菜。{/i}{/size}"
    "{i}{size=28}以后不管走到哪，都能自己给自己做饭吃。{/i}{/size}"
    "{i}{size=28}——奶奶{/i}{/size}"
    "{i}{size=28}2003年秋{/i}{/size}"

    hide item_recipe_first with dissolve

    qiu_inner "2003年。我出生的那年。"

    narrator "我继续翻。菜谱里夹着照片，写着密密麻麻的笔记。"
    narrator "七道菜，七段故事。"

    # 解锁初始内容
    $ cg_gallery["cg10"] = True
    $ recipes["tomato_egg"] = True

    # 画外音
    grandma "（画外音）小秋！粥好了，来喝粥！"

    narrator "我合上菜谱，抱在胸前。"

    qiu_inner "我离开家去外地上学的时候，奶奶站在楼下送了很远。"
    qiu_inner "那天她说：'放假就回来，奶奶给你做你爱吃的。'"
    qiu_inner "我不能只是等着吃她做的菜了。"
    qiu_inner "这次回来，我要学会这本菜谱里的每一道菜。"

    scene black with dissolve
    play sound "audio/sfx/page_turn.mp3"

    # 标题出现
    show text "{size=60}{font=fonts/handwrite.ttf}奶奶的菜谱{/font}{/size}" at truecenter with dissolve
    pause 12.0
    hide text with dissolve

    return