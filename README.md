## TC.DETECT
# Сar license plate recognition software (Python, OpenCV, yoloV7)

# Installation

```bash
git clone https://github.com/Lagushka1984/TC.DETECT.git
cd TC.DETECT
bash install.sh
```

# Launch
```bash
python3 main.py config.txt
```

# Config file

### Default command template
```bash
cmd=param=name
```

### debug
Description:
Show frames, output in terminal

Template:
```bash
debug=True/False=None
```

Example:
```bash
debug=True=None
```

### image
Description:
Emulation image like a video source

Template:
```bash
image=image-name=camera-name
```

Example:
```bash
image=test.jpg=CAM0
```

### video
Description:
Emulation video like a video source

Template:
```bash
video=video-name=camera-name
```

Example:
```bash
video=test.mp4=CAM1
```

### rtps
Description:
Connection rtsp camera

Template:
```bash
rtps=rtps-link=camera-name
```

Example:
```bash
rtps=https://...=CAM2
```

### xy
Description:
Cutting frames

Template:
```bash
xy=(x1, x2, y1, y2)=None
```

Example:
```bash
xy=(0, 1080, 0, 1920)=None
```

### time
Description:
Delay between frames, milliseconds

Template:
```bash
time=delay=None
```

Example:
```bash
time=3000=None
```

### Config file example
```bash
debug=True=None
image=test.jpg=CAM0
video=test.mp4=CAM1
rtps=https://...=CAM2
xy=(300, 600, 0, 1920)=None
time=3000=None
```

