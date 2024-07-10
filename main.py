# Imports
import pygame
import sys
import random

# Initialise pygame
pygame.init()

# Initialize screen and set window dimensions
WIDTH = 500
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Basic settings for pygame
clock = pygame.time.Clock()  # Used for frame rate setting

# Font sizes
fontTitle = pygame.font.Font(None, 50)
fontSubitle = pygame.font.Font(None, 30)
fontParagraph = pygame.font.Font(None, 25)

# Initialize global variables
background = pygame.image.load('images/galaxyfaraway.png')

# Initialize variables for calculating the final score that the user got
ending_hps = []
ending_fuels = []


# UTIL FUNCTIONS
def clearScreen():
    screen.fill((0, 0, 0))  # Fill screen to be black
    pygame.display.flip()  # Update screen


def setBackground(imageName):
    # Get global background variable
    global background
    # Set background image
    background = pygame.image.load(f'images/{imageName}')
    # Scale image to fit screen
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    # Set background to screen
    screen.blit(background, (0, 0))
    # Update the screen
    pygame.display.update()


def continuationHandler():
    # Wait for user to press a key to start
    endLoop = False
    while not endLoop:  # Using not instead of comparison
        # Event listener
        for event in pygame.event.get():
            # User has clicked a key
            if event.type == pygame.KEYDOWN:
                endLoop = True
            # User clicks the exit button
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def createClickBox(text, box_color, text_color, box_x, box_y, box_w, box_h):
    # Initialize local variables
    mouse_pos = 0

    # Render box and text (used once)
    box_rect = pygame.Rect(box_x, box_y, box_w, box_h)
    text_surface = fontTitle.render(text, True, text_color)

    # Get the rectangle of the text surface to center it within the box (used once)
    text_rect = text_surface.get_rect(center=box_rect.center)

    running = True  # Running variable only for the while loop
    while running:
        for event in pygame.event.get():
            # Event handler for when user clicks their mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if box_rect.collidepoint(mouse_pos):
                    running = False  # Terminate loop, button clicked

        # Draw the box and text
        pygame.draw.rect(screen, box_color, box_rect)
        screen.blit(text_surface, text_rect)

        # Update the display
        pygame.display.flip()


def createCaption(text, captionHeight, bgColor, textColor, postition):
    # Initialize local variables
    lines = []
    current_line = []
    captionBox = 0
    max_width = 0
    max_height = 0
    words = 0
    space_width = 0
    space_height = 0
    word_width = 0
    word_height = 0
    captionBox = 0
    captionText = ""

    # ___ CAPTION BOX ___
    # Create the caption surface with dimensions
    captionBox = pygame.Surface((WIDTH, captionHeight))
    # Fill caption box with a color
    captionBox.fill(bgColor)

    # ___ CAPTION TEXT ___
    # Split text into words
    words = text.split(' ')
    # Retrieve the width and heigh of fontParagraph
    space_width, space_height = fontParagraph.size(' ')
    # Set the boundaries of the caption box
    max_width, max_height = WIDTH, captionHeight
    # Set the initial places of x and y
    x, y = 0, 0
    
    # Iterate through each word and add it to the line
    for word in words:
        # Retrieve the width and height of word
        word_width, word_height = fontParagraph.size(word)
        # If the word is less than the max width of the box
        if x + word_width <= max_width:
            # Add the word to the line
            current_line.append(word)
            # Add how much space is used up for the current line
            x += word_width + space_width
        # When we reached the max width of box
        else:
            # Join the list of words in current line together
            lines.append(' '.join(current_line))
            # Current line will be reset and set the first word in the line
            current_line = [word]
            # Add how much space is used up for the current line
            x = word_width + space_width
            # Add how much space is used up for the height of the box
            y += word_height

    lines.append(' '.join(current_line))  # Add the last line
    lines.append(" ")  # Add space
    lines.append(
        "[Press Any Key to Continue]")  # Add [Press Space to Continue] at end

    # Render each line and blit it onto the captionBox
    y = 10  # Reset y so it can be used as the index for rendering lines (10 is the magin on top of text)
    for line in lines:
        captionText = fontParagraph.render(line, True, textColor)
        captionBox.blit(captionText, (0, y))
        y += space_height  # Go to y position of next line

    # Set caption in box
    if postition == "bottom":
        screen.blit(captionBox, (0, HEIGHT - captionHeight))
    else:
        screen.blit(captionBox, (0, 0))

    # Update the screen
    pygame.display.update()


# START SCREEN
def s_start():
    # Set background
    setBackground("galaxyfaraway.png")

    # Render start message (used once)
    startMsg1 = fontTitle.render("The Story of Star Boy", False, "white")
    startMsg2 = fontSubitle.render("Press Any Key to Start", False, "White")

    # Get the dimensions of the start message (used once)
    startMsg1_rect = startMsg1.get_rect()
    startMsg2_rect = startMsg2.get_rect()

    # Display captions
    screen.blit(startMsg1, ((WIDTH - startMsg1_rect.width) // 2,
                            (HEIGHT - startMsg1_rect.height) // 2))
    screen.blit(
        startMsg2,
        ((WIDTH - startMsg1_rect.width) // 2,
         (HEIGHT - startMsg2_rect.height) // 2 + startMsg1_rect.height))

    # Update the screen
    pygame.display.update()

    continuationHandler()  # Wait for user response


# BEGINNING SCENES
def s_beginning():
    # List of scenes in order of occurance
    scenesPictures = [
        "starcollision.png", "shootingstar.png", "boyonrooftop.png",
        "alleyscene1.png", "alleyscene2.png", "alleyscene3.png",
        "alleyscene4.png", "darknebula1.png", "darknebula2.png", "skyscene.png"
    ]
    # List of captions corresponding to the scenes in order of occurance
    scenesText = [
        [
            "In a galaxy far, far away, two neutron stars hurtled towards each other at unimaginable speeds. Suddenly, BOOM! The stars collided in a spectacular explosion, sending ripples through the universe and flinging fragments in all directions, creating a dazzling cosmic display.",
            150, "Black", "White", "top"
        ],
        [
            "However, one particularly special star fragment hurled towards the Earth's solar system.",
            80, "Black", "White", "bottom"
        ],
        [
            "On Earth, there was a boy who was enjoying the views of the city, unaware that this day, his fate would change.",
            80, "Black", "White", "bottom"
        ],
        [
            "Unexpectedly, the boy was knocked off the building by a tremendous force. But somehow, he survived the fall as a faint glow of a star illuminated his body.",
            110, "Black", "White", "bottom"
        ],
        [
            "The bright light from the star then started to glow, slowly enveloping the boy's body.",
            80, "Black", "White", "bottom"
        ],
        [
            "The starlight swallowed the boy whole, and he started to levitate into the air.",
            80, "Black", "White", "bottom"
        ],
        [
            "When the boy opened his eyes, he had fully transformed into a star. He discovered that he could harness energy and fly, making him incredibly happy.",
            100, "Black", "White", "bottom"
        ],
        [
            "But little did Star Boy know, in a nearby galaxy, an entity named Dark Nebula wanted the star fragment for itself. Dark Nebula gathered all its space monkey minions to go to Earth and take the star fragment from Star Boy.",
            140, "Black", "White", "bottom"
        ],
        [
            "Thankfully, a voice in Star Boy's head warned him of Dark Nebula's plans, and Star Boy knew he had to go to Dark Nebula and take the fight away from Earth.",
            110, "Black", "White", "bottom"
        ],
        [
            "So Star Boy harnessed energy and used it to fly. His first obstacle was to fly out of Earth's atmosphere by collecting scattered energy.",
            110, "Black", "White", "top"
        ]
    ]

    clearScreen()

    # Loop through all of the scenes, set background, and set captions
    for index in range(len(scenesPictures)):
        setBackground(scenesPictures[index])
        createCaption(scenesText[index][0], scenesText[index][1],
                      scenesText[index][2], scenesText[index][3],
                      scenesText[index][4])

        # Update the screen
        pygame.display.update()

        # Wait for response from user before continuing
        continuationHandler()  # Wait for user response


# CUT SCENES
def cut_scene1():
    # Initialize local variables
    frameRate = 20
    starBoySize = 65
    starBoySizeMax = 200
    starBoyInitY = 400
    starBoyY = starBoyInitY
    starBoy_rect = 0
    starBoy_image = pygame.image.load('images/starboyWithTrail.png')

    clearScreen()
    setBackground("outofearth1.png")  # Set scene background

    # Animation of Star Boy flying out of Earth's atmosphere
    running = True  # Running variable only for the while loop
    while running:
        # Clear screen and set background
        clearScreen()

        # Clear the screen by redrawing the background
        screen.blit(background, (0, 0))

        # Update size if it is less than the maximum size
        if starBoySize < starBoySizeMax:
            starBoySize += 5

        # Update position to move up
        starBoyY -= 8

        # Check if Star Boy has moved out of the screen
        if starBoyY + starBoySize < 0:
            running = False  # Stop loop and continue cut scene

        # Update Star Boy size and position
        scaled_starBoy_image = pygame.transform.scale(
            starBoy_image, (starBoySize, starBoySize))
        starBoy_rect = scaled_starBoy_image.get_rect(center=(WIDTH / 2,
                                                             starBoyY +
                                                             starBoySize / 2))

        # Draw Star Boy at the updated position
        screen.blit(scaled_starBoy_image, starBoy_rect)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(frameRate)

    # Scene part 1
    clearScreen()
    setBackground("outofearth2.png")  # Set scene background
    createCaption(
        "With your help, Star Boy left Earth's atmosphere and continue his journey through space. But oh no! What is that up ahead?!?",
        110, "Black", "White", "top")
    continuationHandler()  # Wait for user response

    # Scene part 2
    clearScreen()
    setBackground("outofearth3.png")  # Set scene background
    createCaption(
        "It's Dark Nebula's minion, Enemy! Is that an explosive banana hes holding? We better avoid that! Help Star Boy fly past the space monkey's attacks.",
        110, "Black", "White", "top")
    continuationHandler()  # Wait for user response


def cut_scene2():
    # Scene part 1
    clearScreen()
    setBackground("darknebulascene1.png")
    createCaption(
        "Star Boy flew at full speed past the Enemy, entering a dark and eerie galaxy. Little did he know that very soon he would encounter a formidable and mysterious presence.",
        110, "Black", "White", "top")
    continuationHandler()  # Wait for user response

    # Scene part 2
    clearScreen()
    setBackground("darknebulascene2.png")
    createCaption(
        "As he flew further, he heard a distant, thundering, and terrifying crackle. Suddenly, things started to get darker, and the energy became scarce.",
        110, "Black", "White", "top")
    continuationHandler()  # Wait for user response

    # Scene part 3
    clearScreen()
    setBackground("darknebulascene3.png")
    createCaption(
        "[Dark Nebula] Finally, we meet, Star Boy! HAHAHAHAHA! It's too bad for you, though. That star fragment belongs to me! How nice of you to come directly to me—it saves me the trouble of hunting you down!",
        120, "Black", "White", "bottom")
    continuationHandler()  # Wait for user response


def final_scene():
    # Initialize local variables
    explosion_size = 200
    explosion_growth_rate = 5
    explosion_occurance = 400  # frames
    exploding = False
    explosing_x = 0
    explosing_y = 0
    final_score = 0
    frameRate = 20

    darknebula_rect = 0

    darknebula_image = 0
    finalscene_image = 0
    explosion_image = 0
    darknebula_scaled = 0

    # Load images
    darknebula_image = pygame.image.load('images/darknebula_sad.png')
    finalscene_image = pygame.image.load('images/finalscene.png')
    explosion_image = pygame.image.load(
        'images/explosion.png')  # Ensure you have an explosion image

    # Set the co-ordinates of explostion
    explosing_x = WIDTH // 2
    explosing_y = HEIGHT // 2 - 100

    # Set Dark nebula's box for animation control
    darknebula_rect = darknebula_image.get_rect(center=(explosing_x,
                                                        explosing_y))

    # Set the background once
    background = pygame.image.load('images/finalscene.png')
    screen.blit(background, (0, 0))

    # Calculate the final score
    final_score = calculateTotalScore()

    # Animation loop
    running = True
    while running:
        if not exploding:
            explosion_size += explosion_growth_rate  # Increase the size for explostion effect
            # Set the new size of the explstion
            darknebula_scaled = pygame.transform.scale(
                darknebula_image, (explosion_size, explosion_size))
            # Reset the co-ordinates of the explostion with the scaled image
            darknebula_rect = darknebula_scaled.get_rect(center=(explosing_x,
                                                                 explosing_y))
            screen.blit(background, (0, 0))  # Redraw the background
            screen.blit(darknebula_scaled,
                        darknebula_rect)  # Redraw dark nebula

            # Change the image to the exmplostion image when it reaches eplosion point
            if explosion_size > explosion_occurance:
                exploding = True
        else:
            # Set the box for the explosion image with the co-ordinates
            explosion_rect = explosion_image.get_rect(center=(explosing_x,
                                                              explosing_y))
            screen.blit(background, (0, 0))  # Redraw the background
            screen.blit(explosion_image, explosion_rect)  # Draw the explosion
            running = False  # Leave animation loop

        # Update the dispaly
        pygame.display.flip()

        # Cap frame rate
        clock.tick(frameRate)

    # Create and place an ending caption
    createCaption(
        "After a long-fought battle and with your help, the battered Dark Nebula contracted under the relentless barrage of light pulses, then expanded and exploded across space. Finally, Dark Nebula was defeated. And that is the end of the story of Star Boy.",
        140, "Black", "White", "top")
    continuationHandler()  # Wait for user response

    clearScreen()
    setBackground("endcover.png")

    # Set the final score message and create a rect so it can be used to be put in the middle of screen
    scoreMsg = fontTitle.render(f"{final_score:,}", False, "white")
    scoreMsg_rect = scoreMsg.get_rect()

    # Display captions
    screen.blit(scoreMsg, ((WIDTH - scoreMsg_rect.width) // 2,
                           (HEIGHT - scoreMsg_rect.height) // 2))

    # Update the screen
    pygame.display.update()
    continuationHandler()  # Wait for user response


# TOTAL SCORE CALCULATOR
def calculateTotalScore():
    # Get global ending points
    global ending_hps
    global ending_fuels

    # Initialize local variables
    final_score = 0

    # Loop through all ending hps and calculate the score user has achieved
    for index in range(len(ending_hps)):
        final_score += (
            index + 1) * ending_hps[index]  # Higher scores for higher levels

    # Loop through all ending fuels and calculate the score user has achieved
    for index in range(len(ending_fuels)):
        final_score += (
            index + 1) * ending_fuels[index]  # Higher scores for higher levels

    return final_score  # Return the final score


# LEVELS GENERATOR
def levelGenerator(level, bg, altitudeGoal, outlineColor, enemyImage):
    # Initialize global variables
    global ending_hps
    global ending_fuels
    
    # Initialize local variables
    timeElapsed = 0
    starBoySize = 65
    enemy_size = 100
    energySize = 40
    banana_size = 70
    lightPulse_size = 30
    explosion_size = 100
    yLevel = 0
    yLine = 0
    frameRate = 60

    starBoy_health = 5
    starBoy_attackCharge = 10
    starBoy_maxAttackCharge = 10

    trail_width = 10
    trail_maxHeight = 180
    trail_yLevel = 0

    fuelPercent = 0
    maxFuel = 100
    fuel = 100
    fuelDepletionRate = 90  # Increase to deplete fuel slower (per amount of frames)
    fuelDepletion_counter = 0
    fuelLossPerDepletion = 5
    fuelPerEnergy = 3
    altitude = 0
    altitudeRate = 10  # Increase to make gaining altitude easier

    energy_x = 0
    energy_dropRate = 30  # Increase to drop energy more often (per amount of frames)
    energy_dropSpeed = 10  # Increase to make energy drop faster
    energy_boxes = []
    energyDrop_counter = 0

    enemy_direction = 1  # Initially moving right (1 for right and -1 for left)
    enemy_speed = 1
    enemy_yLevel = 90
    enemy_health = 100

    banana_boxes = []
    banana_drop_counter = 0
    banana_dropSpeed = 4
    banana_dropRate = 120  # Increase to drop energy more often (per amount of frames)

    lightPulsePerEnergy = 1
    lightPulse_boxes = []
    lightPulse_speed = 6
    lightPulse_storage = 20
    lightPule_storageMax = 20
    lightPulse_launch = False  # For handling key event but displaying later

    starBoy_rect = 0
    trail_rect = 0
    enemy_rect = 0

    starBoy_image = 0
    energy_image = 0
    banana_image = 0
    enemy_image = 0
    explosion_image = 0
    lightPulse_image = 0

    # Set y-levels
    yLevel = HEIGHT - 3 * starBoySize
    yLine = yLevel + starBoySize + 20  # y-coordinate of line below Star Boy
    trail_yLevel = yLevel + starBoySize - 20

    clearScreen()

    # Set level start background
    setBackground(f"levelcover{level}.png")

    # Wait for response from user before starting game
    continuationHandler()  # Wait for user response

    clearScreen()

    # Load and scale the level background image once
    setBackground(bg)

    # Load images
    starBoy_image = pygame.image.load('images/starboy.png')
    energy_image = pygame.image.load('images/energy.png')
    banana_image = pygame.image.load('images/explosivebanana.png')
    explosion_image = pygame.image.load('images/explosion.png')
    enemy_image = pygame.image.load(
        f'images/{enemyImage or "spacemonkey.png"}'
    )  # Render space monkey if there is no image
    lightPulse_image = pygame.image.load("images/lightPulse.png")

    # Scaling images
    starBoy_image = pygame.transform.scale(starBoy_image,
                                           (starBoySize, starBoySize))
    energy_image = pygame.transform.scale(energy_image,
                                          (energySize, energySize))
    banana_image = pygame.transform.scale(banana_image,
                                          (banana_size, banana_size))
    explosion_image = pygame.transform.scale(explosion_image,
                                             (explosion_size, explosion_size))
    enemy_image = pygame.transform.scale(enemy_image, (enemy_size, enemy_size))
    lightPulse_image = pygame.transform.scale(
        lightPulse_image, (lightPulse_size, lightPulse_size))

    # Create a rect for Star Boy to manage its position
    starBoy_rect = starBoy_image.get_rect()
    starBoy_rect.y = yLevel

    # Render trail with rect
    trail_rect = pygame.Rect(starBoy_rect.x, trail_yLevel, trail_width,
                             trail_maxHeight)

    # Render Enemy with rect
    enemy_rect = enemy_image.get_rect()
    enemy_rect.y = enemy_yLevel  # Starting y position

    # Main game loop for the level
    running = True  # Running variable only for the while loop
    while running:
        timeElapsed += 1  # Increase how much time has passed
        # Get user events
        for event in pygame.event.get():
            # Handle user quiting program
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Handle if user presses space to shoot light pulse and if they are allowed to
            if (level == 3 and event.type == pygame.KEYDOWN
                    and event.key == pygame.K_SPACE
                    and lightPulse_storage > 0):
                lightPulse_launch = True

        # Clear the screen by redrawing the background
        screen.blit(background, (0, 0))

        # Get the current mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # ________ Handle Fuel and Altitude ________
        # Deplete fuel at intervals
        fuelDepletion_counter += 1
        if fuelDepletion_counter > fuelDepletionRate:  # Fuel depletion per amount of frames
            fuel -= fuelLossPerDepletion  # Decrease fuel
            fuelPercent = round(fuel / maxFuel, 3)
            fuelDepletion_counter = 0  # Reset counter

        # Increase altitude according fuel
        altitude += int(altitudeRate * fuelPercent)

        # ________ Handle Star Boy ________
        # Update Star Boy's x position to follow the mouse, y position stays constant
        starBoy_rect.x = mouse_x - starBoy_rect.width // 2  # Center the image on the cursor horizontally

        # Update and draw trail position
        trail_rect.x = starBoy_rect.x + int(starBoySize / 2)
        trail_rect.y = trail_yLevel
        trail_rect.height = int(
            trail_maxHeight *
            fuelPercent)  # Change trail length depending on the amount of fuel
        pygame.draw.rect(screen, "yellow", trail_rect)

        # Draw Star Boy at the updated position
        screen.blit(starBoy_image, starBoy_rect)

        # Draw the fixed line under Star Boy
        pygame.draw.line(screen, outlineColor, (0, yLine), (WIDTH, yLine), 5)

        # ________ Handle Energy ________
        # Drop energy boxes at intervals
        energyDrop_counter += 1
        if energyDrop_counter > energy_dropRate:  # Drop an energy per amount of frames
            # Spawn energy at random location
            energy_x = random.randint(0, WIDTH - energySize)
            # Add energy to list of energies which is displayed on screen
            energy_boxes.append(
                pygame.Rect(energy_x, 0, energySize, energySize))
            energyDrop_counter = 0  # Reset counter

        # Update and draw energy boxes
        for energy_rect in energy_boxes[:]:
            energy_rect.y += energy_dropSpeed  # Move energy box down speed
            screen.blit(energy_image, energy_rect)  # Draw energy
            # Remove energy box if it goes off the screen
            if energy_rect.y > HEIGHT:
                energy_boxes.remove(energy_rect)

            # Handle when Star Boy touches energy
            if energy_rect.colliderect(starBoy_rect):
                energy_boxes.remove(energy_rect)  # remove energy from list

                # Check if fuel is not full then add more fuel
                if fuel < maxFuel:
                    if fuel + fuelPerEnergy > maxFuel:
                        fuel = maxFuel  # So fuel never goes over max fuel
                    else:
                        fuel += fuelPerEnergy  # Add fuel

                # Check if light pulse storage is not full then add more fuel
                if lightPulse_storage < lightPule_storageMax:
                    if lightPulse_storage + lightPulsePerEnergy > lightPule_storageMax:
                        lightPulse_storage = lightPule_storageMax  # So fuel never goes over max fuel
                    else:
                        lightPulse_storage += lightPulsePerEnergy  # Add fuel

        # ________ Handle Enemy Movement and Explosive Bananas ________
        # If the level is over 1
        if level > 1:
            # Move Enemy side to side
            enemy_rect.x += enemy_direction * enemy_speed
            if enemy_rect.right >= WIDTH or enemy_rect.left <= 0:
                enemy_direction *= -1  # Change direction when hitting screen edge

            # Draw Enemy
            screen.blit(enemy_image, enemy_rect)

            # Drop bananas at intervals based on drop_rate
            banana_drop_counter += 1
            if banana_drop_counter > banana_dropRate:
                # Randomly decide whether to drop from the monkey's x-coordinate or a random position
                if random.random(
                ) < 0.5:  # 50% chance to drop from the monkey's x-coordinate
                    banana_x = enemy_rect.centerx - banana_size // 2
                else:
                    banana_x = random.randint(0, WIDTH - banana_size)
                banana_boxes.append(
                    pygame.Rect(banana_x, enemy_rect.bottom, banana_size,
                                banana_size))
                banana_drop_counter = 0

            # Update and draw bananas
            for banana_rect in banana_boxes[:]:
                banana_rect.y += banana_dropSpeed  # Move explosive banana box down speed
                screen.blit(banana_image, banana_rect)  # Draw explosive banana

                # Remove explosive banana box if it goes off the screen
                if banana_rect.y > HEIGHT:
                    banana_boxes.remove(
                        banana_rect)  # remove explosive banana from list

                # Handle when Star Boy touches explosive banana
                if banana_rect.colliderect(starBoy_rect):
                    screen.blit(explosion_image,
                                banana_rect)  # Draw explosion on the banana
                    pygame.display.flip()  # Update the display for explosion
                    banana_boxes.remove(
                        banana_rect)  # remove explosive banana from list
                    starBoy_health -= 1  # Deduct health from Star Boy

        # _________ Handle Light Pulse Movement ________
        if lightPulse_launch:
            # Draw the light pulse from location of Star Boy
            lightPulse_boxes.append(
                pygame.Rect(starBoy_rect.centerx, yLevel, lightPulse_size,
                            lightPulse_size))
            lightPulse_storage -= 1  # Decrease a light pulse from the storage
            lightPulse_launch = False  # Reset pulse launch

        # Update and draw light pulses
        for lightPulse_rect in lightPulse_boxes[:]:
            lightPulse_rect.y -= lightPulse_speed  # Move the light pulse up the screen
            screen.blit(lightPulse_image, lightPulse_rect)  # Draw light pulse

            # Remove light pulse if it goes off the screen
            if lightPulse_rect.y > HEIGHT:
                lightPulse_boxes.remove(
                    lightPulse_rect)  # remove light pulse from list

            # Handle when Enemy touches light pulse
            if lightPulse_rect.colliderect(enemy_rect):
                lightPulse_boxes.remove(
                    lightPulse_rect)  # remove light pulse from list
                enemy_health -= 1  # Deduct health from enemy
                pygame.display.flip()  # Update the display for explosion

        # Display fuel (used once)
        fuel_text = fontParagraph.render(f"Fuel: {fuel}", True, outlineColor)
        screen.blit(fuel_text, (10, 20))

        # If the level is over 1, display health bar
        if level > 1:
            hp_text = fontParagraph.render(f"HP: {starBoy_health}", True,
                                           outlineColor)
            screen.blit(hp_text, (10, 60))

        # Handle if there is an altitude goal
        if altitudeGoal > 0:
            # Display altitude (used once)
            altitude_text = fontParagraph.render(
                f"Altitude: {altitude:,} / {altitudeGoal:,}", True,
                outlineColor)
            screen.blit(altitude_text, (10, 40))

            # Handle when the altitude goal is reached
            if altitude > altitudeGoal:
                running = False  # Exit level loop

                # Quick win animation
                while starBoy_rect.y > 0:
                    # ____ UPDATE TOTAL SCORE ____
                    ending_hps.append(starBoy_health)
                    ending_fuels.append(fuel)

                    # Decrease y levels for Star Boy and Trail
                    trail_yLevel -= 1
                    yLevel -= 1

                    # Set the new y levels to the trail and star boy
                    trail_rect.y = trail_yLevel
                    starBoy_rect.y = yLevel

                    # Clear the screen by redrawing the background
                    screen.blit(background, (0, 0))

                    # Draw Star Boy and trail at the updated position
                    pygame.draw.rect(screen, "yellow", trail_rect)
                    screen.blit(starBoy_image, starBoy_rect)

                    # Update the display
                    pygame.display.flip()
        # Handle if it is level 3 and there is an enemy to defeat
        elif level == 3:
            # Display enemy HP and light pulses avaliable
            enemyHP_text = fontParagraph.render(f"Enemy HP: {enemy_health}",
                                                True, outlineColor)
            screen.blit(enemyHP_text, (10, 40))
            lightPulse_text = fontParagraph.render(
                f"Light Pulses: {lightPulse_storage}", True, outlineColor)
            screen.blit(lightPulse_text, (10, 80))

            if enemy_health <= 0:
                # ____ UPDATE TOTAL SCORE ____
                ending_hps.append(starBoy_health)
                ending_fuels.append(fuel)

                running = False  # Exit level loop

        # Handle lose when the fuel or health is 0 or below
        if fuel <= 0 or starBoy_health <= 0:
            clearScreen()
            setBackground("gameover.png")  # Set game over background
            running = False  # Stop level loop

            # Create a click box for retrying level
            createClickBox("Retry Level", "White", "Black", 150, 550, 200, 80)
            levelGenerator(
                level, bg, altitudeGoal, outlineColor,
                enemyImage)  # Recursive which will run the level again

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(frameRate)


# MAIN FUNCTION
def main():
    s_start()
    s_beginning()
    levelGenerator(1, "sky.png", 30000, "White", None)
    cut_scene1()
    levelGenerator(2, "outerspace.png", 50000, "White", "spacemonkey.png")
    cut_scene2()
    levelGenerator(3, "finalbattlebg.png", 0, "White", "darknebula.png")
    final_scene()


# RUN MAIN FUNCTION
main()
