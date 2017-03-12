.PHONY: build clean build-addon build-movie build-serie build-anime build-subs

build-movie:
	#Directory, File: Default Test (BlueRay)
	mkdir -p ~/galung-project/test-library/'Sisters.And.Brothers.2011.1080p.BluRay.H264.AAC-RARBG'
	touch ~/galung-project/test-library/'Sisters.And.Brothers.2011.1080p.BluRay.H264.AAC-RARBG'/'Sisters.And.Brothers.2011.1080p.BluRay.H264.AAC-RARBG.mkv'
	
	#Directory, File: Default Test
	mkdir -p ~/galung-project/test-library/'Innocent.Bystanders.1972.BRRip.XviD.MP3-RARBG'
	touch ~/galung-project/test-library/'Innocent.Bystanders.1972.BRRip.XviD.MP3-RARBG'/'Innocent.Bystanders.1972.BRRip.XviD.MP3-RARBG.mkv'
	
	#Directory, File: Default Test (Dates)
	mkdir -p ~/galung-project/test-library/'Meet.Him.And.Die.1976.1080p.BluRay.H264.AAC-RARBG'
	touch ~/galung-project/test-library/'Meet.Him.And.Die.1976.1080p.BluRay.H264.AAC-RARBG'/'Meet.Him.And.Die.1976.1080p.BluRay.H264.AAC-RARBG.mkv'
	
	#Directory, Subdirectory, File: Default Test (Mp3)
	mkdir -p ~/galung-project/test-library/'Littlerock.2010.BRRip.XviD.MP3-RARBG'
	mkdir -p ~/galung-project/test-library/'Littlerock.2010.BRRip.XviD.MP3-RARBG'/'Littlerock.2010(subtitle)'
	touch ~/galung-project/test-library/'Littlerock.2010.BRRip.XviD.MP3-RARBG'/'Littlerock.2010(subtitle)'/'Littlerock.2010(english).srt'
	touch ~/galung-project/test-library/'Littlerock.2010.BRRip.XviD.MP3-RARBG'/'Littlerock.2010.BRRip.XviD.MP3-RARBG.mkv'
	
	#Directory, Subdirectory, File: Default Test (EXTENDED.CUT,BRRip, XviD)
	mkdir -p ~/galung-project/test-library/'Were.the.Millers.2013.EXTENDED.CUT.BRRip.XviD.MP3-RARBG'
	mkdir -p ~/galung-project/test-library/'Were.the.Millers.2013.EXTENDED.CUT.BRRip.XviD.MP3-RARBG'/'Were.the.Millers.2013.(subtitle)'
	touch ~/galung-project/test-library/'Were.the.Millers.2013.EXTENDED.CUT.BRRip.XviD.MP3-RARBG'/'Were.the.Millers.2013.(subtitle)'/'Were.the.Millers.2013(english).srt'
	touch ~/galung-project/test-library/'Were.the.Millers.2013.EXTENDED.CUT.BRRip.XviD.MP3-RARBG'/'System.nfo'
	touch ~/galung-project/test-library/'Were.the.Millers.2013.EXTENDED.CUT.BRRip.XviD.MP3-RARBG'/'Readme.txt'
	touch ~/galung-project/test-library/'Were.the.Millers.2013.EXTENDED.CUT.BRRip.XviD.MP3-RARBG'/'RARBG.com'
	touch ~/galung-project/test-library/'Were.the.Millers.2013.EXTENDED.CUT.BRRip.XviD.MP3-RARBG'/'Were.the.Millers.2013.EXTENDED.CUT.BRRip.XviD.MP3-RARBG.mkv'

	#Directory, File: Unkonw Movie
	#mkdir -p ~/galung-project/test-library/'Lost.Kiddo.The.Movie.(1080p).(2015)'
	#touch ~/galung-project/test-library/'Lost.Kiddo.The.Movie.(1080p).(2015)'/'Lost.Kiddo.The.Movie.(1080p).(2015).mkv'

build-serie:
	#Directory, File: Default Test
	mkdir -p ~/galung-project/test-library/'Game Of Thrones'
	mkdir -p ~/galung-project/test-library/'WestWorld'
	
	mkdir -p ~/galung-project/test-library/'Game.of.Thrones.S06.1080p.BluRay.x264-ROVERS[rartv]'
	touch ~/galung-project/test-library/'Game.of.Thrones.S06.1080p.BluRay.x264-ROVERS[rartv]'/'Game.of.Thrones.S06E01.1080p.BluRay.x264-ROVERS[rartv].mkv'
	touch ~/galung-project/test-library/'Game.of.Thrones.S06.1080p.BluRay.x264-ROVERS[rartv]'/'Game.of.Thrones.S06E02.1080p.BluRay.x264-ROVERS[rartv].mkv'
	touch ~/galung-project/test-library/'Game.of.Thrones.S06.1080p.BluRay.x264-ROVERS[rartv]'/'Game.of.Thrones.S06E03.1080p.BluRay.x264-ROVERS[rartv].mkv'
	touch ~/galung-project/test-library/'Game.of.Thrones.S06.1080p.BluRay.x264-ROVERS[rartv]'/'system.nfo'
	touch ~/galung-project/test-library/'Game.of.Thrones.S06.1080p.BluRay.x264-ROVERS[rartv]'/'system.txt'
	touch ~/galung-project/test-library/'Game.of.Thrones.S06.1080p.BluRay.x264-ROVERS[rartv]'/'system.com'
	
	#Directory, Subdirectory, File: Default Test
	#mkdir -p ~/galung-project/test-library/'Game.of.Thrones-season2'/
	mkdir -p ~/galung-project/test-library/'Game.of.Thrones.season-3'/
	mkdir -p ~/galung-project/test-library/'Game.of.Thrones [Season 1]'/
	mkdir -p ~/galung-project/test-library/'Game.of.Thrones [Season 1]'/'Game.Of.Thrones.S01E01.1080p.BluRay.x265-PODO[rartv]'/
	touch ~/galung-project/test-library/'Game.of.Thrones [Season 1]'/'Game.Of.Thrones.S01E01.1080p.BluRay.x265-PODO[rartv]'/'Game.Of.Thrones.S01E01.1080p.mkv'
	mkdir -p ~/galung-project/test-library/'Game.of.Thrones [Season 1]'/'Game.Of.Thrones.S01E02.1080p.BluRay.x265-PODO[rartv]'/
	touch ~/galung-project/test-library/'Game.of.Thrones [Season 1]'/'Game.Of.Thrones.S01E02.1080p.BluRay.x265-PODO[rartv]'/'Game.Of.Thrones.S01E02.1080p.mkv'
	mkdir -p ~/galung-project/test-library/'Game.of.Thrones [Season 1]'/'Game.Of.Thrones.S01E03.1080p.BluRay.x265-PODO[rartv]'/
	touch ~/galung-project/test-library/'Game.of.Thrones [Season 1]'/'Game.Of.Thrones.S01E03.1080p.BluRay.x265-PODO[rartv]'/'Game.Of.Thrones.S01E03.1080p.mkv'
	mkdir -p ~/galung-project/test-library/'Game.of.Thrones [Season 1]'/'Game.Of.Thrones.S01E03.1080p.BluRay.x265-PODO[rartv]'/'Game.Of.Thrones.S01E03.subtitles'
	touch ~/galung-project/test-library/'Game.of.Thrones [Season 1]'/'Game.Of.Thrones.S01E03.1080p.BluRay.x265-PODO[rartv]'/'Game.Of.Thrones.S01E03.subtitles'/'Game.Of.Thrones.s01e03(english).srt'
	
	#Directory, File: Retrieving Lost Episode Test
	mkdir -p ~/galung-project/test-library/'Game.Of.Thrones.S01E05.1080p.BluRay.x265-PODO[rartv]'/
	touch ~/galung-project/test-library/'Game.Of.Thrones.S01E05.1080p.BluRay.x265-PODO[rartv]'/'Game.Of.Thrones.S01E05.1080p.mkv'
	mkdir -p ~/galung-project/test-library/'Game.Of.Thrones.S01E05.1080p.BluRay.x265-PODO[rartv]'/'Game.Of.Thrones.S01E05.subtitles'
	touch ~/galung-project/test-library/'Game.Of.Thrones.S01E05.1080p.BluRay.x265-PODO[rartv]'/'Game.Of.Thrones.S01E05.subtitles'/'Game.Of.Thrones.S01E05(english).srt'
	touch ~/galung-project/test-library/'Game.Of.Thrones.S01E05.1080p.BluRay.x265-PODO[rartv]'/'Game.Of.Thrones.S01E05.subtitles'/'Game.Of.Thrones.S01E05(es).srt'
	
	#Directory, File: Default
	mkdir -p ~/galung-project/test-library/'Teen.Wolf.S01E05.1080p.BluRay.x265-PODO[rartv]'/
	touch ~/galung-project/test-library/'Teen.Wolf.S01E05.1080p.BluRay.x265-PODO[rartv]'/'Teen.Wolf.S01E05.1080p.mkv'
	mkdir -p ~/galung-project/test-library/'Teen.Wolf.S01E05.1080p.BluRay.x265-PODO[rartv]'/'Teen.Wolf.S01E05.subtitles'
	#touch ~/galung-project/test-library/'Teen.Wolf.S01E05.1080p.BluRay.x265-PODO[rartv]'/'Teen.Wolf.S01E05.subtitles'/'Teen.Wolf.S01E05(english).srt'
	#touch ~/galung-project/test-library/'Teen.Wolf.S01E05.1080p.BluRay.x265-PODO[rartv]'/'Teen.Wolf.S01E05.subtitles'/'Teen.Wolf.S01E05(es).srt'
	
	#Directory, File: Retrieving Repetead Lost Episode Test
	#mkdir -p ~/galung-project/test-library/'Game.Of.Thrones.S01E01.1080p.BluRay.x265-PODO[rartv]'/'Game.Of.Thrones.S01E01.1080p.mkv'
	
	#Directory, Subdirectory, File: Unkonwn Show
	#mkdir -p ~/galung-project/test-library/'Krystal-The.Black Stripper-S02E01-The.dAy.0f.7he stripper.720p[rartv]'
	#touch ~/galung-project/test-library/'Krystal-The.Black Stripper-S02E01-The.dAy.0f.7he stripper.720p[rartv]'/'System.nfo'
	#touch ~/galung-project/test-library/'Krystal-The.Black Stripper-S02E01-The.dAy.0f.7he stripper.720p[rartv]'/'rartv.txt'
	#mkdir -p ~/galung-project/test-library/'Krystal-The.Black Stripper-S02E01-The.dAy.0f.7he stripper.720p[rartv]'/'sub'
	#touch ~/galung-project/test-library/'Krystal-The.Black Stripper-S02E01-The.dAy.0f.7he stripper.720p[rartv]'/'sub'/'Krystal-The.Black Stripper-S02E01(es).srt'

build-anime:
	mkdir -p ~/galung-project/test-library/'[PuyaSubs!] Yuri!!! On ICE - 11 [720p][663F641B]'/
	touch ~/galung-project/test-library/'[PuyaSubs!] Yuri!!! On ICE - 11 [720p][663F641B]'/'[PuyaSubs!] Yuri!!! On ICE - 11 [720p][663F641B].mkv'
	mkdir -p ~/galung-project/test-library/'[PuyaSubs!] Yuri!!! On ICE - 11 [720p][663F641B]'/'[PuyaSubs!] Yuri!!! On ICE - 11 subtitle'/
	touch ~/galung-project/test-library/'[PuyaSubs!] Yuri!!! On ICE - 11 [720p][663F641B]'/'[PuyaSubs!] Yuri!!! On ICE - 11 subtitle'/'[PuyaSubs!] Yuri!!! On ICE - 11(spanish).srt'
	
	mkdir -p ~/galung-project/test-library/'[Krosis] Getsuyoubi no Tawawa - 10 [1E0FA286]'/
	touch ~/galung-project/test-library/'[Krosis] Getsuyoubi no Tawawa - 10 [1E0FA286]'/'[Krosis] Getsuyoubi no Tawawa - 10 [1E0FA286].mkv'
	mkdir -p ~/galung-project/test-library/'[Krosis] Getsuyoubi no Tawawa - 10 [1E0FA286]'/'[Krosis] Getsuyoubi no Tawawa - 10 subtitle'/
	touch ~/galung-project/test-library/'[Krosis] Getsuyoubi no Tawawa - 10 [1E0FA286]'/'[Krosis] Getsuyoubi no Tawawa - 10 subtitle'/'[Krosis] Getsuyoubi no Tawawa - 10(eng).srt'
	
	mkdir -p ~/galung-project/test-library/'[HorribleSubs] One Piece - 768 [1080p]'/
	touch ~/galung-project/test-library/'[HorribleSubs] One Piece - 768 [1080p]'/'[HorribleSubs] One Piece - 768 [1080p].mkv'
	mkdir -p ~/galung-project/test-library/'[HorribleSubs] One Piece - 768 [1080p]'/'[HorribleSubs] One Piece - 768 subtitle'/
	touch ~/galung-project/test-library/'[HorribleSubs] One Piece - 768 [1080p]'/'[HorribleSubs] One Piece - 768 subtitle'/'[HorribleSubs] One Piece - 768(eng).srt'

	mkdir -p ~/galung-project/test-library/'[HorribleSubs] One Piece x769 [1080p]'/
	touch ~/galung-project/test-library/'[HorribleSubs] One Piece x769 [1080p]'/'[HorribleSubs] One Piece x769 [1080p].mkv'
	mkdir -p ~/galung-project/test-library/'[HorribleSubs] One Piece x769 [1080p]'/'[HorribleSubs] One Piece x769 subtitle'/
	touch ~/galung-project/test-library/'[HorribleSubs] One Piece x769 [1080p]'/'[HorribleSubs] One Piece x769 subtitle'/'[HorribleSubs] One Piece x769(eng).srt'

	mkdir -p ~/galung-project/test-library/'[Ohys-Raws] Detective Conan - 842 (NTV 1280x720 x264 AAC)'/
	touch ~/galung-project/test-library/'[Ohys-Raws] Detective Conan - 842 (NTV 1280x720 x264 AAC)'/'[Ohys-Raws] Detective Conan - 842 (NTV 1280x720 x264 AAC).mp4'
	mkdir -p ~/galung-project/test-library/'[Ohys-Raws] Detective Conan - 842 (NTV 1280x720 x264 AAC)'/'[Ohys-Raws] Detective Conan - 842 subtitle'/
	touch ~/galung-project/test-library/'[Ohys-Raws] Detective Conan - 842 (NTV 1280x720 x264 AAC)'/'[Ohys-Raws] Detective Conan - 842 subtitle'/'[Ohys-Raws] Detective Conan - 842(eng).srt'
	
	#CASO PARTICULAR DEL PUTO ANIME con Episode
	mkdir -p ~/galung-project/test-library/'[Dcms-Fansubs] Detective Conan Episode 840 [1080p]'/
	touch ~/galung-project/test-library/'[Dcms-Fansubs] Detective Conan Episode 840 [1080p]'/'[Dcms-Fansubs] Detective Conan Episode 840 [1080p].mkv'
	mkdir -p ~/galung-project/test-library/'[Dcms-Fansubs] Detective Conan Episode 840 [1080p]'/'[Dcms-Fansubs] Detective Conan Episode 840 subtitle'/
	touch ~/galung-project/test-library/'[Dcms-Fansubs] Detective Conan Episode 840 [1080p]'/'[Dcms-Fansubs] Detective Conan Episode 840 subtitle'/'[Dcms-Fansubs] Detective Conan Episode 840(eng).srt'
	
	#Number on name
	mkdir -p ~/galung-project/test-library/'[HorribleSubs] Mob Psycho 100 - 12 [1080p]'/
	touch ~/galung-project/test-library/'[HorribleSubs] Mob Psycho 100 - 12 [1080p]'/'[HorribleSubs] Mob Psycho 100 - 12 [1080p].mkv'
	mkdir -p ~/galung-project/test-library/'[HorribleSubs] Mob Psycho 100 - 12 [1080p]'/'[HorribleSubs] Mob Psycho 100 - 12 subs'/
	touch ~/galung-project/test-library/'[HorribleSubs] Mob Psycho 100 - 12 [1080p]'/'[HorribleSubs] Mob Psycho 100 - 12 subs'/'[HorribleSubs] Mob Psycho 100 - 12 (eng).srt'

build-subs:
	cp -ar ~/galung-project/subs ~/galung-project/test-library/


build-addon:
	rm -f ~/galung-project/trunk/addon/'script.galung.project.zip'
	zip -r ~/galung-project/trunk/addon/script.galung.project.zip ~/TFG/trunk/addon/script.galung.project/


build-all:
	make build-movie
	make build-serie
	make build-anime

clean:
	rm -rf ~/galung-project/test-library/*
