# ============================================================
# 第二章：清蒸鲈鱼（1970年代）
# ============================================================

label chapter2:
    $ current_chapter = 2

    # 标题出现
    show text "{size=60}{font=fonts/handwrite.ttf}第二道菜{/font}{/size}" at truecenter with dissolve
    pause 10.0
    hide text with dissolve

    scene bg_kitchen with fade
    play music "audio/bgm/gentle_morning.mp3" fadein 1.0

    show grandma happy at left with dissolve
    show qiu neutral at right with dissolve

    grandma "(从冰箱里拿出鲈鱼)今天教你蒸鱼。"
    grandma "蒸鱼最要紧的是什么，知道吗？"

    qiu "火候？"

    grandma "也对，也不对。"

    qiu "那是什么？"

    grandma "是鱼要新鲜。鱼不新鲜，再怎么蒸都不鲜。"

    show qiu surprised
    qiu "(凑近看)这条鱼新鲜吗？"

    grandma "当然。我早上六点去菜市场挑的。"
    grandma "我去的时候，卖鱼的刚摆摊。"

    qiu "您走那么远？菜市场在下面那条街，来回要二十分钟。"

    grandma "走走路对身体好。再说——给我孙女买鱼，能嫌远吗？"

    show qiu touched

    narrator "我顿了一下。"

    qiu "(轻声)奶奶，下次我跟您一起去。"

    # 备鱼
    show qiu focused

    grandma "好了，看好了。鱼身上划三刀，方便入味。"
    grandma "葱切段，姜切片。鱼肚子里也塞葱姜，去腥。"

    qiu_inner "我小心翼翼地拿起刀，在鱼身上划了三道口子。"

    qiu "这样对吗？"

    grandma "(看了一眼)再深一点。别怕，鱼不会疼的。"

    qiu "我怕切坏。"

    grandma "切坏了也是鱼。人做的菜，哪有完美的。"

    # 蒸鱼时间选择
    qiu_inner "鱼放进蒸锅。现在最关键的是——时间。"

    menu:
        "蒸8分钟":
            $ companionship += 10
            qiu_inner "我定了八分钟的计时器。"

            narrator "八分钟后，我打开锅盖。"

            show item_steamed_fish at truecenter with dissolve
            # show item_rice at rice_left with dissolve
            # show item_rice at rice_right as item_rice_right with dissolve

            narrator "蒸汽涌出。鱼肉洁白，筷子轻轻一拨就散开。"

            grandma "(满意地点头)刚刚好。鱼肉最嫩的时候就是现在。"

            qiu "真的吗？"

            grandma "你尝一口就知道了。好的蒸鱼，不用嚼，舌头一抿就化了。"

        "蒸12分钟":
            qiu_inner "我定了十二分钟的计时器。"

            narrator "十二分钟后。开锅时鱼肉有些发紧。"

            show item_steamed_fish at truecenter with dissolve
            # show item_rice at rice_left with dissolve
            # show item_rice at rice_right as item_rice_right with dissolve

            qiu "(用筷子戳了一下)好像有点老。"

            grandma "(笑)蒸过头了。记住，蒸鱼不能超过十分钟。"
            grandma "过了这道线，鱼肉就柴了。"

            qiu "我下次注意。"

            grandma "没事。做人不能太紧张，做鱼也不能。"

    # 浇热油
    play sound "audio/sfx/sizzle_oil.mp3"

    narrator "奶奶把热油浇在鱼身上。刺啦一声——葱姜的香味弥漫了整个厨房。"

    # 上桌
    scene bg_diningtable with dissolve
    show item_steamed_fish at truecenter with dissolve
    show item_rice at rice_left with dissolve
    show item_rice at rice_right as item_rice_right with dissolve
    show grandma reminisce at left

    qiu "奶奶，您说这是爸爸最爱吃的？"

    grandma "是啊。你爸爸小时候身体不好，三天两头发烧。"
    grandma "有次烧得厉害，什么都吃不下。我急得不行。"

    # 解锁CG
    $ cg_gallery["cg02"] = True
    show cg02 with dissolve
    pause 3.0

    grandma "后来我托人从水库买了一条鲈鱼。那个年代鱼可不好买，尤其是鲜鱼。"
    grandma "我蒸好了，他只喝了一口汤，就说好鲜。"
    grandma "我说那你多喝点。他说，妈，以后我病了你就蒸鱼给我吃。"

    hide cg02 with dissolve

    qiu "然后就病好了？"

    grandma "(笑)哪有那么神。不过第二天烧确实退了。"
    grandma "后来他考上大学，走之前我蒸了一条鱼。"
    grandma "他说火车上吃完了还想吃，连饭盒都舍不得洗，说里面有家里的味道。"

    show qiu thoughtful at right

    narrator "我想到在北京的爸爸。他很少回来。"

    qiu "爸爸现在在北京……很少回来。"

    grandma "(顿了顿)他忙。忙了好，说明有出息。"
    grandma "你爷爷当年就说，儿子要有出息，不能一辈子窝在这个小地方。"

    qiu "您想他吗？"

    narrator "奶奶没有立刻回答。她给鱼又浇了一勺汁。"

    grandma "想。哪个当妈的不想孩子。"
    grandma "不过他好好的就行了。他能吃上蒸鱼吗？北京有鲈鱼吧？"

    qiu "有的，奶奶。北京什么都有。"

    grandma "什么都有，也不是家里的味道。"

    narrator "沉默了一会儿。"

    grandma "(话锋一转)小秋，你会想家吗？在学校。"

    qiu "会。有时候晚上睡不着，就想喝您的粥。"

    grandma "(笑)所以你要好好学。以后想喝粥了，自己也能做。"

    scene black with dissolve
    play sound "audio/sfx/page_turn.mp3"

    return