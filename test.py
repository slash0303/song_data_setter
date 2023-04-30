import eyed3

song = eyed3.load("Egzod - Rise Up (ft. Veronica Bravo & M.I.M.E) [NCS Release].mp3")

song = song.tag

song.artist = "hello"

song.save(version=eyed3.id3.ID3_V2_3)