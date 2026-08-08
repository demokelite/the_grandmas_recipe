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

    narrator "第四天。我走进厨房。"

    show grandma confused at center with dissolve

    narrator "奶奶站在灶台前，手里拿着一个土豆。"
    narrator "但她一动不动。切菜板上的刀没有动过。锅是冷的。"

    show qiu neutral at right with dissolve

    qiu "(轻声)奶奶？"

    grandma "(慢慢转头)嗯？"

    qiu "我们今天学什么菜？"

    grandma "(低头看土豆)这个是……这个是……"

    narrator "她的声音越来越小。手指在土豆上摩挲。"

    grandma "这个要……要怎么做来着？"

    qiu_inner "我的心揪了一下。"

    # 关键选择
    menu:
        "温柔提醒":
            $ companionship += 10
            qiu "(轻声)奶奶，今天学酸辣土豆丝。要切丝的，记得吗？"

            show grandma relieved
            grandma "(眼神亮了一下)对对对！酸辣土豆丝！"
            grandma "我就说怎么拿着土豆想不起来要干嘛。"
            grandma "来，奶奶教你。"

            qiu_inner "她开始削土豆皮。动作有些迟疑，但慢慢熟练起来。"

        "沉默等待":
            $ companionship += 5
            qiu_inner "我没有说话。站在旁边，等她自己想起来。"

            narrator "奶奶拿着土豆，站了十几秒。"

            grandma "(突然)酸辣土豆丝！"
            grandma "小秋，快帮奶奶拿醋！咱们今天做这个。"

            qiu_inner "我松了一口气，转身去拿醋。"

            grandma "(自言自语)这脑子，最近老卡壳。"

            qiu_inner "我背对着奶奶，眼眶有些发酸。"

    # 切土豆丝
    show qiu focused
    qiu_inner "我开始切土豆。刀工一般，切出来的丝粗细不一。"

    grandma "(凑过来看)哎哟，这是土豆丝还是土豆条？"

    qiu "我已经很努力了。"

    grandma "看奶奶的。"

    narrator "奶奶接过刀。起初有些生疏，但切了几刀之后，节奏渐渐流畅。"
    play sound "audio/sfx/chopping.mp3"

    narrator "笃笃笃笃的声音在厨房里回荡。"

    qiu "(惊叹)奶奶，你切得好快。"

    grandma "那当然。切了二十年的土豆丝。"
    grandma "你妈第一次来家里，我就做了这道菜。"

    qiu "妈妈跟我提起过。她说你切的丝特别细，她学了三个月也没学会。"

    grandma "(得意)你妈那手，拿笔杆子行，拿菜刀不行。"
    grandma "她来学的时候，把我家的土豆全切坏了。"

    qiu "后来呢？"

    grandma "后来你爸说，妈你别难为她了。"
    grandma "我说，她要是切不好，以后就你切。"

    qiu "(笑)爸会做饭吗？"

    grandma "不会！他把鸡蛋煎成了黑炭。"
    grandma "你妈后来说，她愿意吃一辈子黑炭。"

    # 下锅
    play sound "audio/sfx/sizzle_hot.mp3"

    grandma "大火快炒！不然土豆丝就软了。"
    grandma "听到这个声音了吗？这叫锅气。"

    # 解锁CG
    $ cg_gallery["cg04"] = True
    show cg04 with dissolve
    pause 3.0
    hide cg04 with dissolve

    # 成品
    show item_shredded_potato at truecenter with dissolve
    show item_rice at rice_left with dissolve
    show item_rice at rice_right as item_rice_right with dissolve

    narrator "一盘酸辣土豆丝上桌。色泽金黄，醋香扑鼻。"

    qiu "(吃了一口)奶奶，您切的土豆丝真的不一样。"

    grandma "那是。切了二十年了。你太姥姥传的手艺。"
    grandma "你奶奶我发扬光大。"

    qiu "那以后传给谁？"

    grandma "当然是传给你。你学会了吗？"

    qiu "学会了。以后我也切二十年。"

    grandma "(笑)傻孩子。你切二十年，奶奶都变成土了。"

    qiu "您别说这种话。"

    grandma "好好好，不说。"
    grandma "不过就算变成土，奶奶也会惦记着——小秋学会切土豆丝没有。"

    scene black with dissolve
    play sound "audio/sfx/page_turn.mp3"

    return