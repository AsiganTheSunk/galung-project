.PHONY: build clean build-addon build-movie build-serie build-anime build-subs

build-movie:
	#Directory, File: Default Test (BlueRay)
	mkdir -p ~/TFG/testlibrary/'Sisters.And.Brothers.2011.1080p.BluRay.H264.AAC-RARBG'
	touch ~/TFG/testlibrary/'Sisters.And.Brothers.2011.1080p.BluRay.H264.AAC-RARBG'/'Sisters.And.Brothers.2011.1080p.BluRay.H264.AAC-RARBG.mkv'
	
	#Directory, File: Default Test
	mkdir -p ~/TFG/testlibrary/'Innocent.Bystanders.1972.BRRip.XviD.MP3-RARBG'
	touch ~/TFG/testlibrary/'Innocent.Bystanders.1972.BRRip.XviD.MP3-RARBG'/'Innocent.Bystanders.1972.BRRip.XviD.MP3-RARBG.mkv'
	
	#Directory, File: Default Test (Dates)
	mkdir -p ~/TFG/testlibrary/'Meet.Him.And.Die.1976.1080p.BluRay.H264.AAC-RARBG'
	touch ~/TFG/testlibrary/'Meet.Him.And.Die.1976.1080p.BluRay.H264.AAC-RARBG'/'Meet.Him.And.Die.1976.1080p.BluRay.H264.AAC-RARBG.mkv'
	
	#Directory, Subdirectory, File: Default Test (Mp3)
	mkdir -p ~/TFG/testlibrary/'Littlerock.2010.BRRip.XviD.MP3-RARBG'
	mkdir -p ~/TFG/testlibrary/'Littlerock.2010.BRRip.XviD.MP3-RARBG'/'subs'
	mkdir -p ~/TFG/testlibrary/'Littlerock.2010.BRRip.XviD.MP3-RARBG'/'sub'
	touch ~/TFG/testlibrary/'Littlerock.2010.BRRip.XviD.MP3-RARBG'/'sub'/'Littlerock.2010(english).str'
	touch ~/TFG/testlibrary/'Littlerock.2010.BRRip.XviD.MP3-RARBG'/'Littlerock.2010.BRRip.XviD.MP3-RARBG.mkv'
	
	#Directory, Subdirectory, File: Default Test (EXTENDED.CUT,BRRip, XviD)
	mkdir -p ~/TFG/testlibrary/'Were.the.Millers.2013.EXTENDED.CUT.BRRip.XviD.MP3-RARBG'
	mkdir -p ~/TFG/testlibrary/'Were.the.Millers.2013.EXTENDED.CUT.BRRip.XviD.MP3-RARBG'/'sub'
	touch ~/TFG/testlibrary/'Were.the.Millers.2013.EXTENDED.CUT.BRRip.XviD.MP3-RARBG'/'sub'/'Were.the.Millers.2013(english).str'
	touch ~/TFG/testlibrary/'Were.the.Millers.2013.EXTENDED.CUT.BRRip.XviD.MP3-RARBG'/'System.nfo'
	touch ~/TFG/testlibrary/'Were.the.Millers.2013.EXTENDED.CUT.BRRip.XviD.MP3-RARBG'/'Readme.txt'
	touch ~/TFG/testlibrary/'Were.the.Millers.2013.EXTENDED.CUT.BRRip.XviD.MP3-RARBG'/'RARBG.mkv'
	touch ~/TFG/testlibrary/'Were.the.Millers.2013.EXTENDED.CUT.BRRip.XviD.MP3-RARBG'/'Were.the.Millers.2013.EXTENDED.CUT.BRRip.XviD.MP3-RARBG.mkv'

	#Directory, File: Unkonw Movie
	#mkdir -p ~/TFG/testlibrary/'Lost.Kiddo.The.Movie.(1080p).(2015)'
	#touch ~/TFG/testlibrary/'Lost.Kiddo.The.Movie.(1080p).(2015)'/'Lost.Kiddo.The.Movie.(1080p).(2015).mkv'

build-serie:
	#Directory, File: Default Test
	mkdir -p ~/TFG/testlibrary/'Game.of.Thrones.S06.1080p.BluRay.x264-ROVERS[rartv]'
	touch ~/TFG/testlibrary/'Game.of.Thrones.S06.1080p.BluRay.x264-ROVERS[rartv]'/'Game.of.Thrones.S06E01.1080p.BluRay.x264-ROVERS[rartv].mkv'
	touch ~/TFG/testlibrary/'Game.of.Thrones.S06.1080p.BluRay.x264-ROVERS[rartv]'/'Game.of.Thrones.S06E02.1080p.BluRay.x264-ROVERS[rartv].mkv'
	touch ~/TFG/testlibrary/'Game.of.Thrones.S06.1080p.BluRay.x264-ROVERS[rartv]'/'Game.of.Thrones.S06E03.1080p.BluRay.x264-ROVERS[rartv].mkv'
	
	#Directory, Subdirectory, File: Default Test
	mkdir -p ~/TFG/testlibrary/'Game.of.Thrones-season2'/
	mkdir -p ~/TFG/testlibrary/'Game.of.Thrones.season-3'/
	mkdir -p ~/TFG/testlibrary/'Game.of.Thrones [Season 1]'/
	mkdir -p ~/TFG/testlibrary/'Game.of.Thrones [Season 1]'/'Game.Of.Thrones.S01E01.1080p.BluRay.x265-PODO[rartv]'/
	touch ~/TFG/testlibrary/'Game.of.Thrones [Season 1]'/'Game.Of.Thrones.S01E01.1080p.BluRay.x265-PODO[rartv]'/'Game.Of.Thrones.S01E01.1080p.mkv'
	mkdir -p ~/TFG/testlibrary/'Game.of.Thrones [Season 1]'/'Game.Of.Thrones.S01E02.1080p.BluRay.x265-PODO[rartv]'/
	touch ~/TFG/testlibrary/'Game.of.Thrones [Season 1]'/'Game.Of.Thrones.S01E02.1080p.BluRay.x265-PODO[rartv]'/'Game.Of.Thrones.S01E02.1080p.mkv'
	mkdir -p ~/TFG/testlibrary/'Game.of.Thrones [Season 1]'/'Game.Of.Thrones.S01E03.1080p.BluRay.x265-PODO[rartv]'/
	touch ~/TFG/testlibrary/'Game.of.Thrones [Season 1]'/'Game.Of.Thrones.S01E03.1080p.BluRay.x265-PODO[rartv]'/'Game.Of.Thrones.S01E03.1080p.mkv'
	mkdir -p ~/TFG/testlibrary/'Game.of.Thrones [Season 1]'/'Game.Of.Thrones.S01E03.1080p.BluRay.x265-PODO[rartv]'/'subtitles'
	#touch ~/TFG/testlibrary/'Game.of.Thrones [Season 1]'/'Game.Of.Thrones.S01E03.1080p.BluRay.x265-PODO[rartv]'/'subtitles'/'Game.Of.Thrones.s01.e03(english).srt'
	
	#Directory, File: Retrieving Lost Episode Test
	mkdir -p ~/TFG/testlibrary/'Game.Of.Thrones.S01E05.1080p.BluRay.x265-PODO[rartv]'/
	touch ~/TFG/testlibrary/'Game.Of.Thrones.S01E05.1080p.BluRay.x265-PODO[rartv]'/'Game.Of.Thrones.S01E05.1080p.mkv'
	mkdir -p ~/TFG/testlibrary/'Game.Of.Thrones.S01E05.1080p.BluRay.x265-PODO[rartv]'/'subtitles'
	#touch ~/TFG/testlibrary/'Game.Of.Thrones.S01E05.1080p.BluRay.x265-PODO[rartv]'/'subtitles'/'Game.Of.Thrones.S01.E05(english).srt'
	#touch ~/TFG/testlibrary/'Game.Of.Thrones.S01E05.1080p.BluRay.x265-PODO[rartv]'/'subtitles'/'Game.Of.Thrones.S01.E05(es).srt'
	
	#Directory, File: Default
	mkdir -p ~/TFG/testlibrary/'Teen.Wolf.S01E05.1080p.BluRay.x265-PODO[rartv]'/
	touch ~/TFG/testlibrary/'Teen.Wolf.S01E05.1080p.BluRay.x265-PODO[rartv]'/'Teen.Wolf.S01E05.1080p.mkv'
	mkdir -p ~/TFG/testlibrary/'Teen.Wolf.S01E05.1080p.BluRay.x265-PODO[rartv]'/'subtitles'
	#touch ~/TFG/testlibrary/'Teen.Wolf.S01E05.1080p.BluRay.x265-PODO[rartv]'/'subtitles'/'Teen.Wolf.S01.E05(english).srt'
	#touch ~/TFG/testlibrary/'Teen.Wolf.S01E05.1080p.BluRay.x265-PODO[rartv]'/'subtitles'/'Teen.Wolf.S01.E05(es).srt'

	#Directory, File: Retrieving Repetead Lost Episode Test
	#mkdir -p ~/TFG/testlibrary/'Game.Of.Thrones.S01E01.1080p.BluRay.x265-PODO[rartv]'/'Game.Of.Thrones.S01E01.1080p.mkv'
	
	#Directory, Subdirectory, File: Unkonwn Show
	#mkdir -p ~/TFG/testlibrary/'Krystal-The.Black Stripper-S02E01-The.dAy.0f.7he stripper.720p[rartv]'

	#touch ~/TFG/testlibrary/'Krystal-The.Black Stripper-S02E01-The.dAy.0f.7he stripper.720p[rartv]'/'System.nfo'
	#touch ~/TFG/testlibrary/'Krystal-The.Black Stripper-S02E01-The.dAy.0f.7he stripper.720p[rartv]'/'rartv.txt'
	#mkdir -p ~/TFG/testlibrary/'Krystal-The.Black Stripper-S02E01-The.dAy.0f.7he stripper.720p[rartv]'/'sub'
	#touch ~/TFG/testlibrary/'Krystal-The.Black Stripper-S02E01-The.dAy.0f.7he stripper.720p[rartv]'/'sub'/'Krystal-The.Black Stripper-S02E01(es).srt'
	
build-anime:
	mkdir -p ~/TFG/testlibrary/'[PuyaSubs!] Yuri!!! On ICE - 11 [720p][663F641B]'/
	touch ~/TFG/testlibrary/'[PuyaSubs!] Yuri!!! On ICE - 11 [720p][663F641B]'/'[PuyaSubs!] Yuri!!! On ICE - 11 [720p][663F641B].mkv'
	mkdir -p ~/TFG/testlibrary/'[PuyaSubs!] Yuri!!! On ICE - 11 [720p][663F641B]'/'subs'/
	touch ~/TFG/testlibrary/'[PuyaSubs!] Yuri!!! On ICE - 11 [720p][663F641B]'/'subs'/'subtitles_(eng).srt'
	
	mkdir -p ~/TFG/testlibrary/'[Krosis] Getsuyoubi no Tawawa - 10 [1E0FA286]'/
	touch ~/TFG/testlibrary/'[Krosis] Getsuyoubi no Tawawa - 10 [1E0FA286]'/'[Krosis] Getsuyoubi no Tawawa - 10 [1E0FA286].mkv'
	mkdir -p ~/TFG/testlibrary/'[Krosis] Getsuyoubi no Tawawa - 10 [1E0FA286]'/'subs'/
	touch ~/TFG/testlibrary/'[Krosis] Getsuyoubi no Tawawa - 10 [1E0FA286]'/'subs'/'subtitles.(eng).srt'	
	
	mkdir -p ~/TFG/testlibrary/'[HorribleSubs] One Piece - 768 [1080p]'/
	touch ~/TFG/testlibrary/'[HorribleSubs] One Piece - 768 [1080p]'/'[HorribleSubs] One Piece - 768 [1080p].mkv'
	mkdir -p ~/TFG/testlibrary/'[HorribleSubs] One Piece - 768 [1080p]'/'subs'/
	touch ~/TFG/testlibrary/'[HorribleSubs] One Piece - 768 [1080p]'/'subs'/'subtitles_coco(eng).srt'
	
	mkdir -p ~/TFG/testlibrary/'[Ohys-Raws] Detective Conan - 842 (NTV 1280x720 x264 AAC)'/
	touch ~/TFG/testlibrary/'[Ohys-Raws] Detective Conan - 842 (NTV 1280x720 x264 AAC)'/'[Ohys-Raws] Detective Conan - 842 (NTV 1280x720 x264 AAC).mp4'
	mkdir -p ~/TFG/testlibrary/'[Ohys-Raws] Detective Conan - 842 (NTV 1280x720 x264 AAC)'/'subs'/
	touch ~/TFG/testlibrary/'[Ohys-Raws] Detective Conan - 842 (NTV 1280x720 x264 AAC)'/'subs'/'subtitles(eng).srt'
	
	#CASO PARTICULAR DEL PUTO ANIME con Episode
	mkdir -p ~/TFG/testlibrary/'[Dcms-Fansubs] Detective Conan Episode 840 [1080p]'/
	touch ~/TFG/testlibrary/'[Dcms-Fansubs] Detective Conan Episode 840 [1080p]'/'[Dcms-Fansubs] Detective Conan Episode 840 [1080p].mkv'
	mkdir -p ~/TFG/testlibrary/'[Dcms-Fansubs] Detective Conan Episode 840 [1080p]'/'subs'/
	touch ~/TFG/testlibrary/'[Dcms-Fansubs] Detective Conan Episode 840 [1080p]'/'subs'/'subtitles_coco(eng).srt'
	
	#Number on name
	mkdir -p ~/TFG/testlibrary/'[HorribleSubs] Mob Psycho 100 - 12 [1080p]'/
	touch ~/TFG/testlibrary/'[HorribleSubs] Mob Psycho 100 - 12 [1080p]'/'Mob Psycho 100 - 12 [1080p].mkv'
	mkdir -p ~/TFG/testlibrary/'[HorribleSubs] Mob Psycho 100 - 12 [1080p]'/'subs'/
	touch ~/TFG/testlibrary/'[HorribleSubs] Mob Psycho 100 - 12 [1080p]'/'subs'/'subtitles(eng).srt'

build-subs:
	cp -ar ~/TFG/subs ~/TFG/testlibrary/


build-addon:
	rm -f ~/TFG/trunk/addon/'script.galung.project.zip'
	zip -r ~/TFG/trunk/addon/script.galung.project.zip ~/TFG/trunk/addon/script.galung.project/


build-all:
	make build-movie
	make build-serie
	make build-anime

clean:
	rm -rf ~/TFG/testlibrary/*
