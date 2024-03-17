import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants for the game window
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000
BG_COLOR = (50, 50, 50)  # A dark gray background

player_stats = {
    'hp': 10,  # Starting health points
    'mp': 0,   # Starting mana points
}

# Setup the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Not Enough Mana - Main Menu')

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Sample deck (placeholder for actual card objects)
card_types = {
    "Fire Arrow": 8,
    "Fireball": 6,
    "Meteor Shower": 3,
    "Armageddon": 1,
    "Mana Implosion": 2,
    "Ice Bolt": 6,
    "Blizzard": 3,
    "Ice Boomerang": 3,
    "Vampiric Touch": 3,
    "Freeze": 2,
    "Icy Grasp": 2,
    "Lightning": 9,
    "Electric Explosion": 3,
    "Blinding Flash": 2,
    "Electric Arc": 5,
    "Paralysing Touch": 2,
    "Magic Shield": 11,
    "Mirror Shield": 5,
    "Frozen Bunny": 1,
    "Last Wish": 1,
    "Magic Capture": 3,
    "Annihilation": 2,
    "Heal": 10,
    "Greater Heal": 4,
    "Book Exchange": 2,
    "Magic Hand": 2,
    "Force Field": 3,
    "Potent Elixir": 4,
    "Space Shift": 2,
    "Curse of Rules":3,
    "Curse of the Elder": 1,
    "Curse of the Younger": 1,
    "Curse of Vigour": 1,
    "Curse of Even": 1,
    "Curse of Odd": 1,
    "Fireproof Tiara": 1
}



def initialize_game():
    global player_stats, hand, deck
    # Reset player stats
    player_stats = {'hp': 10, 'mp': 0}

    deck = [card for card, quantity in card_types.items() for _ in range(quantity)]

    # Reset the player's hand (assuming you have a function to deal cards)
    num_cards_to_deal = 5
    hand = deal_cards(deck, num_cards_to_deal)  # Example: hand = deal_cards(deck, num_cards_to_deal)

    # Reset/recreate the deck
      
    random.shuffle(deck)  # Shuffle the deck

def deal_cards(deck, num_cards):
    random.shuffle(deck)  # Shuffle the deck
    hand = deck[:num_cards]  # Deal the specified number of cards from the deck to the hand
    del deck[:num_cards]  # Remove the dealt cards from the deck
    return hand




# Font for text rendering
font = pygame.font.SysFont(None, 55)

def draw_text(text, font, color, surface, x, y, center=False):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    if center:
        textrect.center = (x, y)
    else:
        textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
    while True:
        screen.fill(BG_COLOR)
        draw_text('Main Menu', font, WHITE, screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        button_3 = pygame.Rect(50, 300, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                initialize_game()
                play()
        if button_2.collidepoint((mx, my)):
            if click:
                rules()
        if button_3.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen, BLUE, button_1)
        pygame.draw.rect(screen, BLUE, button_2)
        pygame.draw.rect(screen, BLUE, button_3)

        draw_text('Play', font, WHITE, screen, 70, 110)
        draw_text('Rules', font, WHITE, screen, 70, 210)
        draw_text('Quit', font, WHITE, screen, 70, 310)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()

def create_button(text, x, y, w, h, color):
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, rect)
    draw_text(text, font, WHITE, screen, x + w // 2, y + h // 2, center=True)
    return rect

def load_card_images(card_type):
    return pygame.image.load(f"cards/{card_type}.png")


# Drawing the hand of cards, dynamically loading images
def draw_hand(hand):
    spacing = 20  # Space between cards
    card_images = [load_card_images(card_type) for card_type in hand]  # Load images for cards in hand
    
    # Calculate total width to center the hand
    total_width = sum(image.get_width() for image in card_images) + spacing * (len(hand) - 1)
    start_x = (SCREEN_WIDTH - total_width) // 2
    y = (SCREEN_HEIGHT - card_images[0].get_height()) // 2
    
    for image in card_images:
        screen.blit(image, (start_x, y))
        start_x += image.get_width() + spacing

def increase_hp(amount):
    player_stats['hp'] += amount
    player_stats['hp'] = min(player_stats['hp'], 100)  # Assuming 100 is the max HP

def increase_mp(amount):
    player_stats['mp'] += amount
    player_stats['mp'] = min(player_stats['mp'], 100)  # Assuming 100 is the max MP

def draw_stats():
    global hp_rect, mp_rect  # Use global variables to make these accessible in the play function
    hp_text = f"HP: {player_stats['hp']}"
    mp_text = f"MP: {player_stats['mp']}"
    hp_surface = font.render(hp_text, True, WHITE)
    mp_surface = font.render(mp_text, True, WHITE)

    hp_rect = hp_surface.get_rect(topleft=(20, SCREEN_HEIGHT - 80))
    mp_rect = mp_surface.get_rect(topleft=(20, SCREEN_HEIGHT - 40))

    screen.blit(hp_surface, hp_rect)
    screen.blit(mp_surface, mp_rect)


def play():
    running = True

    # Define the draw card button position and size
    draw_button_x, draw_button_y, draw_button_w, draw_button_h = SCREEN_WIDTH - 220, SCREEN_HEIGHT - 80, 200, 50
    draw_button = create_button('Draw Card', draw_button_x, draw_button_y, draw_button_w, draw_button_h, BLUE)

    while running:
        screen.fill(BG_COLOR)
        draw_hand(hand)  # Draw the hand with dynamic card images
        draw_stats()
        draw_button = create_button("Draw Card", draw_button_x, draw_button_y, draw_button_w, draw_button_h, BLUE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if draw_button.collidepoint(event.pos):
                    if deck:
                        hand.append(deck.pop())
                        print("Drew a card. Hand now has:", len(hand), "cards.")  # Debugging print
                    else:
                        print("Deck is empty.")
                # Check if the click is within the HP or MP display areas
                if hp_rect.collidepoint(event.pos):
                    increase_hp(1)  # Increase HP by 1
                elif mp_rect.collidepoint(event.pos):
                    increase_mp(1)  # Increase MP by 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Placeholder for ending turn (for demonstration)
                    running = False
        
        pygame.display.update()

def rules():
    running = True
    while running:
        screen.fill(BG_COLOR)
        
        draw_text('Rules', font, WHITE, screen, SCREEN_WIDTH // 2, 20, center=True)
        rules_text = [
            "1. The eldest wizard starts the game. Then, the wizards take their turns clockwise.",
            "2. You can drink mana potions at any point in the game (even outside your turn)."
            "Each potion replenishes 3 mana points. This value, alongside potion’s mana essence potency,",
            "can be adjusted to better account for the wizards’ might.",
            "There is no limit to how many mana points a wizard can accumulate.",
            "If there are no crystals in the common pool, mana potions grant no points.",
            "3. When you lose all health points or have Too Much Mana and cannot continue the fight,",
            "you are eliminated from the game.",
            "4. The battle ends when the last, victorious wizard remains on the battlefield."
        ]
        
        for i, rule in enumerate(rules_text):
            draw_text(rule, pygame.font.SysFont(None, 35), WHITE, screen, 20, 100 + i * 40)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                running = False
        
        pygame.display.update()

main_menu()


