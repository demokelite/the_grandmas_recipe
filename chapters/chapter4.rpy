# ============================================================
# 第四章：酸辣土豆丝（1990年代）
# ============================================================

label chapter4:
    $ current_chapter = 4

    # 标题出现
    show text "{size=60}{font=fonts/handwrite.ttf}第四道菜{/font}{/size}" at truecenter with dissolve
    pause 10.0
    hide text with dissolve

    scene bg_kitchen with fade
    play music "audio/bgm/gentle.mp3" fadein 1.0

    narrator "第四天。我走进厨房。清晨的空气还带着露水的凉意，灶台上的铁锅泛着冷冷的光。"

    show grandma confused at center with dissolve

    narrator "奶奶站在灶台前，手里拿着一个土豆。"
    narrator "但她一动不动。切菜板上的刀没有动过。锅是冷的。窗外的光照在她侧脸上，把她的轮廓勾得有些苍白。"

    qiu_inner "我站在门口看了她好一会儿。她的肩膀微微佝偻，手里那个土豆被她攥得发白。这是我从未见过的奶奶。"

    show qiu neutral at right with dissolve

    qiu "(轻声)奶奶？"

    grandma "(慢慢转头)嗯？"

    qiu "我们今天学什么菜？"

    grandma "(低头看土豆)这个是……这个是……"

    narrator "她的声音越来越小。手指在土豆上摩挲，像是在抚摸一件遗忘了名字的老物件。"

    grandma "这个要……要怎么做来着？"

    qiu_inner "我的心揪了一下。那种感觉，像是有人在我胸口轻轻拧了一把。"
    qiu_inner "昨天她还在跟我讲爷爷杀猪的故事，今天就忘了手里拿的是什么。这种落差，比任何一道菜都让人难以下咽。"

    # 关键选择
    menu:
        "温柔提醒":
            $ companionship += 10
            qiu "(轻声)奶奶，今天学酸辣土豆丝。要切丝的，记得吗？"

            show grandma relieved
            grandma "(眼神亮了一下)对对对！酸辣土豆丝！"
            grandma "我就说怎么拿着土豆想不起来要干嘛。"
            grandma "来，奶奶教你。"

            qiu_inner "她开始削土豆皮。动作有些迟疑，但慢慢熟练起来。削皮刀在土豆上沙沙地响，一条条薄薄的土豆皮落到盆里。"
            qiu_inner "我看到她的手在轻轻发抖，但她的眼神却渐渐恢复了往日的专注。这一刻，她还是那个能切出二十年夜功的奶奶。"

        "沉默等待":
            $ companionship += 5
            qiu_inner "我没有说话。站在旁边，等她自己想起来。我不忍心打断她，也不忍心看到她为难的样子。"

            narrator "奶奶拿着土豆，站了十几秒。厨房里安静得能听到挂钟走针的声音，滴答，滴答。"

            qiu_inner "这十几秒，长得像一辈子。我的手指抠着衣角，眼睛不敢看她。"

            grandma "(突然)酸辣土豆丝！"
            grandma "小秋，快帮奶奶拿醋！咱们今天做这个。"

            qiu_inner "我松了一口气，胸口那块石头终于落了地。转身去拿醋的时候，我努力让自己的步伐看起来轻松些。"

            grandma "(自言自语)这脑子，最近老卡壳。"

            qiu_inner "我背对着奶奶，眼眶有些发酸。我使劲眨了眨眼，不让眼泪掉下来。醋瓶子在手里凉得沁人。"

    # 切土豆丝
    show qiu focused
    qiu_inner "我开始切土豆。刀工一般，切出来的丝粗细不一。有的细得像发丝，有的粗得像筷子。"

    grandma "(凑过来看)哎哟，这是土豆丝还是土豆条？"
    grandma "你这刀工，是要做土豆丝还是做土豆棍儿？"

    qiu "我已经很努力了。"
    qiu_inner "我有些不好意思。在学校里我也做过饭，但从没被这样挑剔过。可奶奶说得对，我切的这些，实在称不上'丝'。"

    grandma "看奶奶的。"

    narrator "奶奶接过刀。起初有些生疏，但切了几刀之后，节奏渐渐流畅。她的眼神变得专注，仿佛整个厨房只剩下她和那块土豆。"
    play sound "audio/sfx/chopping.mp3"

    narrator "笃笃笃笃的声音在厨房里回荡。刀刃落在砧板上，每一下都干脆利落，像是节拍器在打拍子。"

    qiu_inner "我看得呆了。土豆在她手下变成了细细的丝，每一根都差不多粗细，齐齐整整地倒在砧板上，像一捧刚捞起来的银丝。"

    qiu "(惊叹)奶奶，你切得好快。"

    grandma "那当然。切了二十年的土豆丝。"
    grandma "你妈第一次来家里，我就做了这道菜。"

    qiu "妈妈跟我提起过。她说你切的丝特别细，她学了三个月也没学会。"
    qiu "她还说，那天她紧张得手心全是汗，切到自己手指头了。"

    grandma "(得意)你妈那手，拿笔杆子行，拿菜刀不行。"
    grandma "她来学的时候，把我家的土豆全切坏了。"
    grandma "切完了砧板上像堆了一座小山，一半是丝，一半是块。"

    qiu "后来呢？"

    grandma "后来你爸说，妈你别难为她了。"
    grandma "我说，她要是切不好，以后就你切。"

    qiu "(笑)爸会做饭吗？"

    grandma "不会！他把鸡蛋煎成了黑炭。"
    grandma "锅都黑了三天洗不掉。"
    grandma "你妈后来说，她愿意吃一辈子黑炭。"

    qiu_inner "我笑出了声。原来爸爸妈妈年轻的时候，是这样的。我从未在他们身上看到过这些故事的影子。他们现在的生活，像一本已经写好的书，每一页都整整齐齐。可原来，他们也曾笨手笨脚，也曾闹过这样的笑话。"

    # 下锅
    play sound "audio/sfx/sizzle_hot.mp3"

    grandma "大火快炒！不然土豆丝就软了。"
    grandma "听到这个声音了吗？这叫锅气。"
    grandma "会做饭的人，听到这声儿就知道火候到了。"

    narrator "油在锅底噼啪作响，土豆丝下锅的瞬间，腾起一阵白雾。醋从锅边淋下去，刺啦一声，酸香立刻冲了出来，呛得我鼻子发酸。"

    qiu_inner "这就是奶奶说的'锅气'。原来一锅好菜，是有声音、有香气、有温度的。它不是食谱上那些冷冰冰的克数和时间。"

    # 解锁CG
    $ cg_gallery["cg04"] = True
    show cg04 with dissolve
    pause 3.0
    hide cg04 with dissolve

    # 成品
    show item_shredded_potato at truecenter with dissolve
    show item_rice at rice_left with dissolve
    show item_rice at rice_right as item_rice_right with dissolve

    narrator "一盘酸辣土豆丝上桌。色泽金黄，醋香扑鼻。每一根土豆丝都裹着薄薄的油光，红红的干辣椒点缀其间，像秋日落叶上的露珠。"

    qiu "(吃了一口)奶奶，您切的土豆丝真的不一样。"
    qiu "又脆又爽，酸辣刚好，一点都不涩。"

    grandma "那是。切了二十年了。你太姥姥传的手艺。"
    grandma "你奶奶我发扬光大。"

    qiu "那以后传给谁？"

    grandma "当然是传给你。你学会了吗？"

    qiu "学会了。以后我也切二十年。"

    grandma "(笑)傻孩子。你切二十年，奶奶都变成土了。"

    qiu "您别说这种话。"

    grandma "好好好，不说。"
    grandma "不过就算变成土，奶奶也会惦记着——小秋学会切土豆丝没有。"
    grandma "变成土，也要长出一棵土豆来给你切。"

    qiu_inner "我低下头，假装专心吃饭，不让她看到我红了的眼眶。她笑着说这些话，我却听不出一点玩笑的意味。"
    qiu_inner "这一刻我突然明白，所谓的传承，不是一道菜的食谱，而是这样一个人切给你的、带着她温度的土豆丝。"

    scene black with dissolve
    play sound "audio/sfx/page_turn.mp3"

    return