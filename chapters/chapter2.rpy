# ============================================================
# 第二章：清蒸鲈鱼（1970年代）
# ============================================================

label chapter2:
    $ current_chapter = 2

    # 标题出现
    show text "{size=60}{font=fonts/handwrite.ttf}第二道菜{/font}{/size}" at truecenter with dissolve
    pause 10.0
    hide text with dissolve

    scene bg_kitchen with fade
    play music "audio/bgm/gentle_morning.mp3" fadein 1.0

    show grandma happy at left with dissolve
    show qiu neutral at right with dissolve

    grandma "(从冰箱里拿出鲈鱼)今天教你蒸鱼。"
    grandma "蒸鱼最要紧的是什么，知道吗？"
    grandma "你先想想，猜猜看。"

    qiu "火候？"
    qiu "我看电视上说，蒸东西火候最重要。"

    grandma "也对，也不对。"
    grandma "火候是手上的事，但有些事比火候更在前头。"

    qiu "那是什么？"

    grandma "是鱼要新鲜。鱼不新鲜，再怎么蒸都不鲜。"
    grandma "不新鲜的鱼，蒸出来腥气重，肉也散。"
    grandma "你以后买鱼，先看眼睛——眼睛亮的、清楚的，才新鲜。"

    show qiu surprised
    qiu "(凑近看)这条鱼新鲜吗？"
    qiu "眼睛……是亮的！奶奶您看，像玻璃珠一样。"

    grandma "当然。我早上六点去菜市场挑的。"
    grandma "我去的时候，卖鱼的刚摆摊。"
    grandma "我从三筐鱼里挑了这一条，最精神的一条。"

    qiu "您走那么远？菜市场在下面那条街，来回要二十分钟。"
    qiu "您腿不好，下坡还疼。"

    grandma "走走路对身体好。再说——给我孙女买鱼，能嫌远吗？"
    grandma "你奶奶这把老骨头，还没到走不动的时候。"

    show qiu touched

    narrator "我顿了一下。"
    narrator "厨房的窗透进来清晨的光，照在奶奶花白的头发上。"
    narrator "她的手背上有几道浅浅的口子，是择鱼鳞时划的。"

    qiu "(轻声)奶奶，下次我跟您一起去。"
    qiu "我陪您挑，您就不用一个人走那么远了。"

    # 备鱼
    show qiu focused

    grandma "好了，看好了。鱼身上划三刀，方便入味。"
    grandma "刀要斜着下去，划到骨头，但别切断。"
    grandma "葱切段，姜切片。鱼肚子里也塞葱姜，去腥。"
    grandma "葱姜得多放点，鱼腥味压不住就毁了。"

    qiu_inner "我小心翼翼地拿起刀，在鱼身上划了三道口子。"
    qiu_inner "鱼皮很滑，刀一滑就怕切到手指。"
    qiu_inner "我屏住呼吸，一刀一刀地划，像在做一件很庄重的事。"

    qiu "这样对吗？"

    grandma "(看了一眼)再深一点。别怕，鱼不会疼的。"
    grandma "你看，划到骨头边上就行，这样蒸的时候味道才进得去。"

    qiu "我怕切坏。"
    qiu "我怕一刀下去切断了，整条鱼就不好看了。"

    grandma "切坏了也是鱼。人做的菜，哪有完美的。"
    grandma "你爷爷当年说我蒸的鱼好看，我说那是因为他没见过更好看的。"
    grandma "其实好看不好看不要紧，要紧的是用心。"

    # 蒸鱼时间选择
    qiu_inner "鱼放进蒸锅。现在最关键的是——时间。"

    menu:
        "蒸8分钟":
            $ companionship += 10
            qiu_inner "我定了八分钟的计时器。"
            qiu_inner "我心里默念奶奶的话——蒸鱼不能超过十分钟。"
            qiu_inner "八分钟，应该刚刚好。"

            narrator "八分钟，我站在蒸锅边，看着锅盖边缘冒出的白汽。"
            narrator "厨房里弥漫着鱼香和葱姜的气息，时间过得特别慢。"
            narrator "八分钟后，我打开锅盖。"

            show item_steamed_fish at truecenter with dissolve
            # show item_rice at rice_left with dissolve
            # show item_rice at rice_right as item_rice_right with dissolve

            narrator "蒸汽涌出。鱼肉洁白，筷子轻轻一拨就散开。"
            narrator "鱼眼珠变白凸起，鱼皮微微裂开，露出底下雪白的肉。"

            grandma "(满意地点头)刚刚好。鱼肉最嫩的时候就是现在。"
            grandma "你看这肉，一瓣一瓣的，像蒜瓣一样。这就是火候到了。"

            qiu "真的吗？"
            qiu "真的能用筷子拨开，一点都不费劲。"

            grandma "你尝一口就知道了。好的蒸鱼，不用嚼，舌头一抿就化了。"
            grandma "这就是新鲜鱼蒸对了时间的味道。记住了？"

        "蒸12分钟":
            qiu_inner "我定了十二分钟的计时器。"
            qiu_inner "我想着多蒸一会儿总没错，熟透点更放心。"

            narrator "十二分钟里，我时不时掀开锅盖看一眼。"
            narrator "奶奶皱了皱眉，没说话。"
            narrator "十二分钟后。开锅时鱼肉有些发紧。"

            show item_steamed_fish at truecenter with dissolve
            # show item_rice at rice_left with dissolve
            # show item_rice at rice_right as item_rice_right with dissolve

            qiu "(用筷子戳了一下)好像有点老。"
            qiu "肉有点发柴，不像奶奶做的那么嫩。"

            grandma "(笑)蒸过头了。记住，蒸鱼不能超过十分钟。"
            grandma "过了这道线，鱼肉就柴了。"
            grandma "还有，蒸东西最忌讳老掀锅盖，一掀一盖，气就跑了。"

            qiu "我下次注意。"
            qiu "原来蒸鱼这么多讲究。"

            grandma "没事。做人不能太紧张，做鱼也不能。"
            grandma "紧张了手就抖，手抖了刀就不稳。慢慢来，急不得。"

    # 浇热油
    play sound "audio/sfx/sizzle_oil.mp3"

    narrator "奶奶把热油浇在鱼身上。刺啦一声——葱姜的香味弥漫了整个厨房。"
    narrator "油在鱼皮上滋滋作响，葱姜丝被烫得卷起了边。"
    narrator "那一瞬间，整间屋子都被这股香味暖了起来。"
    narrator "奶奶的手很稳，油浇得均匀，一圈一圈，像在画一幅画。"

    # 上桌
    scene bg_diningtable with dissolve
    show item_steamed_fish at truecenter with dissolve
    show item_rice at rice_left with dissolve
    show item_rice at rice_right as item_rice_right with dissolve
    show grandma reminisce at left

    qiu "奶奶，您说这是爸爸最爱吃的？"
    qiu "爸爸小时候经常吃您蒸的鱼吗？"

    grandma "是啊。你爸爸小时候身体不好，三天两头发烧。"
    grandma "那时候家里穷，没什么好吃的。有次烧得厉害，什么都吃不下。我急得不行。"
    grandma "他烧了三天，我三天没合眼。"
    grandma "后来退烧了，人却瘦了一圈，看着心疼。"

    # 解锁CG
    $ cg_gallery["cg02"] = True
    show cg02 with dissolve
    pause 3.0

    grandma "后来我托人从水库买了一条鲈鱼。那个年代鱼可不好买，尤其是鲜鱼。"
    grandma "托了三层关系，等了一周才等到。"
    grandma "我蒸好了，他只喝了一口汤，就说好鲜。"
    grandma "我说那你多喝点。他说，妈，以后我病了你就蒸鱼给我吃。"
    grandma "那天他喝完了一整碗汤，吃了半条鱼。"

    hide cg02 with dissolve

    qiu "然后就病好了？"

    grandma "(笑)哪有那么神。不过第二天烧确实退了。"
    grandma "也许是睡够了，也许是鱼汤养人，也许是心里踏实了。"
    grandma "后来他考上大学，走之前我蒸了一条鱼。"
    grandma "他说火车上吃完了还想吃，连饭盒都舍不得洗，说里面有家里的味道。"
    grandma "我那时候就知道，这个孩子，留不住了。"

    show qiu thoughtful at right

    narrator "我想到在北京的爸爸。他很少回来。"
    narrator "一年到头也就过年见一面，平时打个电话也是匆匆几句。"

    qiu "爸爸现在在北京……很少回来。"
    qiu "他总说忙，等忙完了就回来。"

    grandma "(顿了顿)他忙。忙了好，说明有出息。"
    grandma "你爷爷当年就说，儿子要有出息，不能一辈子窝在这个小地方。"
    grandma "可人出去了，心就得自己撑着。做妈的，只能远远看着。"

    qiu "您想他吗？"

    narrator "奶奶没有立刻回答。她给鱼又浇了一勺汁。"
    narrator "勺子在碗边磕了磕，发出轻轻的响声。"
    narrator "阳光透过窗帘照在她脸上，照出了她眼角的纹路。"

    grandma "想。哪个当妈的不想孩子。"
    grandma "不过他好好的就行了。他能吃上蒸鱼吗？北京有鲈鱼吧？"
    grandma "北京的水好，鱼应该也新鲜吧？"

    qiu "有的，奶奶。北京什么都有。"
    qiu "超市里什么鱼都能买到，比咱这儿还全。"

    grandma "什么都有，也不是家里的味道。"
    grandma "他吃的是鱼，缺的是家里的灶。"

    narrator "沉默了一会儿。"
    narrator "饭桌上只剩下筷子碰碗的轻响。"
    narrator "鱼已经凉了一些，但汤还是鲜的。"

    grandma "(话锋一转)小秋，你会想家吗？在学校。"
    grandma "你一个人在外面，奶奶也帮不上忙。"

    qiu "会。有时候晚上睡不着，就想喝您的粥。"
    qiu "想您炒的青菜，想您蒸的鱼，想咱们家厨房的灯光。"

    grandma "(笑)所以你要好好学。以后想喝粥了，自己也能做。"
    grandma "想家了，就给自己做一道家里的菜。"
    grandma "做菜的时候，家就在你身边了。"

    scene black with dissolve
    play sound "audio/sfx/page_turn.mp3"

    return