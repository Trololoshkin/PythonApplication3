import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Trading Bot")
        self.geometry("400x300")
        
        self.learning_rate_default = 0.001
        self.training_epochs_default = 100
        self.batch_size_default = 100
        self.display_step_default = 1
        
     def create_widgets(self):
        # ...

        # Параметры нейронной сети
        self.learning_rate_label = tk.Label(self, text='Learning rate:')
        self.learning_rate_label.grid(row=3, column=0)
        self.learning_rate_entry = tk.Entry(self)
        self.learning_rate_entry.insert(tk.END, self.learning_rate_default)
        self.learning_rate_entry.grid(row=3, column=1)

        self.training_epochs_label = tk.Label(self, text='Training epochs:')
        self.training_epochs_label.grid(row=4, column=0)
        self.training_epochs_entry = tk.Entry(self)
        self.training_epochs_entry.insert(tk.END, self.training_epochs_default)
        self.training_epochs_entry.grid(row=4, column=1)

        self.batch_size_label = tk.Label(self, text='Batch size:')
        self.batch_size_label.grid(row=5, column=0)
        self.batch_size_entry = tk.Entry(self)
        self.batch_size_entry.insert(tk.END, self.batch_size_default)
        self.batch_size_entry.grid(row=5, column=1)

        self.display_step_label = tk.Label(self, text='Display step:')
        self.display_step_label.grid(row=6, column=0)
        self.display_step_entry = tk.Entry(self)
        self.display_step_entry.insert(tk.END, self.display_step_default)
        self.display_step_entry.grid(row=6, column=1)
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

