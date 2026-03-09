class Cursor:
    @classmethod
    def move_home(self):
        print("\033[H", end='')
    

    @classmethod
    def move_to(self, line: int = 0, column: int = 0):
        print(f"\033[{line};{column}H", end='')
    

    @classmethod
    def move_up(self, lines: int = 0):
        print(f"\033[{lines}A", end='')

    
    @classmethod
    def move_down(self, lines: int = 0):
        print(f"\033[{lines}B", end='')


    @classmethod
    def move_right(self, columns: int = 0):
        print(f"\033[{columns}C", end='')


    @classmethod
    def move_left(self, columns: int = 0):
        print(f"\033[{columns}D", end='')

    
    @classmethod
    def move_right(self, columns: int = 0):
        print(f"\033[{columns}C", end='')

    
    @classmethod
    def move_to_column(self, column: int = 0):
        print(f"\033[{column}G", end='')


    @classmethod
    def hide(self):
        print("\033[?25l", end='')

    
    @classmethod
    def show(self):
        print("\033[?25h", end='')



class Earse:
    @classmethod
    def earse_in(self):
        """erase from cursor until end of screen"""
        print("\033[0J", end='')


    @classmethod
    def earse_out(self):
        """erase from cursor to beginning of screen"""
        print("\033[1J", end='')

    
    @classmethod
    def earse_all(self):
        """erase entire screen"""
        print("\033[2J", end='')


    @classmethod
    def earse_saved(self):
        """erase saved lines"""
        print("\033[3J", end='')


    @classmethod
    def earse_in_line(self):
        """erase from cursor to end of line"""
        print("\033[0K", end='')


    @classmethod
    def earse_out_line(self):
        """erase start of line to the cursor"""
        print("\033[1K", end='')

    
    @classmethod
    def earse_all_line(self):
        """erase the entire line"""
        print("\033[2K", end='')

        
    
class Graphics:
    @classmethod
    def color_8_16(self, color: int = 39, ):
        """Set text color from 8-16 console colors
        
        Args:
            Color(`int`, optional): color to set, default - 39 (resets color), 0 - reset color and text effects
        """
        print(f"\033[0;{color}m", end='')


    @classmethod
    def foreground_256_color(self, color: int = 255):
        """Set text color from 256 console colors"""
        print(f"\033[38;5;{color}m", end='')


    @classmethod
    def background_256_color(self, color: int = 255):
        """Set background color from 256 console colors"""
        print(f"\033[48;5;{color}m", end='')


    @classmethod
    def reset(self):
        print("\033[0m", end='')

    
    @classmethod
    def bold(self):
        print("\033[1m", end='')

    
    @classmethod
    def reset_bold(self):
        print("\033[22m", end='')


    @classmethod
    def italic(self):
        print("\033[3m", end='')

    
    @classmethod
    def reset_italic(self):
        print("\033[23m", end='')

    
    @classmethod
    def underline(self):
        print("\033[4m", end='')

    
    @classmethod
    def reset_underline(self):
        print("\033[24m", end='')


    @classmethod
    def strikethrough(self):
        print("\033[9m", end='')

    
    @classmethod
    def reset_strikethrough(self):
        print("\033[29m", end='')