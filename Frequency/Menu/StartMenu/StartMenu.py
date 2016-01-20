import pygame

class StartMenu:

    def __init__(self, background, logo, buttons, settings):
        self.Background = background
        self.Logo = logo
        self.Buttons = buttons
        self.Settings = settings

    def Update(self):
        return StartMenu(map((lambda smi: smi.Update()), self.StartMenuItems.map()))

    def Draw(self, screen):

        # Extra screen-based properties
        screen_centerX = int(self.Settings.Resolution.X / 2)
        screen_centerY = int(self.Settings.Resolution.Y / 2)
        screen_marginX = int(self.Settings.Resolution.Y / 18)
       
        # Logo position
        gLogoSize = self.Logo.get_rect()
        gLogoCenterX = screen_centerX - gLogoSize.centerx
        gLogoCenter = (gLogoCenterX, screen_marginX)

        # Basic margin for buttons
        topMargin = screen_centerY + 20
        
         # Basic screen loaded elements
        screen.fill((255, 255, 255))
        screen.blit(self.Background, (0,0))
        screen.blit(self.Logo, gLogoCenter)
        
        # Loop through every button and show it on the screen
        for name, btn in enumerate(self.Buttons):
            btnSize = btn.get_rect()
            # If it isn't the first button, the margin-top will be 70
            if (name != 0):
                topMargin += 70
            screen.blit(btn, ((screen_centerX - btnSize.centerx), topMargin))

            if(btn.get_rect().collidepoint(pygame.mouse.get_pos())):
                print('Hovered!')
        
        #pass
        #for smi in self.StartMenuItems:
        #    smi.Draw()