import pygame

class StartMenu:

    def __init__(self, background, logo, settings):
        self.Background = background
        self.Logo = logo
        self.Settings = settings

    def Update(self):
        return StartMenu(map((lambda smi: smi.Update()), self.StartMenuItems.map()))

    def Draw(self, screen):

        # Extra screen-based properties
        screen_centerX = int(self.Settings.Resolution.X / 2)
        screen_centerY = int(self.Settings.Resolution.Y / 2)
        screen_marginX = int(self.Settings.Resolution.Y / 18)
       
        gLogoSize = self.Logo.get_rect()
        gLogoCenter = (screen_centerX - gLogoSize.centerx, screen_marginX)

         # Basic screen loaded elements
        screen.fill((255, 255, 255))
        screen.blit(self.Background, (0,0))
        screen.blit(self.Logo, gLogoCenter)
        
        #pass
        #for smi in self.StartMenuItems:
        #    smi.Draw()