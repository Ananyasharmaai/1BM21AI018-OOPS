class songs():
  def __init__(self,lyrics):
    self.lyrics=lyrics
  def sing_me_a_song(self):
    for x in self.lyrics:
      print(x)

x=eval(input("Enter the song : "))
s=songs(x)
s.sing_me_a_song()