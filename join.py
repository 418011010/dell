# coding=utf-8


def mixmp3(num):
    f1_read = open('sound\\first.mp3', 'rb')
    num_read = open('sound\\{}.mp3'.format(num), 'rb')
    f2_read = open('sound\\end.mp3', 'rb')

    f3_write = open('out.mp3', 'wb')
    f3_write.write(f1_read.read())
    f3_write.write(num_read.read())
    f3_write.write(f2_read.read())

    f1_read.close()
    num_read.close()
    f2_read.close()
    f3_write.flush()
    f3_write.close()

