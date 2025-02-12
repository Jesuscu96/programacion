class Video:
    def __init__(self, titulo_video, duracion, categoria):
        self.titulo_video = titulo_video
        self.duracion = duracion
        self.categoria = categoria
    
    def mirar_video(self):
        return (f"Iniciando video cuyo titulo es {self.titulo_video} cuya duracion: {self.duracion} y su categoria: {self.categoria}.")
    
    def detener_video(self):
        return ("Video detenido.")
    
class Audio:
    def __init__(self, titulo_audio, nom_artista):
        self.titulo_audio = titulo_audio
        self.nom_artista = nom_artista
    
    def escuchar_audio(self):
        return (f"El titulo: {self.titulo_audio}, nombre del artista: {self.nom_artista}.")
    
    def detener_audio(self):
        return ("El audio se ha detenido.")
    
class Media (Video, Audio):
    def __init__(self, titulo_video, duracion, categoria, nom_artista, titulo_audio):
        Video.__init__(self, titulo_video, duracion, categoria)
        Audio.__init__(self,titulo_audio, nom_artista)

medio_1 = Media("titulo 1", 180, "infantil", "Artista 1", "titulo audio") 
print(medio_1.escuchar_audio())
print(medio_1.mirar_video()) 
print(medio_1.detener_audio()) 
print(medio_1.detener_video())
