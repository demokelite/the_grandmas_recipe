# ============================================================
# 结局判定与片尾
# ============================================================

# 图片偏上居中位置（用于二维码与下方文字错开）
transform top_center:
    xalign 0.5
    yalign 0.32
    zoom 0.45

# 二维码下方文字位置
transform qr_bottom:
    xalign 0.5
    yalign 0.68

label ending_judgment:
    $ renpy.log("[ending] === 结局判定 开始 ===")
    $ renpy.log("[ending] scene: black")
    scene black with dissolve
    $ renpy.log("[ending] stop music")
    stop music fadeout 2.0

    # 判定结局
    if companionship >= 80:
        $ ending_type = "good"
        jump ending_good
    elif companionship >= 50:
        $ ending_type = "normal"
        jump ending_normal
    else:
        $ ending_type = "sad"
        jump ending_sad

# ========== 好结局 ==========
label ending_good:
    $ renpy.log("[ending] === 好结局 开始 ===")
    # 标题出现
    show text "{size=60}{font=fonts/handwrite.ttf}好结局{/font}{/size}" at truecenter with dissolve
    pause 10.0
    hide text with dissolve

    $ renpy.log("[ending] scene: bg_kitchen")
    scene bg_kitchen with fade
    $ renpy.log("[ending] music: audio/bgm/reunion.mp3")
    play music "audio/bgm/reunion.mp3" fadein 2.0

    narrator "寒假。我推开奶奶家的门。"

    $ renpy.log("[ending] show: grandma happy at center")
    show grandma happy at center with dissolve

    grandma "(转身，眼神清澈)小秋！快进来，外面冷！"
    grandma "奶奶做了你爱吃的红烧肉。"

    $ renpy.log("[ending] show: qiu happy at left")
    show qiu happy at left with dissolve

    qiu "(走过去帮忙端菜)奶奶，我在学校创了一道新菜。"
    qiu "我写在菜谱后面了。"

    grandma "什么菜？"

    qiu "西红柿炒方便面。"

    grandma "(愣了一秒，大笑)这是什么黑暗料理！"
    grandma "快做给奶奶尝尝！"

    narrator "我们在厨房里忙碌。笑声传出窗外。"

    show text "{size=40}结局：菜谱在继续{/size}" at truecenter with dissolve
    pause 2.0

    show text "{size=24}记忆会模糊，但爱会不断续写。{/size}" at truecenter with dissolve
    pause 3.0

    $ renpy.log("[ending] === 好结局 结束 ===")
    return

# ========== 普通结局 ==========
label ending_normal:
    $ renpy.log("[ending] === 普通结局 开始 ===")
    # 标题出现
    show text "{size=60}{font=fonts/handwrite.ttf}普通结局{/font}{/size}" at truecenter with dissolve
    pause 10.0
    hide text with dissolve

    $ renpy.log("[ending] scene: bg_livingroom")
    scene bg_livingroom with fade
    $ renpy.log("[ending] music: audio/bgm/bittersweet.mp3")
    play music "audio/bgm/bittersweet.mp3" fadein 2.0

    narrator "寒假。我推开奶奶家的门。"

    $ renpy.log("[ending] show: grandma neutral at center")
    show grandma neutral at center with dissolve

    grandma "(看到我，愣了愣)你……你是来找谁的？"

    $ renpy.log("[ending] show: qiu touched at left")
    show qiu touched at left with dissolve

    qiu_inner "我忍住鼻酸，走进厨房。"
    qiu_inner "做了一盘西红柿炒鸡蛋，端到奶奶面前。"

    grandma "(吃了一口，突然停下来)"

    qiu "怎么了？不好吃吗？"

    grandma "(缓缓开口)这个味道……是我教的人做的。"
    grandma "你……你是谁？是不是我的徒弟？"

    qiu "(含泪笑)对。我是您的徒弟。我叫小秋。"

    grandma "小秋……这个名字好听。"

    show text "{size=40}结局：味道记得{/size}" at truecenter with dissolve
    pause 2.0

    show text "{size=24}她忘了你的名字，但记得你带来的味道。{/size}" at truecenter with dissolve
    pause 3.0

    $ renpy.log("[ending] === 普通结局 结束 ===")
    return

# ========== 感人结局 ==========
label ending_sad:
    $ renpy.log("[ending] === 感人结局 开始 ===")
    # 标题出现
    show text "{size=60}{font=fonts/handwrite.ttf}感人结局{/font}{/size}" at truecenter with dissolve
    pause 10.0
    hide text with dissolve

    $ renpy.log("[ending] scene: bg_balcony")
    scene bg_balcony with fade
    $ renpy.log("[ending] music: audio/bgm/gentle_sadness.mp3")
    play music "audio/bgm/gentle_sadness.mp3" fadein 2.0

    narrator "寒假。我推开奶奶家的门。"

    $ renpy.log("[ending] show: grandma calm at center")
    show grandma calm at center with dissolve

    narrator "奶奶在阳台上晒太阳。"
    narrator "腿上的毛毯滑落了。我走过去帮她盖好。"

    grandma "(看向我，礼貌地微笑)你好。"

    $ renpy.log("[ending] show: qiu sad at left")
    show qiu sad at left with dissolve

    qiu_inner "我走进奶奶的房间。"
    qiu_inner "床头柜上放着菜谱。翻开最后一页——信纸上似乎被抚摸过很多次。"

    qiu_inner "我走进厨房，做了一碗小米粥。"
    qiu_inner "端到奶奶面前。"

    narrator "奶奶喝了一口，没有说话。"
    narrator "但她把粥都喝完了。"
    narrator "那是她唯一没忘记的事——有人给她做饭，她就该好好吃完。"

    show text "{size=40}结局：信还在{/size}" at truecenter with dissolve
    pause 2.0

    show text "{size=24}即使世界变得陌生，爱依然在某处活着。{/size}" at truecenter with dissolve
    pause 3.0

label credits:
    $ renpy.log("[ending] === 片尾 开始 ===")
    $ renpy.log("[ending] scene: black")
    scene black with dissolve
    $ renpy.log("[ending] stop music")
    stop music fadeout 2.0
    $ renpy.log("[ending] music: audio/bgm/ending.mp3")
    play music "audio/bgm/ending.mp3" fadein 3.0 loop

    # 片尾文字
    show text "{size=48}{color=#ffd700}谨以此游戏{/color}{/size}\n{size=40}献给所有正在或将要{color=#ff9999}面对亲人遗忘{/color}的你。{/size}" at truecenter with dissolve
    pause 4.0
    hide text with dissolve

    show text "{size=40}阿尔兹海默症带走了记忆，{color=#ffd700}带不走爱{/color}。{/size}" at truecenter with dissolve
    pause 3.0
    hide text with dissolve

    show text "{size=38}如果你的家人出现以下情况：{/size}\n\n{size=36}{color=#e8c547}1. 经常忘记关火、关水{/color}{/size}\n{size=36}{color=#e8c547}2. 反复询问同样的问题{/color}{/size}\n{size=36}{color=#e8c547}3. 忘记回家的路{/color}{/size}\n{size=36}{color=#e8c547}4. 性格突然变得多疑或暴躁{/color}{/size}\n\n{size=38}请及时带他们去医院检查。{/size}\n{size=38}{color=#ff9999}早期干预，可以有效延缓病情。{/color}{/size}" at truecenter with dissolve
    pause 8.0
    hide text with dissolve

    show text "{size=46}{color=#ffd700}陪伴，是最好的治疗。{/color}{/size}" at truecenter with dissolve
    pause 3.0
    hide text with dissolve

    $ renpy.log("[ending] show: qrcode_care at top_center")
    show qrcode_care at top_center with dissolve
    show text "{size=34}了解更多：{color=#4fc3f7}认知症友好社区公益项目{/color}{/size}\n{size=28}https://gongyi.qq.com/succor/detail.htm?id=3013612{/size}" at qr_bottom with dissolve
    pause 5.0
    hide text with dissolve
    hide qrcode_care with dissolve

    # 制作人员
    show text "{size=38}{color=#ffd700}制作团队{/color}{/size}\n\n{size=30}知识混子{/size}\n{size=30}制作{/size}\n\n{size=24}参考素材来源：{/size}\n{size=24}阿尔兹海默症相关公益组织{/size}" at truecenter with dissolve
    pause 6.0
    hide text with dissolve

    show text "{size=44}{color=#ffd700}感谢您的游玩。{/color}{/size}\n\n{size=30}—— 奶奶的菜谱 ——{/size}" at truecenter with dissolve
    pause 4.0
    hide text with dissolve

    $ renpy.log("[ending] === 片尾 结束 ===")
    return
