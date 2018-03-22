import mmap


with open("file") as f:
    mm = mmap.mmap(f.fileno(), 0)
