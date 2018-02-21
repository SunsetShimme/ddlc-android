label ch20_from_ch10:
    scene bg residential_day
    with dissolve_scene_half
    play music t2
    jump ch20_main2

label ch20_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2

label ch20_main2:
    "Это был обычный, ничем не примечательный школьный день."
    "И, как всегда, ужасное утро — время, когда я окружён влюблёнными парочками и компаниями друзей, идущими в школу вместе."
    "В то время как я всегда хожу в школу один."
    "Я постоянно твержу себе, что пора бы уже, что ли, начинать знакомиться с девушками..."
    "Но у меня нет желания вступать в клубы."
    "Меня абсолютно устраивает то, что я трачу своё свободное время в основном на игры и аниме."
    "Всегда остаётся клуб аниме, но не думаю, что там есть девушки..."

    scene bg class_day
    with wipeleft_scene

    "Сегодня в школе всё шло своим чередом, и не успел я оглянуться, как день уже закончился."
    "Я сложил свои вещи в сумку и тупо уставился в стену, пытаясь собраться с духом."
    mc "Клубы..."
    "Мне действительно не нравится ни один."
    "Кроме того, в большинстве из них, скорее всего, слишком много всяких обязанностей, чтобы мне хотелось с ними связываться."
    "Думаю, у меня нет выбора, кроме как начать с клуба аниме..."

    $ m_name = "???"

    m "...[player]?"
    window hide(None)
    show monika g2 zorder 2 at t11
    pause 0.75
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    window show(None)
    show monika 1 zorder 2 at t11
    mc "...Моника?"
    $ m_name = "Моника"
    m 1b "Боже мой, я совсем не ожидала увидеть тебя здесь!"
    m 5 "Давно не виделись, да?"
    mc "Эх..."
    mc "Да, давненько."
    "Моника мило улыбнулась."
    "Мы знаем друг друга — ну, общались-то мы редко, но в прошлом году учились в одном классе."
    "Моника была самой популярной девушкой: умная, красивая, спортивная."
    "Совершенно не мой уровень."
    "Так что видеть её искреннюю улыбку, обращённую ко мне, как-то даже..."
    mc "А что ты тут, кстати, делаешь?"
    m 1a "Ой, просто ищу кое-какие материалы для своего клуба."
    m 1d "Не знаешь, здесь есть картон?"
    m "Или маркеры?"
    mc "Попробуй заглянуть в кладовку."
    mc "...Ты же в клубе дебатов, так?"
    m 5 "Ха-ха-ха, вообще-то..."
    m "Я ушла из этого клуба."
    mc "Серьёзно? Ушла?"
    m "Да..."
    m 2e "Честно говоря, я терпеть не могу всю эту политику, без которой в больших клубах никак."
    m "Там только и делаешь, что занимаешься выбиванием бюджета, рекламой и подготовкой к мероприятиям..."
    m "Я предпочла заняться тем, что нравится мне лично, и превратить это в нечто особенное."
    mc "И в какой же клуб ты решила вступить?"
    m 1b "А я создала собственный!"
    m "Литературный клуб!{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    window show(None)
    m "Литературный клуб!{fast}"
    window auto
    mc "Литературный?.."
    "Это звучит... тупо?"
    mc "И сколько участников у вас набралось за это время?"
    m 5 "Эм..."
    m "А-ха-ха..."
    m "Стыдно сказать, но нас пока только трое."
    m "Очень сложно найти новых участников для того, что кажется скучным..."
    mc "Ну, могу понять..."
    m 3d "Но знаешь, вообще-то это совсем не скучно!"
    m "Литература может быть чем угодно. Чтение, писательство, поэзия..."
    m 3e "Один из участников даже держит в клубе свою коллекцию манги..."
    mc "Подожди... Правда?"
    m 2k "Да, забавно, скажи?"
    m 2e "Она постоянно твердит о том, что манга — это литература."
    m "Ну, в чём-то она, конечно, права..."
    m "И всё-таки, член клуба это член клуба, да?"
    "...Моника сказала \"она\"?"
    "Хм-м..."
    m 1a "Эй, [player]..."
    m "Ты случайно... не выбрал ещё клуб для вступления?"
    mc "Эм..."
    mc "Ну, вроде как да, но..."
    m "В таком случае..."
    m 5 "Я могу надеяться, что ты окажешь мне большую услугу?"
    m "Я не прошу тебя вступать, но..."
    m "Если бы ты мог хотя бы забежать ко мне в клуб, я была бы безумно рада."
    m "Пожалуйста!"
    mc "Эм..."
    "Ну, думаю, у меня нет причин отказываться..."
    "Кроме того, разве я могу отказать такой девушке, как Моника?"
    mc "Конечно. Думаю, загляну на минутку."
    m 1k "А-а-а, круто!"
    m 1b "Ты в курсе, что ты замечательный, [player]?"
    mc "Д-да брось, это ерунда..."
    m 1a "Тогда идём?"
    m "Материалы поищу в другой раз — ты сейчас важнее."

    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene

    "Итак, сегодняшний день войдёт в историю как день, в который я продал душу Монике и её неотразимой улыбке."
    "Я робко шёл за Моникой — сначала по коридорам, а потом вверх по лестнице, в то крыло, которое я посещал редко, поскольку в нём располагались только секции и учебные классы выпускников."
    "Моника энергично распахнула двери класса."

    scene bg club_day2
    with wipeleft
    play music t3

    if renpy.random.randint(0, 2) == 0:
        show monika g1 at l31
    else:
        show monika 3b at l31
    m "Я ве-ернула-ась!"
    m "И привела с собой гостя!"
    show yuri 2t zorder 2 at t33
    if not config.skipping:
        show screen invert(0.15, 0.3)
    y "Что?"
    y "Г... Гость?"
    show natsuki 4c zorder 2 at t32
    n "Серьёзно? Ты привела парня?"
    n "Хана атмосфере."
    show monika 3m zorder 3 at f31
    m "Не груби, Нацуки..."
    m 3b "...В общем, добро пожаловать в клуб, [player]!"
    show monika 3a zorder 2 at t31
    mc "..."
    "Все слова вылетели из головы."
    "В этом клубе..."
    "{i}...полно очаровательных девушек!{/i}"

    show natsuki zorder 3 at f32
    n 5c "Так, дай угадаю..."
    n "Ты парень Моники, да?"
    show natsuki zorder 2 at t32
    mc "Чт..."
    mc "Нет!"
    show yuri zorder 3 at f33
    y 2l "Нацуки..."
    $ n_name = 'Нацуки'
    "Неприветливая девушка, которую, судя по всему, звали Нацуки, была единственной, кого я здесь не знал."
    "Её низкий рост наталкивал на мысли, что она, скорее всего, первогодка."

    show yuri zorder 2 at t33
    show monika zorder 3 at f31
    m 2l "В... В общем, это Нацуки — всегда полна энергии..."
    m 2b "А это Юри, вице-президент!"
    $ y_name = 'Юри'
    show monika 2a zorder 2 at t31
    show yuri zorder 3 at f33
    y 4 "П-приятно познакомиться..."
    "Юри, которая выглядела более взрослой и застенчивой, кажется, с трудом уживалась с таким человеком, как Нацуки."
    show yuri zorder 2 at t33
    mc "Ага... Приятно с вами обеими познакомиться."
    show monika zorder 3 at f31
    m 1a "Так вот, [player] случайно встретился мне в классе и ему захотелось посмотреть на наш клуб."
    m "Правда, классно?"
    show monika zorder 2 at t31
    show natsuki zorder 3 at f32
    n 4e "Стоять, Моника!"
    n "Разве я не просила тебя предупреждать меня заранее, прежде чем приводить новичков?"
    n 4q "Я хотела... Ну, ты знаешь..."
    show natsuki zorder 2 at t32
    show monika zorder 3 at f31
    m 1e "Прости, прости!"
    m "Я это помню, но мы столкнулись совершенно непредсказуемо."
    show monika zorder 2 at t31
    show yuri zorder 3 at f33
    y 1a "В таком случае мне следует хотя бы чаю сделать, да?"
    show yuri zorder 2 at t33
    show monika zorder 3 at f31
    m 1b "Да, было бы здорово!"
    m "Почему бы тебе не присесть, [player]?"
    hide monika
    hide natsuki
    hide yuri
    with wipeleft
    "Несколько парт были сдвинуты вместе, создавая импровизированный стол."
    "Юри прошла в угол помещения и открыла кладовку."
    "А Моника и Нацуки в это время сели за стол напротив друг друга."
    "До сих пор ощущая неловкость, я сел рядом с Моникой."
    show monika 1a zorder 2 at t11
    m "Что же, я знаю, что ты на самом деле не планировал приходить сюда..."
    m "Но мы позаботимся о том, чтобы ты чувствовал себя как дома, хорошо?"
    m 1j "Мой президентский долг — сделать клуб весёлым и интересным для всех!"
    mc "Я удивлён, что у вас до сих пор так мало людей."
    mc "Должно быть, трудно создать новый клуб."
    m 3b "Можно и так выразиться."
    m "Немногие заинтересованы в том, чтобы прикладывать большие усилия для создания чего-то нового..."
    m "Тем более когда это что-то настолько непримечательное, как литература."
    m "Сложно убедить людей в том, что это весело и полезно."
    m "Но таким образом школьные мероприятия вроде фестиваля приобретают огромную важность."
    m 2k "Я уверена, что вместе нам удастся взрастить этот клуб до выпуска!"
    m "Правда, Нацуки?"
    show monika zorder 2 at t22
    show natsuki 4q zorder 2 at t21
    n "Ну..."
    n "...Наверное."
    "Нацуки неохотно согласилась."
    "Такие разные девушки, объединённые общей целью..."
    "Моника, похоже, сильно постаралась, чтобы найти этих двоих."
    "Юри вернулась к столу с чаем."
    "Она аккуратно поставила по чайной чашке перед каждым из нас, прежде чем разместить чайничек в центре стола."
    show natsuki zorder 1 at thide
    show monika zorder 1 at thide
    hide natsuki
    hide monika
    show yuri 1a zorder 2 at t21
    mc "Вы держите в классе целый чайный сервиз?"
    y "Не волнуйся, у нас есть разрешение от учителей."
    y "В конце концов, разве чашка горячего чая не помогает насладиться хорошей книгой?"
    mc "А... П-пожалуй..."
    show monika 4a zorder 3 at f22
    m "Хи-хи, не пугайся, Юри просто пытается произвести на тебя впечатление."
    show monika zorder 2 at t22
    show yuri at hf21
    y 3n "Э-э?! Это не..."
    "Юри обиженно отвернулась."
    y 4b "Я имела в виду, ну... это..."
    show yuri zorder 2 at t21
    mc "Верю."
    mc "Ну, чтение под чашку чая, быть может, и не для меня, но, по крайней мере, сам чай я люблю."
    show yuri zorder 3 at f21
    y 2u "Я рада..."
    show yuri zorder 2 at t21
    "Юри расслабилась и незаметно улыбнулась."
    show monika zorder 1 at thide
    hide monika
    show yuri 1a zorder 2 at t32
    y "Итак, [player], какую литературу ты предпочитаешь?"
    mc "Ну... Эм..."
    "Учитывая то, как мало я читал в последние годы, у меня не нашлось приемлемого ответа на этот вопрос."
    mc "Мангу..."
    "Тихо и неуверенно промямлил я."
    show natsuki 1c zorder 2 at t41
    "Нацуки внезапно вскинула голову."
    "Кажется, она хотела что-то сказать, но смолчала."
    show natsuki zorder 1 at thide
    hide natsuki
    y 3u "Н-не слишком большой любитель читать, получается..."
    mc "Ну, это может измениться..."
    "Что я несу?"
    "Это вырвалось само собой, стоило мне увидеть грустную улыбку Юри."
    mc "Вот так вот. А ты, Юри?"
    y 1l "Ну, дай-ка подумать..."
    "Юри провела пальцем по краю своей чашки."
    y 1a "Мне больше всего нравятся романы с хорошо прописанными и сложно устроенными фантастическими мирами."
    y "Я восхищаюсь уровнем креативности и авторского мастерства."
    y 1f "Равно как и способностью выстроить интересный сюжет в таком чуждом мире."
    "Юри продолжала. Было понятно, что книги — её страсть."
    "Она казалась такой сдержанной и робкой до этого момента, но теперь, по тому, как загорелись её глаза, стало очевидно, что ей уютно именно в мире книг, а не людей."
    y 2m "Ну а вообще, мне многое нравится."
    y "Допустим, меня также увлекают рассказы с глубокой психологической подоплёкой."
    y 2a "Разве не поразительно, что автор может сознательно использовать недостаток воображения читателя, чтобы зациклить его мысли?"
    y "Кстати, в последнее время я читала много ужасов..."
    mc "О, я когда-то тоже читал одну книгу ужасов..."
    "В отчаянии хватаюсь за минимальное соответствие теме из собственного опыта."
    "Учитывая мои познания, Юри с тем же успехом могла бы пообщаться с камнем."
    show monika 1j zorder 3 at f33
    m "А-ха-ха. Я подозревала что-то подобное, Юри."
    m 1a "Это соответствует твоему характеру."
    show monika zorder 2 at t33
    show yuri zorder 3 at f32
    y 1a "Оу, правда?"
    y "Если история заставляет меня задуматься или переносит в другой мир, то я действительно не могу бросить её на полпути."
    y "Сюрреалистические ужасы часто изменяют восприятие мира, хоть и на короткое время."
    show yuri zorder 2 at t32
    show natsuki 5q zorder 3 at f31
    n "Фу, ненавижу ужасы..."
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f32
    y 1f "О, и почему же?"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f31
    n 5c "Ну, я просто..."
    "Нацуки бросила на меня короткий взгляд."
    n 5q "Неважно."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 1a "Точно, ты же обычно любишь писать о милых вещах, не так ли, Нацуки?"
    show monika zorder 2 at t33
    show natsuki 1o zorder 3 at f31
    n "Ч-чего?"
    n "С чего ты взяла?"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 3b "На прошлом собрании клуба ты забыла свой черновичок."
    m "Кажется, ты работала над стихом под названием..."
    show monika zorder 2 at t33
    show natsuki 1p zorder 3 at f31
    n "Не говори вслух!"
    n "И верни обратно!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 1j "Хорошо, хорошо-о-о..."
    show monika 1a zorder 2 at t33
    mc "Нацуки, ты пишешь стихи?"
    show natsuki zorder 3 at f31
    n 1c "М? Ну, иногда."
    n "Почему спрашиваешь?"
    show natsuki zorder 2 at t31
    mc "По-моему, это впечатляет."
    mc "Не покажешь как-нибудь?"
    show natsuki zorder 3 at f31
    n 5q "Н-Нет!"
    "Нацуки отвела взгляд."
    n "Тебе не... понравятся они..."
    show natsuki zorder 2 at t31
    mc "А-а... Не очень уверенный писатель?"
    show yuri zorder 3 at f32
    y 2f "Я понимаю, что чувствует Нацуки."
    y "Для того, чтобы делиться подобными вещами, требуется не только уверенность."
    y 2k "Истинная форма письма — письмо самому себе."
    y "Ты должен быть готов раскрыться своим читателям, обнажить перед ними свои уязвимости и выставить на обозрение самые потайные уголки своего сердца."
    show yuri zorder 2 at t32
    show monika 2a zorder 3 at f33
    m "У тебя тоже имеется писательский опыт, Юри?"
    m "Может, если ты поделишься своей работой, подавая пример, то это поможет Нацуки более спокойно отнестись к тому, чтобы прочли её собственную."
    show yuri at s32
    y 3o "..."
    mc "Подозреваю, что у Юри та же проблема..."
    "Какое-то время мы просидели в тишине."
    show monika zorder 3 at f33
    m 5a "Слушайте, у меня есть идея!"
    m "Как насчёт такого?"
    show monika zorder 2 at t33
    show natsuki 2k zorder 3 at f31
    show yuri 3e zorder 3 at f32
    ny "?.."
    "Нацуки и Юри недоумённо посмотрели на Монику."
    show natsuki zorder 2 at t31
    show yuri zorder 2 at t32
    show monika zorder 3 at f33
    m 2b "Расходимся по домам и пишем стихотворения!"
    m "И когда в следующий раз встретимся, то покажем их друг другу."
    m "Так будет честно!"
    show monika 2a zorder 2 at t33
    show natsuki zorder 3 at f31
    n 5q "Э-Эм..."
    show natsuki zorder 2 at t31
    show yuri 3v zorder 3 at f32
    y "..."
    show yuri zorder 2 at t32
    show monika 2m zorder 3 at f33
    m "Эх..."
    m "А я думала, что это хорошая идея..."
    show monika zorder 2 at t33
    show yuri zorder 3 at f32
    y 2l "Ну..."
    y "...Я думаю, ты права, Моника."
    y 2f "Мы, наверное, должны заняться поиском занятий для каждого, чтобы мы все что-то делали вместе."
    y 2h "В конце концов, я же решила взять на себя ответственность вице-президента..."
    y "Я должна сделать всё возможное, чтобы улучшить клуб, а также его участников."
    y 2a "Кроме того, теперь, когда у нас появился новичок..."
    y "Мне кажется, это хороший шаг вперёд."
    y "Ты согласен, [player]?"
    show yuri zorder 2 at t32
    mc "Погодите... Есть одна проблема."
    show monika zorder 3 at f33
    m 1d "Э-э? Что не так?"
    "Теперь, когда мы вернулись к изначальной теме, насчёт моего вступления в клуб, я прямо сказал о том, о чём думал всё это время."
    show monika zorder 2 at t33
    mc "Я не говорил, что вступлю в ваш клуб!"
    mc "Моника, может, и уговорила меня заглянуть, но я не принимал окончательного решения."
    mc "Мне нужно ещё посмотреть на другие клубы и... эм..."
    show monika 1g
    show natsuki 4g
    show yuri 2e
    "Я потерял ход мыслей."
    "Все три девушки смотрели на меня потухшими взглядами."
    show monika at s33
    m 1p "Н-Но..."
    show yuri at s32
    y 2v "Прости, я думала..."
    show natsuki at s31
    n 5s "Пф."
    mc "Что?.."
    "Девушки переглянулись, а затем Моника повернулась ко мне."
    show monika zorder 3 at f33
    m 1m "Думаю... я должна сказать тебе правду, [player]."
    m "Дело в том, что..."
    m 1p "...У нас недостаточно участников, чтобы стать официальным клубом."
    m "Нам нужен четвёртый."
    m "И я очень, очень долго пыталась искать новичков."
    m "И если мы не найдём ещё одного участника до фестиваля..."
    show monika zorder 2 at t33
    mc "..."
    "Я... Я беззащитен против них."
    "Как я должен принимать взвешенное решение при вот этом всём?"
    "Меня совесть замучает, если я подведу их..."
    "И кроме того, сам клуб кажется довольно спокойным..."
    "Что ж, если писать стихи — это цена, которую мне нужно заплатить, чтобы проводить каждый день с этими красивыми девушками..."
    mc "...Хорошо."
    mc "Ладно, я принял решение."
    mc "Я вступаю в литературный клуб."
    show monika 1e zorder 2 at t33
    show yuri 3f zorder 2 at t32
    show natsuki 1k zorder 2 at t31
    "Глаза девушек позагорались обратно."
    show monika zorder 3 at f33
    m "О боже мой, серьёзно?"
    m "Ты правда сделаешь это, [player]?"
    show monika zorder 2 at t33
    mc "Ага..."
    mc "Это ведь будет весело?"
    show yuri zorder 3 at f32
    y 1m "Ты сумел меня испугать на какое-то мгновение..."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f31
    n 5q "Если бы ты развернулся и ушёл после всего этого, я бы дико взбесилась."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m "[player], я так рада..."
    m 1k "Теперь мы можем стать официальным клубом!"
    m 1e "Большое спасибо тебе за это. Ты невероятный."
    m "Я сделаю всё, что в моих силах, чтобы тебе здесь понравилось, окей?"
    show monika zorder 2 at t33
    mc "Эм... Спасибо, наверное."
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    show monika zorder 2 at t11
    hide yuri
    hide natsuki
    m 3b "Так, ребята!"
    m "Думаю, на этой прекрасной ноте можно завершить нашу сегодняшнюю встречу."
    m "Помните о задании на вечер:"
    m "Напишите к следующей встрече стихотворения, чтобы мы могли обменяться ими!"
    "Моника снова взглянула на меня."
    m 1a "[player], я буду с нетерпением ждать, как ты покажешь себя."
    show monika 5 at hop
    m "Хи-хи-хи-и!"
    mc "А-ага..."
    show monika zorder 1 at thide
    hide monika
    "Смогу ли я впечатлить звезду класса своими посредственными писательскими навыками?"
    "Я уже чувствовал, как внутри нарастает волнение."
    "Тем временем девушки продолжили болтать, дожидаясь, пока Юри помоет посуду."
    mc "Тогда я пошёл..."
    show monika 5a zorder 2 at t11
    m "Хорошо!"
    m "Тогда увидимся завтра."
    m "Не могу дождаться!"

    scene bg residential_day
    with wipeleft_scene

    "Я покинул класс и направился домой."
    "Всю дорогу мои мысли то и дело обращались к одной из этих трёх девушек:"
    show natsuki 4a zorder 2 at t31
    "Нацуки,"
    show yuri 1a zorder 2 at t32
    "Юри,"
    show monika 1a zorder 2 at t33
    "и, конечно, Монике."
    "Буду ли я действительно счастлив, каждый день проводя время после занятий в литературном клубе?"
    "Возможно, у меня появится шанс сблизиться с одной из этих девушек..."
    hide natsuki
    hide yuri
    hide monika
    with wipeleft
    "Ладно!"
    "Нужно просто выжать из обстоятельств по максимуму. Уверен, удача меня найдёт."
    "И начнётся всё, наверное, с моего вечернего стихотворения..."

    stop music fadeout 2.0
    scene black with dissolve_scene_full
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False

    call screen confirm("Вы открыли особый стих.\nХотите прочесть его?", Return(True), Return(False))
    if _return:
        call expression "poem_special_" + str(persistent.special_poems[0]) from _call_expression_17
    else:
        pass

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc