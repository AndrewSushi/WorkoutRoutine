from bardapi import Bard

token = 'Ywh86LjgaRZp2GIRlNofoGjHKkW8yUzp4iYXXlZGnziQHZ4R6hASf5s4mpuIo4SGi8B3Qg.'
bard = Bard(token=token)
answer = bard.get_answer("How do you make spaghetti")