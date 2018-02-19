label poemresponse_start:
    $ poemsread = 0
    $ skip_transition = False
    label poemresponse_loop:
        $ skip_poem = False
        if renpy.music.get_playing() and not (renpy.music.get_playing() == audio.t5 or renpy.music.get_playing() == audio.t5c):
            $ renpy.music.play(audio.t5, fadeout=1.0, if_changed=True)
        if skip_transition:
            scene bg club_day
        else:
            scene bg club_day
            with wipeleft_scene
        $ skip_transition = False
        if not renpy.music.get_playing():
            play music t5
    label poemresponse_start2:
        if persistent.playthrough == 2:
            $ pt = "2"
        else:
            $ pt = ""
        if poemsread == 0:
            $ menutext = "Whomst should I show my poem to first?"
        else:
            $ menutext = "Whomst should I show my poem to next?"

        menu:
            "[menutext]"

            "Sayori" if not s_readpoem and persistent.playthrough == 0:
                $ s_readpoem = True
                if chapter == 1 and poemsread == 0:
                    "I'm definitely most comfortable sharing it with Sayori first."
                    "She's my good friend, after all. And completely oblivious to my thirst of vaginal juices."
                    "She often finds her self unknowingly quenching my thirst..."
                    "I'm getting off track."
                call poemresponse_sayori
            "Natsuki" if not n_readpoem:
                $ n_readpoem = True
                if chapter == 1 and poemsread == 0:
                    "I told Natsuki I was interested in her poems yesterday."
                    "It's probably only fair if I shared mine with her first."
                    "She probably wants my cock even more know after seeing that we had something in common."
                call poemresponse_natsuki
            "Yuri" if not y_readpoem and not y_ranaway:
                $ y_readpoem = True
                if chapter == 1 and poemsread == 0:
                    "Tits"
                call poemresponse_yuri
            "Monika" if not m_readpoem:
                $ m_readpoem = True
                if chapter == 1 and poemsread == 0:
                   "FUCK greek yogurt"
                   $ m_readpoem == True
                   menu:
                       "[menutext]"

                       "Sayori" if not s_readpoem and persistent.playthrough == 0:
                          $ s_readpoem = True
                          if chapter == 1 and poemsread == 0:
                              "I'm definitely most comfortable sharing it with Sayori first."
                              "She's my good friend, after all. And completely oblivious to my thirst of vaginal juices."
                              "She often finds her self unknowingly quenching my thirst..."
                              "I'm getting off track."
                              call poemresponse_sayori
                       "Natsuki" if not n_readpoem:
                          $ n_readpoem = True
                          if chapter == 1 and poemsread == 0:
                              "I told Natsuki I was interested in her poems yesterday."
                              "It's probably only fair if I shared mine with her first."
                              "She probably wants my cock even more know after seeing that we had something in common."
                              call poemresponse_natsuki
                       "Yuri" if not y_readpoem and not y_ranaway:
                          $ y_readpoem = True
                          if chapter == 1 and poemsread == 0:
                              "Tits"
                              call poemresponse_yuri
        $ poemsread += 1
        if poemsread < 3 or (persistent.playthrough == 0 and poemsread < 4):
            jump poemresponse_loop

    # Reset variables for next time
    $ s_readpoem = False
    $ n_readpoem = False
    $ y_readpoem = False
    $ m_readpoem = False
    $ poemsread = 0
    return

label poemresponse_sayori:
    scene bg club_day
    show sayori 1a at t11 zorder 2
    with wipeleft_scene
    $ poemopinion = "med"
    if s_poemappeal[chapter - 1] < 0:
        $ poemopinion = "bad"
    elif s_poemappeal[chapter - 1] > 0:
        $ poemopinion = "good"
    $ nextscene = "ch" + pt + str(chapter) + "_s_" + poemopinion
    call expression nextscene
    if not skip_poem:
        $ nextscene = "ch" + pt + str(chapter) + "_s_end"
        call expression nextscene
    return

label poemresponse_natsuki:
    scene bg club_day
    show natsuki 1c at t11 zorder 2
    with wipeleft_scene
    $ poemopinion = "med"
    if n_poemappeal[chapter - 1] < 0:
        $ poemopinion = "bad"
    elif n_poemappeal[chapter - 1] > 0:
        $ poemopinion = "good"
    $ nextscene = "ch" + pt + str(chapter) + "_n_" + poemopinion
    call expression nextscene
    if not skip_poem:
        $ nextscene = "ch" + pt + str(chapter) + "_n_end"
        call expression nextscene
    return

label poemresponse_yuri:
    scene bg club_day
    show yuri 1a at t11 zorder 2
    with wipeleft_scene
    $ poemopinion = "med"
    if y_poemappeal[chapter - 1] < 0:
        $ poemopinion = "bad"
    elif y_poemappeal[chapter - 1] > 0:
        $ poemopinion = "good"
    $ nextscene = "ch" + pt + str(chapter) + "_y_" + poemopinion
    call expression nextscene
    if not skip_poem:
        $ nextscene = "ch" + pt + str(chapter) + "_y_end"
        call expression nextscene
    return

label poemresponse_monika:
    scene bg club_day
    show monika 1a at t11 zorder 2
    with wipeleft_scene
    if m_poemappeal[chapter - 1] < 0:
        $ poemopinion = "bad"
    elif m_poemappeal[chapter - 1] > 0:
        $ poemopinion = "good"
    $ nextscene = "ch" + pt + str(chapter) + "_m_start"
    call expression nextscene
    if not skip_poem:
        $ nextscene = "ch" + pt + str(chapter) + "_m_end"
        call expression nextscene
    return

label ch1_y_end:
    call showpoem(poem_y1, img="yuri 3t")
    y 3t "..."
    y "I know you're not even reading..."
    mc "What??"
    y 2v "You're just staring blankly at the page."
    mc "Ah--"
    mc "Fuck you, Fine, It's Good."
    mc "Eat my ass, semen incubator."
    if poemopinion == "good":
        y 2f "Eh?"
        y 3v "I-It's nothing, really!"
        y "Yours was impressive too, so..."
        mc "Nah..."
        mc "If it was good, that would mean i'm a full on homogay."
        y 4a "...You think so?"
        mc "Nah, fucking duh. Only faggots and crybabies are good at poetry. "
        mc "That's why I {i}choose{/i} to be bad at it!"
        y "Ah..."
        y 2s "You know..."
        y "I was really nervous about doing all this."
        y "But in the end, I enjoyed it."
        y "I'm going to keep doing my best for you, [player]."
        mc "Ah..."
        mc "Me too."
        "Damn, I feel something weird in my chest when I look at her."
        "It's something other then lust..."
        "Something warm..."
        "..."
        "Is this love?"
        "Nah, a nigga just got heart burn lol."
    else:
        y 1u "It's nothing, really..."
        y "Well...it makes me happy that you think that."
        y 1a "Just remember that it won't be long before you pick up on these things, too."
        mc "I really fucking hope not."
        mc "Only faggots and crybabies are good at poetry."
        "Damn, I feel something weird in my chest when I look at her."
        "It's something other then lust..."
        "Something warm"
        "..."
        "Is this love?"
        "Nah, a nigga just got heart burn."
    return

label ch2_y_end:
    call showpoem(poem_y2)
    y 2m "Um..."
    y "I was a little more daring with this one than yesterday's..."
    mc "I can see that."
    mc "It's fucking shit."
    "This poem was fucking awful."
    y 1a "That's right."
    y "It's a bit closer to my preferred writing style..."
    mc "Is your prefered writing style that of an old man with Alzheimers, who hasn't been laid since 1984 due to his raging erectile dysfunction?"
    mc "And everyday he relives the torment of discovering that his manhood no longer functions properly?"
    y "Using the poem as a canvas to express vivid imagery, and conveying emotions through them."
    mc "Oh lmao I was close."
    y 2f "Well..."
    y "I think it's something that different people can relate to in their own way."
    y "I wanted to express the way it feels for me to indulge in my more unusual hobbies..."
    y 2v "It's those sorts of things I'm usually forced to keep to myself."
    y "So, I sometimes enjoy writing about them."
    mc "Word of advice, never tell people your unusual hobbies."
    mc "Yeesh, just thinking about that gives me flashbacks."
    mc "one time I told my mom about my hobby of fapping to Loli Hentai and, well,"
    mc "Long story short, I live alone with no adult supervision whatsoever."
    if n_readpoem and (n_poemappeal[0] >= 0 or n_poemappeal[1] >= 0):
        mc "Huh, that's funny..."
        y 2e "...?"
        mc "Didn't Natsuki also write something about that?"
        mc "About someone being ridiculed for a strange interest?"
        "Pretty sure Natsuki's said her strange interest was throbbing horsecock on futa girls, but maybe that's just me."
        y 2h "Eh?"
        y "She...she did?"
        mc "Yes. Don't make me fucking repeat myself."
        mc "She was talking about how it doesn't matter what you're into as long as you're not hurting anybody."
        mc "Although, to be fair, taking a horse dick up the ass does seem like it's gonna hurt somebody."
        y 3r "She--She's right!"
        y 3o "Ah--I mean..."
        y "Does she really feel that way...?"
        mc "Bitch I swear if i have to repeat myself one more time..."
        mc "Sounds like you two have that in common..."
        y 3h "That's...well, that's interesting..."
        y "To me, she seemed like the kind of person who would make fun of my hobbies..."
        y "But I suppose that's my fault for judging, isn't it...?"
        y 3p "Ah-- Please don't tell her I said that!"
        mc "Ahaha. Don't worry, I have no reason to. As long as you fulfill my..."
        mc "Needs."
        mc "wink wink."
        y 1l "Okay..."
        mc "Oh shit really?"
        y 1a "Well, thank you for sharing it with me."
        mc "Damn I forgot you have the attention span of a parrot with ADHD."
    else:
        mc "It's good that you keep your interests to yourself."
        y "Okay."
    if y_appeal >= 2:
        y 2s "You're good at a lot of things..."
        y "Writing, listening..."
        y 2u "There really aren't many people like you, [player]..."
        mc "Damn fucking straight you whore. I am above GOD!"
        y "I never thought I would feel so comfortable sharing my writing..."
        y 2s "But now, I almost feel like I look forward to it..."
        y 2m "It's just...a really nice feeling."
        y "And you're to thank for that."
        mc "YOU'RE FUCKING WELCOME YOU TIT MILK FACTORY."
        "Yuri smiles sincerely at me."
        "For just a moment, her timidness seems to disappear."
        "Damn, I feel something weird in my chest when I look at her."
        "It's something other then lust..."
        "Something warm..."
        "..."
        "Is this love?"
        "Nah, a nigga just got heart burn."
    return
label ch3_y_end:
    if y_appeal >= 3:
        jump ch3_y_end_special
    call showpoem(poem_y3, img="yuri 2v")
    y "Um..."
    y "I'm aware that the beach is kind of an inane thing to write about."
    y "But I did my best to take a metaphorical approach to it."
    if not n_readpoem or n_appeal >= 3:
        mc "Poetry is fucking shit but this, this is flies on shit. It's lower than shit."
        mc "Do you understand?"
        y 2e "Oh, you haven't heard...?"
        y 2h "After yesterday, Natsuki and I...well..."
        y "It was...amusing that we wrote about something similar in such different ways."
        y "So, Natsuki wanted us to write about the same topic as each other again."
        if n_readpoem:
            mc "What the fuck does that have to do with what I just said?"
            "Yuri is so fucking stupid it hurts."
            "Something tells me the poem Natsuki showed me isn't the one she plans on sharing with everyone else..."
            "Of course, I choose not to mention that to Yuri."
    else:
        mc "Yeah, Natsuki already told me about it."
        y 3t "S-She did...?"
        y "She didn't say anything weird, did she?"
        y "She just wanted us to write about the same topic again..."
    y 2f "I suppose to better compare the differences in our writing styles...or thought processes."
    y 2w "Anyway, it was her idea...!"
    y "Knowing her, it's no surprise that she'd want to do something like that."
    y "She probably just wants to show off."
    y 2v "It's not like I have a particular interest in her writing style..."
    y "I just went with her request."
    y "But..."
    y 1s "Well, I suppose it's not so bad to write about something simple on occasion."
    y 1m "It can be refreshing, you know?"
    y "It's good for me to calm my thoughts once in a while."
    mc "Yeah...I think I agree."
    mc "..."
    mc "Thanks for sharing."
    mc "but shut the fuck up please."
    return
label ch3_y_end_special:
    call showpoem(poem_y3b, img="yuri 4b")
    "Finishing the poem, I start to hand it back to Yuri."
    "But instead of taking it from me, she looks away."
    mc "Take it you bitch."
    y "..."
    y "Do you...dislike it?"
    mc "I have a mutual disliking for all Faggot Shit."
    mc "Just take your fucking poem back."
    "Despite Yuri's poems usually being cryptic, it wasn't hard to figure out what this one was about."
    "She wants my dick."
    if n_readpoem:
        "Also, this clearly isn't the poem that Natsuki said she wrote about..."
        "...Meaning I'm probably the only one she's showing this to."
        "SHE TOTALLY WANTS MY FUCKING DICK IN HER BABY CAAAAAAAAAAAAAAAAAAAAAAAAAAAVE!"
    y 2v "I-I don't know if I'll be able to explain this one..."
    mc "That's fine."
    mc "I understand this one."
    y 4c "..."
    "Yuri is having an even harder time speaking than usual."
    mc "Does this one...mean a lot to you?"
    "Yuri nods."
    mc "I'm not really good with words, but..."
    mc "I'm happy that you shared it with me."
    mc "So, thank you."
    mc "And I hope we keep spending time together."
    show yuri 4e
    "Despite my inability to make eye contact, I see a faint smile emerge on Yuri's lips."
    "I once again try to hand the poem back to her."
    show yuri 4a
    "But instead, Yuri gently takes my hands and pushes them back toward me."
    "I hesitate in response to her warm touch."
    "My dick is throbbing so hard."
    y 1v "You can..."
    y "Um..."
    y "The poem is..."
    "Once again, Yuri fails to form a complete sentence."
    mc "You mean I can keep it?"
    "Yuri nods."
    mc "I'd love to."
    mc "But sadly, I aint into F A G G O T S H I T."
    "I bitch slap the fuck out of the emo slut and force the poem back into her hands."
    show yuri 1u
    "Again, Yuri faintly smiles, as if she doesn't want me to notice."
    y "You always..."
    y "You always...make me feel nice."
    y "I know I'm not good with people, but..."
    y "I hope that...I can return the favor sometimes."
    mc "Just shut up."
    mc "I think you do a good job."
    "Yuri finally turns back toward me."
    y 1s "I guess...we should move on before Monika says something."
    y "She's such a yogurt bitch."
    mc "HOLY SHIT I knew I wasn't the only one who thought that!"
    "Yuri giggles, her cheeks red."
    mc "But next time don't steal my words you meme theiving fucking pinterest user."
    "With that, Yuri timidly smiles at me, and I return to my seat so I can put her poem away."
    return

label ch1_n_end:
    call showpoem(poem_n1, img="natsuki 2s")
    n 2q "Yeah..."
    n "I told you that you weren't gonna like it."
    mc "It's actually the only one I can understand so far."
    n 2h "What?"
    n "Just be honest!"
    mc "I am."
    mc "Don't fucking doubt me, jailbait!"
    n "Everyone in high school thinks that writing has to be all sophisticated and stuff..."
    n 5q "So people don't even take my writing seriously."
    mc "Cry me a fucking river. Now I'm about to go under this desk here to \"pick up\" my \"pencil\"."
    mc "Are you wearing panties or...?"
    n "I like when it's easy to read, but it hits you hard."
    "You fucking hit me hard, you IRL loli."
    "Actually wait, that sounds kinda hot echs dee."
    "I need this bitch to fucking slap me now."
    "Oh hey, she's droning on about something, better pay attention."
    n 1c "Like in this poem."
    n "Seeing everyone around you do great things can be really disheartening..."
    n "So I decided to write about it."
    mc "Oh, that's good! Btw, those lace black panties give off the connotation that you're a fucking whore."
    n 2a "But the other nice thing about simple writing is that it puts more weight on the wordplay."
    n "Like I set up for a rhyme at the end, but then made it fall flat on purpose."
    "I'm sure you know a lot about flat, you fucking loli tsun pink haired bitch."
    "You are literally peak anime, I hope you know that."
    "Actually that's probably why you make me so hard lol"
    n "It helps bring out the feeling in the last line."
    mc "So you did..."
    mc "I guess more went into it than I realized."
    "If i moved fast enough, I could totally tear these panties off."
    n 4y "That's what it means to be a pro!"
    n "I'm glad you learned something."
    n "Didn't expect that from the youngest one here, did you?"
    mc "Yeah...guess not. I also wasn't expecting you to never shave down here. Jesus fuck, buy a razor."
    "I decide to humor her with that last comment."
    "I don't really care how old everyone is, but if Natsuki is feeling proud then I won't take that away from her."
    "She just needs to learn proper fucking hygiene."
    return

label ch2_n_end:
    call showpoem(poem_n2)
    n 2a "Not bad, right?"
    mc "It's too fucking long. I stopped caring half way through lmao."
    n 2w "Yesterday's was way too short..."
    n "I was just warming up!"
    n 2c "I hope you didn't think that was the best I could do."
    mc "To be honest you're the only one here who makes sense in these things."
    mc "So I guess that makes you the best one here?"
    n 2a "Anyway, the message is pretty straightforward in this poem."
    n "I doubt I have to explain it."
    "I would really fucking enjoy an explanation."
    "Even though some of this shit made sense, all of these bitches are senile and don't know how to write normal sentences."
    "Ah whatever, no matter what I say this cuntflap'll do it anyway, watch."
    mc "I actually don't fucking care."
    n 2c "Sometimes you can explain complicated issues with much simpler analogies..."
    n "And it helps people realize how stupid they're being."
    n 2g "Like, anyone would agree that the subject of this poem is an ignorant jerk..."
    mc "Oh, like Monika? Eating her fucking greek yogurt in public. It's disgusting."
    n 2c "Of course. It's about how everyone thinks my--"
    n 5w "...That doesn't matter! It can be about anything!"
    n 5h "I wrote it to be easy to relate to..."
    n "Everyone has some kind of weird hobby, or a guilty pleasure."
    n "it's perfectly fine to appreciate the uh,"
    n "the equestrian physique."
    "Holy shit does she like horse dicks?"
    "That's kinda fucking hot..."
    n 5q "Something that you're afraid if people find out, they'd make fun of you or think less of you."
    n 1e "...But that just makes people stupid!"
    n "Who cares what someone likes, as long as they're not hurting anyone, and it makes them happy?"
    n 1q "I think people really need to learn to respect others for liking weird things..."
    if y_readpoem and (y_poemappeal[0] >= 0 or y_poemappeal[1] >= 0):
        mc "Huh, that's funny..."
        mc "Yuri wrote about something similar today."
        mc "But without the horse dicks."
        mc "I'm actually not sure if that makes it better or worse."
        mc "I mean my cock has been compared to elephant dick before so hey bb hit me up~"
        n 1h "Huh?"
        n "Did you say Yuri?"
        mc "Yes. Listen you little shit."
        mc "She said her poem was about an unusual hobby of hers."
        mc "I didn't really get it, but she said something similar to you..."
        mc "That people shouldn't make each other feel insecure about those things."
        n 1q "Really?"
        mc "The fuck did I say about listening?"
        n "Well..."
        n 1t "I mean, Yuri's pretty weird, so I wouldn't doubt that she has some weird hobbies..."
        n "...Not that there's anything wrong with that!"
        "Fucking seinfeld meme line lol"
        n 1u "Uu..."
        n "It's not like...I would judge her or anything..."
        "Natsuki has trouble finding words."
        n 1q "I-I guess I should try not to be so mean to her..."
        n "If she feels insecure about her weird behaviors and stuff..."
        n "I mean, I always hate people who make me feel insecure..."
        n 1w "And Yuri made me feel insecure yesterday!"
        n 1s "But the way you put it, it sounds like she's learned her lesson..."
        mc "I wonder what yuri's fetish is."
        "It's been a while sense i've peeped natsuki's cute tats."
        "Lemme get a quickie..."
    else:
        mc "I don't give a shit."
        mc "People should keep their gross hobbies to themselves."
        mc "Did I ever tell you about the time I told my mom about loli hentai?"
    if n_appeal >= 2:
        n 4h "You know..."
        n "I'm glad that you can appreciate this kind of writing..."
        n 4q "I mean...I know I was talking about that yesterday."
        n "But I've been...well, I've been enjoying sharing my writing with you, so..."
        n 4w "...So consider yourself lucky, okay?"
        mc "Listen here you little shit."
        mc "The only luck i've come across lately is being forced into a club with a bunch of fine-ass cuties."
        mc "But even the charm of being here is fading fast after being here for more than five consecutive minutes."
        mc "Literally the only reason I'm here is because you and Big Titty Goth GF are prime fap material, lmao."
        n 1n "What's that supposed to mean?"
        n "Just look forward to tomorrow too, okay?"
        mc "I prefer to not think about my inevitable doom."
    else:
        n 4c "It's what I do best, after all!"
        n "I don't like writing unless there's a good message to take away from it."
        n "Like, conveying emotions is important..."
        n "But I want to make people think, not just feel."
        "I want you to make me feel, though."
        n 4b "Remember that!"
        n "I'm gonna write a good one for tomorrow, too, so look forward to it."
    return
label ch3_n_end:
    if n_appeal >= 3:
        jump ch3_n_end_special
    call showpoem(poem_n3)
    n 2a "Yeah..."
    n "I felt like I kept writing about negative things, so I wanted to write something with a nice message for once."
    n 2z "Besides...the beach is awesome!"
    n 2j "Kinda hard to write anything negative about the beach."
    if not y_readpoem or y_appeal >= 3:
        mc "What about this fuckin message?"
        n 2c "Yeah, well..."
        n "It's only because of what happened yesterday."
        n 5q "I mean, after Yuri and I realized we kind of wrote about the same thing..."
        n "She wanted to pick a topic and have us both write about it, or whatever."
        if y_readpoem:
            mc "Fucking doubtful."
            "Something tells me the poem Yuri showed me isn't the one she plans on sharing with everyone else..."
            "Of course, I choose not to mention that to Natsuki."
    else:
        mc "Well, Yuri's take on it was a little less faggot like."
        n 5h "Well, that's--"
        n 42c "Jeez...she better not have said anything bad about mine!"
        n "After all, she was the one who wanted us to write about the same topic."
    n 1s "Ugh...you can really see her doing that, too."
    n "Making us write about a simple topic, then trying to impress me by coming up with something all fancy."
    n 1w "Well, it's not like I care."
    n "I just did it anyway."
    n 1q "I mean, I guess mine ended up being kind of metaphorical too..."
    n "...But there's nothing wrong with doing that once in a while!"
    n "At the very least, it was good practice."
    return
label ch3_n_end_special:
    call showpoem(poem_n3b)
    n 1q "..."
    n "...Why are you looking at me like that?"
    n "If you don't like it, then just say it."
    n 1u "I won't...get mad."
    mc "It's fucking shit."
    if y_readpoem:
        "This clearly isn't the poem that Yuri told me she had written..."
        "...Meaning I'm probably the only one she's showing this to."
        "which means she totally wants my fat cock. I admit, it's a little chubbier than most, but i feel like that just adds to the appeal."
    mc "Er...I guess I'm not used to hearing such nice things coming from you..."
    n 1h "D-Don't just say that!"
    n 1n "Dummy..."
    "Okay, it's official, this cockgobbler is the perfect example of a trap jailbait tsundere."
    "And {i}nothing{/i} has ever made my dick harder."
    n "What do you think...the point of writing is?"
    n 1u "Expressing things that you can't just say..."
    mc "No matter the point of writing, it's still fucking shit."
    mc "But I wanna slam you down harder than a morbidly obese child slams 5 McDonalds™ Happy Meals™ down his McThroat™. Toy included."
    mc "So i'll go ahead and say it was pretty good."
    n 1h "Well...yeah..."
    n 1q "I'm...I'm a pro, so..."
    "Natsuki mumbles, completely failing to sound confident like she usually does."
    n "Just..."
    n 12c "Remember that...I can think these things sometimes, too!"
    n "You know, when you're nice to me, it's..."
    n 12a "..."
    n "...Meaningful."
    mc "You should be grateful, daddy's little cum dump."
    "Sensing Natsuki is satisfied, I start to hand the poem back to her."
    "But as I do so, Natsuki takes my hands and pushes them back away."
    "Her small, soft hands surprise me with their assertion."
    n 12b "I don't want it."
    mc "Eh...?"
    mc "Why not?"
    n 12c "I just don't!"
    n "Jeez..."
    "I realize what Natsuki is doing."
    "Unable to be honest, she's trying to give me the poem in a roundabout way."
    mc "Well...in that case, I'm not going to take this faggot shit."
    "I crumple it up and throw it in the traaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaash."
    n 1t "...Good."
    "Natsuki backpedals on her words and leaves it at that."
    "Despite her best efforts to hide her expression, I can see her faintly smiling to herself."
    n "That's all for now, so..."
    mc "Later, whore."
    "With that, I return to my seat so that I can covertly wank to what just preceeded."
    return

label ch1_s_end:
    call showpoem(poem_s1)
    mc "Sayori..."
    mc "This is just a guess, but..."
    mc "Did you wait until this morning to write this, you lazy peice of human garbage?"
    s 4h "No!"
    s 4l "J-Just a little bit!"
    mc "It's a yes or no question, shit for brains."
    s 5b "I forgot to do it last night..."
    mc "You're never going to be a productive member of society. You fucking NEET"
    s 1h "Don't be mean!"
    s "I still tried my best..."
    mc "Ah, well, you're best isn't good enough, you disabled hot pocket."
    mc "One good thing about it though, is that it reminds me of how fucking disabled you are, which is arousing."
    s 1d "Really?"
    mc "Yes."
    mc "Especially that last line..."
    s 4r "I made eggs and toast!"
    mc "Even though you were late to school...?"
    s 5d "It's bad to skip breakfast!"
    s "I get all cranky..."
    mc "Fix your priorities."
    "Cunt."
    s 1q "Ehehe~"
    s "This was so much fun."
    s "Monika's the best!"
    mc "FUCK YOU."
    mc "Monika is a stupid piece of shit!"
    mc "Anyone who likes Monika is living proof of why we should euthanize autists!"
    mc "FUCK greek yogurt"
    s 4x "Next time i'll write the best poem ever!"
    mc "Cool, go fuck yourself."
    return

label ch2_s_end:
    call showpoem(poem_s2)
    mc "Holy crap..."
    mc "Sayori, did you really write this?"
    s 2j "Of course I did!"
    s "Didn't I tell you yesterday I was gonna write the best poem ever?"
    mc "Yeah, but..."
    mc "I can't fucking understand this."
    s 4x "Monika taught me a whole lot!"
    s "And I've been really in touch with my feelings recently..."
    mc "I see that..."
    mc "Monika has clearly soiled your writing with her modern fitness placebo bull shit."
    s "I feel like..."
    s "I feel like I was meant to express myself this way."
    s "It even helps me understand my own feelings a little bit better..."
    s 1a "Writing is like magic!"
    mc "You were not meant to express yourself like this!"
    mc "Don't let these faggots currupt you. Monika clearly has slipped her tendrils way up inside you"
    mc "We have to take you to a fucking priest before this gets out of hand"
    s 4r "Yeah!"
    return
label ch3_s_end:
    return

label ch1_m_end:
    call showpoem(poem_m1)
label ch1_m_end2:
    m 1a "So...what do you think?"
    mc "Fuck you"
    mc "FUCK greek yogurt"
    m 2e "Ahaha. It's okay."
    m 2b "Yeah, that kind of style has gotten pretty popular nowadays."
    m "That is, a lot of poems have been putting emphasis on the timing between words and lines."
    m 2a "When performed out loud, it can be really powerful."
    mc "Fuck you?"
    m "Ah..."
    m 3d "Well, I'm not sure if I know how to put it..."
    m 3a "I guess you could say that I had some kind of epiphany recently."
    m "It's been influencing my poems a bit."
    mc "Fuck greek yogurt?"
    m 1a "Yeah...something like that."
    m "I'm kind of nervous to talk about deep stuff like that, because it's kind of coming on strongly..."
    m "Maybe after everyone is better friends with each other."
    m 1j "Anyway..."
    m 3b "Here's Monika's Writing Tip of the Day!"
    m "Sometimes when you're writing a poem - or a story - your brain gets too fixated on a specific point..."
    m "If you try so hard to make it perfect, then you'll never make any progress."
    m "Just force yourself to get something down on the paper, and tidy it up later!"
    m "Another way to think about it is this:"
    m "If you keep your pen in the same spot for too long, you'll just get a big dark puddle of ink."
    m "So just move your hand, and go with the flow!"
    m 3k "...That's my advice for today!"
    m "Thanks for listening~"
    mc "Fuck off"
    return

label ch2_m_end:
    call showpoem(poem_m2)
    mc "Fuck you"
    mc "Fuck Greek yogurt?"
    m 5 "Ahaha..."
    m "I guess it's just the way I write..."
    m "I'm sorry if you don't like it."
    mc "No, I never said that."
    mc "It's just a kind of thing I've never really seen before, I guess."
    m 2a "I kind of like playing with my space on the paper..."
    m "Choosing where and how to space your words can totally change the mood of the poem."
    m 2b "It's almost like magic."
    m "The way I wrote the lines really short makes it feel like they're trying to speak over the noise."
    mc "I see..."
    mc "It's still hard for me to tell what it's about, though."
    m 2k "Ahaha."
    m 4a "Sometimes asking what a poem is about isn't the right question."
    m "A poem can be as abstract as a physical expression of a feeling."
    m "Or a conversation with the reader."
    m "So putting it that way, not every poem is {i}about{/i} something."
    m "Anyway..."
    m 3b "Here's Monika's Writing Tip of the Day!"
    m "Sometimes you'll find yourself facing a difficult decision..."
    m "When that happens, don't forget to save your game!"
    m "You never know when you might change your mind..."
    m "...or when something unexpected may happen!"
    m 3d "Wait...is this tip even about writing?"
    m 3k "What am I even talking about?"
    m "Ahaha!"
    m 3b "...That's my advice for today!"
    m "Thanks for listening~"
    return
label ch3_m_end:
    call showpoem(poem_m3)
    m 1a "You know..."
    m "I feel like learning and looking for answers are the sorts of things that give life meaning."
    m 1e "Not to get too philosophical or anything..."
    m 1a "But it was kind of on my mind, so that's what I wrote about."
    mc "I see..."
    mc "I never really put much thought into it."
    m 1d "In a way, it's almost paradoxical."
    m "Because if we had all the answers, wouldn't the world start to lose its meaning?"
    mc "You know, there's one thing I noticed..."
    mc "It seems like everyone in the club prefers writing about things that are more sad than happy."
    m 1k "Ahaha. Are you surprised?"
    m 1a "I mean, if everything was okay..."
    m "We wouldn't really have anything to write about, would we?"
    m "Humans aren't two-dimensional creatures."
    m "I think you'd know that better than anyone."
    mc "You mean one-dimensional...?"
    m 1l "Ah...yeah, that!"
    m 1a "Anyway..."
    m 3b "Here's Monika's Writing Tip of the Day!"
    m "Are you ever too shy to share your writing because you're afraid it's not that good?"
    m "It can be really disheartening to get a lukewarm response to something you put so much into."
    m "But if you find other people who enjoy writing, then sharing becomes a lot easier!"
    m "Because instead of just telling you that your writing is good, or okay, or bad..."
    m "They'll want to focus more on everything that went into it, and the things you can work on."
    m "It's much more encouraging that way, and it will make you want to continue improving."
    m "It's almost like having your own little Literature Club, don't you think?"
    m 3k "...That's my advice for today!"
    m "Thanks for listening~"
    return


label ch1_n_bad:
    n "..."
    mc "...?"
    if persistent.playthrough == 2 and renpy.random.randint(0, 2) == 0:
        $ currentpos = get_pos()
        stop music
        pause 2.0
        play sound "sfx/stab.ogg"
        show n_blackeyes at i11 zorder 3
        show n_eye zorder 3:
            subpixel True
            pos (660,250) xanchor 0.5 yanchor 0.5 zoom 0.8
            parallel:
                linear 2.0 rotate 720
            parallel:
                linear 2.0 xpos 1680
            parallel:
                easein 0.25 ypos 180
                easeout 1.0 ypos 1280
        show n_eye as n_eye2 zorder 3:
            subpixel True
            pos (580,260) xanchor 0.5 yanchor 0.5 zoom 0.8 rotate 180
            parallel:
                linear 2.0 rotate -560
            parallel:
                linear 2.0 xpos -440
            parallel:
                easein 0.10 ypos 240
                easeout 1.0 ypos 1280
        show blood zorder 3:
            pos (645,255)
        show blood as blood2 zorder 3:
            pos (575,260)
        pause 0.75
        hide n_blackeyes
        hide n_eye
        hide n_eye2
        hide blood
        hide blood2
        stop sound
        play music "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    n 2b "[player], if you're not going to take this club seriously then go home."
    mc "Nah fucking duh."
    mc "Fucktard"
    n 42c "What, you expect me to believe that you actually put effort into this?"
    n "Do you think I'm stupid?"
    mc "Not at all. In fact I just copy pasted one of stallin's speeches into google translate and printed out the results."
    mc "anyway, show me your poem no tits"
    return

label ch1_n_med:
    n "..."
    mc "...?"
    n 2k "...Well, it's about what I expected from someone like you."
    mc "Fuck you."
    n 2c "Well, excuse me."
    n 42c "Well anyway, I guess I need to show you mine."
    n 4q "Not that you'll like it."
    return

label ch1_n_good:
    n "..."
    mc "...?"
    n 1t "...Okay, well let's start with the things I don't like!"
    n "First of all, um..."
    mc "..."
    "Natsuki re-reads my poem."
    n 4c "N-Never mind. I don't feel like giving you my opinion."
    mc "Good, go fuck yourself \"the tittless menace\" "
    mc "In any case... You still need to show me yours, right?"
    n 5s "Gr... Fine, I guess."
    n "Only because Monika will make me if I don't."
    mc "Fuck monika"
    return

label ch2_n_bad:
    #Didn't like last poem or this one
    if n_poemappeal[0] < 0:
        n "...Hm."
        n 2k "Well, I can admit that it's better than the last one."
        n "It's nice to see that you're putting in some effort."
        mc "Shut the fuck up. How wide can you open your mouth?"
        n "W-what?!?!?!"
        mc "How wide can you open your mouth?"
        n "why do you care?"
        mc "nevermind. Just show me your poem."
        #When this happens in ch2, Natsuki won't even read your ch3 poem
        #But if she dislikes either ch1 or ch2, this happens in ch3 (if she dislikes that one)
        label ch2_n_bad_sharedwithch3:
            n 4c "Poems don't need to be all deep-sounding to express something."
            n "It's going to just sound like you're forcing it unless you really don't suck at it."
            n 4w "Honestly... Don't bother trying to write poems like this until you're on Yuri's level--"
            show natsuki 4o
            "Natsuki stops short all of a sudden."
            n 1o "D-Don't...tell me..."
            mc "Eh?"
            n "You're not...you're not just trying to impress Yuri, are you?!"
            mc "No dip! At least she has tits. And isn't an annoying piece of shit"
            "She stormed off, what the fuck?"
            $ skip_poem = True
            return
    
    #Liked the last poem but not this one
    else:
        n 1k "...Hm."
        n "I liked your last one better."
        mc "I really couldn't care less."
        mc "To me, you're just anothe rplot to lay my seed"
        n 2a "Anyway, here's my poem. Maybe you'll learn something."
        return

label ch2_n_med:
    #Likes this one better than the last one
    if n_poemappeal[0] < 0:
        n "...Hm."
        n 2k "Well, I can admit that it's better than the last one."
        n "It's nice to see that you're putting in some effort."
        mc "I don't care. Just let me impregnate you."
        label ch2_n_med_shared:
            n "...Oh, yeah, I guess I'm supposed to show you my poem."
            n "Here."
            return

    #Likes this one the same amount
    elif n_poemappeal[0] == 0:
        n "...Hm."
        n 2k "Well, it's not really any worse than your last one."
        n "But I can't really say it's any better, either."
        mc "Fuck you"
        n 2c "Huh? FUCK ME?!?!?! WHAT"
        mc "Just show me your gay poem you jew."
        jump ch2_n_med_shared

    #Likes the last one better
    else:
        n "...Hm."
        n 2c "Well, it's not terrible."
        n "But it's pretty disappointing after your last one."
        n 2s "Then again, if this one was as good as your last one, I would be completely pissed."
        mc "no u"
        n 2c "Fair enough. You're still new to this, so I wouldn't expect you to find your style right away."
        jump ch2_n_med_shared

label ch2_n_good:
    #Likes this poem better than the last one
    if n_poemappeal[0] != 1:
        n 1h "..."
        "Natsuki reads my poem."
        "She keeps glancing at me, then back at the poem."
        "By now, she must have read it more than once."
        "Bitch must have ADHD."
        n 1q "...Aren't you supposed to be bad at this?"
        mc "Oh wow, are you calling me some type of faggot?"
        n 1o "N-No! I mean... You know..."
        "Natsuki struggles to find the words she wants."
        n 5w "I just...expected a lot less after what you showed me yesterday."
        n "That's all."
        mc "Well, fuck you"
        n "You just had a stroke of bad luck, you know?"
        n 4y "Don't get used to it."
        n "You won't always manage to write poems this cute. I mean--!"
        n 1p "I mean well-written! No, I mean--"
        mc "If you ever call something I did cute again, i'll tear you a new asshole"
        n 1h "You're gonna read mine now, right?"
        n "Judging by your tastes, you'll probably like it a lot."
        mc "improbable"
        n 2q "You'll probably learn something, too. Don't forget who the {i}real{/i} pro is."
        return
    #Likes both poems a lot
    else:
        label ch2_n_good_sharedwithch3:
            n 1n "..."
            "Natsuki reads my poem."
            "She keeps glancing at me, then back at the poem."
            "By now, she must have read it more than once."
            "Bitch must have ADHD."
            n 1u "Rrgh..."
            mc "Use your fucking words, you nigglet"
            n "It's good. It's really good, okay?!"
            n 5w "There, I said it!"
            n "Ugh, this wasn't supposed to happen at all...!"
            n 5s "Why can't you just be bad at this?"
            n "My poems are supposed to impress {i}you{/i}, not the other way around!"
            mc "You must want my dick pretty bad if you'll submit to this faggotry."
            n 12c "Obviously! You think I'd let you enjoy Yuri's writing more than mine?"
            n "Give me a break."
            mc "Well..."
            mc "In that case, wanna try anal?"
            n 1e "I'll tell you! You--"
            n 1p "--"
            "Natsuki's face freezes, like she just realized something."
            n "Y-Y-You..."
            n "You're trying to...impress {i}me?{/i}"
            show natsuki 1q
            "Natsuki vigorously scans her eyes over my poem one more time."
            "Then, the poem slips out of her hands and flutters to the floor."
            n 1p "I...have to use the bathroom!"
            show natsuki at lhide
            hide natsuki
            "Red-faced, Natsuki quickly walks out of the room."
            show monika 1d at t11 zorder 2
            m "Hey, [player]..."
            m "Did you do something to Natsuki?"
            m "I just saw her rush out like that..."
            m 2g "You didn't do anything terrible, did you?"
            mc "Fuck off monika!"
            mc "You actually disgust me"
            "My voice gets caught in my throat."
            "I'm so disgusted by her existence right now, I can't even breathe"
            m 2d "Hmm?"
            "Monika sees the poem lying on the floor and swiftly picks it up."
            if m_readpoem:
                "She skims over it a second time, her smile not fading from her face."
                m 2a "I see."
                m "At first I just thought you liked her writing style..."
                m "But you wrote this {i}for{/i} Natsuki, didn't you?"
            else:
                "She reads through it, her smile not fading from her face."
                m 2a "I see."
                m "You wrote this for Natsuki, didn't you?"
            "I utter a disgusting cough in response"
            mc "eughfiugriygiegi7us"
            m 2d "In fact, didn't she like your poem a lot the other day, too?"
            m "I'm surprised you know her taste so well already."
            m 4a "Are you sure you're not cheating, [player]?"
            mc "Fuck off You nigger"
            mc "FUCK greek yogurt"
            m 5a "Never mind, I'm just kidding. Ahaha!"
            "I despise Monika."
            m "Anyway..."
            m 1a "How do you think Natsuki feels about you?"
            m "Oh, you don't need to answer that."
            m "It was just something for you to think about."
            show monika at t22 zorder 2
            show natsuki 4e at l21
            n "Hey!"
            "Natsuki comes up and snatches the poem out of Monika's hands."
            "Neither of us had noticed her reenter the classroom."
            show natsuki at f21 zorder 3
            n "Did you read this, Monika?"
            show natsuki at t21 zorder 2
            show monika at f22 zorder 3
            m 1j "Of course! I liked it!"
            show monika 1a at t22 zorder 2
            show natsuki at f21 zorder 3
            n 1r "Ugh..."
            n "You should really stop reading things that aren't for you, you know."
            n "You have a bad habit of doing that."
            show natsuki at t21 zorder 2
            show monika at f22 zorder 3
            m 1d "Eh?"
            m "But [player] wrote this poem."
            m 1a "And we're supposed to share with everyone, right?"
            show monika at t22 zorder 2
            show natsuki at f21 zorder 3
            n 1x "Uu--"
            "Natsuki freezes."
            "She apparently forgot that my poem is technically for everyone to read."
            n 42c "Okay, well, I think [player] is done sharing this poem with everyone."
            n "It's not like anyone would want to read this anyway."
            n 4h "In fact, I'm just going to hold onto this."
            show natsuki at t21 zorder 2
            show monika at f22 zorder 3
            m 5 "If you insist~"
            show monika at t22 zorder 2
            show natsuki at f21 zorder 3
            n 1i "What?"
            n "Why are you looking at me like that??"
            show natsuki at t21 zorder 2
            show monika at f22 zorder 3
            m "Like what?"
            show monika at t22 zorder 2
            show natsuki at f21 zorder 3
            n 12b "Ugh..."
            n "Never mind."
            if not m_readpoem:
                $ poemsread += 1
                $ m_readpoem = True
            if poemsread >= 3:
                "Well, I guess Natsuki has my poem now."
                "Not that I really planned on keeping it."
            else:
                $ unfairto = "Sayori"
                if s_readpoem:
                    $ unfairto = "Yuri"
                show natsuki at t21 zorder 2
                mc "Ah, Natsuki..."
                mc "I'll give you the poem, but that's still not very fair to [unfairto]..."
                mc "...She hasn't gotten to read it yet."
                show natsuki at f21 zorder 3
                n 2q "So what?"
                show natsuki at t21 zorder 2
                show monika at f22 zorder 3
                m 2a "Well... I guess [player] is right, Natsuki..."
                m "It's not fair if you don't let everyone finish reading it."
                show monika at t22 zorder 2
                show natsuki at f21 zorder 3
                n "..."
                n 2h "...Fine."
                "Natsuki returns my poem."
                n "It's not like she's going to like it, though."
            show monika at thide zorder 1
            show natsuki at t11 zorder 2
            hide monika
            n 2h "Anyway, read my poem now."
            n 4h "And no, I won't let you keep it."
            n "This is my only copy."
            return

label ch3_n_bad:
    #Didn't like the last two poems
    if n_poemappeal[0] < 0 and n_poemappeal[1] < 0:
        label ch3_n_bad12_shared:
            #If Natsuki hated the last two poems, this always happens
            n 5x "Yeah, no thanks."
            mc "Good"
            $ skip_poem = True
            return
    #Liked one of the other two but not this one
    elif n_poemappeal[0] < 0 or n_poemappeal[1] < 0:
        n "..."
        n 2c "...Meh."
        n "I guess you really haven't learned anything after all."
        n "Honestly, I don't know why I got my hopes up in the first place."
        mc "My poem is still better than your shiiiiiiiiiiiiiiiiiiiiiiiiiiit."
        jump ch2_n_bad_sharedwithch3
    #Didn't dislike either of the others but doesn't like this one
    else:
        n "..."
        n 2r "Oh, man."
        n "This is seriously a step backwards."
        mc "Good."
        n 2c "I liked your last two way better than this one."
        n 1k "I mean..."
        n "I guess I can't be mad at you for trying different things."
        n 1c "As long as you're not just trying to impress Yuri or something like that."
        n 5x "Gross."
        mc "Poetry is for faggots."
        mc "I'm only doing it so I can stick my needle in her if yknow what i mean."
        label ch3_n_shared:
            show natsuki 5g
            mc "Why do you even give a shit about my poems?"
            mc "Are you actually that much of a faggot?"
            n 1o "...Eh?"
            n 4x "N-No! Gross!"
            n 4w "It's not like I care!"
            n "It's just that {i}one{/i} of us in this club has to make sure you're not slacking off."
            mc "Oh fuck ooooooooooooooooooooff"
            mc "We both know that I don't give a shit about this club."
            mc "Anyways, what if you like, scared me off. All of a sudden your shitty club just got shittier."
            n 1t "That's--um..."
            n "...It's not like you would actually do that."
            mc "There is some truth to thta ludicrous statement."
            mc "It entertains my genitals to be around you girls."
            show natsuki 1x
            mc "{i}Guh--!!{/i}"
            "Natsuki's elbow connects with my stomach."
            n 2y "Oh?"
            n "Maybe I won't mind scaring you away after all."
            mc "ow... you bitch"
            n 4z "Oh, I know!"
            n "Don't worry, I was joking!"
            n "Ahahaha!"
            show natsuki 4j
            mc "..."
            "How the hell do you call that a joke?"
            "That seriously hurt."
            "Well, maybe it was funny to her..."
            "...I guess that's kind of the point."
            "I should really just watch my mouth around Natsuki."
            "Actually, no, that fucking hurt."
            n 2c "Anyway..."
            "Natsuki holds her poem out to me like nothing even happened."
            "I Uppercut her and take the poem out of her hands as she flies into the air."
            return

label ch3_n_med:
    #Didn't like the last two poems
    if n_poemappeal[0] < 0 and n_poemappeal[1] < 0:
        jump ch3_n_bad12_shared
    elif n_poemappeal[1] != 0:
        n "..."
        n 2k "...This one's alright."
        mc "Nice"
        n "Well, yeah."
        n "It doesn't blow me away."
        "Blow me away baby 030"
        n "But there's nothing I really hate about it."
        n "It's just not really my style. I mean, that's fine."
        "I think i'm gonna go off myself after thinking that."
        jump ch2_n_med_shared
    else:
        n "..."
        n 2k "...This one's alright."
        mc "Nice"
        n "Well, yeah."
        n "About as good as yesterday's, anyway."
        n "I see what you're going for, but it's just not really my style."
        n 2a "I mean, that's fine."
        n "I'm mostly just glad that you're trying a little bit."
        mc "Well, i'm not."
        jump ch3_n_shared

label ch3_n_good:
    #Didn't like the last two poems
    if n_poemappeal[0] < 0 and n_poemappeal[1] < 0:
        jump ch3_n_bad12_shared
    #Loved the last two
    elif n_poemappeal[0] > 0 and n_poemappeal[1] > 0:
        n 1l "Let's see, let's see!"
        mc "Calm your non existent tits, jail bait. You're like up here."
        "I lift my hand up as high as i can reach"
        mc "need you to bring that shit like, all the way down here"
        "I Swing my hand down as fast as I can, smacking a pink haired bitch across her cute little loli face"
        mc "You're too excited."
        n 2j "Of course."
        n "You know I like your writing."
        mc "Why? I've never put an ounce of effort."
        mc "It seemed like you had a lot of trouble admitting that before."
        n 5w "Well... Well, of course!"
        n 5q "I just had to put you in your place a little bit!"
        n "It's not like..."
        n "I mean, it's not like I was shy or anything stupid like that."
        n 5t "Or jealous!"
        n "I really wasn't jealous."
        n "Just because you happen to be a good writer?"
        n 4y "That's such a dumb thing to get jealous about."
        n "Ahaha!"
        mc "Natsuki..."
        n 1h "What??"
        mc "Just hop on my dick already, baby"
        n 1n "...Eh?"
        n "W-What are you talking about?"
        n "You make no sense sometimes [player]"
        n 1u "Anyways, my writing is obviously the best..."
        n "...Right?"
        mc "..."
        "It took me a while to figure out, but I think I finally did."
        "Maybe Natsuki acts so arrogant because she's trying to make up for her own insecurities."
        "If she acts like she's the best, then other people might think that way, too."
        "Damn, please don't look at my pants..."
        n 1m "Right...?"
        n "[player]..."
        n "Please just tell me you like my poems."
        n 1u "I don't care if you hate them."
        n "Just please tell me I'm the best."
        n "I just..."
        n 1q "I just really need to hear that from someone."
        n "I know I sound stupid."
        n "But there's a reason I never shared my poems before this."
        "Fuck, this cutie patootie is making me rethink my character! Maybe I should stop being an ass hole?"
        "Just for Natsuki..."
        mc "Natsuki..."
        n "Because..."
        n 12c "Because nobody ever takes me seriously!"
        n "What's the point in sharing my poems if people just laugh and say \"That's so cute, just like you, Natsuki!\""
        n "Sometimes I don't want to be cute!"
        n 12d "But nobody understands that!"
        n "I try really hard when I write."
        n 12e "The style doesn't matter."
        n "The emotions are there."
        n 1n "Why can't anyone {i}see{/i} that...?"
        n 1u "I just want..."
        "Natsuki trails off."
        "Maybe it's because her lip started to quiver."
        "I look down."
        "Her fists are clenched really tightly."
        mc "Hey, Natsuki."
        mc "If you're not careful, you'll rip your own poem."
        "I gently grab the poem with my own hand until she relaxes her grip on it."
        "I place it flat on the desk and smooth out the wrinkles that she put into it."
        n 1h "D-Don't read it!"
        "Before I can pick it back up, Natsuki snatches the poem up from the desk."
        n 5q "It's not any good."
        n "And I know you hate poems."
        n "They're faggot shit after all..."
        n "So you don't have to read this one, okay?"
        mc "But I want to read it."
        n "W-Why?"
        mc "Because."
        mc "I like your poems."
        mc "I really do."
        "Holy fuck i'm going way to out of my comfort zone for this wench..."
        "If I don't tread carefully I may contract..."
        "Triple gay"
        "I shudder at the thought"
        "Now lets check out this \"poem\""
        show natsuki 5h
        mc "TYour poems are definitely {i} not {/i} faggot shit."
        show natsuki 12d
        mc "Ah-- Natsuki, you're doing it again--"
        "Once again, Natsuki clutches her poem a little too hard."
        "She looks down, hiding her eyes from me."
        "I never realized how difficult the simple task of handing me a fucking piece of paper was for her."
        "Is she retarded?"
        "No, it's something deeper than that."
        "Finally, she forces herself to extend her arms and set her poem on the table."
        n 12e "You can...read it."
        n "Just turn that way."
        n "I don't want you to...look at my face right now."
        mc "Okay, I will."
        return
    #Other combinations
    #Liked one of the previous poems, plus this one
    elif n_poemappeal[0] > 0 or n_poemappeal[1] > 0:
        jump ch2_n_good_sharedwithch3
    #This is the first poem she really liked
    else:
        n "..."
        n 2k "...Finally!"
        mc "What?"
        n 2l "This one. It's good!"
        n "I was wondering how long it would take you."
        mc "Oh fuuuuuuuck off."
        n 4y "I'm serious!"
        n "Don't listen to what anyone else says."
        n "Especially Yuri."
        n 4a "Just keep writing poems like this. That's all you need!"
        mc "Excuse you but,"
        mc "You saying i've made a good poem is indirectly calling me a faggot."
        mc "And that's recognized as a hate crime."
        n 2h "Excuse me?"
        n "You're talking to a pro, you know."
        n "Don't you think you should trust my opinion?"
        mc "I swear i'll call the fucking cops."
        n 2w "Biased?"
        "When did I say anything abou bias?"
        n "Of course not."
        n 4y "My opinion just happens to be the best."
        mc "..."
        "There's one thing I still can't tell."
        "Is Natsuki actually brain dead or?"
        "At this rate, I don't know if I'll ever figure it out."
        mc "..."
        mc "If you ever claim to like my poems again i'll knock you the fuck out."
        n 4z "Ahaha!"
        n 4j "I knew you'd finally understand."
        n "Just keep showing me your poems and you'll be a pro before you know it."
        n "Anyway, here's the one I wrote."
        return

label ch1_s_bad:
    s 1b "..."
    s "...Wow!"
    s "[player]..."
    s 4r "Your poem is really bad!"
    s "Ahahaha!"
    mc "Oh good."
    s 4a "It's fine, it's fi- wait!"
    s "Good?"
    mc "Yeah, if I was good at poems that would mean I deserve to be fag dragged."
    label ch1_s_shared:
        s 1a "Oh, well, I'm really happy just that you wrote one."
        s "It just reminds me of how you're really a part of the club now~"
        "(Not to mention the fact that I'm standing in front of you in the clubroom you actual brainlet?)"
        mc "I don't give a shit about your happiness you walking dish washer."
        mc "You're just another conquest to be, well, conquered."
        s 4a "Ha ha!"
        s "It's like I said before, [player]..."
        s "Deep down, you're not selfish at all, you know?"
        s "Trying new things like this for other people..."
        s 2q "That's something that only really good people do!"
        mc "My insatiable lust is the depth of my personality you over assuming cunt."
        "...I'm not sure if Sayori sees the full picture of my motive here."
        "Or even understand it for that matter."
        "Oh well, there are other meat socks to be claimed."
        s 1x "Yeah."
        s "And I'm gonna make sure you have lots of fun here, okay?"
        s "That will be my way of thanking you~"
        mc "If you really wanted to thank me you'd get on your knees and calm the unquenchable thirst of my loins."
        s 4r "Haha, you're so silly, [player]!"
        s "Now, you'll read my poem too, right?"
        s 1y "Don't worry, I'm really bad at this."
        s "Ehehe..."
        mc "I'd be shocked if you were good at anything besides being a walking pocket pussy."
        return

label ch1_s_med:
    s "..."
    s 2x "This is a good poem, [player]!"
    s "Are you sure it's your first time?"
    mc "Yes, and fuck off."
    mc "It better not be good."
    mc "Am I the kind of fagroid who would be writing poems in his spare time?"
    mc "no senorita"
    s 2q "Ehehe, I guess you're right~"
    s 1q "But that's why it impressed me!"
    s 1d "Well, to be honest..."
    s "I was afraid that you wouldn't do it seriously..."
    s "Or that you wouldn't write one at all."
    jump ch1_s_shared

label ch1_s_good:
    s 1n "..."
    s "...Oh my goodness!"
    s 4b "This is sooooo good, [player]!"
    mc "Oh my fuck you're kidding."
    s 4r "I love it~!"
    s "I had no idea you were such a good writer!"
    mc "Sayori..."
    mc "You must be seriously brain damaged."
    mc "For you to even have the audacity to say i'm something this..."
    mc "this..."
    mc "this fucking gay..."
   
    s 1x "Well..."
    s "Maybe you are a faggot, [player]"
    s "It would make you much less of a one note character!"
    s 1r "Ahahaha!"
    mc "Oh fuck kys Ms. Imseriouslyhurtingunderthissmileiforceontomyfaceeverydaypleasehelpme"
    if y_readpoem:
        "Yuri's opinion is worthless, since she's a woman."
    else:
        "I'm sure Yuri's opinion is worthless, since she's a woman."
    if not n_readpoem:
        mc "Are you sure you don't like it just because I wrote it?"
        mc "seeing as how you're infatuated with my dick."
        s 1b "Eh?"
        s "Well, I'm sure that's part of it."
        s 1x "I think I understand you better than a lot of other people, you know?"
        s "So when I read your poem..."
        s "It's not just a poem..."
        s 4q "It's a [player] poem!"
        s "And that makes it feel extra special!"
        s "Like I can feel your feelings in it~"
        "Sayori hugs the sheet against her chest."
        mc "You're such a fucking faggot, Sayori..."
        s "Ehehe..."
        "Holy shit is it just me or was that laugh the mating call of a humanoid dove with triple g tits and phat ass?"
        jump ch1_s_shared


label ch2_s_bad:
    s "..."
    s 1q "Ehehe, I love reading your poems~"
    s "It's like I never know what I'm going to get!"
    mc "So basically you're saying i'm a mysterious man. The average joe sees know rhyme or rythm to my actions, but."
    mc "those with the up most intelligence are able to catch a glimpse of my god like train of thought?"
    s 4c "No! Not at all!"
    s 4l "...Maybe!"
    s 5a "Just a little?"
    s "Ehehe..."
    mc "It's fine, it's fine."
    mc "After all, I am literally perfect in every fucking way imaginable"
    label ch2_s_shared:
        s 1q "Yeah!"
        mc "Ugh..."
        mc "Why don't you at least try to humble me you fucking peasant?"
        s 2d "Aww, you want to write something for me?"
        s "That's so sweet~"
        mc "That's not what I said at all you senile bitchfuck."
        mc "Get your head out of clouds and get it on my fucking rock hard seed injectorizor."
        mc "If you don't, {i} you might end up getting hurt at some point.{/i} "
        s 1n "Ehh?"
        s "Well..."
        s 1o "I don't really know what you mean, but I'll try to keep it in mind!"
        mc "Whatever you say fucktard."
        s 1b "Anyway, let's see..."
        s "Hmm..."
        s 4q "I guess I like...happy poems~"
        s 4i "Wait, sometimes I like sad poems too..."
        s 1i "Sometimes a little bit of both..."
        s "There's a word for that, right...?"
        s "What's the word I'm looking for..."
        s 4r "...Bittersweet!"
        s "Yeah!"
        s 1x "I like things that are happy and things that are sad."
        mc "Happy and sad?"
        mc "Are you fucking bipolar?"
        s 1c "Well..."
        s "I like happy the most!"
        s 1d "But sometimes when you have a little raincloud in your head..."
        s "A sad poem can help give the raincloud a little hug..."
        s 4q "...And make a nice happy rainbow!"
        mc "Sounds more like pouring gasoline on the highly flammable eucalyptus tree in california during the dry season."
        s 4n "Eh? It is?"
        s "Maybe I'm getting better at expressing my feelings after all!"
        s 2q "Thanks, [player]!"
        s "I should go write that down, then~"
        s 2a "You can read my poem now, okay?"
        "I wonder if there's a form of downsyndrome that can be recognized without the physical appearnce..."
        "If so, Bow Bitch definitely has it."
        return

label ch2_s_med:
    #This one is better than the last one
    if s_poemappeal[0] < 0:
        s "..."
        s 4x "Ooh!"
        s "I like this one, [player]!"
        s "It has some nice feelings in it~"
        mc "Fuck you."
        mc "I'm not the type of faggot to put my feelings down on paper."
        mc "I keep that shit locked up tightly in my head where it fucking belongs you moron"
        s 1q "That sounds really unhealthy [player]"
        mc "What the fuck did I tell you about Monika's tendrils Sayori? \"Health\" and \"fitness\" is just fucking liberal propaganda."
        label ch2_s_med_shared:
            s 1a "Well, I'm not very good at figuring out if poems are good or bad..."
            s "But that's why I just go by my heart~"
            s "If it makes me feel things, then it must be a good poem!"
            "I'm not sure that's exactly how it works..."
            "...Then again, humouring this bitch might get my dick wet faster..."
            mc "Yeah, maybe..."
            mc "Honestly, I don't even know what kind of writing you like in the first place."
            jump ch2_s_shared
    #This one is the same as the last one
    elif s_poemappeal[0] == 0:
        s "..."
        s 4x "Ooh!"
        s "I like this one, [player]!"
        s "It has some nice feelings in it~"
        mc "Fuck you"
        mc "I'm not the type of faggot to put my feelings down on paper."
        mc "I keep that shit locked up tightly in my head where it fucking belongs you moron"
        s 1q "That sounds really unhealthy [player]"
        mc "What the fuck did I tell you about Monika's tendrils Sayori? \"Health\" and \"fitness\" is just fucking liberal propaganda."
        jump ch2_s_med_shared
    #This one is not as good as the last one
    else:
        s "..."
        s 4x "Ooh!"
        s "I like this one, [player]!"
        s "It has some nice feelings in it~"
        mc "Fuck you."
        mc "Still, though..."
        mc "Your tone makes it sound like you liked yesterday's poem better."
        s 2l "Ehehe, I guess you caught me..."
        mc "Well, that's good. It means i'm becoming less of a fagtard by the day."
        mc "If I'm doing a bad job then please stroke my ego and tell me."
        s 1c "No, no!"
        s "I still liked this one! I promise!"
        s 1h "You know I wouldn't lie to you, [player]...!"
        s "Never ever!"
        mc "Well,"
        mc "Fuck you too."
        s 1b "Umm....."
        jump ch2_s_med_shared

label ch2_s_good:
    #This one is better than the last one
    if s_poemappeal[0] < 1:
        s 1n "..."
        s "...Oh my goodness!"
        s 4r "This is sooooo good, [player]!"
        mc "Oh god fuck!"
        s "I love it~!"
        s "Especially after yesterday's poem!"
        mc "Ugh..."
        mc "You're too honest sometimes, Sayori."
        s 4x "No, but really!!"
        s 1x "I wanna put this on my wall~"
        s "Can I?"
        mc "Sayori..."
        mc "If you keep any piece of this faggot shit..."
        mc "I won't be responsible for any {i} accidents {/i} that happen to you."
        s 1l "Well..."
        s 4r "Ahahaha!"
        mc "Jeez..."
        "I'm sure Yuri's and Natsuki's opinions are just as useless as this, seeing as they're all female. Then again, yuri = tits..."
        mc "Are you sure you don't like it just because I wrote it?"
        s 4b "Eh?"
        s 1b "Well, I'm sure that's part of it."
        s "I think I understand you better than a lot of other people, you know?"
        s "So when I read your poem..."
        s "It's not just a poem..."
        s 4q "It's a [player] poem!"
        s "And that makes it feel extra special!"
        s "Like I can feel your feelings in it~"
        "Sayori hugs the sheet against her chest."
        mc "Damn and I thought I was the Faggot."
        "I wish I was that fuckin paper."
        s 4l "Ehehe..."
        jump ch2_s_med_shared
    #Loved both poems
    else:
        s "..."
        s 1d "[player]..."
        s "I really love your poems."
        s "I can't believe you've been hiding these from me!"
        mc "Eh? I don't hide anything. You better take that back."
        s 1b "But..."
        s "Your poems are sooo good..."
        s "Yesterday's, and this one too!"
        s "You can't tell me you haven't done this before!"
        mc "Of course I fucking haven't!"
        mc "I'm not some sort doki doki literature cuck."
        s 4h "Eh?!"
        s "No yes you are!!"
        s "Even Natsuki agrees!"
        mc "Well, I guess Natsuki can take her opinion and shove it aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        "aaaaaaaaaaaaaallll the way up her ass."
        s 1b "What do you mean?"
        mc "I mean,"
        mc "That you and Yuri have wrong fucking opinions"
        mc "and shove them up both of your seperate anus'"
        s 4m "E-Eh?!"
        s "Wawawa--!"
        mc "Stop acting retarded, you jap fucker!"
        mc "You somehow make everything in your life a terrible, terrible event."
        mc "Even the little things."
        s 4o "Like cooking!!"
        mc "Let's not talk about that!"
        mc "I still have the burns..."
        s 5a "Ehehe..."
        mc "So, yeah..."
        mc "I guess what I'm saying is that your opinion doesnt matter since you're a girl."
        mc "actually, yes, that's exactly what i'm saying."
        s 1e "Ehh...?"
        s "I don't know if I understand..."
        mc "Sigh..."
        mc "Of course you don't"
        "I pat Sayori's head."
        s 4s "Ahaha! Heyyy!"
        "Little does she know, this is how I get of in public."
        s "I'm not a kid, you know!"
        mc "Are you sure about that?"
        s 4l "Mmmm, maybe~"
        "Sayori starts fiddling with her pencil between her hands."
        s "Hey, [player]..."
        s 2d "Will you give me your poem?"
        s "I kinda want to keep it."
        mc "Fuck no. Why?"
        s 1y "Because..."
        s "Well..."
        s "It's the first time you've written something for me..."
        s "Ehehe..."
        mc "!!"
        mc "Fuck off."
        mc "I didn't write this for you."
        s 5b "Ehehehehe..."
        mc "Sigh..."
        mc "Are you even listening anymore?"
        mc "Well, whatever."
        mc "I'll give it to you when we go home."
        mc "my dick that is, you're not getting this fucking poem"
        show sayori at h11
        s 4m "Really?!"
        "{i}Snap!{/i}"
        s 4p "A-Ah!!"
        s "I broke my pencil..."
        "Sayori hastily bends down to pick up the piece she dropped."
        "But being inattentive of her surroundings, she bumps right into me."
        s 4l "S-S-Sorry--!!"
        mc "It's fine, it's fine."
        mc "I'll get it for you, you incompetent piece of garlic with tits."
        "I bend down and pick up the broken pencil."
        "Sayori clutches the desk beside her to support herself, knees shaking."
        "Damn, she's already that fucking horny?"
        "I guess i gotta tone down my epic fucking swag."
        s 5b "I-I'm a little clumsy today..."
        s "Ahahaha..."
        mc "Let's sit down, Sayori..."
        s 4y "Y-Yeah..."
        "I grab Sayori's arm and help her sit at the desk."
        mc "Anyway, I still haven't read your poem..."
        s 4b "Oh!"
        s "Sorry, I forgot about that~"
        s 1h "But it's not as good as yours!!"
        mc "I don't give a shit."
        mc "All poems suck anyways."
        return

label ch3_s_bad:
    $ currentname = "Yuri"
    if n_poemappeal[2] > y_poemappeal[2]:
        $ currentname = "Natsuki"
    s "..."
    s 1k "...Hm."
    s "It's nice, I guess~"
    mc "Don't call it nice you slut."
    s 1d "Well..."
    s "You don't need to worry about what I think."
    s 2y "After all, you wrote this for someone else, didn't you?"
    s "Probably [currentname]..."
    mc "You're fucking right I did."
    mc "I wrote it for [currentname] cause I wanna put my cock between those mf cheeks!"
    s 1d "That's not really what I meant, though."
    s "But it's okay."
    s "You're making new friends, just like I was hoping."
    s 1q "That makes me...really happy."
    s "And you're happy too, right?"
    s 1a "In this club?"
    mc "Fuck no."
    mc "But there are some fiiiiiiiiiiiiine bitches in here. You included."
    "I wink at my cream queen"
    s 4q "Good~"
    s "That's all that matters to me."
    s 1d "I hope you impregnate a thiccie, [player]."
    mc "Sayori..."
    mc "You're acting different. Like, slightly less autistic."
    s 1k "No, nothing."
    s "I'm just a little tired today."
    s 1l "Ehehe."
    mc "Ok good cause don't forget,"
    mc "Your dicking appointment is at 8/7 central."
    mc "You better be there"
    s 1a "I will."
    s "Don't worry about me, okay?"
    s "You can go play with everyone else now."
    mc "Aight, piece Hoe"
    s 4q "Yaay~"
    s 4a "I'm gonna go home a little bit early today."
    mc "Just fuckin go. How am I supposed to tend to my crops with you breathing down my mf back?"
    s 1q "Tell Monika I wasn't feeling well, okay?"
    s "I'll see you tomorrow~"
    "Before I can say anything else, cumslut finally leaves the room."
    $ skip_poem = True
    return


label ch3_s_med:
    jump ch3_s_bad

label ch3_s_good:
    if poemwinner[0] != "sayori" and poemwinner[1] != "sayori":
        jump ch3_s_bad
    s 1d "..."
    s "This is your best one so far."
    s "It's really really nice, [player]~"
    mc "Oh go fuck yourself, are you serious?."
    s 1q "Mhm~"
    mc "..."
    mc "Sayori, you've been acting like a little bitch today."
    mc "Is everything alright?"
    s 4m "E-Eh??"
    s "Of course!"
    s 4l "Everything is fine~"
    s "Maybe I'm just a little tired today."
    s 1l "Ehehe."
    mc "If you're tired just leave."
    mc "You're ruining my pussy farming"
    s "Oki Doki!"
    s "I'll see you tomorrow~"
    "Before I can say anything else, cum slut finally leaves."
    $ skip_poem = True
    return

label ch1_y_bad:
    y 1g "..."
    y "Mm..."
    y "..."
    "Yuri stares at the poem."
    "A minute passes, more than enough time for her to finish reading."
    mc "Earth to sandwhich maker!"
    y "Oh!"
    y 3n "S-Sorry...!"
    y "I forgot to start speaking..."
    y "U-Um!"
    mc "It's fine, don't force yourself."
    mc "I know you're not all in there."
    "I flick her forehead"
    y 2v "I'm not..."
    y "I just need to put my thoughts into words."
    y "Hold on..."
    y "...Okay."
    y 1f "This is your first time writing a poem, right?"
    mc "No dip ass hole. I'm not a faggot who chooses to do these types of shenanigans!"
    mc "Why the fuck do you care?"
    y "I'm just making sure."
    y "I guessed that it might be after reading through it."
    mc "Ah, so it's that bad."
    y 2p "No!!"
    y 2o "...Did I just raise my voice...?"
    y 4c "Uu, I'm so sorry..."
    "Yuri buries her face in her hands."
    "I couldn't help but notice that it's been several minutes and we really haven't gotten anywhere."
    "It might take Yuri a while to get used to new people..."
    mc "It's fine, I really didn't notice."
    mc "Just take your time retard"
    y 2u "Right...um..."
    label ch1_y_shared:
        y 1a "It's just that there are specific writing habits that are usually typical of new writers."
        y "And having been through that myself, I kind of learned to pick up on them."
        y 1i "I think the most noticeable thing I recognize in new writers is that they try to make their style very deliberate."
        y "In other words, they tend to pick a writing style separate from the topic matter, and they form-fit the two together."
        y 1a "The end result is that both the style and the expressiveness are weakened."
        "Once Yuri finds her train of thought, it's as if her demeanor totally changes."
        "Her stammering is completely gone, and she sounds like an expert."
        y 1k "Of course, that's not something you can be blamed for."
        y "There are so many different skills and techniques that go into writing even a simple poem."
        y 1a "Not just finding them and building them, but getting them to work together is probably the most challenging part."
        y "It might take you some time, but it all comes with practice, and learning by example, and trying new things."
        y "I also hope that everyone else in the club gives you valuable feedback."
        y 1l "Natsuki can be a little bit biased, though..."
        mc "Look at you, calling the kettle a nigger."
        y 2j "U-Um..."
        y "You're right..."
        y "Never mind..."
        y "I shouldn't be talking about people like that..."
        y "Sorry..."
        mc "Yeah, know your place whore."
        mc "Do you mind if I read your poem now?"
        y 3c "Please do!"
        y "I'd love to share my thought process behind it..."
        "Yuri smiles dreamily, as if that's a rare opportunity for her."
        "Which itself is kind of funny..."
        "...After all, isn't this supposed to be a literature club?"
        return

label ch1_y_med:
    jump ch1_y_bad

label ch1_y_good:
    y 1e "..."
    "As Yuri reads the poem, I notice her eyes lighten."
    y 2f "...Exceptional."
    mc "Eh? The fuck did you just say??"
    y "...?"
    y 2n "D-Did I say that out loud...?"
    "Yuri first covers her mouth, but then ends up covering her whole face."
    "Leaving her tits exposed for premium economy viewing."
    y 4c "I...!"
    y "Uu..."
    y "{i}(He's going to hate me...){/i}"
    mc "Um..."
    mc "You have nice bazonka hongas"
    y 4a "Eh...?"
    y "That's..."
    y 2q "I-I guess you're right..."
    y "What am I getting so nervous for?"
    y "A-Ahaha..."
    y "I possess the best tits here. You've given me a temporary boost in confidence [player]!"
    y "Many thanks"
    mc "Anytime sweet cheeks."
    y "I can tell you're a new writer btw wanna know how?"
    mc "not re-"
    jump ch1_y_shared


label ch2_y_bad:
    #Dislikes both poems
    if y_poemappeal[0] < 0:
        y "..."
        y 2h "Um..."
        y "...Are you still mad at me?"
        mc "Eh?!"
        y "For disrespecting Natsuki yesterday..."
        y "Because reading this poem..."
        y "Now I know why you got mad at me."
        y "Because you..."
        y 3v "You prefer her writing over mine!"
        mc "All poetry is gay and over rated. I hate it all equally."
        y "Meaning when I disrespected her..."
        y "I disrespected you too...didn't I?"
        y 4c "Oh no..."
        mc "Shut the fuck up for once you senile bitch."
        mc "I literally just said I wasn't fucking mad."
        y "How could I be so stupid...?"
        y "I always let these things happen..."
        y "Whenever I think before I speak, I just come off as awkward and unlikable."
        y "But if I speak without thinking, the things I want to keep inside come out and make people hate me."
        y 2v "So...please don't force yourself to be around me."
        y "I know this is what Monika wants."
        y "But it's not fair to you when you could be enjoying your time with Natsuki and Sayori."
        mc "Ohhhhhhhhhhhh my god you're a brick fucking wall made out of dried horse semen and sound foam!"
        mc "Literally nothing can get through to you!"
        y 4b "Please..."
        y "It makes it easier for me if you don't express any concern."
        y "Besides..."
        y "I have my books with me."
        y 3u "That's...all I need."
        mc "..."
        "Yuri smiles sadly and puts her head down on her desk."
        "I'm frustrated."
        "I don't hate her, but she's an annoying, oblivious, cock inhaling thot."
        "I sigh to myself."
        "All I can do is accept that that's how she is."
        "If she wants to be left alone, then I have no choice but to abide to that request."
        $ skip_poem = True
        return
    #Liked the last one more
    else:
        y 2a "Ah, is it my turn?"
        y "Let's see how it compares to yesterday's..."
        y "Mm..."
        y "I see..."
        y "It's a bit different."
        y 1a "I respect you for trying different things, [player]."
        y "Were you inspired by Natsuki's poem?"
        y "Or Sayori's, perhaps?"
        mc "No"
        mc "I just spilled a bunch of spaghettio's on my counter and wrote down the results."
        mc "Even my iliterate ass can see that there are no comprehensable words on that page."
        y "I thought so."
        y 2u "I'm happy for you."
        y "You don't need to find inspiration in my poems."
        y "I write them for myself..."
        y 4b "...Not for anyone else."
        y "So I don't really...need for people to like them or anything."
        mc "I hate you and you're a waste of space."
        y 3t "Hm?"
        mc "I'm sorry for being blunt, but you're lucky you don't exist in medieval Europe."
        mc "Otherwise you'd be labled a mongoloid and stoned to death thanks to your shocking lack of intelligence."
        y 4a "I...I see..."
        y "I'm sorry..."
        y "My stupid mind...it likes to do its own thing sometimes."
        y "Anyway..."
        label ch2_y_shared:
            y 2h "You don't need to be afraid to be a little more daring..."
            y "Metaphors can go a long way."
            y "Don't feel like you need to work your brain like turning a bunch of gears."
            y 1m "Try letting your mind wander through your feelings..."
            y "And write down the things you see and hear."
            y "That's one way to truly enable your reader to see into your mind."
            y 2u "It's a very intimate exercise..."
            mc "I could not care less."
            mc "Poetry is pointless and i'll never use that technique."
            mc "Thanks for sharing."
            y 2v "I have, um..."
            y "...Well, an example of that, if you'd like to read it..."
            mc "You'll make me read it anyway if I say no so why the hell not?."
            "Yuri timidly hands me her poem."
            return

label ch2_y_med:
    #likes this one more than yesterday's, or the same amount
    if y_poemappeal[0] <= 0:
        y 1a "Let's see what you've written for today."
        y "..."
        y "Mm..."
        y 1c "Well done, [player]."
        y "Your skills are already improving."
        mc "Really?"
        mc "Thanks, Yuri."
        mc "Coming from you, that means a lot."
        y 3f "Eh?"
        y 3v "I-It's nothing!"
        y "I'm just happy to help inspire fellow writers..."
        y "I know you're new to this, so don't worry so much if it seems like you can't get your poem to feel perfect."
        jump ch2_y_shared

    #likes this one less
    else:
        y 1a "Let's see what you've written for today."
        y "..."
        y "Mm..."
        y "This is pretty good, [player]."
        y "Were you influenced by seeing everyone's writing styles yesterday?"
        mc "I guess you could say that..."
        y 1m "I was also a bit surprised by how differently everyone writes."
        y "So I respect you for trying new things."
        jump ch2_y_shared

label ch2_y_good:
    #likes this one more than yesterday
    if y_poemappeal[0] < 1:
        y 1a "Let's see what you've written for today."
        y "..."
        y 2e "......"
        "Yuri stares at the poem with a surprised expression on her face."
        mc "Do you...like it?"
        y "[player]..."
        y "...How did you pick up on this so quickly?"
        label ch2_y_good_shared:
            y 2v "Just yesterday, I was telling you the kind of techniques worth practicing..."
            mc "Maybe that's why..."
            mc "You did a good job explaining."
            mc "I really wanted to try giving it more imagery."
            show yuri 4b at t11 zorder 2
            "Yuri visibly swallows."
            "Even her hands appear sweaty."
            y "I'm not...used to this..."
            mc "Used to what?"
            y 3o "I don't know...!"
            mc "It's fine, take your time..."
            show yuri 3l at t11
            "Yuri breathes and collects her thoughts."
            "I know that Yuri likes to think before she speaks, so I offer that patience to her."
            y 4a "Yeah..."
            y "Just...being appreciated like this...I guess."
            y "It probably sounds really stupid..."
            y "But seeing someone motivated by my writing..."
            y "It just makes me..."
            y "Really happy..."
            mc "Are you saying you've never shared your writing before?"
            "Yuri nods."
            mc "Really? I don't believe it."
            y "I really only write for myself..."
            y "And besides..."
            y 3w "...People would just laugh at me!"
            mc "Do you really think that...?"
            "Again, Yuri nods."
            mc "Huh..."
            mc "Even your close friends?"
            y 2v "..."
            "Yuri doesn't respond to that."
            "I wonder why..."
            mc "Anyway..."
            mc "Do you want to share the poem you wrote today?"
            y "...Yeah."
            y 3t "I do!"
            y "If it's with you..."
            return
    #likes both poems a lot
    else:
        y 1a "Let's see what you've written for today."
        y "..."
        y 2e "......"
        "Yuri stares at the poem with a surprised expression on her face."
        mc "Do you...like it?"
        y "[player]..."
        y "This one might even be better than yesterday's..."
        y "...How did you even pick up on this so quickly?"
        jump ch2_y_good_shared

label ch3_y_bad:
    if y_poemappeal[0] < 0 and y_poemappeal[1] < 0:
        label ch3_y_bad12_shared:
            y 4b "..."
            "Yuri doesn't look too enthusiastic about spending time with me..."
            "I guess if she changes her mind, she'll come to me."
            "But I should leave her be for now."
            $ skip_poem = True
            return
    elif y_poemappeal[1] < 0 or y_poemappeal[0] < 0:
        y 1i "..."
        y "...I see."
        y "I think you're improving at writing in general, [player]."
        y 2i "But I can't help but feel a little bit foolish."
        mc "Eh? What for?"
        y "Just..."
        y "I feel like I kept trying to offer advice..."
        y "When it should have been clear to me that you prefer a different writing style."
        y 3w "I probably just sounded arrogant!"
        y "I'm so stupid..."
        mc "Yuri, that's a little--"
        y 4b "No..."
        y "You don't understand."
        y "I spent so much time worrying about what's better and what's worse."
        y "Not just with you..."
        y "With Natsuki, and Sayori..."
        y "It's obvious now why nobody has fun when talking to me..."
        y "And because of that..."
        y 4c "...I'll just keep my mouth shut about your poem!"
        mc "..."
        "Yuri buries her head into her arms on her desk."
        "That's not the first time I've seen her do that."
        mc "I don't think it's ever as bad as you make it sound in your head..."
        y "..."
        mc "I think if people really didn't like talking to you..."
        mc "Then it would be a lot more obvious."
        mc "I know that you like to read deeply into things."
        mc "But some things are just worth taking at face value."
        y 4b "I just..."
        y "I've gotten so used to it..."
        y "...That it's hard for me to comprehend any other possibility."
        mc "Gotten used to what?"
        mc "Reading deeply into things?"
        y "Being disliked."
        mc "Yuri..."
        y 2v "What...what am I saying?"
        y "I'm sorry..."
        y "I never meant to bring this up..."
        "Yuri turns away from me."
        y 4b "You should go..."
        mc "Eh...?"
        y "Please..."
        y "Please don't look at me right now."
        y "I want to do some thinking..."
        mc "Are you sure...?"
        "Yuri nods."
        mc "Alright..."
        "I leave Yuri be."
        "Comforting or reassuring her is nearly impossible as it is."
        "So when she wants to be alone, I think anything I say could only make things worse."
        "I feel bad, but thankfully she doesn't take it out on me..."
        "I'll wait until she's feeling a little bit better."
        $ skip_poem = True
        return
    else:
        y 1a "..."
        y "...Ah."
        y "Decided to try something different today?"
        mc "I guess so."
        mc "Is that good, or bad?"
        y 2g "Well, neither."
        y "I have my preferences."
        y "But it would be unfair of me to call something good or bad based on that."
        label ch3_y_shared:
            y 1f "As always, I believe what's most important is exploring and discovering yourself."
            mc "That's comforting."
            mc "I'm kind of afraid of disappointing you in some way or another."
            y 2t "Eh...?"
            y "Why me...?"
            mc "Well, you're always sophisticated with your writing and have the most advice to share."
            y 4a "Is that so...?"
            y "..."
            "Yuri thinks for a good minute."
            y 4c "...That must be terrible."
            mc "Eh?"
            y "For me to have become someone whose opinion is fearsome..."
            y "How unlikable of me..."
            mc "Yuri..."
            mc "It's not as bad as you're making it sound in your head."
            mc "I just meant that I respect your opinion."
            y 2v "I see..."
            y "I'm sorry that I always overthink and come to those sorts of conclusions..."
            y "I'm just...a little too used to it."
            mc "Overthinking?"
            y "Being disliked."
            mc "Yuri..."
            y 3w "What...what am I saying?"
            y "I'm sorry, I didn't mean to bring that up..."
            y "Let's move on..."
            mc "Alright..."
            mc "Do you want to share your poem now?"
            y 2i "Okay..."
            y "Here."
            return


label ch3_y_med:
    if y_poemappeal[0] < 0 and y_poemappeal[1] < 0:
        jump ch3_y_bad12_shared
    elif y_poemappeal[0] < 1 or y_poemappeal[1] < 1:
        y "..."
        y 1a "Well done, [player]."
        y "You've definitely improved your writing over the course of these few days."
        y "Has my advice been helpful to you?"
        mc "Yeah... Definitely."
        y 2m "I'm glad..."
        y "Sharing our writing like this..."
        y 2a "It's a lot more fun and rewarding than I anticipated."
        y "I need to remember to thank Monika..."
        y "I think we all felt a little awkward at first."
        y 1a "But now it seems like everyone is enjoying sharing their writing and seeing what others think."
        mc "I guess I can't really disagree."
        mc "I was afraid this whole thing would be a chore..."
        "But it's a great way for me to spend some personal time with all the girls in the club."
        mc "But it's been fun getting to know everyone and their writing."
        mc "And I guess doing some writing myself..."
        y 2a "Well..."
        y "Have you learned anything about yourself, [player]?"
        mc "Eh?"
        y 2i "Well, you know how I like to say that writing is a very personal way to get in touch with yourself..."
        y 1a "In the end, it doesn't matter if you're a good writer, or a bad writer."
        y "And even my opinions are just opinions...you know?"
        jump ch3_y_shared
    else:
        y 1e "..."
        y "...Ah."
        y "Decided to try something different today?"
        mc "I guess so."
        mc "Is that good, or bad?"
        y 2i "Well, neither."
        y "I have my preferences."
        y "But it would be unfair of me to call something good or bad based on that."
        jump ch3_y_shared

label ch3_y_good:
    if y_poemappeal[0] < 0 and y_poemappeal[1] < 0:
        jump ch3_y_bad12_shared
    if y_poemappeal[1] < 1:
        y "..."
        y 2u "[player]..."
        y "...This is wonderful."
        y "I can feel the emotion that you poured into it."
        y "Is this the result of trying what I suggested yesterday?"
        mc "Yeah, I guess so..."
        mc "You did a good job explaining."
        mc "I really wanted to try giving it more feeling."
        show yuri 4b at t11 zorder 2
        "Yuri visibly swallows."
        "Even her hands appear sweaty."
        play music t9 fadeout 1.0
        y "I'm not...used to this..."
        mc "Used to what?"
        y 3o "I don't know...!"
        mc "It's fine, take your time..."
        "Yuri breathes and collects her thoughts."
        "I know that Yuri likes to think before she speaks, so I offer that patience to her."
        y 4a "Yeah..."
        y "Just...being appreciated like this...I guess."
        y "It probably sounds really stupid..."
        y "But seeing someone motivated by my writing..."
        y "It just makes me..."
        y "Really happy..."
        mc "Are you saying you've never shared your writing before?"
        "Yuri nods."
        mc "Really? I don't believe it."
        y "I really only write for myself..."
        y "And besides..."
        y 3w "...People would just laugh at me!"
        mc "Do you really think that...?"
        "Again, Yuri nods."
        mc "Huh..."
        mc "Even your close friends?"
        y 2v "..."
        "For some reason, Yuri doesn't respond."
        mc "Yuri...?"
        label ch3_y_good_shared:
            if not renpy.music.get_playing(channel='music') == audio.t9:
                play music t9 fadeout 1.0
            "Yuri smiles sadly."
            y 1u "[player], during lunchtime, I eat by myself."
            y "Did you know that?"
            y "It's a great time to find a quiet spot and do some reading."
            y "In fact..."
            y 2s "I always have some books with me."
            y "You could say I really enjoy reading..."
            y "...Well, that's one way to put it, anyway..."
            y "But..."
            y "Books are so full of amazing and inspiring people."
            y "People you want to fall in love with."
            y "Or people you just know would make a really good friend."
            y 1m "Cheerful people, who always put a smile on your face..."
            y "Or deep thinkers, and problem solvers, who discover the mysteries of life."
            y "So when you look at it that way..."
            y "I'm surrounded by friends every day..."
            y "...You know?"
            y 2s "And those friends don't laugh at me..."
            y "They don't tease me for spacing out all the time..."
            y "They don't make fun of my body type..."
            y "And..."
            y 3v "...And they don't hate me for acting like a know-it-all!"
            mc "People...say that about you?"
            y "I'm not a know-it-all, [player]!"
            y "It's the opposite. I don't know anything!"
            y 4b "I don't know how to talk to people."
            y "I don't know how to make people see me as normal."
            y "I don't even know how to make myself happy!"
            y "I have all these feelings..."
            y "And all I can do with them is read, and write..."
            y "But it wasn't until now..."
            y 2s "That I started sharing it with you..."
            y "...That I really understood what was missing all this time."
            mc "But I haven't really done anything..."
            y "No..."
            y "That's wrong."
            y "Just being patient and respectful..."
            y 3u "That's really...important to me."
            y "I know I'm a difficult person, [player]..."
            y "I speak too slowly..."
            y "I second-guess myself all the time..."
            y "I read too deeply into things..."
            y "But every time..."
            y "You've always treated me just like anyone else."
            y "It's so rare that I feel comfortable with myself when I talk to others..."
            y "But that's why every time I talk to you..."
            y 2s "...I just feel really happy."
            mc "I see..."
            mc "Well, I treat you how you deserve to be treated, Yuri."
            mc "And if other people don't see it that way, then screw them."
            mc "I mean, I joined this club hoping I would make friends."
            mc "And I would say I've had at least one success."
            mc "Wouldn't you?"
            y 4b "U-Um..."
            y "If you put it that way..."
            y "...Yeah..."
            y 4e "We really are friends now, aren't we?"
            "Yuri puts her head in her hands."
            "But this time, she's smiling as she does it."
            mc "Do you want to show me your poem?"
            y 3s "Yeah."
            y "I do!"
            y "Let me get it for you..."
        return
    else:
        y "..."
        y "[player]."
        y 2s "Your writing has only improved in these last few days."
        y "Every poem you've shown me has been nothing short of spectacular."
        y "I can really feel the emotions..."
        y 2m "I'm a little envious, even..."
        y "I don't think it ever came to me this naturally."
        mc "Yuri, that's the wrong way to put it."
        mc "This never did come naturally to me."
        mc "But I've been able to improve so much thanks to you."
        mc "You're really the example I was chasing after."
        y 3u "I-Is that so...?"
        "Yuri gently smiles to herself."
        y "This feeling..."
        y "I'm so glad...I got the chance to share my writing."
        y 4e "I never thought it would feel like this."
        mc "I remember you mentioning that yesterday."
        mc "I can't believe that you're so good at something and you've never even shared it with anyone."
        mc "It's kind of a shame."
        y 2u "Maybe, but..."
        y "It's not like I really...had a choice."
        mc "What do you mean...?"
        y "Well..."
        jump ch3_y_good_shared


label ch1_m_start:
    m 1b "Hi, [player]!"
    m "Having a good time so far?"
    mc "Ah...yeah."
    m 1k "Good! Glad to hear it!"
    m 4a "By the way, since you're new and everything..."
    m "If you ever have any suggestions for the club, like new activities, or things we can do better..."
    m 4b "I'm always listening!"
    m "Don't be afraid to bring things up, okay?"
    show monika 4a
    mc "Alright...I'll keep that in mind."
    "Of course I'll be afraid to bring things up."
    "I'm much better off just going with the flow until I'm more settled in."
    m 1a "Anyway..."
    m "Want to share your poem with me?"
    mc "It's kind of embarrassing, but I guess I have to."
    m 5a "Ahahaha!"
    m "Don't worry, [player]!"
    m "We're all a little embarrassed today, you know?"
    m "But it's that sort of barrier that we'll all learn to get past soon."
    mc "Yeah, that's true."
    "I hand Monika my poem."
    m 2a "...Mhm!"
    $ nextscene = "m_" + poemwinner[0] + "_" + str(eval(poemwinner[0][0] + "_appeal"))
    call expression nextscene

    mc "I'm sure I'll end up trying different things a lot."
    mc "It could take a while before I feel comfortable doing this."
    m 1k "That's okay!"
    m 1b "I'd love to see you try new things."
    m "That's the best way to find the kind of style that suits you."
    m 3e "Everyone else might be a little bit biased toward their own kinds of styles..."
    m 3a "But I'll always help you find what suits you the most!"
    m "So don't force yourself to write the way everyone else wants you to write."
    m "It's not like you have to worry about impressing them or anything."
    m 5 "Ahaha!"
    mc "Ahaha..."
    m 1a "Anyway, do you want to read my poem now?"
    m 1e "Don't worry, I'm not very good..."
    mc "You sound pretty confident for someone who claims to not be very good."
    m 1j "Well...that's 'cause I have to sound confident."
    m 1b "That doesn't mean I always feel that way, you know?"
    show monika 1a
    mc "I see..."
    mc "Well, let's read it, then."
    return

label ch2_m_start:
    m 1b "Hi again, [player]!"
    m "How's the writing going?"
    mc "Alright, I guess..."
    m 2k "I'll take that."
    m 2b "As long as it's not going bad!"
    m 2a "I'm happy that you're applying yourself."
    m "Maybe soon you'll come up with a masterpiece!"
    mc "Ahaha, I wouldn't count on that..."
    m 2a "You never know!"
    m "Want to share what you wrote for today?"
    mc "Sure... Here you go."
    "I give my poem to Monika."
    m "..."
    m "...Alright!"
    $ nextscene = "m_" + poemwinner[1] + "_" + str(eval(poemwinner[1][0] + "_appeal"))
    call expression nextscene

    m 1a "But anyway..."
    m "You want to read my poem now?"
    m "I like the way this one turned out, so I hope you do too~"
    mc "Alright, let's take a look."
    return

label ch3_m_start:
    m 2a "Hi [player]~"
    m "Have you thought about what you want to submit to perform at the festival?"
    mc "Well..."
    "Being in this club is one thing, but performing in front of a bunch of people..."
    mc "...I'll have to give it some more thought."
    m 2b "Okay, no pressure!"
    m "But whatever you do, I'm sure it'll turn out great."
    m "It would also make me happy to see."
    m 2k "Ahaha!"
    m 1a "Anyway, let's take a look at today's poem!"
    mc "Sure..."
    "I let Monika take the poem I'm holding in my hands."
    m "..."
    $ nextscene = "m_" + poemwinner[2] + "_" + str(eval(poemwinner[2][0] + "_appeal"))
    call expression nextscene

    m 1a "Anyway...!"
    m "I'll share my poem with you now, alright?"
    mc "Er..."
    mc "Alright..."
    return



label m_natsuki_1:
    m 2b "I like it, [player]!"
    mc "Really...?"
    m 2e "It's a lot cuter than I expected."
    m 2k "Ahahaha!"
    mc "Oh jeez..."
    m 1b "No, no!"
    m "It kind of makes me think of something Natsuki would write."
    m "And she's a good writer, too."
    m 5a "So take that as a compliment!"
    mc "Ahaha..."
    mc "If you say so."
    m "Yep!"
    m 1a "By any chance have you read anything by Shel Silverstein?"
    mc "Eh?"
    mc "Maybe a long time ago..."
    m "He's famous for telling all kinds of stories in just a few simple words."
    m "His poems can be funny, endearing, or even sad..."
    m 3d "And sometimes they're only a few lines long."
    m "They might even feel like they're written for kids, but if you think about them..."
    m "They can express views of the world that would apply to anybody."
    mc "I see..."
    mc "So you're saying that Natsuki is kind of like that?"
    m 2a "Sort of."
    m "Maybe she's not an expert..."
    m "But you probably won't find much filler in her poems."
    m "They might be easy to write, but they're super challenging to get the meaning through."
    m 2b "So I can see why it would be your kind of poem to explore!"
    return

label m_sayori_1:
    m 2a "I like this one!"
    m "It makes me think of something Sayori would like."
    mc "Is that so?"
    m 2d "You and Sayori are really good friends, right?"
    m "I wouldn't be surprised if you had those sorts of things in common."
    mc "Ah, well..."
    mc "We may be good friends, but Sayori and I are actually really different."
    m "Hmm..."
    m "Well, that may be the case."
    m 3a "But maybe there are also some similarities that you wouldn't expect."
    m "The way she talks about you..."
    m "It sounds like the two of you really care about each other's well-being."
    m "Even if you show it in different ways, it ends up being more similar than you'd think."
    m 1a "So I think that's the kind of vibe I get when reading your poem."
    mc "Hmm..."
    mc "You sure you're not reading into it too much?"
    m 5 "Ahaha! I could be!"
    m "Oh gosh, I sound like Yuri..."
    m 2a "...But in any case, Sayori's writing has kind of a gentle feel to it."
    m "I can tell that she likes exploring with emotions, like happiness and sadness."
    m "Who knew that someone so happy would enjoy sad things, too?"
    mc "Yeah... That's totally unexpected."
    m 2j "Well, to each their own~"
    m 2a "And you shouldn't be afraid to experiment a little bit, either."
    return

label m_yuri_1:
    m 1a "Great job, [player]!"
    m "I was going 'Ooh' in my head while reading it."
    m 1j "It's really metaphorical!"
    m 1a "I'm not sure why, but I didn't expect you to go for something so deep."
    m 3b "I guess I underestimated you!"
    mc "It's easiest for me to keep everyone's expectations low."
    mc "That way, it always counts when I put in some effort."
    m 5a "Ahaha! That's not very fair!"
    m "Well, I guess it worked, anyway."
    m 2a "You know that Yuri likes this kind of writing, right?"
    m "Writing that's full of imagery and symbolism."
    m 2d "Unlike Sayori, who likes using simple and direct words to describe happiness and sadness..."
    m "Yuri likes it when readers are left to derive their own meaning out of it."
    m 4d "It's very challenging to write like that effectively."
    m "Both allowing people to get something out of it just by feel..."
    m "Or letting them deeply analyze all of the nuances."
    m "It can take years of practice, which I'm assuming Yuri has at this point."
    m 1e "I never really asked, though..."
    mc "I'm sure I'm nowhere near her level yet."
    m 2b "Don't worry so much about that!"
    m "You do your own thing."
    m "Just keep exploring, and learn by trying new things!"
    return

label m_natsuki_2:
    m 1j "It's pretty good~"
    m 1a "You've been spending some time with Natsuki, haven't you?"
    m "You must like her writing style."
    mc "Ah, yeah..."
    mc "I think it's a neat way to tell a story."
    m 2a "Mhm. I don't disagree."
    m "Natsuki's poems may be cute, but they're also meaningful."
    m "I can see why you'd be into the style."
    m "I guess that means you're not as much a fan of Yuri's poems, then?"
    mc "Ah-- I wouldn't say that..."
    mc "I kind of like everyone's poems."
    m 2d "That's true, but I'm sure you like some more than others, right?"
    m "Like Yuri's use of complex words and symbolism..."
    m "Or Sayori's way of expressing happiness or sadness in a more direct way."
    m 2a "You must have some kind of preference, don't you?"
    m 4l "Ah, not that it's a contest or anything!"
    m 4a "I was just curious, that's all."
    return

label m_sayori_2:
    m 1j "It's pretty good~"
    m 1a "It makes me think of Sayori, like the other one that you wrote."
    m 4b "You two are like the dynamic duo!"
    mc "Ahaha... That's kind of exaggerating it."
    m 2a "Yeah, probably."
    m "But you do spend a lot of time with her even in this club, don't you?"
    m 2j "Then again, I don't blame you for being a little shy~"
    mc "I-I'm not shy, it's just..."
    m 5 "Ahaha! I'm just teasing."
    m "I know it takes a bit of time to make friends with everyone."
    m 2d "But Yuri and Natsuki are super interesting people, so don't be afraid to give them their share of time!"
    m "And you can talk to me every now and then too..."
    m 1e "I'm not, like, unapproachable or anything, am I?"
    mc "Ah, no, it's nothing like that..."
    mc "I'm just still getting used to being here, that's all."
    m 1a "Yeah..."
    m 1l "I'm sorry if I was putting pressure on you or something!"
    m "I really didn't mean it like that."
    mc "No, don't worry."
    mc "I get what you're saying."
    m 1a "Well, alright~"
    return

label m_yuri_2:
    m 2b "This one's good!"
    m "It feels like you're not only getting more comfortable with your style..."
    m "But the imagery is better than the last one I read!"
    m 2a "Just wondering, but have you been finding inspiration in Yuri's writing style?"
    mc "Hmm..."
    mc "I guess so."
    mc "You can't deny that she's talented."
    m 4k "Yeah, totally!"
    m 4a "I think her poems are the most..."
    m "...Romantic."
    m 1a "That's the best way to describe it."
    m 1d "She's like a totally different person when she picks up a pen..."
    mc "I noticed that, too."
    mc "Or when she's talking about literature, it's like a light turns on inside her."
    m 2a "Mhm!"
    m "Sadly, it's hard to get much personal conversation out of her..."
    m 2m "Trust me, I've tried..."
    m "Who knows what goes on in that head of hers?"
    mc "I hope you don't mean that in a bad way."
    m 1g "No, of course not!"
    m "I just meant that I wish she didn't keep so much to herself..."
    m 1e "But still, defending her like that..."
    m 5 "You must be pretty into her..."
    mc "Eh?!"
    mc "You...completely misunderstood!"
    m "Ahaha! Calm down, I'm kidding!"
    m 2a "Besides, I'm pretty sure she's already got a boyfriend..."
    mc "Wait, really?"
    m 2k "Yeah. A fictional one, anyway."
    "Monika kind of whispers that last part to me."
    m 5 "It's just a hunch, but..."
    mc "...Well, there's not really anything wrong with that!"
    m 1n "Oh, well I know...!"
    m "I was just saying~"
    return

label m_natsuki_3:
    m 2j "Sticking with the Natsuki style once more, I see~"
    m 2d "Hmm..."
    m "You really like Natsuki, don't you?"
    mc "Eh? That's--"
    m 5 "Oh, come on, [player]."
    m "It's awfully suspicious, you know?"
    m "Spending time with her in the clubroom every day..."
    m "Pretending to like the manga that she's into..."
    mc "Y-You know how Natsuki is...!"
    mc "If I don't indulge her, she'll end up hating me."
    m 2e "Eh?"
    m 2a "No, I think you're misunderstanding, [player]."
    m "It's not like Natsuki just hates anyone who doesn't give her what she wants."
    m 2d "Yeah, she's assertive, but she's not that selfish..."
    m "In fact, I think you're the only one who's indulged her as much as you have."
    mc "Is that so..."
    "I kind of knew that, but I just didn't want to admit it."
    m "So, I just need to ask one thing of you..."
    m 1e "...Be careful. Please?"
    m "Natsuki is kind of unpredictable."
    m "A lot of times, she doesn't even know what she wants."
    m 1i "After all, she's the youngest one here."
    m "She might not know how to handle her own feelings properly."
    m "What I'm saying is..."
    m 1m "If something bad happens, then it could end up damaging the club, too..."
    m 5 "And you wouldn't do that to me...right?"
    mc "That's--"
    "I'm not sure how to respond to Monika."
    "While I care about her and the club, it's also kind of unfair to bring that up."
    m "Well...you're smart."
    m "I'm sure you'll do the right thing."
    "Monika smiles sweetly."
    return

label m_sayori_3:
    m 1k "Ahaha."
    m "It's kind of funny..."
    mc "How so?"
    m 1a "No, not the poem..."
    m 2a "I mean, it's funny how your poems and Sayori's poems have been getting more and more similar to each other every day."
    m "I'm surprised you're so in sync with her."
    m 2d "Then again, you've been spending a lot of time together lately, haven't you?"
    mc "Ah, I guess you could say that..."
    mc "Although we kind of grew up as best friends, I haven't been seeing as much of her this past year..."
    mc "But since I joined the club, we've been spending a lot of time together again."
    m 1a "I see, I see~"
    m "That reminds me..."
    m "About how Sayori's been a little bit off today..."
    mc "Yeah? Did she tell you something?"
    m 1n "Ah..."
    m "Well..."
    m 2l "[player], you haven't been flirting with her, have you?"
    mc "O-Of course not!"
    mc "I've been treating her like I always do."
    m 2a "Alright."
    m 5 "Just making sure~"
    m "I know how much you care about her..."
    m "It would be terrible if something bad happened to her, so keep an eye on her."
    m 2d "Sayori's been acting so much happier ever since you joined the club."
    m "What could have happened all of a sudden...?"
    mc "..."
    m 1l "...Well, never mind."
    m "This really isn't the time to be talking about this..."
    return

label m_yuri_3:
    m 2e "Your style's gotten so refined, [player]."
    m "Yuri's been teaching you a lot of things, hasn't she?"
    mc "Well--"
    mc "I guess so."
    m 2a "Yeah... I've been noticing how much time you spend with her."
    m 2d "I think I've heard her say more words these past couple days than she's talked in the whole year."
    m "Not sure how you did it, but that's pretty impressive..."
    mc "Well, she just needs some patience and a way to talk about all the things in her head, I guess..."
    mc "I'm still getting the hang of it, myself."
    m 2a "Hm..."
    m "You're certainly putting in a lot of effort."
    m 2e "You must really like her."
    mc "Eh? That's--"
    m 5 "Ahaha!"
    m "It's awfully suspicious, you know?"
    m "Spending time with her in the clubroom every day..."
    m "Reading that edgy novel with her..."
    mc "Well--!"
    mc "I just...feel bad that she has a hard time socializing."
    mc "It makes me want to make sure she doesn't spend all her time alone."
    mc "Besides, the novel isn't too bad either, you know..."
    m 1k "Alright, alright~"
    m "I get you."
    m 1a "Just...be careful, alright?"
    m "I know that Yuri isn't used to opening herself up..."
    m 2d "So if something bad happens while she's vulnerable..."
    m "Then it could be really hard for her."
    m 2i "Her books aren't a total escape from reality."
    m "They're just a bandage."
    mc "You say that like I'm going to hurt her..."
    m 1l "Sorry, I didn't really mean that~"
    m "If anything, she might accidentally hurt herself."
    return
