import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("PythonGorls")
        
        self.canvas = tk.Canvas(root, width=400, height=400, bg="black")
        self.canvas.pack()
        
        self.snake = [(20, 20), (20, 30), (20, 40)]
        self.snake_direction = "Down"
        self.snake_position = self.create_food()
        self.game_over = False
        
        self.root.bind("<Up>", self.change_direction)
        self.root.bind("<Down>", self.change_direction)
        self.root.bind("<Left>", self.change_direction)
        self.root.bind("<Right>", self.change_direction)
        
        self.update_snake()
        self.move_snake()
        
    def create_food(self):
        x = random.randint(0, 19) * 20
        y = random.randint(0, 19) * 20
        while (x, y) in self.snake:
            x = random.randint(0, 19) * 20
            y = random.randint(0, 19) * 20
            
            self.canvas.create_rectangle(x, y, x+20, y+20, fill="red", tag="food")
            return (x, y)
    def change_direction(self, event):
        new_direction = event.keysym
        all_directions = ["Up", "Down", "Left", "Right"]
        opposites = [{"Up", "Down", "Left", "Right"}]
        
        if (new_direction in all_directions and {new_direction, self.snake_direction} not in opposites):
            self.snake_direction = new_direction
            
    def move_snake(self):
        if self.game_over:
            return
        head_x, head_y = self.snake [-1]
        if self.snake_direction == "Up":
            new_head = (head_x, head_y -20)
        elif self.snake_direction == "Down":
            new_head = (head_x, head_y +20)
        elif self.snake_direction == "Left":
            new_head = (head_x -20, head_y)
        elif self.snake_direction == "Right":
            new_head = (head_x + 20, head_y)
            
        if (new_head[0] < 0 or new_head[0] >= 400 or
            new_head[1] < 0 or new_head[1] >= 400 or
            new_head in self.snake):
            self.end_game()
            return
        
        self.snake.append(new_head)
        
        if new_head == self.food_position:
            self.canvas.delete("food")
            self.food_position = self.create_food()
        else:
            self.snake.pop(0)
            
            self.update_snake()
            self.root.after(100, self.move_snake)
            
    def update_snake(self):
        self.canvas.delete("snake")
        for segment in self.snake: self.canvas.create_rectangle(segment[0], segment[1], segment[0]+20, segment[1]+20, fill="green", tag="snake")
        
    def end_game(self):
        self.game_over = True
        self.canvas.create_text(200, 200, text="Game Over", fill="white", font=("helvetica", 24))
        
if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()