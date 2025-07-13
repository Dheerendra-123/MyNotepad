from PyQt5.QtWidgets import QMainWindow, QApplication ,QFileDialog
from PyQt5.QtPrintSupport import*
from PyQt5 import QtGui
from PyQt5.uic import loadUi
import sys

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("C://Users//DHEERENDRA DIXIT//TextEditor//MynotePad.ui",self)
        
        self.current_path=None
        self.currentfont_size=18
        self.current_zoom=1
        self.setWindowTitle('Untitled-MyNotePad')
        self.actionNew.triggered.connect(self.newfile)
        self.actionSave.triggered.connect(self.save)
        self.actionSave_as.triggered.connect(self.saveAs)
        self.actionUndo.triggered.connect(self.undo)
        self.actionRedo.triggered.connect(self.redo)
        self.actionCut.triggered.connect(self.cut)
        self.actionCopy.triggered.connect(self.copy)
        self.actionDelete.triggered.connect(self.delete)
        self.actionDel.triggered.connect(self.delete)
        self.actionSelectAll.triggered.connect(self.selectAll)
        self.actionPaste.triggered.connect(self.paste)
        self.actionPrint.triggered.connect(self.print)
        self.actionExit.triggered.connect(self.closeEvent)
        self.actionReplace.triggered.connect(self.replace)
        self.actionLight.triggered.connect(self.light)
        self.actionDark.triggered.connect(self.dark)
        self.actionOpen.triggered.connect(self.open)
        self.actionIncrease_Font_size.triggered.connect(self.increasefont)
        self.actionDecrease_font_Size.triggered.connect(self.decreasefont)
        self.actionZoom_in.triggered.connect(self.zoomin)
        self.actionZoom_out.triggered.connect(self.zoomout)
        self.actionBlue.triggered.connect(self.blueColor)
        self.actionGreen.triggered.connect(self.greenColor)
        self.actionBlack.triggered.connect(self.blackColor)
        
    def newfile(self):
       self.textEdit.clear()
       self.setWindowTitle("Untitled-MyNotePad")
       self.current_path=None
       
    def save(self):
       if self.current_path is not None: 
           #save the changes without opening dialog
           filetext=self.textEdit.toPlainText()
           with open(self.current_path,'w') as f:
               f.write(filetext)   
       else:
            self.saveAs()
               
    def saveAs(self):
        pathname=QFileDialog.getSaveFileName(self,'save file','C://Users/DHEERENDRA DIXIT//TextEditor','Text files (*.txt)')  
        filetext=self.textEdit.toPlainText()
        with open(pathname[0],'w') as f:
            f.write(filetext)
        self.current_path=pathname[0]
        self.setWindowTitle(pathname[0])
    def undo(self):
        self.textEdit.undo()
        
    def redo(self):
      self.textEdit.redo()
        
        
    def copy(self):
        self.textEdit.copy()
        
    def cut(self):
        self.textEdit.cut()
        
    def open(self):
        filename=QFileDialog.getOpenFileName(self,'open file','C://Users/DHEERENDRA DIXIT//TextEditor','Text files (*.txt)')
        self.setWindowTitle(filename[0])
        with open(filename[0],'r') as f:
            filetext=f.read()
            self.textEdit.setText(filetext)
        self.current_path =filename[0]
        
    def paste(self):
        self.textEdit.paste()
        
    def print(self):
        printer = QPrintDialog()
        if printer.exec_() == QPrintDialog.Accepted:
            self.textEdit.print_(printer.printer())
        
    # def closeEvent(self, event):
    
    
    def increasefont(self):
        self.currentfont_size+=1
        self.textEdit.setFontPointSize(self.currentfont_size)
        
    def decreasefont(self):
        self.currentfont_size-=1
        self.textEdit.setFontPointSize(self.currentfont_size)
        
    def zoomin(self):
        self.current_zoom+=1
        self.textEdit.zoomIn(self.current_zoom)

        
    def zoomout(self):
        self.current_zoom-=1
        self.textEdit.zoomOut(self.current_zoom)
        
    def blueColor(self):
        self.textEdit.setTextColor(QtGui.QColor('blue'))
    
    def greenColor(self):
        self.textEdit.setTextColor(QtGui.QColor('green'))
        
    def blackColor(self):
        self.textEdit.setTextColor(QtGui.QColor('black'))
    
    def open(self):
        filename=QFileDialog.getOpenFileName(self,'open file','E:\PyQt5\TextEditor','Text files (*.txt)')
        self.setWindowTitle(filename[0])
        with open(filename[0],'r') as f:
            filetext=f.read()
            self.textEdit.setText(filetext)
        self.current_path =filename[0]
       
    def replace(self):
        print("Replace clicked")
        
    def light(self):
         self.setStyleSheet('')
        
    def dark(self):
        self.setStyleSheet('''
             QWidget{
                 background-color:rgb(33,33,33) ;
                 color:white
             }     
             QTextEdit{
                 background-color:rgb(46,46,46) ;
             }   
             QenuBar::item:selected{
                 color:#000000;
                 }     
        ''')
        
    def delete(self):
        print("Delete clicked")
        
    def selectAll(self):
        self.textEdit.selectAll ()
        
        
        
        
         
if __name__ == "__main__":
    app=QApplication(sys.argv)
    
    ui=Main()
    ui.show()
    app.exec_()