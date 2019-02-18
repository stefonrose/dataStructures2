from appJar import gui
import matPlotLibTest as runtime
import subprocess

app=gui("Grid Demo", (1200, 900))
app.setBg("PowderBlue")
app.setSticky("news")
#app.setExpand("both")

app.setFont(18)

def sorts(button):
    if button == "selection":
        runtime.N = int(app.getOptionBox("selectSize"))
        runtime.method = "s"
        subprocess.call(["python3", "matPlotLibTest.py"])
        #exec(open("matPlotLibTest.py").read())

app.addLabel("header", "Sorting Algorithms", 0, 0, 3)
app.addLabel("optionLabel", "Select number of\nelements to sort: ", 1, 0)

app.addButton("selection", sorts, 2, 0)
app.addButton("insertion", sorts, 2, 1)
app.addButton("bubble", sorts, 2, 2)
app.addButton("merge", sorts, 3, 0)
app.addButton("quick", sorts, 3, 1)
app.addButton("radix", sorts, 3, 2)


app.setLabelBg("header", "SteelBlue")
app.setLabelBg("optionLabel", "PowderBlue")

app.setButtonBg("selection", "PowderBlue")
app.setButtonBg("insertion", "PowderBlue")
app.setButtonBg("bubble", "PowderBlue")
app.setButtonBg("merge", "PowderBlue")
app.setButtonBg("quick", "PowderBlue")
app.setButtonBg("radix", "PowderBlue")

app.setLabelPadding("header", [40, 40])

app.setButtonImage("selection", "sort-icons/sIcon2.gif", "top")
app.setButtonImage("insertion", "sort-icons/iSort.gif", "top")
app.setButtonImage("bubble", "sort-icons/bSort2.gif", "top")
app.setButtonImage("merge", "sort-icons/mSort.gif", "top")
app.setButtonImage("quick", "sort-icons/qSort.gif", "top")
app.setButtonImage("radix", "sort-icons/rSort.gif", "top")

app.addOptionBox("selectSize", ["100", "200", "300", "400", "500"], 1, 1)

app.go()