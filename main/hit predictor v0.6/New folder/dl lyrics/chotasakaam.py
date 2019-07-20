keywords = ['you','a','me','in','it','my','on','all','your','be','for','know','just','like','is','with',"don't",'this','when','up','we','what','got','no','can','love','out','go','one','down',"can't",'take','say','how',"you're",'back',"ain't",'wanna','some','too','night','good','around',"we're","let's","em'",'tonight','of','at','&','that','but','get','if','now','see','make','never','was','way','right',"that's",'about','real','stop',"didn't",'do','time','let','want','come','feel','need','tell','baby','gonna','girl','heart',"you'll",'think','give','keep','off',"won't","there's",'really',"what's","you've",'ride',"i'm",'shit','ya','oh','gotta','hit','bitch','crazy',"'cause'",'fuck','yeah',"i'd","i've"]

song = """Oh!\\n\\nAy baby weh you ah deal with?\\nWe come through a lot of things you know?\\nWo wahamum to you?\\nMe make one little mistake you wan dun us?\\n\\n[Verse 1]\\nIf I had you back in my world\\nI would prove that I could be a better girl\\nOh', ' oh', oh,If you let me back in,nI would sho'nuff never never let you go again (hey baby)\\nI was so foolish to ever leave your side\\nSearching for what was right before my eyes\\nIt was me who didn't realize\\n'til it was gone but now I know I need you in my life\\n\\nBoy I need you bad as my heartbeat (bad like the food I eat)\\nBad as the air I breath (baby I want you bad)\\nI need you bad I can't take this pain (bad I can't take this pain)\\nBoy I'm about to go insane (baby I need you bad)\\nI need you\\nI need you\\nWhat I gotta do (baby I want you bad)\\nI need you\\nI need you\\nDo it all for you (baby I need you bad)\\n\\n[Verse 2]\\nBaby there's nothing I wouldn't do\\nTo get back what we had when love was true (oh oh oh)\\nNo lie I'd give up all I got\\nJust so I could get back in my spot (Oh)\\n\\n[Chorus]\\n\\n[Hook]\\nWhen you want him so bad and\\nYou gotta get him back say", " oh oh oh oh (oh oh oh oh)\\nCause it won't get no better\\nTwo you are together say", " oh oh oh oh (oh oh oh oh)\\nIf you believe in love and\\nYou can't give him up say", ' oh oh oh oh (oh oh oh oh)\\nIf there\'s nothing you won\'t do to get\\nBack with your boo say Oh\\n\\n"""
song = """I'm thinking about you
There's nothing left to do
I'm thinking about you
There's nothing left to do
Thinking about ya
Thinking about ya
We must have been stone crazy
When we thought we were just friends
'Cause I miss you baby
And I've got those feelings again
I guess I'm all confused about you
Yes, I am, baby
I feel so in love, oh baby
What can I do?
I've been thinking about ya ('bout ya)
I've been thinking about ya ('bout ya)
I've been thinking about ya ('bout ya)
I've been thinking about ya ('bout ya)
I've been thinking about ya ('bout ya)
I've been thinking about ya ('bout ya)
I've been thinking about ya ('bout ya)
I've been thinking about ya ('bout ya)
Suddenly we're strangers
I watch you walking away
She was my one temptation
Though I did not want her to stay
What good is being here without you
I want to know
I feel so in love
Oh baby (oh baby)
I've been thinking about ya ('bout ya)
I've been thinking about ya ('bout ya)
I've been thinking about ya ('baby)
I've been thinking about ya ('bout ya)
I've been thinking about ya ('bout ya)
I've been thinking about ya ('bout ya)
I've been thinking about ya ('bout ya)
I've been thinking about ya ('bout ya)
Deep down I'm still confused about you
Oh, yes I am baby
I feel so in love, oh baby
(What can I do) what can I do?
About ya
I've been thinking about ya (baby)
I've been thinking about ya ('bout ya)
I've been thinking about ya ('bout ya)
(All I do) thinking about ya (baby)
Thinking about ya (baby)
All I do yea, all I do is think about you
I'm thinking about you
There's nothing left to do
I'm thinking about you
There's nothing left to do
I'm thinking about you
There's nothing left to do
I'm thinking about you
There's nothing left to do
I'm thinking about you
There's nothing left to do
I'm thinking about you
There's nothing left to do
I'm thinking about you
There's nothing left to do
I'm thinking about you
There's nothing left to do"""
song = song.replace("\\n","").strip().split()

print(len(set(song).intersection(set(keywords))))