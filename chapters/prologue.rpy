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
    narrator "车窗外的景色从城市的高楼，慢慢变成了低矮的平房和成片的麦田。"
    narrator "我在颠簸中醒来时，天色已经偏黄。"
    narrator "楼还是那栋楼，只是比记忆里更旧了一些。"
    narrator "外墙的米黄色涂料剥落了大半，露出底下灰扑扑的水泥。"
    narrator "奶奶家在五楼，没有电梯。"
    narrator "我把行李箱从车上拖下来，轮子碾过路面的碎石，发出细碎的响声。"

    # 场景：楼梯间
    scene bg_stairwell with dissolve
    play sound "audio/sfx/footsteps_rolling.mp3"

    narrator "行李箱的轮子磕在台阶上，发出单调的声响。"
    narrator "那声音在狭窄的楼道里回荡，像一下又一下的钟摆。"
    narrator "声控灯忽明忽暗，照得墙壁上的裂纹更深了。"
    narrator "每一层转角都堆着些旧物——一捆报纸、几盆枯了的花、一辆落了灰的儿童车。"
    narrator "小时候觉得这楼梯很高，每一步都像冒险。"
    narrator "我会数着台阶往上爬，数到一半就喘，奶奶就在上面笑着等我。"
    narrator "现在我不觉得高了——只是奶奶还能爬得动吗？"
    narrator "走到三楼时，我不得不停下来歇一歇。空气里有股潮潮的旧味道，混着谁家炒菜的油烟。"

    # 场景：门口
    scene bg_door with dissolve
    play sound "audio/sfx/knocking.mp3"

    narrator "暗红色的铁门，新贴的春联已经翘了边。"
    narrator "墨迹被风吹得有些淡了，'福'字歪着贴在门心。"
    narrator "我敲了三下。没有人应。"
    narrator "又敲了三下，里面传来电视模糊的声响，却没有脚步声。"
    narrator "我等了一会儿，从口袋里掏出那把磨得发亮的钥匙。"

    play sound "audio/sfx/door_open.mp3"
    narrator "用钥匙开了门。"
    narrator "门'咔哒'一声弹开，熟悉的气息扑面而来——是奶奶身上那种洗衣皂和旧木头混在一起的味道。"

    # 场景：客厅
    scene bg_livingroom with fade
    narrator "客厅里，电视开着却没有声音，画面是戏曲频道。"
    narrator "屏幕的蓝光在墙上晃动，戏台上的人咿咿呀呀地张着嘴。"
    narrator "茶几上散着几个药瓶，标签朝向各个方向。"
    narrator "沙发扶手上搭着洗得发白的毛毯，上面还留着坐过的褶皱。"
    narrator "窗帘只拉开了一半，夕阳斜斜地照进来，把空气里的浮尘照得发亮。"

    # 场景：厨房
    scene bg_kitchen with wipeleft
    play sound "audio/sfx/boiling.mp3"

    narrator "厨房里有咕嘟咕嘟的声响。"
    narrator "混着米香和一丝焦糊味，是小米粥的味道。"
    narrator "奶奶背对着我，系着那条蓝布围裙，站在灶台前。"
    narrator "围裙的下摆洗得起了毛边，她的背比记忆里更弯了一些。"

    show grandma neutral at center with dissolve

    grandma "你……你是？"

    narrator "她的眼神隔着一层雾。"
    narrator "她眯起眼睛看了我好一会儿，手里还攥着锅铲，没放下。"

    qiu_inner "小时候我总觉得，不管我走多远，奶奶都会在原地等我。"
    qiu_inner "她记得我喜欢吃什么，记得我怕打雷，记得我所有的事。"
    qiu_inner "可是现在，她看着我的眼神，像是在努力拼起一幅打乱的拼图。"
    qiu_inner "那一瞬间，我喉咙发紧，眼眶忽然就热了。"

    # 关键选择
    menu:
        "“奶奶，我是小秋啊，您的孙女。”":
            $ companionship += 5
            show grandma happy
            grandma "小秋！哎呀，你看我这脑子……"
            grandma "小秋回来了！快让奶奶看看，瘦了没有？"
            grandma "怎么晒黑了？大学食堂不好吃吧？"
            grandma "你想吃什么？奶奶给你做。"
            grandma "冰箱里还有昨天买的排骨，要不红烧？还是糖醋？"
            narrator "她的眼睛一下子亮了起来，雾散了，像拨云见日。"

        "“我回来啦。好香啊，锅里在煮什么？”":
            $ companionship += 10
            show grandma calm
            grandma "煮粥呢。你最爱喝的小米粥。"
            grandma "放了红枣和枸杞，补血。"
            grandma "你小时候啊，一生病就想喝这个粥。"
            grandma "有次你发烧，我喂你喝了一碗，你烧就退了。"
            grandma "其实哪是粥退的烧，是你吃了东西有了精神。"
            narrator "她说着，用勺子慢慢搅了搅锅里的粥，热气扑上她的脸。"

    show grandma neutral

    narrator "奶奶最终认出了我。"
    narrator "她回过神来的那一刻，像是重新找回了什么。"
    narrator "但我瞥了一眼灶台。"

    # 盐罐糖罐细节
    show item_salt_sugar at truecenter with dissolve
    pause 2.0
    hide item_salt_sugar with dissolve

    qiu_inner "盐罐里放着糖，糖罐里放着盐。"
    qiu_inner "两个罐子都是一样的青花瓷，是奶奶用了几十年的。"
    qiu_inner "她以前从不弄错——做饭时闭着眼睛都能摸对。"
    qiu_inner "我心里咯噔一下，但什么也没说。"

    grandma "你先去放行李，你房间我上周就收拾好了。"
    grandma "就是你小时候那些东西，我没舍得扔。"
    grandma "被褥我晒过了，有太阳味儿。"

    # 场景：小秋的房间
    scene bg_xiaoqiu_room with fade

    narrator "我的房间还是老样子。"
    narrator "单人床铺着碎花床单，墙上还贴着我初中的奖状。"
    narrator "书桌上的台灯还是那盏旧的，灯罩被烤得发黄。"
    narrator "窗台上摆着一排小时候的玩偶，落了一层薄薄的灰。"
    narrator "床头柜上放着一本泛黄的旧本子。"
    narrator "本子的封皮是深蓝色的布面，边角磨得起了毛。"

    # 菜谱第一页
    show item_recipe_first at truecenter with dissolve
    play sound "audio/sfx/page_turn.mp3"

    narrator "我拿起本子，翻开第一页。"
    narrator "纸页很脆，翻动时发出沙沙的轻响。"

    # 展示奶奶的手写文字
    "{i}{size=28}给我的小秋——{/size}{/i}"
    "{i}{size=28}等你长大，奶奶教你做菜。{/i}{/size}"
    "{i}{size=28}以后不管走到哪，都能自己给自己做饭吃。{/i}{/size}"
    "{i}{size=28}吃饱了，才不会想家。{/i}{/size}"
    "{i}{size=28}——奶奶{/i}{/size}"
    "{i}{size=28}2003年秋{/i}{/size}"

    hide item_recipe_first with dissolve

    qiu_inner "2003年。我出生的那年。"
    qiu_inner "原来从那时起，奶奶就准备好了这本本子。"
    qiu_inner "她一笔一画写的字，比印的还端正。"

    narrator "我继续翻。菜谱里夹着照片，写着密密麻麻的笔记。"
    narrator "有的页角卷了边，有的夹着一两根干枯的香菜叶。"
    narrator "七道菜，七段故事。"
    narrator "每一道菜后面都写着一段话，是奶奶年轻时候的事。"

    # 解锁初始内容
    $ cg_gallery["cg10"] = True
    $ recipes["tomato_egg"] = True

    # 画外音
    grandma "（画外音）小秋！粥好了，来喝粥！"

    narrator "我合上菜谱，抱在胸前。"
    narrator "本子被体温焐热了，像奶奶的手心。"

    qiu_inner "我离开家去外地上学的时候，奶奶站在楼下送了很远。"
    qiu_inner "那天她说：'放假就回来，奶奶给你做你爱吃的。'"
    qiu_inner "我每次回来，她的白发都多一些，背都更弯一些。"
    qiu_inner "我不能只是等着吃她做的菜了。"
    qiu_inner "这次回来，我要学会这本菜谱里的每一道菜。"
    qiu_inner "等她哪天真的记不清了，换我给她做。"

    scene black with dissolve
    play sound "audio/sfx/page_turn.mp3"

    # 标题出现
    show text "{size=60}{font=fonts/handwrite.ttf}奶奶的菜谱{/font}{/size}" at truecenter with dissolve
    pause 12.0
    hide text with dissolve

    return