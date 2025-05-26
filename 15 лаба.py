import tkinter as tk
import random

class MagicBallApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Магический шар (ДА/НЕТ)")

        #Создаем холст
        self.canvas = tk.Canvas(root, width=400, height=500, bg="black")
        self.canvas.pack()

        self.create_gradient_bg()

        #Создаем градиентный шар
        self.create_ball_gradient()

        #Внутренний круг для ответов
        self.inner_circle = self.canvas.create_oval(150, 150, 250, 250, fill="blue", outline="gray")

        #Поле для текста ответа
        self.text_answer = self.canvas.create_text(200, 200, text="Задайте вопрос", font=("Brotesk (Trial) Semibold", 14, "bold"), fill="white", width=120)

        #Поле ввода вопроса
        self.entry = tk.Entry(root, font=("Helvetica", 14))
        self.entry.pack(pady=10)

        #Кнопка для активации шара
        self.button = tk.Button(root, text="Спросить", font=("Helvetica", 14), command=self.shake_ball)
        self.button.pack(pady=10)

    def create_gradient_bg(self):
        for i in range(500):
            r = min(10, i // 3)
            g = 0
            b = max(10, 255 - i // 3)
            color = f'#{r:02x}{g:02x}{b:02x}'
            self.canvas.create_line(0, i, 400, i, fill=color)

    def create_ball_gradient(self):
        for i in range(150):
            color = f'#{0+i:02x}{0+i:02x}{0+i:02x}'
            self.canvas.create_oval(50+i, 50+i, 350-i, 350-i, outline=color)

    def shake_ball(self):
        answers = ["ДА", "НЕТ", "НЕУВЕРЕН", "НАВЕРНОЕ"]
        new_answer = random.choice(answers)

        #Анимация вибрации шара и изменения цвета
        for _ in range(5):
            self.canvas.move(self.inner_circle, 3, 0)
            self.canvas.move(self.text_answer, 3, 0)
            self.canvas.itemconfig(self.inner_circle, fill=random.choice(["blue", "purple", "black"]))
            self.root.update()
            self.canvas.move(self.inner_circle, -3, 0)
            self.canvas.move(self.text_answer, -3, 0)
            self.root.update()

        #Эффект увеличения и уменьшения шара
        for scale_factor in [1.05, 0.95, 1.05, 0.95]:
            self.canvas.scale(self.inner_circle, 200, 200, scale_factor, scale_factor)
            self.canvas.scale(self.text_answer, 200, 200, scale_factor, scale_factor)
            self.root.update()

        self.canvas.itemconfig(self.text_answer, text=new_answer)

if __name__ == "__main__":
    root = tk.Tk()
    app = MagicBallApp(root)
    root.mainloop()