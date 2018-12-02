try:
    from pip import main as pipmain
except:
    from pip._internal import main as pipmain

pipmain(['install', "--upgrade", "pip"])
pipmain(['install',"opencv-python==3.4.4.19"])
pipmain(['install',"pygame==1.9.4"])
pipmain(['install',"numpy==1.15.4"])
pipmain(['install',"pyaudio==0.2.11"])
