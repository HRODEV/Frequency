import pygame

class Popup:

    def __init__(self, screen, content,
                width=960,
                height=540,
                x=0,
                y=0,
                backgroundColor=(0,0,0),
                textColor=(255,255,255),
                fontsize=24,
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


    def Draw(self, file):
        # Create a font
        textFont = pygame.font.Font(None, self.Fontsize)

        # Render the basic font so we can use this for the rectangle
        textRender = textFont.render('', True, self.TextColor, self.BackgroundColor)

        # Get the text lines from the file
        instructionsFile = open(file)
        self.Content = instructionsFile.readlines()
        instructionsFile.close()

        # Create a rectangle
        textRect = textRender.get_rect()

        # Get X and Y position
        drawPosition = self.DrawPosition()

        # Center the rectangle
        textRect.centerx = self.Width//4
        textRect.centery = self.Height//20

        # Draw background
        pygame.draw.rect(self.Screen, self.BackgroundColor, (drawPosition['X'], drawPosition['Y'], self.Width, self.Height))
        # Load the image
        btn = pygame.image.load('images/buttons/closeButton.png')
        # Blit the close button
        self.CloseButton = self.Screen.blit(btn, (drawPosition['X'] + self.Width-20, textRect.centery))

        # Place the text on the screen
        for index in self.Content:
            # We render the text on the screen.
            # [:-1] = Starts at 0, ends at 1 before the last element
            content = textFont.render(index[:-1], True, self.TextColor)
            # 25 margin bottom
            textRect.centery += 25
            # Blit the text
            self.Screen.blit(content, textRect)

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