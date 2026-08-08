# ============================================================
# 第三章：红烧肉（1980年代）
# ============================================================

label chapter3:
    $ current_chapter = 3

    # 标题出现
    show text "{size=60}{font=fonts/handwrite.ttf}第三道菜{/font}{/size}" at truecenter with dissolve
    pause 10.0
    hide text with dissolve

    scene bg_kitchen with fade
    play music "audio/bgm/lively.mp3" fadein 1.0

    show grandma energetic at left with dissolve
    show qiu neutral at right with dissolve

    narrator "今天奶奶的精神特别好。她拿出一块五花肉，动作利落。"

    grandma "今天教你做红烧肉。"
    grandma "这道菜啊——你爸考上大学那年，我做了满满一大锅。"

    qiu "为什么要做那么多？"

    grandma "因为全村的人都来吃。"
    grandma "你爸爸是村里第一个大学生。"
    grandma "你爷爷高兴得把猪圈里最后一头猪宰了。"
    grandma "村里人说他疯了——他说，儿子考上大学，杀一头猪算什么。"

    qiu "爷爷好豪气。"

    grandma "他那个人啊，一辈子穷大方。自己舍不得吃穿，对别人倒是大方得很。"

    # 切肉
    show qiu focused
    qiu_inner "我把五花肉切成方块，冷水下锅焯水。"

    # 炒糖色
    grandma "红烧肉最关键的——炒糖色。"
    grandma "小秋，你来。"

    menu:
        "小火慢炒":
            $ companionship += 10
            qiu_inner "我把糖放进锅里，开了小火。"

            show grandma teach
            grandma "好，小火就对了。别着急，慢慢搅。"
            grandma "看到颜色变深了吗？"

            narrator "糖浆慢慢变成漂亮的琥珀色。焦糖的香气弥漫开来。"

            grandma "下肉！翻炒，让每块肉都裹上糖色！"

            play sound "audio/sfx/sizzle.mp3"
            narrator "肉块在锅里翻腾，染上红亮的光泽。"

            qiu "好漂亮！"

            grandma "这就是红烧肉的颜色。你爷爷说，这颜色看着就高兴。"

        "火大了":
            qiu_inner "我把糖放进锅里，开了中火。"

            narrator "糖融化得很快，边缘开始冒烟。"

            grandma "小秋，火太大了！要糊了！"

            qiu_inner "我赶紧关小火，但糖已经变成了深褐色。"

            show qiu worried
            qiu "(慌)奶奶，是不是糊了？"

            grandma "(接过铲子)有一点。没关系，糊了一点点有焦香味。"
            grandma "你爷爷就好这一口，说带点焦味才是红烧肉。"

            qiu "真的吗？"

            grandma "(笑)当然是假的。他就是怕我难堪。"
            grandma "不过没关系。炒糖色就是练出来的。"

    # 炖肉
    narrator "奶奶加入酱油和香料，盖上锅盖。"

    grandma "要炖一个小时。炖到肉烂了，肥而不腻。"

    # 等待时的对话
    scene bg_kitchen_stools with dissolve
    show grandma reminisce at left
    show qiu neutral at right

    narrator "我们坐在厨房的小板凳上。阳光从窗户照进来，落在奶奶的膝盖上。"

    qiu "奶奶，能多讲讲我爸小时候的事吗？"

    grandma "你爸啊——小时候可皮了。"
    grandma "有一年夏天，他跑到后山掏鸟窝，从树上摔下来，把胳膊摔断了。"

    qiu "啊？我怎么不知道？"

    grandma "他肯定不好意思跟你说。"
    grandma "胳膊打着石膏，还惦记着那只小鸟。"
    grandma "我就做了红烧肉给他吃。他用左手吃，吃了三碗饭。"
    grandma "'妈，受伤真好。'——你爸的原话。"

    qiu "(笑)这是什么逻辑。"

    # 解锁CG
    $ cg_gallery["cg03"] = True

    grandma "后来他考上大学走的那天，我给他装了一饭盒红烧肉。"
    grandma "他说火车上吃完了，饭盒舍不得扔。说上面有家里的味道。"

    qiu "他跟我说过。那个饭盒现在还放在家里的橱柜里。"

    show grandma confused
    grandma "(愣住)是吗？我……我不记得了。"

    narrator "奶奶的表情有些恍惚。"

    grandma "(努力回忆)是什么样子的饭盒？"

    qiu "(轻声)白色的，上面有红色的字——'劳动光荣'。"

    show grandma happy
    grandma "(眼神亮起来)对对对！你爷爷厂里发的！"
    grandma "他说以后就用来给孩子带饭。你爸带了很多年。"

    # 肉好了
    scene bg_kitchen with dissolve
    play sound "audio/sfx/lid_open.mp3"
    show item_braised_pork with dissolve

    narrator "锅盖打开。一锅红亮的红烧肉，肥瘦相间，筷子夹起来微微颤动。"

    show qiu happy
    qiu "(吃了一块)奶奶，这也太好吃了。"

    grandma "好吃就多吃点。你太瘦了。"

    qiu "(连吃了三块)以后我要是想家了，就做红烧肉。"

    grandma "好。做红烧肉要舍得放料，也要舍得花时间。"
    grandma "做人也是。该大方的时候要大方，该等待的时候要耐心。"

    scene black with dissolve
    play sound "audio/sfx/page_turn.mp3"

    return