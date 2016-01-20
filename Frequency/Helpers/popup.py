import pygame

class Popup:

    def __init__(self, screen, content,
                width=960,
                height=540,
                x=0,
                y=0,
                backgroundColor=(0,0,0),
                textColor=(255,255,255),
                fontsize=32
                ):

        self.Screen = screen
        self.X = x
        self.Y = y
        self.Width = width
        self.Height = height
        self.Content = content
        self.BackgroundColor = backgroundColor
        self.TextColor = textColor
        self.Fontsize = fontsize
        self.CloseButton = None
        self.text = None


    def Update(self, events):
        # Handle all the events
        for event in events:
            if self.CloseButton is not None and event.type == pygame.MOUSEBUTTONUP:
                mousePosition = pygame.mouse.get_pos()
                if self.CloseButton.collidepoint(mousePosition):
                    return None
                else :
                    return self
        return self


    def Draw(self):
        # Create a font
        font = pygame.font.Font(None, self.Fontsize)

        # Render the text
        text = font.render(self.Content, True, self.TextColor)

        # Create a rectangle
        textRect = text.get_rect()

        # Get X and Y position
        drawPosition = self.DrawPosition()

        # Draw background
        pygame.draw.rect(self.Screen, self.BackgroundColor, (drawPosition['X'], drawPosition['Y'], self.Width, self.Height))

        # Draw the close popup button
        self.CloseButton = pygame.draw.rect(self.Screen, (255, 0, 0), (drawPosition['X'] + self.Width -20, drawPosition['Y'], 20, 20))

        # Center the rectangle
        textRect.centerx = drawPosition['X'] + self.Width//2
        textRect.centery = drawPosition['Y'] + self.Height//2

        # Blit the text
        self.Screen.blit(text, textRect)
        pygame.display.update()


    def DrawPosition(self):
        # Define local variables
        centerX = self.Screen.get_rect().centerx
        centerY = self.Screen.get_rect().centery

        # Calculate the X and Y position
        positionX = centerX - (self.Width//2) if self.X == 0 else self.X
        positionY = centerY - (self.Height//2) if self.Y == 0 else self.Y

        # Return the position as a list
        return {'X': positionX, 'Y': positionY}