xcute = True

def xhotkey(event):
    global xcute
    xcute = False

Env.addHotkey(Key.F1, KeyModifier.CTRL,xhotkey)

ch = switchApp("Calculator")

if ch.hasWindow():
    click(Pattern("1497567150854.png").targetOffset(-2,-66))
else:
    type("r",KeyModifier.WIN)
    type("calc"+ Key.ENTER)

wait("1497567150854.png")

Settings.MoveHouseDelay = 0.0

while exists("1497567150854.png") and xcute:
    
    click(Pattern("1497567150854.png").targetOffset(-82,27))
    
    click(Pattern("1497567150854.png").targetOffset(34,58))

click(Pattern("1497567150854.png").targetOffset(-79,30))

click(Pattern("1497567150854.png").targetOffset(75,40))
    