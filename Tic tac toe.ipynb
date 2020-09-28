{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "pygame 1.9.6\n",
      "Hello from the pygame community. https://www.pygame.org/contribute.html\n"
     ]
    }
   ],
   "source": [
    "import pygame as pg,sys\n",
    "from pygame.locals import *\n",
    "import time\n",
    "XO = 'x'\n",
    "winner = None\n",
    "draw = False\n",
    "width = 400\n",
    "height = 400\n",
    "white = (255, 255, 255)\n",
    "line_color = (10, 10, 10)\n",
    "TTT = [[None]*3, [None]*3, [None]*3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "pg.init()\n",
    "fps = 30\n",
    "CLOCK = pg.time.Clock()\n",
    "screen = pg.display.set_mode((width,\n",
    "                     height+100), 0, 32)\n",
    "pg.display.set_caption(\"Tic Tac Toe\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "opening = pg.image.load('Pictures/tic tac opening.png')\n",
    "x_img = pg.image.load('Pictures/x.png')\n",
    "o_img = pg.image.load('Pictures/o.png')\n",
    "x_img = pg.transform.scale(x_img,(80, 80))\n",
    "o_img = pg.transform.scale(o_img,(80, 80))\n",
    "opening = pg.transform.scale(opening,(width, height+100))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def game_opening():\n",
    "    screen.blit(opening,(0,0))\n",
    "    pg.display.update()\n",
    "    time.sleep(1)\n",
    "    screen.fill(white)\n",
    "    pg.draw.line(screen,line_color,(width/3,0),(width/3, height),7)\n",
    "    pg.draw.line(screen,line_color,(width/3*2,0),(width/3*2, height),7)\n",
    "    pg.draw.line(screen,line_color,(0,height/3),(width, height/3),7)\n",
    "    pg.draw.line(screen,line_color,(0,height/3*2),(width, height/3*2),7)\n",
    "    draw_status()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def draw_status():\n",
    "    global draw\n",
    "    if winner is None:\n",
    "        message = XO.upper() + \"'s Turn\"\n",
    "    else:\n",
    "        message = winner.upper() + \" won!\"\n",
    "    if draw:\n",
    "        message = 'Game Draw!'\n",
    "    font = pg.font.Font(None, 30)\n",
    "    text = font.render(message, 1, (255, 255, 255))\n",
    "    screen.fill ((0, 0, 0), (0, 400, 500, 100))\n",
    "    text_rect = text.get_rect(center=(width/2, 500-50))\n",
    "    screen.blit(text, text_rect)\n",
    "    pg.display.update()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def check_win():\n",
    "    global TTT, winner,draw\n",
    "    for row in range (0,3):\n",
    "        if ((TTT [row][0] == TTT[row][1] == TTT[row][2]) and(TTT [row][0] is not None)):\n",
    "            winner = TTT[row][0]\n",
    "            pg.draw.line(screen, (250,0,0), (0, (row + 1)*height/3 -height/6),\\\n",
    "                              (width, (row + 1)*height/3 - height/6 ), 4)\n",
    "            break\n",
    "    for col in range (0, 3):\n",
    "        if (TTT[0][col] == TTT[1][col] == TTT[2][col]) and (TTT[0][col] is not None):\n",
    "            winner = TTT[0][col]\n",
    "            pg.draw.line (screen, (250,0,0),((col + 1)* width/3 - width/6, 0),\\\n",
    "                          ((col + 1)* width/3 - width/6, height), 4)\n",
    "            break\n",
    "    if (TTT[0][0] == TTT[1][1] == TTT[2][2]) and (TTT[0][0] is not None):\n",
    "        winner = TTT[0][0]\n",
    "        pg.draw.line (screen, (250,70,70), (50, 50), (350, 350), 4)\n",
    "    if (TTT[0][2] == TTT[1][1] == TTT[2][0]) and (TTT[0][2] is not None):\n",
    "        winner = TTT[0][2]\n",
    "        pg.draw.line (screen, (250,70,70), (350, 50), (50, 350), 4)\n",
    "    if(all([all(row) for row in TTT]) and winner is None ):\n",
    "        draw = True\n",
    "    draw_status()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "def drawXO(row,col):\n",
    "    global TTT,XO\n",
    "    if row==1:\n",
    "        posx = 30\n",
    "    if row==2:\n",
    "        posx = width/3 + 30\n",
    "    if row==3:\n",
    "        posx = width/3*2 + 30\n",
    "    if col==1:\n",
    "        posy = 30\n",
    "    if col==2:\n",
    "        posy = height/3 + 30\n",
    "    if col==3:\n",
    "        posy = height/3*2 + 30\n",
    "    TTT[row-1][col-1] = XO\n",
    "    if(XO == 'x'):\n",
    "        screen.blit(x_img,(posy,posx))\n",
    "        XO= 'o'\n",
    "    else:\n",
    "        screen.blit(o_img,(posy,posx))\n",
    "        XO= 'x'\n",
    "    pg.display.update()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "def userClick():\n",
    "    x,y = pg.mouse.get_pos()\n",
    "    if(x<width/3):\n",
    "        col = 1\n",
    "    elif (x<width/3*2):\n",
    "        col = 2\n",
    "    elif(x<width):\n",
    "        col = 3\n",
    "    else:\n",
    "        col = None\n",
    "    if(y<height/3):\n",
    "        row = 1\n",
    "    elif (y<height/3*2):\n",
    "        row = 2\n",
    "    elif(y<height):\n",
    "        row = 3\n",
    "    else:\n",
    "        row = None\n",
    "    if(row and col and TTT[row-1][col-1] is None):\n",
    "        global XO\n",
    "        drawXO(row,col)\n",
    "        check_win()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "def reset_game():\n",
    "    global TTT, winner,XO, draw\n",
    "    time.sleep(3)\n",
    "    XO = 'x'\n",
    "    draw = False\n",
    "    game_opening()\n",
    "    winner=None\n",
    "    TTT = [[None]*3,[None]*3,[None]*3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyboardInterrupt",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-10-b97e09688c05>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     11\u001b[0m                 \u001b[0mreset_game\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     12\u001b[0m     \u001b[0mpg\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdisplay\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 13\u001b[1;33m     \u001b[0mCLOCK\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtick\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfps\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: "
     ]
    }
   ],
   "source": [
    "game_opening()\n",
    "while(True):\n",
    "    for event in pg.event.get():\n",
    "        if event.type == QUIT:\n",
    "            pg.quit()\n",
    "            sys.exit()\n",
    "        elif event.type is MOUSEBUTTONDOWN:\n",
    "            # the user clicked; place an X or O\n",
    "            userClick()\n",
    "            if(winner or draw):\n",
    "                reset_game()\n",
    "    pg.display.update()\n",
    "    CLOCK.tick(fps)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
