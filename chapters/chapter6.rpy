# ============================================================
# 第六章：小米粥（现在）
# ============================================================

label chapter6:
    $ current_chapter = 6

    # 标题出现
    show text "{size=60}{font=fonts/handwrite.ttf}第六道菜{/font}{/size}" at truecenter with dissolve
    pause 10.0
    hide text with dissolve

    scene bg_kitchen with fade
    play music "audio/bgm/tender.mp3" fadein 2.0

    narrator "第六天傍晚。我从外面回来，楼道里飘着一股淡淡的焦味。"
    narrator "我推开厨房的门，门轴发出一声轻响。"

    show grandma crying at center with dissolve

    narrator "灶火开着，蓝色的火苗舔着空荡荡的锅底。"
    narrator "锅里空空如也，连一滴水都没有。"
    narrator "奶奶站在灶台前——在哭。"
    narrator "她的肩膀一抖一抖的，围裙的一角被攥得皱巴巴。"
    narrator "灶台上的米袋敞着口，量米的碗掉在了地上，米粒撒了一地。"

    show qiu worried at left with dissolve

    qiu_inner "我的心一下子揪紧了。奶奶从来不在厨房哭的。"
    qiu_inner "厨房是她的地方，是她最自信的地方。"

    qiu "(快步上前)奶奶！怎么了？烫到了吗？有没有伤着？"

    grandma "(转身，满脸泪痕)我……我忘了。"

    qiu "忘了什么？"

    grandma "我忘了怎么煮粥。"
    grandma "明明煮了几十年，今天突然就忘了。"
    grandma "米放多少，水放多少——我想不起来了。"
    grandma "我站在这里想了半天，越想越糊涂，锅都烧干了我都没发现。"

    qiu_inner "奶奶像一个做错事的孩子，无助地看着我。"
    qiu_inner "那双曾经麻利地翻锅颠勺的手，此刻不知道往哪儿放。"
    qiu_inner "我突然意识到——她不是在为忘记煮粥而哭。"
    qiu_inner "她是在为'自己正在忘记'这件事本身而哭。"

    qiu "(握住奶奶的手，发现她的手冰凉)没事的，奶奶。您说，我做。"
    qiu "您想起来多少，就说多少。咱们慢慢来。"

    grandma "可是我不记得了。"
    grandma "刚才我想淘米，却不知道该淘几遍。"
    grandma "站在这里发呆，火就一直烧着……"

    qiu "没事。那您慢慢想。水放多少？米淘几遍？"

    grandma "(沉默良久，眼神有些涣散)水……水放三碗。"

    qiu "好。三碗水。您记得真清楚。"

    narrator "我关掉灶火，重新打火。拿起碗，量了三碗水，倒进锅里。"
    narrator "水落进锅里发出哗啦一声，奶奶的肩膀松了一点。"

    qiu "然后呢？米怎么淘？"

    grandma "两遍。不要淘太多遍……营养会洗掉。"
    grandma "(像是在回忆)小米最怕的就是淘太狠。表面的那层油,淘没了就不香了。"

    qiu "对，您之前教过我。"

    narrator "我把撒在地上的米粒一粒一粒捡起来，淘了两遍，倒入锅中。"
    narrator "米粒落进水里，发出细碎的声响，像下雨。"

    qiu "然后？大火还是小火？"

    grandma "大火煮开，小火慢熬。"
    grandma "开了以后要搅一搅……不然会粘锅。"
    grandma "搅的时候要从锅底往上翻，别乱搅。"

    qiu "(轻声笑了)奶奶您看，您全都记得。"
    qiu "每一个步骤，都没忘。"

    narrator "奶奶看着锅里开始冒泡的米和水。眼泪还在流，但渐渐平静下来。"
    narrator "灶火映着她的脸，皱纹里都是岁月。"

    grandma "小秋，我是不是……是不是要变成废人了。"
    grandma "连粥都不会煮了，还能干什么呢。"

    qiu "不是的奶奶。医生说只是偶尔会忘。"
    qiu "您教了我这么多道菜，每一道都记得清清楚楚。"
    qiu "今天只是累了，想不起来了而已。"
    qiu "您不是废人——您是我最好的老师。"

    # 关键选择
    menu:
        "“以后我教您。”":
            $ companionship += 10
            qiu "没事的奶奶。我记得，以后换我教您。"
            qiu "您忘了哪一步，我就提醒您哪一步。"

            grandma "(含泪笑)那你得好好学。奶奶这点手艺，不能丢了。"
            grandma "传到你这里，就是第四代了。"

            qiu "不会丢的。我都记下来了，每个步骤。"
            qiu "连您说的'搅的时候要从锅底往上翻'，我都记着呢。"

            grandma "(擦了擦眼泪)好。那奶奶放心了。"

        "“我们都在一起。”":
            $ companionship += 10
            qiu "奶奶，医生说了，只是偶尔会忘。"
            qiu "不管怎样，我们都在您身边。"
            qiu "忘了一起想，想不起来就一起做。"

            grandma "嗯……你们在就好。"
            grandma "一个人忘事最怕的是——连提醒你的人都没有。"

            qiu "我陪您熬粥。以后天天陪您。"
            qiu "等开学了，我也天天给您打电话，问您今天吃了什么。"

    # 熬粥
    play sound "audio/sfx/gentle_boiling.mp3"

    narrator "小米粥在锅里咕嘟咕嘟地冒着泡。"
    narrator "金黄色的米油慢慢浮上来，像一层薄薄的纱。"
    narrator "我用长勺轻轻搅着，从锅底往上翻——就像奶奶说的那样。"
    narrator "奶奶搬了个小板凳，坐在旁边看着。厨房里弥漫着小米特有的清香。"

    qiu_inner "小时候我生病，奶奶也是这样给我熬粥的。"
    qiu_inner "她坐在床边，一口一口喂我，吹凉了才送到我嘴边。"
    qiu_inner "'慢慢喝，喝完就好了。'——她总是这么说。"
    qiu_inner "那会儿我觉得，只要喝了奶奶的粥，什么病都会好。"
    qiu_inner "现在轮到我熬粥给她喝了。"
    qiu_inner "时光绕了一个圈，把我们换了个位置。"

    # 阳台喝粥
    scene bg_balcony with fade
    play music "audio/bgm/sunset.mp3" fadein 2.0

    narrator "粥煮好了。我们端着碗坐到阳台上。"
    narrator "碗是奶奶惯用的那只青花瓷碗，边沿已经磕了一个小口。"

    show grandma calm at left with dissolve
    show qiu calm at right with dissolve

    narrator "楼下传来孩子们玩耍的声音，远远的，像隔着一层水。"
    narrator "夕阳把整座城市染成金红色，连阳台上的晾衣杆都泛着暖光。"
    narrator "风里带着邻居家炒菜的香味，混着我们碗里的粥香。"

    show item_millet_porridge at truecenter with dissolve
    pause 1.5
    hide item_millet_porridge with dissolve

    grandma "(双手捧着碗，喝了一口，闭上眼睛)好喝。是这个味道。"

    qiu "什么味道？"

    grandma "我说不上来。就是……就是家的味道。"
    grandma "你太姥姥熬的粥是这个味道。我熬的也是。你熬的也是。"
    grandma "这味道传了四代人，一点没变。"

    qiu "那我算是学到真传了。"

    grandma "(认真地看着我)不是真传，是血脉。"
    grandma "有些东西不用教，你的手记得，你的舌头记得。"

    grandma "(放下碗，看着远方)我年轻的时候，觉得人生好长。"
    grandma "觉得有做不完的饭，洗不完的衣服。"
    grandma "恨不得日子过得快点，把孩子盼大，把自己盼老。"
    grandma "现在坐在这里喝粥——突然觉得好像也没有那么长。"
    grandma "不过就是一碗粥的功夫。"

    qiu "那我也慢慢喝。"
    qiu "一口一口地喝。"

    grandma "嗯。粥要趁热喝——但别烫着。"
    grandma "人生也是这样，要趁热——但别急。"

    # 解锁CG
    $ cg_gallery["cg07"] = True
    show cg07 with dissolve
    pause 4.0
    hide cg07 with dissolve

    narrator "我们在夕阳中安静地喝粥。"
    narrator "没人说话，但什么都说了。"
    narrator "碗里的粥慢慢见底，金红色的光一点一点沉下去。"

    grandma "(突然)小秋，你什么时候开学？"

    qiu "还有十天。"

    grandma "那明天学最后一道菜。学完你就毕业了。"

    qiu "好。奶奶，您说话的语气——好像我真的要毕业了一样。"

    grandma "当然是真的。你会做的菜越来越多了。"
    grandma "以后不管去哪里，都能照顾好自己。"
    grandma "饿不着肚子，就是一个人也能把日子过好。"
    grandma "这就是奶奶想看到的。"

    qiu_inner "奶奶说'毕业'的时候，眼神里有一种说不出的东西。"
    qiu_inner "像是骄傲，又像是舍不得。"

    narrator "夕阳又沉下去一点。"
    narrator "风轻轻吹动阳台上晾着的衣服。"
    narrator "有一件是我小时候的衬衫，奶奶一直没舍得扔。"

    scene black with dissolve
    play sound "audio/sfx/page_turn.mp3"

    return