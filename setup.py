""" CODED BY HUSSAIN AFRIDI """
import os
from rich.panel import Panel
from rich.console import Console
console=Console()
W = "\033[1;37m";G2 = "\033[38;5;48m";R = "\033[38;5;196m";A1="\033[38;5;250m"
class setup():
  def __init__(self):
    self.zx=f'{R}● {W}'
    self.a=f'{W}|{G2}1{W}|{W} '
    self.b=f'{W}|{G2}2{W}|{W} '
    self.line = "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    self.fail = Panel.fit('[bold][red]PYCURL SETUP FAILED !!',border_style='bright_white')
    self.complete = Panel.fit('[bold][bright_green]PYCURL SETUP COMPLETE !!',border_style='bright_white')
    self.logo = Panel.fit("""[bold][bright_white]___  _   _ ____ _  _ ____ _    \n|__]  \_/  |    |  | |__/ |    \n|      |   |___ |__| |  \ |___ 
\n[deep_pink2]●[/deep_pink2] CODED BY [/bright_white][red]>>[/red] [bright_white]HUSSAIN AFRIDI[/bright_white][/bold]""",border_style='bright_white')
  def clean(self):
    os.system('clear')
    console.print(self.logo)
  def menu(self):
    self.clean()
    print(f'{self.a}START SETUP\n{self.b}EXIT TERMINAL\n{W}{self.line}')
    ax = input(f'{self.zx}CHOOSE {A1}: {G2}')
    if ax in ['1','a']:
      setup().install()
    elif ax in ['2','b']:
      exit(f'\n{W}{self.line}\n{self.zx}{G2}THANKS FOR USING !!')
    else:
      print(f'\n{W}{self.line}\n{self.zx}{R}WRONG INPUT !!');sleep(3);print(f'{W}{self.line}\n{G2}TRY AGAIN !! ');self.menu()
  def install(self):
    try:
      self.clean()
      print(f'{G2}WAIT FOR SETUP !! ')
      os.system('pip uninstall pycurl -y');os.system('mv pycurl.cpython-311.so /data/data/com.termux/files/usr/lib/python3.11/site-packages');os.system('chmod 777 /data/data/com.termux/files/usr/lib/python3.11/site-packages/pycurl.cpython-311.so');os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/curl');os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/pycurl-7.45.3.dist-info');os.system('mv pycurl-7.45.3.dist-info /data/data/com.termux/files/usr/lib/python3.11/site-packages');os.system('mv curl /data/data/com.termux/files/usr/lib/python3.11/site-packages');print(f'\n')
      console.print(self.complete)
      exit()
    except Exception as e :console.print(e);console.print(self.fail);exit()
setup().menu()
