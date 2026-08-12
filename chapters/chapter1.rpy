# ============================================================
# 第一章：西红柿炒鸡蛋（1960年代）
# ============================================================

label chapter1:
    $ current_chapter = 1

    # 标题出现
    show text "{size=60}{font=fonts/handwrite.ttf}第一道菜{/font}{/size}" at truecenter with dissolve
    pause 10.0
    hide text with dissolve

    scene bg_kitchen_morning with fade
    play music "audio/bgm/warm_kitchen.mp3" fadein 1.0

    narrator "第二天早上。阳光透过窗户照进厨房。"
    narrator "光是那种清晨特有的淡金色，落在灶台上，连水渍都发亮。"
    narrator "窗外的麻雀叽叽喳喳地叫着，远处传来卖豆浆的三轮车的喇叭声。"

    show grandma happy at left with dissolve
    show qiu neutral at right with dissolve

    grandma "小秋，今天奶奶教你做第一道菜。"
    grandma "就学最简单也最难的那个。"

    qiu "是什么？"

    grandma "西红柿炒鸡蛋。"
    grandma "这是你爸小时候天天吵着要吃的菜。"

    qiu "简单我懂——为什么说最难？"

    grandma "(笑)因为越简单的菜，越看功夫。"
    grandma "火候、调味、放的顺序——差一点味道就不一样。"
    grandma "做好了是家的味道，做不好就是大锅饭的味道。"
    grandma "做菜跟做人一样，越简单的事，越要用心。"

    qiu "那我可要认真学了。"
    qiu "我昨天翻菜谱翻到半夜，想把第一页背下来。"

    # 备菜阶段
    show qiu neutral

    qiu_inner "我从菜篮里拿起两颗西红柿，放在水龙头下冲洗。"
    qiu_inner "水很凉，西红柿红得发亮，皮上还挂着水珠。"

    grandma "洗干净了吗？用手搓一搓。"
    grandma "蒂那块要抠掉，那里最容易藏泥。"

    qiu "洗好了。"
    qiu "奶奶您看，干净吧？"

    # 切西红柿选择
    menu:
        "切成大块":
            show qiu neutral
            qiu_inner "我拿起菜刀，把西红柿切成几大块。"
            qiu_inner "刀有点沉，我切得小心翼翼，怕切到手。"

            show grandma laugh
            grandma "(探头一看)你这是喂兔子呢？这么大块，炒出来出不了汁。"
            grandma "做菜要想着吃菜的人，嘴小的就切小点，嘴大的就切大点。"

            show grandma teach
            grandma "看好了，切滚刀块。左手按住西红柿，右手拿刀斜着切。"
            grandma "一面大一面小，这样汁水足，也容易熟。"
            grandma "切一刀，转一下，再切一刀——像这样。"

            show qiu surprised
            qiu "奶奶你好厉害。"
            qiu "切得这么快，还这么匀。"

            grandma "切了五十年了，能不会吗？"
            grandma "你爷爷当年说我切的菜像写的字，越来越利索。"

        "切成小块":
            $ companionship += 5
            show qiu neutral
            qiu_inner "我认真地把西红柿切成小块。"
            qiu_inner "一块一块，尽量切得大小一致。"

            show grandma calm
            grandma "(点头)可以，切得挺仔细。"
            grandma "看得出你用心了。"
            grandma "不过奶奶习惯切滚刀块。"

            qiu "滚刀块？"

            show grandma teach
            grandma "就是这样斜着切，一块大一块小，汁水更足。"
            grandma "以后做多了就明白了。"
            grandma "刀工这东西，急不来，做一顿有一顿的功夫。"

    # 打鸡蛋
    show qiu neutral
    show grandma neutral

    qiu_inner "我打了三个鸡蛋，加了一点盐，用筷子搅。"
    qiu_inner "蛋液在碗里发出清脆的声响，黄澄澄的，像初升的太阳。"
    play sound "audio/sfx/egg_whisk.mp3"

    grandma "看到蛋液上有小泡泡就行了。"
    grandma "别太用力——鸡蛋会生气的。"
    grandma "搅到看不见蛋白就行，再搅就过了。"

    qiu "(笑)鸡蛋还会生气？"

    grandma "会啊。你把它搅得太狠，炒出来就不嫩了。"
    grandma "什么事都得有个度。"
    grandma "对人也是，太较真了，日子就过僵了。"

    # 炒制顺序选择
    play sound "audio/sfx/sizzle.mp3"

    menu:
        "先炒鸡蛋":
            $ companionship += 10
            show qiu focused
            qiu_inner "我把蛋液倒进热油锅。刺啦一声，蛋液迅速膨胀。"
            qiu_inner "金黄色的边儿瞬间鼓起来，像一朵炸开的花。"

            grandma "对对对！铲子推一下，让蛋液流下来。"
            grandma "好了，盛出来。别炒太久，老了就不好吃了。"
            grandma "鸡蛋这东西，宁可生一点，不能老。"

            qiu_inner "我把金黄色的炒蛋盛进碗里。"
            qiu_inner "蛋香扑鼻，我忍不住偷偷夹了一小块尝。"

            grandma "然后再起锅炒西红柿。等西红柿出汁了，把鸡蛋倒回去。"
            grandma "加盐，加一点点糖提鲜。"
            grandma "糖不能多——多了就甜得发腻，少了又不鲜。"

            narrator "鲜红的西红柿和金黄的鸡蛋在锅里翻腾。"
            narrator "锅铲碰着铁锅发出叮叮当当的声音，像一首小曲。"

            qiu "(凑近闻)好香！"
            qiu "奶奶，整个厨房都是这个味儿。"

            grandma "这就是家的味道。"
            grandma "以后你在外头闻到这个味儿，就会想起奶奶的厨房。"

        "先炒西红柿":
            show qiu focused
            qiu_inner "我把西红柿倒进油锅。"
            qiu_inner "汁水一下子溅出来，我吓得往后退了一步。"

            show grandma laugh
            grandma "哎哟，错了错了！先炒鸡蛋，鸡蛋盛出来再炒西红柿！"
            grandma "你这一下西红柿出水多，成西红柿汤泡蛋了。"
            grandma "不过也没事，汤泡饭也好吃。"

            grandma "来，看奶奶的。鸡蛋先盛出来，不然就不嫩了。"

            qiu "(不好意思)我下次记住。"
            qiu "我以为先炒的菜后放呢。"

            grandma "(笑)没关系。我第一次做也弄错了。"
            grandma "你爷爷说，错着错着就对了。过日子也是这样。"
            grandma "错过的别记太久，记住下次怎么做对就行。"

    # 成品上桌
    scene bg_diningtable with dissolve
    show item_tomato_egg at truecenter with dissolve
    show item_rice at rice_left with dissolve
    show item_rice at rice_right as item_rice_right with dissolve
    show grandma happy at left

    narrator "一盘红黄相间的西红柿炒鸡蛋摆在饭桌上。"
    narrator "红的鲜亮，黄的油润，热气一缕一缕往上飘。"
    narrator "旁边放着两碗白米饭，米粒颗颗分明。"

    grandma "(夹菜)尝尝。"
    grandma "趁热，凉了就不是那个味儿了。"

    show qiu happy at right
    qiu "(吃了一口)好吃！就是小时候的味道。"
    qiu "甜里带酸，蛋嫩得能在舌头上化开。"

    grandma "(满足地笑)那当然。奶奶做的西红柿炒鸡蛋，可是让你爸从小吃到大的。"
    grandma "你爸上学那会儿，饭盒里带的都是这个。"

    narrator "奶奶拿起桌上的老花镜，翻开菜谱，在第一页上写了一个'优'字。"
    narrator "她的字一笔一画，'优'字写得端端正正。"

    qiu "奶奶，您还给我打分啊？"

    grandma "那当然。七道菜，都学会了给你发毕业证。"
    grandma "我给你盖章，盖我手心印的那种。"

    # 奶奶的回忆
    qiu "奶奶，您第一次做这道菜是什么时候？"

    show grandma reminisce

    grandma "(眼神飘远)那是……六几年的事了。"
    grandma "我嫁给你爷爷那年，刚过门。"
    grandma "那年冬天特别冷，河里的冰能走人。"

    # 解锁CG
    $ cg_gallery["cg01"] = True
    show cg01 with dissolve
    pause 3.0

    grandma "你太姥姥说，新媳妇得会做菜。我说我会。她就让我做一道西红柿炒鸡蛋。"
    grandma "那时候西红柿金贵，是专门为你太姥姥留的。"
    grandma "然后我进了厨房——你爷爷偷偷跟在后面。"
    grandma "他把家里老母鸡下的第一颗蛋塞给我。"
    grandma "'用这个，这个好吃。'我当时觉得这个人真傻，鸡蛋哪有不一样的。"
    grandma "后来我才知道，那颗蛋是他攒了三天没舍得吃，想给我做见面礼。"

    hide cg01 with dissolve

    qiu "后来呢？"
    qiu "爷爷吃了你做的菜吗？"

    grandma "(笑)后来我炒好了端上桌。你太姥姥尝了一口，说：'这媳妇可以。'"
    grandma "你爷爷在桌子下面偷偷给我竖大拇指。"
    grandma "他那天笑得跟个傻子似的，被你太姥爷瞪了一眼。"

    qiu "爷爷真好。"
    qiu "你们那时候真有意思。"

    grandma "(轻轻摩挲菜谱封面)是啊。他走得早。"
    grandma "但这本菜谱里，到处都是他的影子。"
    grandma "他说的对——鸡蛋真的不一样。那颗蛋的味道，我记了一辈子。"
    grandma "后来我再做这道菜，总觉得差一点什么。其实差的不是味道，是人。"

    show qiu touched

    narrator "我们沉默了一会儿。"
    narrator "窗外有风吹过，吹动了挂在墙上的旧挂历。"
    narrator "奶奶低着头，手指还停在那页菜谱上。"

    qiu "奶奶，明天教我下一道菜吧。"
    qiu "我想把这本菜谱一道一道学完。"

    grandma "好。明天教你蒸鱼。那可是你爸最爱吃的。"
    grandma "你爷爷在的时候，我蒸鱼他总要多吃一碗饭。"
    grandma "睡吧，明天早起。做菜要赶早，鱼要鲜，人也要精神。"

    scene black with dissolve
    play sound "audio/sfx/page_turn.mp3"

    return