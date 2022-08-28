import maya.cmds as cmds


def rightEyeButtonPush(*args):
    print('Right Eye')
    cmds.select('rightEye')


def leftEyeButtonPush(*args):
    print('Left Eye')
    cmds.select('leftEye')


def mouthButtonPush(*args):
    print('Mouth')
    cmds.select('mouth')


def noseButtonPush(*args):
    print('Nose')
    cmds.select('nose')


mhWindows = cmds.window(s=False, width=400, height=400, t='FacePicker')
mhLayout = cmds.columnLayout(adj=True)
mhform = cmds.formLayout(numberOfDivisions=100, width=400, height=400, e=False)
mhButton = cmds.button(l='Right Eye', c=rightEyeButtonPush)
mhBGImage = cmds.image(image='../facePicker.png')
b1 = cmds.button(w=20, h=20, l='', bgc=[1, 1, 0], command=rightEyeButtonPush)
cmds.formLayout(mhform, e=True, attachForm=[(b1, 'top', 180), (b1, 'left', 75)])
b2 = cmds.button(w=20, h=20, l='', bgc=[1, 1, 0], command=leftEyeButtonPush)
cmds.formLayout(mhform, e=True, attachForm=[(b2, 'top', 180), (b2, 'left', 230)])
b2 = cmds.button(w=20, h=20, l='', bgc=[1, 1, 0], command=noseButtonPush)
cmds.formLayout(mhform, e=True, attachForm=[(b2, 'top', 260), (b2, 'left', 140)])
b2 = cmds.button(w=20, h=20, l='', bgc=[1, 1, 0], command=mouthButtonPush)
cmds.formLayout(mhform, e=True, attachForm=[(b2, 'top', 300), (b2, 'left', 140)])


cmds.showWindow(mhWindows)
