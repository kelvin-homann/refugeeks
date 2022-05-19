class WrongFormatError(Exception):
    def __str__(self) -> str:
        return "Falsches Dateiformat"


class Song:
    def __init__(self, title, laenge, artist, file_format):
        if file_format != 'mp3' and file_format != 'wma':
            raise WrongFormatError

        self.title = title
        self.laenge = laenge
        self.artist = artist
        self.file_format = file_format

    def __str__(self) -> str:
        return "{}.{}".format(self.title, self.file_format)


class Artist:
    def __init__(self, name):
        self.name = name


eminem = Artist("Eminem")
loose_yourself = Song("Loose yourself", 2000, eminem, 'mp3')
print(loose_yourself)
