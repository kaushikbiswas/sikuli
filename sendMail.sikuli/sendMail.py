
fPath = "C:\\Users\\104947.CTS\\Documents\\mails.xlsx"

type ("r", KeyModifier.WIN)
type (fPath + Key.ENTER)

wait("1497559484867.png")

type (Key.HOME, KeyModifier.CTRL)

chOutlook = switchApp("Outlook")
click(Pattern("1497557908994.png").targetOffset(-7,-11))
wait("1497561235442.png")


chExcel = switchApp("Excel")
type (Key.DOWN)
type ("c", KeyModifier.CTRL)

click("1497562377185.png")
wait("1497561235442.png")
type ("v", KeyModifier.CTRL)

chExcel = switchApp("Excel")
type (Key.RIGHT)
type ("c", KeyModifier.CTRL)
click("1497562377185.png")

wait("1497561235442.png")
type (Key.TAB)
type (Key.TAB)
type ("v", KeyModifier.CTRL)

chExcel = switchApp("Excel")
type (Key.RIGHT)
type ("c", KeyModifier.CTRL)
click("1497562377185.png")

wait("1497561235442.png")
type (Key.TAB)
type ("v", KeyModifier.CTRL)

click (Pattern("1497561235442.png").targetOffset(-13,-4))

waitVanish("1497562804055.png")

chOutlook = switchApp("Outlook")

wait(Pattern("1497557908994.png").targetOffset(-7,-11))

click(Pattern("1497557908994.png").targetOffset(-7,-11))
wait("1497561235442.png")


chExcel = switchApp("Excel")
type (Key.HOME)


type (Key.DOWN)
type ("c", KeyModifier.CTRL)
click("1497562377185.png")
wait("1497561235442.png")
type ("v", KeyModifier.CTRL)

chExcel = switchApp("Excel")
type (Key.RIGHT)
type ("c", KeyModifier.CTRL)
click("1497562377185.png")
wait("1497561235442.png")
type (Key.TAB)
type (Key.TAB)
type ("v", KeyModifier.CTRL)

chExcel = switchApp("Excel")
type (Key.RIGHT)
type ("c", KeyModifier.CTRL)
click("1497562377185.png")
wait("1497561235442.png")
type (Key.TAB)
type ("v", KeyModifier.CTRL)

click (Pattern("1497561235442.png").targetOffset(-13,-4))

waitVanish("1497562804055.png")

chExcel = switchApp("Excel")
wait("1497559484867.png")

type (Key.F4, KeyModifier.ALT)

