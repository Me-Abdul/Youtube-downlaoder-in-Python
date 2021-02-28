import requests
import pytube
import sys
args = sys.argv
print("\n\t\tPythonScript: YouTube Video Downloading ")
if (len(args) > 1):
    url = args[1]
else:
    url = input("\t url: ")

print(f'\t url : {url}')

try:
    yt = pytube.YouTube(url)
    streams = yt.streams
except pytube.exceptions.RegexMatchError:
    print("incorrect url:")
    exit(1)

print(f'\t TITLE: {yt.title}')
print(f'\t AUTOR: {yt.author}')
print(f'\t VIEWS: {yt.views}')

for i,stream in enumerate(streams):
    print(f'\t {i}.stream.title  ({stream.resolution})')

ch = True

while ch:
    try:
        choice = int(input(f"\t Select [0-{len(streams)-1}]: "))
        if choice < len(streams):
            print("\t Downloading.......")

            try:
                with requests.get(streams[choice].url,stream=True) as r:
                    with open(streams[choice].default_filename, "wb") as f:
                        for chunk in r.iter_content(512):
                            f.write(chunk)
                print("\n\t Compleeted downaldspio.")
                ch = False
            except Exception as e:
                print(str(e))
                exit(1)
        else:
            print("invalid chocie")
    except Exception as e:
        print(str(e))
