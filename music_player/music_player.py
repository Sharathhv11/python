import pygame as pg


class music:
	"""music class that has various aspect of music player"""


	def __init__(self,path) -> None:
		#initializing the pygame module
		pg.mixer.init()
		#loading file to pygame module
		pg.mixer.music.load(path)
	
	def play_music(self):
		"""this method plays the loaded music"""
		pg.mixer.music.play()
		
	def pause_music(self):
		"""this method pauses the current playing music"""
		pg.mixer.music.pause()
		
	def unpause_music(self):
		"""this method unpaused the paused music"""
		pg.mixer.music.unpause()
		
	def stop_music(self):
		"""this method stops the current music"""
		pg.mixer.music.stop()


class music_manager:
	def __init__(self,obj) -> None:
		self.obj= obj
	def music_status(self,music_status):
		"""this method handels  the life cycyle of music like play pause and more .."""
		if(music_status==1):
			self.obj.play_music()
		elif(music_status==2):
			self.obj.pause_music()
			
		elif(music_status==3):
			self.obj.unpause_music()

		elif(music_status==4):
			self.obj.stop_music()
		
		else:
			print(f" {music_status} you must have entered the wrong choice")
			return
		
			
	



if (__name__=="__main__"):
	obj = music("E:\music_player\musics\Arijit Singh  Main Tera Boyfriend.mp3")
	music_manager(obj)