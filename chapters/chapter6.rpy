# ============================================================
# 第六章：小米粥（现在）
# ============================================================

label chapter6:
    $ current_chapter = 6

    scene bg_kitchen with fade
    play music "audio/bgm/tender.mp3" fadein 2.0

    narrator "第六天傍晚。我从外面回来，推开厨房的门。"

    show grandma crying at center with dissolve

    narrator "灶火开着。锅里空空如也。"
    narrator "奶奶站在灶台前——在哭。"

    show qiu worried at left with dissolve

    qiu "(快步上前)奶奶！怎么了？烫到了吗？"

    grandma "(转身，满脸泪痕)我……我忘了。"

    qiu "忘了什么？"

    grandma "我忘了怎么煮粥。"
    grandma "明明煮了几十年，今天突然就忘了。"
    grandma "米放多少，水放多少——我想不起来了。"

    qiu_inner "奶奶像一个做错事的孩子，无助地看着我。"

    qiu "(握住奶奶的手)没事的，奶奶。您说，我做。"

    grandma "可是我不记得了。"

    qiu "那您慢慢想。水放多少？米淘几遍？"

    grandma "(沉默)水……水放三碗。"

    qiu "好。三碗水。"

    narrator "我拿起碗，量了三碗水，倒进锅里。"

    qiu "然后呢？米怎么淘？"

    grandma "两遍。不要淘太多遍……营养会洗掉。"

    narrator "我把米淘了两遍，倒入锅中。"

    qiu "然后？大火还是小火？"

    grandma "大火煮开，小火慢熬。"
    grandma "开了以后要搅一搅……不然会粘锅。"

    qiu "(轻声)奶奶您看，您全都记得。"

    narrator "奶奶看着锅里开始冒泡的米和水。眼泪还在流，但渐渐平静下来。"

    grandma "小秋，我是不是……是不是要变成废人了。"

    qiu "不是的奶奶。医生说只是偶尔会忘。"
    qiu "您教了我这么多道菜，每一道都记得清清楚楚。"
    qiu "您不是废人——您是我最好的老师。"

    # 关键选择
    menu:
        "“以后我教您。”":
            $ companionship += 10
            qiu "没事的奶奶。我记得，以后换我教您。"

            grandma "(含泪笑)那你得好好学。奶奶这点手艺，不能丢了。"

            qiu "不会丢的。我都记下来了，每个步骤。"

        "“我们都在一起。”":
            $ companionship += 10
            qiu "奶奶，医生说了，只是偶尔会忘。"
            qiu "不管怎样，我们都在您身边。"

            grandma "嗯……你们在就好。"

            qiu "我陪您熬粥。以后天天陪您。"

    # 熬粥
    play sound "audio/sfx/gentle_boiling.mp3"

    narrator "小米粥在锅里咕嘟咕嘟地冒着泡。"
    narrator "我用长勺轻轻搅着。奶奶搬了个小板凳，坐在旁边看着。"

    qiu_inner "小时候我生病，奶奶也是这样给我熬粥的。"
    qiu_inner "她坐在床边，一口一口喂我。"
    qiu_inner "'慢慢喝，喝完就好了。'——她总是这么说。"
    qiu_inner "现在轮到我熬粥给她喝了。"

    # 阳台喝粥
    scene bg_balcony with fade
    play music "audio/bgm/sunset.mp3" fadein 2.0

    narrator "粥煮好了。我们端着碗坐到阳台上。"

    show grandma calm at left with dissolve
    show qiu calm at right with dissolve

    narrator "楼下传来孩子们玩耍的声音。"
    narrator "夕阳把整座城市染成金红色。"

    show item_millet_porridge at truecenter with dissolve
    pause 1.5
    hide item_millet_porridge with dissolve

    grandma "(喝了一口)好喝。是这个味道。"

    qiu "什么味道？"

    grandma "我说不上来。就是……就是家的味道。"
    grandma "你太姥姥熬的粥是这个味道。我熬的也是。你熬的也是。"

    qiu "那我算是学到真传了。"

    grandma "(放下碗，看着远方)我年轻的时候，觉得人生好长。"
    grandma "觉得有做不完的饭，洗不完的衣服。"
    grandma "现在坐在这里喝粥——突然觉得好像也没有那么长。"
    grandma "不过就是一碗粥的功夫。"

    qiu "那我也慢慢喝。"

    grandma "嗯。粥要趁热喝——但别烫着。"

    # 解锁CG
    $ cg_gallery["cg07"] = True
    show cg07 with dissolve
    pause 4.0
    hide cg07 with dissolve

    narrator "我们在夕阳中安静地喝粥。"

    grandma "(突然)小秋，你什么时候开学？"

    qiu "还有十天。"

    grandma "那明天学最后一道菜。学完你就毕业了。"

    qiu "好。奶奶，您说话的语气——好像我真的要毕业了一样。"

    grandma "当然是真的。你会做的菜越来越多了。"
    grandma "以后不管去哪里，都能照顾好自己。"
    grandma "这就是奶奶想看到的。"

    narrator "夕阳又沉下去一点。"
    narrator "风轻轻吹动阳台上晾着的衣服。"

    scene black with dissolve
    play sound "audio/sfx/page_turn.mp3"

    return