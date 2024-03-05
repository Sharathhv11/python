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

def music_manager(obj : music):
		#creating object for music class y passing file path as constructer argument
		

		#this block of code manages the music player by playing pausing etc
		while (True):
			music_status=input("enter P-play , PA - pause , S - stop , UP - unpause :").lower()
			
			if(music_status=="p"):
				obj.play_music()
			elif(music_status=="pa"):
				obj.pause_music()
				
			elif(music_status=="up"):
				obj.unpause_music()
		
			elif(music_status=="s"):
				obj.stop_music()
			
			else:
				print(f" {music_status} you must have entered the wrong choice")



if (__name__=="__main__"):
	obj = music("E:\music_player\musics\Arijit Singh  Main Tera Boyfriend.mp3")
	music_manager(obj)