# ============================================================
# 第七章：最后一页（离别）
# ============================================================

label chapter7:
    $ current_chapter = 7

    # 标题出现
    show text "{size=60}{font=fonts/handwrite.ttf}第七道菜{/font}{/size}" at truecenter with dissolve
    pause 10.0
    hide text with dissolve

    scene bg_kitchen with fade
    play music "audio/bgm/farewell.mp3" fadein 2.0

    narrator "第七天。我走到厨房门口。"

    show grandma dressed at center with dissolve

    narrator "奶奶已经在里面了。今天她没有系围裙。"
    narrator "她穿着那件出门才穿的藏蓝色外套。"

    show qiu neutral at left with dissolve

    qiu "奶奶，您穿这么整齐干嘛？"

    grandma "今天不学做菜。"
    grandma "今天奶奶带你出去吃。"

    qiu "为什么？"

    grandma "因为——最后一页不是菜谱。"

    # 客厅
    scene bg_livingroom with dissolve
    show grandma calm at left
    show qiu neutral at right

    grandma "是我写给你的话。"
    grandma "我这几天想了想，决定不等了，现在就读给你听。"

    narrator "奶奶从怀里掏出那本菜谱，翻到最后一页。"

    grandma "这页我粘了好几年了。"
    grandma "我怕太早给你，你不懂。"
    grandma "又怕太晚给你——我看不到。"

    narrator "她把菜谱递给我。"

    grandma "你自己看吧。奶奶念不好。"

    # 信的内容
    scene bg_letter with dissolve
    play sound "audio/sfx/paper_unfold.mp3"
    $ cg_gallery["cg08"] = True

    # 用奶奶的"画外音"展示信的内容
    "{i}{size=26}小秋：{/size}{/i}"
    pause 1.0

    "{i}{size=26}等你看到这封信的时候，奶奶可能已经不太认得你了。{/size}{/i}"
    pause 1.0

    "{i}{size=26}但是没关系。你认得奶奶就行。{/size}{/i}"
    pause 1.0

    "{i}{size=26}这本菜谱是你太姥姥传给我的。我本来想等你结婚的时候再给你。{/size}{/i}"
    "{i}{size=26}可是你刚去上大学，我就发现自己老忘事。{/size}{/i}"
    "{i}{size=26}昨天晚上我把饭煮焦了，因为忘了关火。{/size}{/i}"
    pause 1.5

    "{i}{size=26}我怕有一天，我连怎么写字都忘了。{/size}{/i}"
    "{i}{size=26}所以趁还记得，我把想说的话都写在这里。{/size}{/i}"
    pause 1.5

    "{i}{size=26}炒鸡蛋要温柔，{/size}{/i}"
    "{i}{size=26}蒸鱼要有耐心，{/size}{/i}"
    "{i}{size=26}红烧肉要大方放料，{/size}{/i}"
    "{i}{size=26}土豆丝要细致，{/size}{/i}"
    "{i}{size=26}饺子要团圆，{/size}{/i}"
    "{i}{size=26}粥要慢慢熬。{/size}{/i}"
    pause 1.5

    "{i}{size=26}做菜是这样，做人也是这样。{/size}{/i}"
    pause 1.5

    "{i}{size=26}以后想奶奶了，就做一道菜。{/size}{/i}"
    "{i}{size=26}做西红柿炒鸡蛋的时候，记得先炒蛋。{/size}{/i}"
    "{i}{size=26}蒸鱼的时候，记得大火不能超过十分钟。{/size}{/i}"
    "{i}{size=26}红烧肉炒糖色要小火。{/size}{/i}"
    "{i}{size=26}饺子包得丑没关系。{/size}{/i}"
    "{i}{size=26}粥要多搅搅。{/size}{/i}"
    pause 1.5

    "{i}{size=26}奶奶在你做的每一道菜里。{/size}{/i}"
    pause 2.0

    "{i}{size=26}小秋，你是奶奶这辈子最骄傲的成就。{/size}{/i}"
    "{i}{size=26}不是因为你考上了好大学——{/size}{/i}"
    "{i}{size=26}是因为你是一个善良的孩子。{/size}{/i}"
    pause 1.5

    "{i}{size=26}以后你会遇到很多人，有的人好，有的人不好。{/size}{/i}"
    "{i}{size=26}你记住，无论谁让你难过，你都可以回家。{/size}{/i}"
    "{i}{size=26}奶奶给你做饭。{/size}{/i}"
    "{i}{size=26}如果奶奶不在了——你就自己做。{/size}{/i}"
    pause 2.0

    "{i}{size=26}其实我一直很害怕。{/size}{/i}"
    "{i}{size=26}害怕忘了你，忘了你的名字，忘了我自己是谁。{/size}{/i}"
    pause 1.5

    "{i}{size=26}但后来我想通了。{/size}{/i}"
    "{i}{size=26}一个人最后忘掉的，一定是她最在乎的东西。{/size}{/i}"
    pause 1.5

    "{i}{size=26}所以我不会忘掉你的。{/size}{/i}"
    "{i}{size=26}就算我什么都不记得了——{/size}{/i}"
    "{i}{size=26}我的心里也一定有一个位置，是留给你的。{/size}{/i}"
    "{i}{size=26}那个位置的名字就叫'小秋'。{/size}{/i}"
    pause 2.0

    "{i}{size=28}爱你的奶奶{/size}{/i}"
    "{i}{size=22}写于2024年春天{/size}{/i}"

    # 回到现实
    scene bg_livingroom with dissolve
    show grandma worried at left

    narrator "我抬起头。信纸湿了一大片。"

    grandma "(小心地问)能看清吗？我的字……有没有写错？"

    show qiu crying at right

    qiu "(把菜谱抱在胸前)看清了，奶奶。每一个字都看清了。"

    grandma "(松了一口气)那就好。我就是怕你以后不知道。"
    grandma "其实做菜啊，最重要的不是技术。"

    qiu "那是什么？"

    grandma "是有人愿意吃你做的菜。"
    grandma "我做了一辈子，最开心的是看你和你爸把盘子吃干净。"

    qiu "奶奶，我以后每次做了菜，都会拍照片给您看。"

    grandma "好。不过别拍得太难看——奶奶要面子。"

    narrator "我们笑了。笑声里带着鼻酸。"

    $ cg_gallery["cg08"] = True
    show cg08 with dissolve
    pause 4.0
    hide cg08 with dissolve

    # 离别
    scene bg_xiaoqiu_room with fade

    narrator "第二天清晨。我的行李箱摊开在地上。"
    narrator "那本菜谱放在最上面，用毛巾包好。"

    qiu_inner "七天太短了。短到我还没来得及学会奶奶所有的菜。"
    qiu_inner "可是七天也够长了。"
    qiu_inner "长到让我知道——我在她心里，从一开始就有一个位置。"

    scene bg_livingroom with dissolve
    show grandma calm at center

    narrator "奶奶已经起来了，坐在沙发上。"
    narrator "茶几上的药瓶旁边多了一杯水。"
    narrator "她手里拿着我小时候的照片。"

    show qiu neutral at left with dissolve

    qiu "(轻声)奶奶，我走了。"

    grandma "(抬起头)路上小心。到了给奶奶打电话。"

    qiu "嗯。奶奶，记得按时吃药。灶台用完要关火。"

    grandma "我知道。你比我还能念叨。"

    narrator "我走到门口，提起行李箱。回头看了一眼。"

    grandma "(追出来)小秋！"

    qiu "奶奶？"

    grandma "(扶着门框)你……你是去上大学对吧？"
    grandma "我刚才差点想不起来你要去哪里了。"

    show qiu touched

    qiu "(忍住泪水)对。我去上大学。我学的是新闻——以后当记者。"

    grandma "(放心地笑了)记者好。记者能写文章。"
    grandma "你从小作文就写得好。"

    qiu "奶奶，您还记得我小时候写的作文？"

    grandma "记得。你写《我的奶奶》，老师给你评了优。"
    grandma "那篇作文我现在还收在枕头下面。"

    narrator "我放下行李箱——走回来——紧紧抱住了奶奶。"

    qiu "奶奶，我不会忘记您的。永远不会。"

    grandma "(轻轻拍着我的背)奶奶也不会忘记你。"
    grandma "就算忘了全世界——"
    grandma "奶奶也会记得，我有一个孙女，她叫小秋。"

    scene black with dissolve
    play sound "audio/sfx/page_turn.mp3"

    return