import pygame, sys

def textDisp(display,text, posx, posy, font, color, size,background=None,posType="topleft" ):
  try:
    fontObj = pygame.font.Font(font, size)
    textSurfaceObj = fontObj.render(text, True, color, background)
    textRectObj = textSurfaceObj.get_rect()

    if posType == "center":
      textRectObj.center = (posx, posy)
    elif posType == "top":
      textRectObj.top = posy
    elif posType == "bottom":
      textRectObj.bottom = posy
    elif posType == "topright":
      textRectObj.topright = (posx,posy)
    elif posType == "topleft":
      textRectObj.topleft = (posx,posy)
    elif posType == "bottomright":
      textRectObj.bottomright = (posx,posy)
    elif posType == "bottomleft":
      textRectObj.bottomleft = (posx,posy)

    display.blit(textSurfaceObj,textRectObj)
  
  except IOError as e:
    #print(e)
    pass

def main():
  X=500
  Y=500
  pygame.init()
  Surface = pygame.display.set_mode((X,Y),0,32)
  pygame.display.set_caption("Mirror Test")

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    Surface.fill((255,255,255))
    textDisp(Surface,"hello World",100,200,pygame.font.get_default_font(),(0,0,255),60,(0,0,0))
    pygame.display.update()

main()