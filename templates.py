tweets = ["""
Thanks so much for having us, we are <BANDNAME>. Be sure to check out our merch table; we've got our new album <ALBUMNAME>.
""",
"""
It's great to be here, we are <BANDNAME>. Don't forget to tip your bartenders, and check out our new album <ALBUMNAME>, now on Spotify.
""",
]

sentence_1 = ["Thanks so much for having us, we are <BANDNAME>].",
              "It's great to be here, we are <BANDNAME>!"]

sentence_2 = ["Be sure to check out our merch table; we've got our new album <ALBUMNAME>.",
              "Don't forget to tip your bartenders, and check out our new album <ALBUMNAME>, now on Spotify."
              "Stop by our merch table to pick up <MERCH>."]

bandnames = {"<NAME> and the <NOUNS>":2,
             "<ADJ> <NOUN>":10,
             "<NOUN>":10,
             "<ADJ> <ADJ> <NOUN>":7,
             "The <ADJ> <NOUN> Experience":1}