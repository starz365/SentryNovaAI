import time
import sys
from pyfiglet import Figlet
from termcolor import colored
from colorama import init, Fore, Style

def main_logo():
    try:
        # Set up the figlet font (trying different fonts for best mobile fit)
        try:
            f = Figlet(font='big')
        except:
            f = Figlet(font='standard')  # Fallback to standard if big not available
        
        # Generate ASCII art for "Mwikya Os" exactly as spelled
        ascii_art = f.renderText('Mwikya Os')
        
        # Split the ASCII art into lines and remove empty lines
        lines = [line for line in ascii_art.split('\n') if line.strip()]
        
        # Ensure it fits mobile screen (80 chars width max)
        max_width = max(len(line) for line in lines)
        if max_width > 80:
            f = Figlet(font='standard')
            ascii_art = f.renderText('Mwikya Os')
            lines = [line for line in ascii_art.split('\n') if line.strip()]
        
        # Available green colors in termcolor
        green_colors = ['green', 'light_green', 'light_cyan', 'light_yellow']
        
        # Color each line with different shades
        colored_lines = []
        for i, line in enumerate(lines):
            color = green_colors[i % len(green_colors)]
            try:
                colored_lines.append(colored(line, color))
            except:
                colored_lines.append(colored(line, 'green'))  # Fallback to basic green
        
        # Version text
        version_text = "version 200.1.7.26.23"
        
        # Clear screen
        print("\033[H\033[J", end="")
        
        # Print the Mwikya Os ASCII art
        print('\n'.join(colored_lines))
        print()  # Add space before version
        
        # Animation colors for version text
        colors = ['red', 'yellow', 'blue', 'magenta', 'cyan', 'white']
        
        try:
            while True:
                # Create animated version text (colors change over time)
                colored_version = []
                time_offset = time.time() * 3  # Speed of animation
                
                for i, char in enumerate(version_text):
                    color_idx = int((i + time_offset) % len(colors))
                    colored_char = colored(char, colors[color_idx], attrs=['bold'])
                    colored_version.append(colored_char)
                
                # Print in place (using carriage return)
                sys.stdout.write("\r" + ''.join(colored_version))
                sys.stdout.flush()
                time.sleep(0.15)
                
        except KeyboardInterrupt:
            print("\n")
            return

    except Exception as e:
        print("Error:", str(e))
        # Fallback minimal version
        print(colored("Mwikya Os", 'green'))
        print(colored("version 200.1.7.26.23", 'red', attrs=['bold']))

# Run the logo creator
#main_logo()




#secondary_logo()

import time
import sys
from pyfiglet import Figlet
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

def animate_letter(letter_art, colors, duration=0.5):
    """Animate a single letter with color effects"""
    lines = letter_art.split('\n')
    animated_lines = []
    
    # Animate from light to dark green
    for i in range(5):
        print("\033[H\033[J", end="")
        for line_num, line in enumerate(lines):
            if line.strip():
                # Cycle through shades for animation effect
                shade = (i + line_num) % len(colors)
                print(colors[shade] + line)
        time.sleep(duration/5)

def animate_letters(text, font, colors, delay=0.8):
    """Animate text with special effects for each letter"""
    char_arts = [font.renderText(c) for c in text]
    max_height = max(len(art.split('\n')) for art in char_arts)
    
    for i in range(len(text)):
        # Animate the current letter with special effect
        animate_letter(char_arts[i], colors)
        
        # Build and display the current progress
        current_frame = []
        for line_num in range(max_height):
            frame_line = ""
            for char_idx in range(i + 1):
                char_lines = char_arts[char_idx].split('\n')
                if line_num < len(char_lines):
                    color = colors[char_idx % len(colors)]
                    frame_line += color + char_lines[line_num]
                else:
                    frame_line += " "
            current_frame.append(frame_line)
        
        print("\033[H\033[J", end="")
        print('\n'.join(current_frame))
        if i < len(text) - 1:  # No delay after last letter
            time.sleep(delay * 0.3)  # Short pause between letters

def os_logo():
    try:
        # Set up font
        try:
            f = Figlet(font='big')
        except:
            f = Figlet(font='standard')
        
        # Enhanced color palette with more green shades
        colors = [
            Fore.LIGHTGREEN_EX,
            Fore.GREEN,
            Fore.LIGHTYELLOW_EX,
            Fore.LIGHTCYAN_EX,
            Fore.LIGHTGREEN_EX,
            Fore.GREEN
        ]
        
        # Animate "Mwikya Os" with special effects
        print("\033[H\033[J", end="")
        animate_letters("Mwikya Os", f, colors, 0.8)
        
        # Final static display
        ascii_art = f.renderText('Mwikya Os')
        colored_art = ""
        for i, line in enumerate(ascii_art.split('\n')):
            if line.strip():
                color = colors[i % len(colors)]
                colored_art += color + line + '\n'
        
        print("\033[H\033[J", end="")
        print(colored_art)
        
        # Branding text
        time.sleep(1)
        print(f"\n{Fore.GREEN}⚡ {Fore.LIGHTGREEN_EX}POWERED BY MWIKYA TECHNOLOGY{Fore.GREEN} ⚡")
        time.sleep(1.2)
        print(f"{Fore.GREEN}🌱 {Fore.LIGHTGREEN_EX}Custom OS | Green Computing {Fore.GREEN}🌱")
        
        # Version animation
        time.sleep(1.5)
        version = "  version 200.1.7.26.23"
        anim_colors = [Fore.RED, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
        
        print(f"\n{Fore.RESET}", end="")
        while True:
            sys.stdout.write("\r")
            for i, c in enumerate(version):
                color = anim_colors[(i + int(time.time()*4)) % len(anim_colors)]
                sys.stdout.write(color + c)
            sys.stdout.flush()
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\n")
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}")

#os_logo()

import time
import sys
from pyfiglet import Figlet
from colorama import Fore, init

# Initialize colorama for cross-platform colored output
init(autoreset=True)

def animate_text(text, font, colors, delay=0.5):
    """Animate ASCII art text one letter at a time"""
    # Generate full ASCII art for each character first
    char_arts = []
    for char in text:
        char_art = font.renderText(char)
        char_arts.append(char_art.split('\n'))
    
    # Determine maximum height of any character
    max_height = max(len(art) for art in char_arts)
    
    # Build each frame line by line
    for i in range(len(text)):
        # Clear screen
        print("\033[H\033[J", end="")
        
        # Build current frame (all characters up to i)
        current_frame = []
        for line_num in range(max_height):
            frame_line = ""
            for char_idx in range(i + 1):
                char_lines = char_arts[char_idx]
                if line_num < len(char_lines):
                    color = colors[char_idx % len(colors)]
                    frame_line += color + char_lines[line_num]
                else:
                    frame_line += " "  # Padding for shorter characters
            current_frame.append(frame_line)
        
        # Print current frame
        print('\n'.join(current_frame))
        time.sleep(delay)

def mwikya_logo():
    try:
        # Set up the figlet font (with fallback options)
        try:
            f = Figlet(font='big')
        except:
            f = Figlet(font='standard')  # Fallback to standard if big not available
        
        # Define the color palette
        colors = [Fore.GREEN, Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTCYAN_EX]
        
        # Animate "Mwikya Os" letter by letter
        animate_text("Mwikya Os", f, colors, 0.5)
        
        # Generate full ASCII art for the complete text
        ascii_art = f.renderText('      Mwikya  Os')
        
        # Color each non-empty line with rotating colors
        colored_art = ""
        for i, line in enumerate(ascii_art.split('\n')):
            if line.strip():
                color = colors[i % len(colors)]
                colored_art += color + line + '\n'
            else:
                colored_art += '\n'
        
        # Clear screen and print final logo
        print("\033[H\033[J", end="")
        print(colored_art)
        
        # Print additional branding information
        time.sleep(1.2)
        print(f" {Fore.GREEN} ⚡ {Fore.LIGHTGREEN_EX}POWERED BY MWIKYA TECHNOLOGY{Fore.GREEN} ⚡ ")
        time.sleep(1.5)
        print(f"        {Fore.GREEN} 🌱 {Fore.LIGHTGREEN_EX}Custom OS | Green Computing {Fore.GREEN}🌱 ")
       # print()  # Add space before version
        time.sleep(1)
        
        # Version text
        version_text = "               VERSION  V 200.1.7.26.24"
        
        # Animation colors for version text
        anim_colors = [Fore.RED, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
        
        try:
            while True:
                # Create animated version text (colors change over time)
                colored_version = []
                time_offset = time.time() * 3  # Speed of animation
                
                for i, char in enumerate(version_text):
                    color_idx = int((i + time_offset) % len(anim_colors))
                    colored_version.append(f"{anim_colors[color_idx]}{char}")
                
                # Print in place (using carriage return)
                sys.stdout.write("\r" + ''.join(colored_version) + " " * 5)  # Padding
                sys.stdout.flush()
                time.sleep(0.15)
                
        except KeyboardInterrupt:
            print("\n")
            return

    except Exception as e:
        print("Error:", str(e))
        # Fallback minimal version
        print(f"{Fore.GREEN}    Mwikya Os")
        time.sleep(1)
        print(f"{Fore.RED}version 200.1.7.26.24")

# Run the logo creator
#mwikya_logo()

def bios_logo():
    try:
        # Set up font
        try:
            f = Figlet(font='big')
        except:
            f = Figlet(font='standard')
        
        # Enhanced color palette with more green shades
        colors = [
            Fore.LIGHTGREEN_EX,
            Fore.GREEN,
            Fore.LIGHTYELLOW_EX,
            Fore.LIGHTCYAN_EX,
            Fore.LIGHTGREEN_EX,
            Fore.GREEN
        ]
        
        # Animate "Mwikya Os" with special effects
        print("\033[H\033[J", end="")
        animate_text("Mwikya Os", f, colors, 0.8)
    except KeyboardInterrupt:
        print("\n")
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}")

#bios_logo()

