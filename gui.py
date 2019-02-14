from PyQt5 import QtWidgets, QtMultimedia, QtMultimediaWidgets, QtCore
from scraper import webms
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    w = QtMultimediaWidgets.QVideoWidget()
    w.resize(1280, 720)
    w.show()
    w.setWindowTitle('Press <Right Arrow Key> to skip')

    player = QtMultimedia.QMediaPlayer()
    player.setVideoOutput(w)
    videos = webms('wsg') # Safe For Work 4chan board

    def keypressevent(e):
        if e.key() == QtCore.Qt.Key_Right:
            vid = next(videos)
            print(vid)
            player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl(vid)))
            player.play()

    w.keyPressEvent = keypressevent
    player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl(next(videos))))
    player.play()

    sys.exit(app.exec_())