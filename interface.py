import pygame
import math
import time
from PIL import Image, ImageDraw
import os
import json
from datetime import datetime

class IronManInterface:
    """
    Iron Man-style GUI Interface for JARVIS
    Features hexagonal HUD, holographic effects, and visual feedback
    """
    
    def __init__(self, width=1400, height=900):
        pygame.init()
        self.WIDTH = width
        self.HEIGHT = height
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("J.A.R.V.I.S - Iron Man AI Interface")
        
        self.clock = pygame.time.Clock()
        self.fps = 60
        
        # Colors
        self.BLACK = (0, 0, 0)
        self.DARK_BLUE = (5, 15, 35)
        self.BLUE = (0, 100, 200)
        self.CYAN = (0, 200, 255)
        self.GOLD = (255, 184, 82)
        self.RED = (220, 20, 60)
        self.GREEN = (50, 205, 50)
        self.WHITE = (255, 255, 255)
        self.PURPLE = (138, 43, 226)
        
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)
        self.font_tiny = pygame.font.Font(None, 16)
        
        # Animation variables
        self.pulse_value = 0
        self.pulse_speed = 0.05
        self.rotation_angle = 0
        self.scanning_line_y = 0
        self.particle_system = []
        
        # UI state
        self.current_message = ""
        self.message_display_time = 0
        self.is_listening = False
        self.is_processing = False
        self.listening_waves = []
        self.status = "STANDBY"
        self.current_image = None
        self.image_alpha = 255
        
    def draw_background(self):
        """Draw animated background with grid pattern"""
        self.screen.fill(self.DARK_BLUE)
        
        # Draw grid
        grid_spacing = 50
        alpha = 15
        for x in range(0, self.WIDTH, grid_spacing):
            pygame.draw.line(self.screen, self.CYAN, (x, 0), (x, self.HEIGHT), 1)
        for y in range(0, self.HEIGHT, grid_spacing):
            pygame.draw.line(self.screen, self.CYAN, (0, y), (self.WIDTH, y), 1)
    
    def draw_hexagon(self, center_x, center_y, radius, color, width=2):
        """Draw a hexagon shape"""
        points = []
        for i in range(6):
            angle = math.pi / 3 * i + self.rotation_angle
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            points.append((x, y))
        
        if len(points) > 0:
            pygame.draw.polygon(self.screen, color, points, width)
        return points
    
    def draw_central_core(self):
        """Draw the central JARVIS core with pulsing effect"""
        center_x = self.WIDTH // 2
        center_y = self.HEIGHT // 2
        
        # Calculate pulse
        pulse = abs(math.sin(self.pulse_value)) * 30 + 30
        
        # Outer rings
        for i in range(3):
            radius = 100 + i * 40 + pulse * (i + 1) * 0.5
            color_intensity = int(200 - i * 50)
            color = (0, color_intensity, 255)
            pygame.draw.circle(self.screen, color, (center_x, center_y), int(radius), 2)
        
        # Central core
        pygame.draw.circle(self.screen, self.GOLD, (center_x, center_y), 20)
        pygame.draw.circle(self.screen, self.CYAN, (center_x, center_y), 20, 3)
        
        # Pulsing center
        core_pulse = abs(math.sin(self.pulse_value * 2)) * 10 + 5
        pygame.draw.circle(self.screen, self.GOLD, (center_x, center_y), int(core_pulse))
    
    def draw_listening_waves(self):
        """Draw audio waves when listening"""
        if not self.is_listening:
            return
        
        center_x = self.WIDTH // 2
        center_y = self.HEIGHT // 2 + 150
        
        wave_count = 5
        for i in range(wave_count):
            wave_radius = (self.pulse_value * 100 + i * 20) % 200
            alpha = int(255 * (1 - wave_radius / 200))
            
            # Draw wave circles
            color = self.CYAN if alpha > 128 else self.BLUE
            pygame.draw.circle(self.screen, color, (center_x, center_y), int(wave_radius), 2)
    
    def draw_scanning_line(self):
        """Draw horizontal scanning line for activity"""
        if self.is_processing or self.is_listening:
            color = self.RED if self.is_processing else self.GREEN
            self.scanning_line_y = (self.scanning_line_y + 3) % self.HEIGHT
            pygame.draw.line(self.screen, color, (0, self.scanning_line_y), 
                            (self.WIDTH, self.scanning_line_y), 2)
            
            # Add glow effect
            for offset in range(1, 5):
                glow_y1 = (self.scanning_line_y - offset) % self.HEIGHT
                glow_y2 = (self.scanning_line_y + offset) % self.HEIGHT
                glow_color = tuple(int(c * 0.4) for c in color)
                pygame.draw.line(self.screen, glow_color, (0, glow_y1), 
                                (self.WIDTH, glow_y1), 1)
                pygame.draw.line(self.screen, glow_color, (0, glow_y2), 
                                (self.WIDTH, glow_y2), 1)
    
    def draw_top_panel(self):
        """Draw top information panel"""
        # Top bar
        pygame.draw.line(self.screen, self.CYAN, (0, 50), (self.WIDTH, 50), 3)
        
        # Title
        title = self.font_large.render("J.A.R.V.I.S", True, self.GOLD)
        title_rect = title.get_rect(center=(self.WIDTH // 2, 25))
        self.screen.blit(title, title_rect)
        
        # Status
        status_text = self.font_small.render(f"STATUS: {self.status}", True, self.GREEN)
        self.screen.blit(status_text, (20, 10))
        
        # Time and date
        now = datetime.now()
        time_text = self.font_tiny.render(now.strftime("%H:%M:%S"), True, self.CYAN)
        date_text = self.font_tiny.render(now.strftime("%A, %B %d"), True, self.CYAN)
        self.screen.blit(time_text, (self.WIDTH - 200, 10))
        self.screen.blit(date_text, (self.WIDTH - 200, 28))
    
    def draw_message_display(self):
        """Draw current message in the interface"""
        if self.current_message and time.time() - self.message_display_time < 5:
            # Create message box
            text_lines = self.current_message.split('\n')
            box_height = len(text_lines) * 30 + 20
            box_y = self.HEIGHT - box_height - 20
            
            # Draw semi-transparent background
            pygame.draw.rect(self.screen, (10, 30, 60), (20, box_y, self.WIDTH - 40, box_height))
            pygame.draw.rect(self.screen, self.CYAN, (20, box_y, self.WIDTH - 40, box_height), 2)
            
            # Draw text
            for i, line in enumerate(text_lines):
                text_surface = self.font_small.render(line, True, self.CYAN)
                self.screen.blit(text_surface, (40, box_y + 10 + i * 30))
    
    def draw_corner_panels(self):
        """Draw information panels in corners"""
        panel_width = 250
        panel_height = 150
        
        # Top-left panel
        self.draw_panel(10, 70, panel_width, panel_height, "SYSTEMS", [
            f"TIME: {datetime.now().strftime('%H:%M')}",
            f"CPU: {int(self.pulse_value * 10) % 100}%",
            f"MEMORY: {int(self.pulse_value * 5) % 100}%",
            "STATUS: OPERATIONAL"
        ])
        
        # Top-right panel
        self.draw_panel(self.WIDTH - panel_width - 10, 70, panel_width, panel_height, 
                       "AUDIO", [
            f"FREQUENCY: {int(self.pulse_value * 50) % 20} kHz",
            f"VOLUME: 75%",
            f"MODE: {'ACTIVE' if self.is_listening else 'STANDBY'}",
            "CLARITY: EXCELLENT"
        ])
        
        # Bottom-left panel
        self.draw_panel(10, self.HEIGHT - panel_height - 10, panel_width, panel_height,
                       "NETWORK", [
            "CONNECTION: STABLE",
            f"LATENCY: {int(self.pulse_value * 2) % 50} ms",
            "BANDWIDTH: OPTIMAL",
            f"UPTIME: 99.9%"
        ])
    
    def draw_panel(self, x, y, width, height, title, data):
        """Draw an information panel"""
        # Background
        pygame.draw.rect(self.screen, (10, 30, 60), (x, y, width, height))
        pygame.draw.rect(self.screen, self.CYAN, (x, y, width, height), 2)
        
        # Title
        title_text = self.font_small.render(title, True, self.GOLD)
        self.screen.blit(title_text, (x + 10, y + 5))
        
        # Separator line
        pygame.draw.line(self.screen, self.CYAN, (x, y + 30), (x + width, y + 30), 1)
        
        # Data
        for i, line in enumerate(data):
            text_surface = self.font_tiny.render(line, True, self.CYAN)
            self.screen.blit(text_surface, (x + 10, y + 40 + i * 22))
    
    def draw_image_display(self):
        """Display image related to current topic"""
        if self.current_image is not None:
            try:
                image = pygame.image.load(self.current_image)
                # Scale image
                image = pygame.transform.scale(image, (300, 300))
                # Position in right side
                self.screen.blit(image, (self.WIDTH - 330, self.HEIGHT - 330))
                # Draw frame
                pygame.draw.rect(self.screen, self.CYAN, 
                                (self.WIDTH - 330, self.HEIGHT - 330, 300, 300), 3)
            except:
                pass
    
    def draw_holographic_effect(self):
        """Add scanlines and holographic effect"""
        for y in range(0, self.HEIGHT, 2):
            pygame.draw.line(self.screen, (0, 0, 0, 20), (0, y), (self.WIDTH, y), 1)
    
    def update(self):
        """Update animation values"""
        self.pulse_value += self.pulse_speed
        if self.pulse_value > 2 * math.pi:
            self.pulse_value = 0
        
        self.rotation_angle += 0.02
    
    def render(self):
        """Render the entire interface"""
        self.draw_background()
        self.draw_top_panel()
        self.draw_corner_panels()
        self.draw_central_core()
        self.draw_listening_waves()
        self.draw_scanning_line()
        self.draw_image_display()
        self.draw_message_display()
        self.draw_holographic_effect()
        
        pygame.display.flip()
    
    def set_status(self, status):
        """Update system status"""
        self.status = status
    
    def set_message(self, message):
        """Set message to display"""
        self.current_message = message
        self.message_display_time = time.time()
    
    def set_listening(self, is_listening):
        """Set listening state"""
        self.is_listening = is_listening
        self.status = "LISTENING" if is_listening else "STANDBY"
    
    def set_processing(self, is_processing):
        """Set processing state"""
        self.is_processing = is_processing
        self.status = "PROCESSING" if is_processing else "STANDBY"
    
    def set_image(self, image_path):
        """Set image to display"""
        if os.path.exists(image_path):
            self.current_image = image_path
    
    def handle_events(self):
        """Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
        return True
    
    def close(self):
        """Close the interface"""
        pygame.quit()
