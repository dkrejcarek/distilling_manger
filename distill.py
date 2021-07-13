try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk  # python 2

from app import App


def main():
    root = tk.Tk()
    App(root).pack(fill="both", expand=True)
    root.mainloop()


if __name__ == "__main__":
    main()
