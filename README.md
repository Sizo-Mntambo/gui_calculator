# 🧮 GUI Calculator (Tkinter) — Clean, Colorful, and Practical

A simple, focused calculator built with Python’s Tkinter. Clear display, consistent layout, and basic arithmetic you can rely on — with a dash of color and emojis for fun. ✨

Features:
- 📺 Large, readable display
- ➕ Basic operations: +, -, *, /
- 🧩 Parentheses: ( and )
- ⚡ Instant input updates
- 🧯 Error feedback for invalid expressions

Requirements:
- Python 3.8+ (Tkinter included in most standard installs)

Install and Run:
- Windows: py calc.py
- macOS/Linux: python3 calc.py

How to Use:
- Click number and operator buttons to build an expression.
- Press = to evaluate.
- Use ( and ) to control precedence.
- Division uses standard floating-point math.

Layout Overview:
- Uses Tkinter’s grid manager for alignment.
- Digits arranged across rows 2–5; operators in the right column.
- Brackets near the digits for quick access.
- The equals button spans the entire row 6 for a clean, centered result trigger. ✅

Project Files:
- calc.py
  - add_to_calculation(symbol): append input and update display
  - evaluate_calculation(): evaluate and show result
  - clear_field(): clear the display/input (wire to a button if needed)
- README.md (this file)

Safety Note:
- Uses Python’s eval for evaluation. Avoid untrusted input. For production, replace with a safe expression parser. 🔐

Customize:
- 🖋 Fonts: adjust font tuples in Buttons/Text
- 🪟 Window: change root.geometry(...)
- ⌨️ Layout: tweak grid(row, column) positions
- 🧼 Optional Clear button:
  Example:
  button_clear = tk.Button(root, text="C", command=clear_field, font=("Arial", 14))
  button_clear.grid(row=5, column=2, sticky="nsew")

Troubleshooting:
- Tkinter not found: ensure system Python with Tk support.
- Misalignment/spacing: use uniform column weights and sticky="nsew".
- Equals width: ensure button_equal.grid(row=6, column=1, columnspan=5, sticky="nsew").

Roadmap:
- ⌨️ Keyboard input bindings
- 🧽 Clear and Backspace buttons
- 🧮 Scientific extensions (sin, cos, log)
- 🌗 Theme options (light/dark)

