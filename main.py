from pyweb import pydom
from pyscript import document, when
from create_code import create_code

class MasterMind:
    """
        A Mastermind game written in PyScript
    """
    def __init__(self):
        self.log = document.getElementById("output_div")
        self.attempts = 0
        self.console = pydom["script#console"][0]
        self.new_game(None)

    def new_game(self, event):
        self.clear_terminal()
        self.attempts = 0
        self.gamestate = "running"
        self.secret_code = create_code()  
        self.log.innerHTML =""
        print('=================')
        print('NEW GAME STARTING')
        print(self.secret_code)                   

    def clear_terminal(self):
        self.console._js.terminal.clear()
    
    def toggle_terminal(self, event):
        hidden = self.console.parent._js.getAttribute("hidden")
        if hidden:
            self.console.parent._js.removeAttribute("hidden")
        else:
            self.console.parent._js.setAttribute("hidden", "hidden")

    def submit_guess(self,event):
        """
            Checks guess.
        """
        if self.gamestate == "running":
            guess = document.getElementById("guess-input").value
            
            if len(guess) != 4 or not all(c in "123456789" for c in guess):
                self.log.innerHTML += "❌ Invalid guess. Enter 4 digits between 1 and 9. <br>"
                return
    
            self.attempts  += 1
            black = sum(a == b for a, b in zip(self.secret_code, list(map(int, str(guess)))))
            white = len(list(set(self.secret_code).intersection(set(map(int, str(guess)))))) - black
    
            self.log.innerHTML += f"Attempt {self.attempts }: {guess} → ⚫ {black} black, ⚪ {white} white <br>"
        
            if black == 4:
                self.log.innerHTML += f"🎉 You cracked the code in {self.attempts } try! <br>"
                self.gamestate = "ended"
 
GAME = MasterMind()