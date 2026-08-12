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

    narrator "今天奶奶精神焕发。她系着围裙，正在指挥我。厨房里弥漫着面粉的清香，案板上摆着一碗调好的白菜猪肉馅，翠绿的菜末混着粉红的肉糜，看着就让人食指大动。"

    qiu_inner "奶奶难得这么有精神。她今天起的比我还早，把所有材料都备齐了，连围裙都系得整整齐齐。我心里有些高兴，又有些酸涩。"

    grandma "今天包饺子。白菜猪肉馅的。"
    grandma "这饺子啊，是你出生那天奶奶做的第一件事。"

    qiu "冬至还没到呢。"

    grandma "不管了。想吃就包。"
    grandma "你出生那年冬至，奶奶包了一大锅饺子。"
    grandma "那天雪下得大，整个村子都白了。我天没亮就起来和面，手都冻红了。"

    qiu "我出生的时候？"

    grandma "(一边擀皮一边说)对。你妈在产房里——"
    grandma "你爸在家包饺子，心不在焉，包一个破一个。"
    grandma "他包的饺子，馅儿都漏在外面，像一个个开口笑。"

    qiu_inner "奶奶的手在擀面杖下打转。面皮一眨眼就成了一个圆，中间厚，边上薄，像是被施了魔法。"
    qiu_inner "我看着她的手，布满了褐色的斑点和细密的皱纹，却灵活得像年轻人的手指。这双手，抱过我，喂过我，现在又教我包饺子。"

    qiu "(笨拙地擀皮)这也太难了。"
    qiu "我擀出来的不是圆的，是歪歪扭扭的多边形。"

    grandma "慢慢来。手要轻，擀面杖要转。"
    grandma "你爸包饺子不行，擀皮也不行。"
    grandma "他那天擀的皮，厚的地方能咬到牙，薄的地方一煮就破。"

    qiu "他后来去医院了吗？"

    grandma "去了。你妈打电话来说生了。"
    grandma "你爸把手上全是面粉的手往脸上一抹——"
    grandma "骑上自行车就往医院跑。"
    grandma "我追出去喊他——围巾都没戴！雪那么大！"

    qiu "您呢？"

    grandma "我在后面追。手上拎着保温桶，里面装着刚煮好的饺子。"
    grandma "雪深到脚脖子，我一脚深一脚浅地走。路上摔了两跤，保温桶抱在怀里没撒手。"
    grandma "到了医院，你爸守在产房门口，脸白得跟外面的雪似的。"

    # 包饺子选择
    menu:
        "包传统月牙形":
            $ companionship += 5
            qiu_inner "我努力把饺子包成奶奶教的月牙形。左手托皮，右手捏褶，一下一下地往前推。"

            grandma "(端详)不错。第一次就包成这样，比我当年强。"
            grandma "你爷爷第一次吃我包的饺子，说像包子。"

            qiu "为什么像包子？"

            grandma "因为我把馅放太多了，圆鼓鼓的。"
            grandma "他说，媳妇儿，你这饺子够实在，一个能顶一碗饭。"
            grandma "后来我就练啊，练了半年才包出像样的月牙。"

        "自己发挥创意":
            $ companionship += 10
            qiu_inner "我尝试包成小动物的形状——最后包了一个歪歪扭扭的'兔子'。两只耳朵一长一短，肚子鼓鼓囊囊。"

            qiu "奶奶你看，这个是兔子！"
            qiu "我属兔的，这个就是小秋兔。"

            grandma "(端详半天)这是兔子？我还以为是老鼠。"
            grandma "你这耳朵，一只长一只短，哪是兔子，分明是被猫咬过的老鼠。"

            qiu "真的像老鼠吗？"
            qiu_inner "我有些泄气。我明明捏了很久，想把它的耳朵弄得好看一些。"

            grandma "(笑)像。但是你包的，再像老鼠也是好饺子。"
            grandma "反正是给自己吃，形状不重要。"
            grandma "你爷爷当年也说，包饺子嘛，能吃就行。他包的饺子跟馄饨似的，一煮就开馅儿。"

    # 煮饺子
    play sound "audio/sfx/boiling.mp3"

    narrator "饺子下锅。滚水翻腾，白色的饺子一个个浮起来，像一群胖乎乎的小鸭子在水里打滚。"
    narrator "蒸汽从锅里腾起，模糊了奶奶的侧脸。她拿着漏勺，眼神专注地盯着锅里，不时点一点凉水。"

    grandma "点三次凉水，饺子就熟了。这叫'三开三点'。"
    grandma "小秋，调蘸料。醋、酱油、辣椒油，再加一点蒜末。"

    qiu_inner "我调着蘸料，闻着锅里飘出来的面香和肉香。这一刻，厨房像一个温暖的怀抱，把我整个人都裹住了。"
    qiu_inner "原来这就是冬至的味道。原来这就是回家的味道。"

    # 上桌
    scene bg_diningtable with dissolve
    show item_dumplings at truecenter with dissolve
    show item_rice at rice_left with dissolve
    show item_rice at rice_right as item_rice_right with dissolve

    narrator "热腾腾的饺子端上桌。白瓷盘里一个个饺子饱满圆润，冒着白白的热气。醋碟里漂着一层红亮的辣椒油，看着就让人食指大动。"

    qiu "(吃饺子)好吃！奶奶，这是我这辈子吃过最好吃的饺子。"
    qiu "皮薄馅大，一口咬下去，汤汁都流出来了。"

    grandma "那是因为是你自己包的。人对自己做的东西，总是格外喜欢。"
    grandma "自己流过汗的饭菜，吃着才香。"

    qiu "不，是因为跟您一起包的。"
    qiu_inner "我说的是真心话。同样的饺子，在城市里我也吃过很多次，但没有一次像今天这样。这里有奶奶的笑声，有窗外的阳光，有面粉的清香，有岁月沉淀下来的、说不清道不明的东西。"

    narrator "奶奶笑了笑。她夹起一个饺子，慢慢嚼着。阳光落在她脸上，照出她眼角细密的纹路，每一条纹路里都藏着笑意。"

    grandma "你出生的时候，我抱着你，看着你的小手小脚。"
    grandma "我想，这个小生命是从哪里来的呢？怎么这么小，这么软。"
    grandma "那么一点点，连哭声都细细的，像小猫叫。"

    qiu "然后呢？"

    grandma "然后我就想——我要活久一点。"
    grandma "要看着你会走路，会说话，会上学。"
    grandma "要看你去考大学，看你结婚。"
    grandma "要看你过得比奶奶好，比奶奶幸福。"

    narrator "她停顿了一下。窗外的风轻轻吹动窗帘，发出沙沙的声响。"

    qiu_inner "我感觉到有什么东西要来了。奶奶的眼神变得温柔，又变得遥远。她看着我，又像是透过我看着更远的地方。"

    grandma "不过我可能……看不到你结婚了。"

    qiu "奶奶！您别这么说。"
    qiu_inner "我的鼻子一酸，赶紧低下头扒饭。我不敢看她的眼睛，怕一抬头，眼泪就会掉下来。"

    grandma "(摆摆手)没事。奶奶就是想说——"
    grandma "不管看不看得到，你一定要找个像你爷爷那样的人。"
    grandma "不用多有钱，但要疼你。就像你爷爷疼我一样。"
    grandma "你爷爷这辈子，没让我受过一点委屈。穷的时候，他把饭省给我吃；富了以后，他还是先给我夹菜。"
    grandma "找个这样的人，比什么都强。"

    qiu_inner "我抬起头，努力冲她笑了一下。她看着我，眼神里有一种说不出的温柔和担忧。"
    qiu_inner "我突然意识到，奶奶是在交代。这些天她教我的每一道菜，说的每一句话，都像是在慢慢地、一点一点地，把她自己交给我。"

    # 解锁CG
    $ cg_gallery["cg05"] = True
    show cg05 with dissolve
    pause 3.0
    hide cg05 with dissolve

    scene black with dissolve
    play sound "audio/sfx/page_turn.mp3"

    return