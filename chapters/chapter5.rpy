# ============================================================
# 第五章：白菜猪肉馅饺子（2000年代）
# ============================================================

label chapter5:
    $ current_chapter = 5

    # 标题出现
    show text "{size=60}{font=fonts/handwrite.ttf}第五道菜{/font}{/size}" at truecenter with dissolve
    pause 10.0
    hide text with dissolve

    scene bg_kitchen with fade
    play music "audio/bgm/warm_family.mp3" fadein 1.0

    show grandma energetic at left with dissolve
    show qiu neutral at right with dissolve

    narrator "今天奶奶精神焕发。她系着围裙，正在指挥我。"

    grandma "今天包饺子。白菜猪肉馅的。"

    qiu "冬至还没到呢。"

    grandma "不管了。想吃就包。"
    grandma "你出生那年冬至，奶奶包了一大锅饺子。"

    qiu "我出生的时候？"

    grandma "(一边擀皮一边说)对。你妈在产房里——"
    grandma "你爸在家包饺子，心不在焉，包一个破一个。"

    qiu_inner "奶奶的手在擀面杖下打转。面皮一眨眼就成了一个圆。"

    qiu "(笨拙地擀皮)这也太难了。"

    grandma "慢慢来。手要轻，擀面杖要转。"
    grandma "你爸包饺子不行，擀皮也不行。"

    qiu "他后来去医院了吗？"

    grandma "去了。你妈打电话来说生了。"
    grandma "你爸把手上全是面粉的手往脸上一抹——"
    grandma "骑上自行车就往医院跑。"

    qiu "您呢？"

    grandma "我在后面追。手上拎着保温桶，里面装着刚煮好的饺子。"

    # 包饺子选择
    menu:
        "包传统月牙形":
            $ companionship += 5
            qiu_inner "我努力把饺子包成奶奶教的月牙形。"

            grandma "(端详)不错。第一次就包成这样，比我当年强。"
            grandma "你爷爷第一次吃我包的饺子，说像包子。"

            qiu "为什么像包子？"

            grandma "因为我把馅放太多了，圆鼓鼓的。"

        "自己发挥创意":
            $ companionship += 10
            qiu_inner "我尝试包成小动物的形状——最后包了一个歪歪扭扭的'兔子'。"

            qiu "奶奶你看，这个是兔子！"

            grandma "(端详半天)这是兔子？我还以为是老鼠。"

            qiu "真的像老鼠吗？"

            grandma "(笑)像。但是你包的，再像老鼠也是好饺子。"
            grandma "反正是给自己吃，形状不重要。"

    # 煮饺子
    play sound "audio/sfx/boiling.mp3"

    narrator "饺子下锅。滚水翻腾，白色的饺子一个个浮起来。"

    grandma "小秋，调蘸料。醋、酱油、辣椒油，再加一点蒜末。"

    # 上桌
    scene bg_diningtable with dissolve
    show item_dumplings at truecenter with dissolve
    show item_rice at rice_left with dissolve
    show item_rice at rice_right as item_rice_right with dissolve

    qiu "(吃饺子)好吃！奶奶，这是我这辈子吃过最好吃的饺子。"

    grandma "那是因为是你自己包的。人对自己做的东西，总是格外喜欢。"

    qiu "不，是因为跟您一起包的。"

    narrator "奶奶笑了笑。她夹起一个饺子，慢慢嚼着。"

    grandma "你出生的时候，我抱着你，看着你的小手小脚。"
    grandma "我想，这个小生命是从哪里来的呢？怎么这么小，这么软。"

    qiu "然后呢？"

    grandma "然后我就想——我要活久一点。"
    grandma "要看着你会走路，会说话，会上学。"
    grandma "要看你去考大学，看你结婚。"

    narrator "她停顿了一下。"

    grandma "不过我可能……看不到你结婚了。"

    qiu "奶奶！您别这么说。"

    grandma "(摆摆手)没事。奶奶就是想说——"
    grandma "不管看不看得到，你一定要找个像你爷爷那样的人。"
    grandma "不用多有钱，但要疼你。就像你爷爷疼我一样。"

    # 解锁CG
    $ cg_gallery["cg05"] = True
    show cg05 with dissolve
    pause 3.0
    hide cg05 with dissolve

    scene black with dissolve
    play sound "audio/sfx/page_turn.mp3"

    return