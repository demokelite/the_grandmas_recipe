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

    narrator "今天奶奶的精神特别好。清晨的阳光斜斜地穿过木窗格，在灶台上铺开一片暖黄。她从竹篮里拿出一块五花肉，动作利落得像年轻人。"

    qiu_inner "奶奶难得起得这么早。我闻到她衣襟上淡淡的肥皂香，混着厨房里陈年的烟火气。这味道，是我童年的味道。"

    grandma "今天教你做红烧肉。"
    grandma "这道菜啊——你爸考上大学那年，我做了满满一大锅。"

    qiu "为什么要做那么多？"

    grandma "因为全村的人都来吃。"
    grandma "你爸爸是村里第一个大学生。"
    grandma "你爷爷高兴得把猪圈里最后一头猪宰了。"
    grandma "村里人说他疯了——他说，儿子考上大学，杀一头猪算什么。"

    qiu_inner "奶奶说这话时眼睛亮亮的，像是又回到了那个热闹的夏天。我能想象出那口大铁锅下熊熊的柴火，还有院子里坐满的乡亲。"

    qiu "爷爷好豪气。"

    grandma "他那个人啊，一辈子穷大方。自己舍不得吃穿，对别人倒是大方得很。"
    grandma "冬天棉袄里就一件单衣，省下来的钱都给村里的孩子买本子买笔。"
    grandma "你爸后来读书认字，也是跟你爷爷学的。"

    # 切肉
    show qiu focused
    qiu_inner "我把五花肉切成方块，冷水下锅焯水。血沫慢慢浮上来，在水面上聚成一团团褐色的絮。"
    qiu_inner "奶奶在旁边看着，时不时指点我下刀的角度。刀刃划过肉皮的声音，笃笃的，像敲鼓。"

    # 炒糖色
    grandma "红烧肉最关键的——炒糖色。"
    grandma "小秋，你来。"
    grandma "这一步做好了，肉才有红亮亮的颜色，甜丝丝的香气。"

    menu:
        "小火慢炒":
            $ companionship += 10
            qiu_inner "我把糖放进锅里，开了小火。糖粒在锅底沙沙地响，像春雨落在瓦片上。"

            show grandma teach
            grandma "好，小火就对了。别着急，慢慢搅。"
            grandma "看到颜色变深了吗？"
            grandma "等它冒小泡泡，就差不多了。这叫'鱼眼泡'。"

            narrator "糖浆慢慢变成漂亮的琥珀色。焦糖的香气弥漫开来，甜得有些醉人，混着猪肉焯水的淡淡肉香，整个厨房都被这股暖香包裹住。"

            grandma "下肉！翻炒，让每块肉都裹上糖色！"

            play sound "audio/sfx/sizzle.mp3"
            narrator "肉块在锅里翻腾，染上红亮的光泽。油脂遇热发出滋滋的欢叫，像是在唱歌。"

            qiu "好漂亮！"
            qiu_inner "我从来不知道，一块肉可以是这么好看的颜色。像黄昏时天边的霞，又像奶奶陪嫁的首饰盒里那只老玛瑙。"

            grandma "这就是红烧肉的颜色。你爷爷说，这颜色看着就高兴。"
            grandma "高兴的日子，就要吃高兴的菜。"

        "火大了":
            qiu_inner "我把糖放进锅里，开了中火。我想，火大一点应该熟得快些。"

            narrator "糖融化得很快，边缘开始冒烟。一缕焦苦的味道钻进鼻子。"

            grandma "小秋，火太大了！要糊了！"

            qiu_inner "我赶紧关小火，但糖已经变成了深褐色。锅底冒着细细的烟，我心里一沉。"

            show qiu worried
            qiu "(慌)奶奶，是不是糊了？要不要倒了重来？"

            grandma "(接过铲子)有一点。没关系，糊了一点点有焦香味。"
            grandma "你爷爷就好这一口，说带点焦味才是红烧肉。"

            qiu "真的吗？"

            grandma "(笑)当然是假的。他就是怕我难堪。"
            grandma "不过没关系。炒糖色就是练出来的。"
            grandma "你第一次做成这样，比我当年强。我第一次炒糖色，把锅都烧黑了。"

    # 炖肉
    narrator "奶奶加入酱油和香料，盖上锅盖。八角、桂皮、香叶的香气被热气蒸出来，混在厨房的空气里。"

    grandma "要炖一个小时。炖到肉烂了，肥而不腻。"
    grandma "这急不得。好东西都是熬出来的。"

    # 等待时的对话
    scene bg_kitchen_stools with dissolve
    show grandma reminisce at left
    show qiu neutral at right

    narrator "我们坐在厨房的小板凳上。阳光从窗户照进来，落在奶奶的膝盖上，把她灰白的头发照得透亮。"
    narrator "锅里的肉咕嘟咕嘟地响，蒸汽从锅盖边沿溜出来，把厨房熏得暖洋洋的。"

    qiu_inner "这是我回家后，最安静的一段时光。没有城市的车笛，没有手机的提示音，只有锅里的炖肉声和窗外偶尔传来的鸡鸣。"

    qiu "奶奶，能多讲讲我爸小时候的事吗？"

    grandma "你爸啊——小时候可皮了。"
    grandma "有一年夏天，他跑到后山掏鸟窝，从树上摔下来，把胳膊摔断了。"

    qiu "啊？我怎么不知道？"

    grandma "他肯定不好意思跟你说。"
    grandma "胳膊打着石膏，还惦记着那只小鸟。"
    grandma "我就做了红烧肉给他吃。他用左手吃，吃了三碗饭。"
    grandma "'妈，受伤真好。'——你爸的原话。"

    qiu "(笑)这是什么逻辑。"
    qiu_inner "原来爸爸小时候是这样的人。在我印象里，他一直是个严肃的工程师，连笑都很少。原来他小时候也曾经为了掏鸟窝摔断胳膊。"

    # 解锁CG
    $ cg_gallery["cg03"] = True

    grandma "后来他考上大学走的那天，我给他装了一饭盒红烧肉。"
    grandma "他说火车上吃完了，饭盒舍不得扔。说上面有家里的味道。"

    qiu "他跟我说过。那个饭盒现在还放在家里的橱柜里。"
    qiu "每次搬家，他都不肯扔。我妈嫌它旧，他还跟我妈吵过一架。"

    show grandma confused
    grandma "(愣住)是吗？我……我不记得了。"

    narrator "奶奶的表情有些恍惚。她停下话头，眼睛望着窗外的某处，像是有什么东西从记忆里溜走了。"

    qiu_inner "我的心一下子揪了起来。这是这几天来，奶奶第一次在我面前露出这样的神情。"

    grandma "(努力回忆)是什么样子的饭盒？"

    qiu "(轻声)白色的，上面有红色的字——'劳动光荣'。"

    show grandma happy
    grandma "(眼神亮起来)对对对！你爷爷厂里发的！"
    grandma "他说以后就用来给孩子带饭。你爸带了很多年。"
    grandma "你看，这脑子，说着说着就想起来了。"

    # 肉好了
    scene bg_kitchen with dissolve
    play sound "audio/sfx/lid_open.mp3"
    show item_braised_pork at truecenter with dissolve
    show item_rice at rice_left with dissolve
    show item_rice at rice_right as item_rice_right with dissolve

    narrator "锅盖打开。一锅红亮的红烧肉，肥瘦相间，筷子夹起来微微颤动。"
    narrator "浓郁的肉香一下子涌出来，混着酱油的咸鲜和冰糖的甜，整个厨房都被这股味道浸透了。"

    qiu_inner "这就是家的味道。我在城市里吃过很多红烧肉，饭店里的，外卖的，可是没有一锅是这样的。"

    show qiu happy
    qiu "(吃了一块)奶奶，这也太好吃了。"
    qiu "肥的部分入口就化了，瘦的部分又不柴。"

    grandma "好吃就多吃点。你太瘦了。"
    grandma "城里头的饭，哪有家里的实在。"

    qiu "(连吃了三块)以后我要是想家了，就做红烧肉。"

    grandma "好。做红烧肉要舍得放料，也要舍得花时间。"
    grandma "做人也是。该大方的时候要大方，该等待的时候要耐心。"
    grandma "你爷爷常说，日子是一锅红烧肉，急不得，慌不得。"

    qiu_inner "我看着奶奶满足地笑。她夹起一块肉，慢慢嚼着，眼睛眯成一条缝。阳光照在她脸上，连皱纹里都透着暖意。"
    qiu_inner "我想，这一刻，我要记一辈子。"

    scene black with dissolve
    play sound "audio/sfx/page_turn.mp3"

    return