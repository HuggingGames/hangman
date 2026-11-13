"""Mini-game by CAN YILDIRIM · Hugging Games."""
import random
import math

def reply(state, message):
    return state, message

def finish(state, message):
    state["done"] = True
    return state, message + "\n🏁 Oyun bitti. Yeniden başlat ile tekrar oyna."

WORDS=['python','galaksi','robot','oyuncu','kodlama','gezegen','bulmaca','piksel']
def _board(s):return ' '.join(c if c in s['guessed'] else '_' for c in s['word'])
def new_game():
    s={'word':random.choice(WORDS),'guessed':[],'lives':7,'done':False}
    return s,f"Kelime: {_board(s)} | 7 hakkın var. Tek harf yaz."
def play(s,action):
    a=action.strip().lower()
    if s['done']:return reply(s,"Yeni oyun başlat.")
    if len(a)!=1 or not a.isalpha():return reply(s,"Tek bir harf yaz.")
    if a in s['guessed']:return reply(s,"Bu harfi zaten denedin.")
    s['guessed'].append(a)
    if a not in s['word']:s['lives']-=1
    msg=f"{_board(s)} | Kalan hak: {s['lives']}"
    if all(c in s['guessed'] for c in s['word']):return finish(s,"🎉 Kazandın! "+msg)
    if s['lives']<=0:return finish(s,"Kaybettin, kelime: "+s['word'])
    return reply(s,msg)
