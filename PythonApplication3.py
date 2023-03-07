import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Trading Bot")
        self.geometry("400x300")
        
        # Создаем поля для ввода
        data_path_label = tk.Label(self, text="Data Path:")
        data_path_label.pack()
        self.data_path_entry = tk.Entry(self)
        self.data_path_entry.pack()
        
        train_test_split_ratio_label = tk.Label(self, text="Train/Test Split Ratio:")
        train_test_split_ratio_label.pack()
        self.train_test_split_ratio_entry = tk.Entry(self)
        self.train_test_split_ratio_entry.pack()
        
        window_size_label = tk.Label(self, text="Window Size:")
        window_size_label.pack()
        self.window_size_entry = tk.Entry(self)
        self.window_size_entry.pack()
        
        batch_size_label = tk.Label(self, text="Batch Size:")
        batch_size_label.pack()
        self.batch_size_entry = tk.Entry(self)
        self.batch_size_entry.pack()
        
        epochs_label = tk.Label(self, text="Epochs:")
        epochs_label.pack()
        self.epochs_entry = tk.Entry(self)
        self.epochs_entry.pack()
        
        learning_rate_label = tk.Label(self, text="Learning Rate:")
        learning_rate_label.pack()
        self.learning_rate_entry = tk.Entry(self)
        self.learning_rate_entry.pack()
        
        prediction_length_label = tk.Label(self, text="Prediction Length:")
        prediction_length_label.pack()
        self.prediction_length_entry = tk.Entry(self)
        self.prediction_length_entry.pack()
        
        order_size_label = tk.Label(self, text="Order Size:")
        order_size_label.pack()
        self.order_size_entry = tk.Entry(self)
        self.order_size_entry.pack()
        
        profit_margin_label = tk.Label(self, text="Profit Margin:")
        profit_margin_label.pack()
        self.profit_margin_entry = tk.Entry(self)
        self.profit_margin_entry.pack()
        
        # Добавляем кнопку запуска бота
        start_button = tk.Button(self, text="Start Trading Bot", command=self.start_bot)
        start_button.pack(pady=10)
    
    def start_bot(self):
        # Получаем значения параметров из полей ввода
        data_path = self.data_path_entry.get()
        train_test_split_ratio = float(self.train_test_split_ratio_entry.get())
        window_size = int(self.window_size_entry.get())
        batch_size = int(self.batch_size_entry.get())
        epochs = int(self.epochs_entry.get())
        learning_rate = float(self.learning_rate_entry.get())
        prediction_length = int(self.prediction_length_entry.get())
        order_size = int(self.order_size_entry.get())
        profit_margin = float(self.profit_margin_entry.get())
        
        # Запускаем бота с введенными параметрами
        run_bot(data_path, train_test_split_ratio, window_size, batch_size, epochs, learning_rate, prediction_length, order_size, profit_margin)

# Запускаем окно
app = App()
app.mainloop()

