import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import turtle


class EasyGraphics:

    def __init__(self, title="My App", size=(400, 400), bg_color="white", enable_turtle=False):
        # إعداد نافذة التطبيق
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{size[0]}x{size[1]}")
        self.root.configure(bg=bg_color)

        if enable_turtle:
            # إعداد شاشة Turtle
            self.turtle_screen = turtle.Screen()
            self.turtle_screen.setup(width=size[0], height=size[1])
            self.turtle_screen.bgcolor(bg_color)
            self.turtle_screen.title(title)
            self.t = turtle.Turtle()
            self.t.speed(0)

    def add_button(self, text, command=None, place=None, size=None, fg="black", bg="lightgray", borderwidth=2,
                   relief="raised", font=("Arial", 12)):
        """إضافة زر إلى النافذة مع دعم تغيير الألوان والخط والحجم"""
        if place is None:
            place = {"x": 10, "y": 10}  # قيم افتراضية لـ x و y
        if size is None:
            size = {"width": 10, "height": 2}  # قيم افتراضية للعرض والطول

        x = place.get("x", 10)  # افتراض قيمة 10 إذا لم يتم تحديد x
        y = place.get("y", 10)  # افتراض قيمة 10 إذا لم يتم تحديد y
        width = size.get("width", 10)  # افتراض عرض 10 إذا لم يتم تحديده
        height = size.get("height", 2)  # افتراض ارتفاع 2 إذا لم يتم تحديده

        # إنشاء الزر مع التأثيرات والخط والحجم
        button = tk.Button(self.root, text=text, command=command, width=width, height=height, fg=fg, bg=bg,
                           borderwidth=borderwidth, relief=relief, font=font)
        button.place(x=x, y=y)
        return button

    def _get_anchor(self, align):
        """تحديد محاذاة النصوص"""
        return {"L": "w", "C": "center", "R": "e"}.get(align, "w")

    def add_label(self, text, place=None, font=("Arial", 12), fg="black", bg="white", align="L", width=200):
        """إضافة Label إلى الواجهة مع دعم خاصية place"""
        if place is None:
            place = {"x": 10, "y": 10}  # قيم افتراضية لـ x و y

        x = place.get("x", 10)  # افتراض قيمة 10 إذا لم يتم تحديد x
        y = place.get("y", 10)  # افتراض قيمة 10 إذا لم يتم تحديد y

        label = tk.Label(self.root, text=text, font=font, fg=fg, bg=bg, width=width // 10)

        # تعديل الموضع بناءً على المحاذاة
        if align == "L":  # محاذاة لليمين
            label.place(x=x - width, y=y, width=width)
        elif align == "C":  # محاذاة للوسط
            label.place(x=x - (width // 2), y=y, width=width)
        else:  # محاذاة لليسار
            label.place(x=x, y=y, width=width)

        return label

    def add_textbox(self, place=None, size=None, font=("Arial", 12), fg="black", bg="white"):
        """إضافة مربع نص إلى النافذة مع دعم font و fg و bg"""
        if place is None:
            place = {"x": 10, "y": 10}  # قيم افتراضية لـ x و y
        if size is None:
            size = {"width": 20, "height": 2}  # قيم افتراضية للعرض والطول

        x = place.get("x", 10)  # افتراض قيمة 10 إذا لم يتم تحديد x
        y = place.get("y", 10)  # افتراض قيمة 10 إذا لم يتم تحديد y
        width = size.get("width", 20)  # افتراض عرض 20 إذا لم يتم تحديده
        height = size.get("height", 2)  # افتراض ارتفاع 2 إذا لم يتم تحديده

        # إنشاء مربع النص مع الخط والألوان
        textbox = tk.Text(self.root, width=width, height=height, font=font, fg=fg, bg=bg)
        textbox.place(x=x, y=y)
        textbox.configure(fg=fg, bg=bg, insertbackground=fg)  # تلوين النص ومؤشر الكتابة
        return textbox

    def add_dropdown(self, options=None, place=None, size=None, font=("Arial", 12), fg="black", bg="white",
                     default_text="اختر عنصرًا", command=None):
        """إضافة قائمة منسدلة مع دعم الخيارات كقاموس وتخصيص الموقع والألوان والإجراءات"""
        if place is None:
            place = {"x": 10, "y": 10}  # قيم افتراضية لـ x و y
        if size is None:
            size = {"width": 15, "height": 1}  # قيم افتراضية للعرض والطول
        if options is None:
            options = {"Option 1": lambda: print("Option 1 selected")}

        x = place.get("x", 10)  # افتراض قيمة 10 إذا لم يتم تحديد x
        y = place.get("y", 10)  # افتراض قيمة 10 إذا لم يتم تحديد y
        width = size.get("width", 15)  # افتراض عرض 15 إذا لم يتم تحديده
        height = size.get("height", 1)  # افتراض ارتفاع 1 إذا لم يتم تحديده

        # إعداد قائمة الخيارات
        variable = tk.StringVar(self.root)
        variable.set(default_text)  # النص الافتراضي عند بدء التشغيل

        # إنشاء القائمة المنسدلة
        dropdown = tk.OptionMenu(self.root, variable, *options.keys())

        # تخصيص الألوان والخط
        dropdown.config(font=font, width=width, fg=fg, bg=bg, activebackground=bg, activeforeground=fg)
        dropdown.place(x=x, y=y)

        # إعداد الإجراء عند تغيير الاختيار
        def on_select(*args):
            selected_option = variable.get()
            if selected_option in options:
                options[selected_option]()  # تنفيذ الإجراء المرتبط بالاختيار

        variable.trace("w", on_select)

        return dropdown

    def add_image(self, image_path, place=None, size=None, borderwidth=0, bordercolor="black", bg=None):
        """إضافة صورة إلى النافذة مع دعم place و size والإطار ولون الخلفية"""
        if place is None:
            place = {"x": 10, "y": 10}  # قيم افتراضية لـ x و y
        if size is None:
            size = {"width": None, "height": None}  # القيم الافتراضية تعني عدم تغيير الحجم

        x = place.get("x", 10)  # افتراض قيمة 10 إذا لم يتم تحديد x
        y = place.get("y", 10)  # افتراض قيمة 10 إذا لم يتم تحديد y
        width = size.get("width", None)  # افتراض عدم تغيير العرض إذا لم يتم تحديده
        height = size.get("height", None)  # افتراض عدم تغيير الارتفاع إذا لم يتم تحديده

        # تحديد لون الخلفية الافتراضي (شفاف)
        if bg is None:
            bg = self.root["bg"]  # لون نافذة التطبيق الافتراضي

        try:
            # تحميل الصورة باستخدام PIL
            img = Image.open(image_path)
            if width and height:
                img = img.resize((width, height), Image.LANCZOS)  # تغيير الحجم إذا تم تحديده

            photo = ImageTk.PhotoImage(img)

            # إنشاء إطار إذا تم تحديد borderwidth
            frame = tk.Frame(self.root, bg=bordercolor,
                             width=(width + borderwidth * 2 if width else img.width + borderwidth * 2),
                             height=(height + borderwidth * 2 if height else img.height + borderwidth * 2))
            frame.place(x=x - borderwidth, y=y - borderwidth)

            # إنشاء الـ Label لإظهار الصورة داخل الإطار
            label = tk.Label(frame, image=photo, bg=bg)  # تعيين خلفية الصورة بناءً على المعامل bg
            label.image = photo  # الاحتفاظ بالصورة لمنع إزالتها من الذاكرة
            label.pack(padx=borderwidth, pady=borderwidth)

            return label
        except Exception as e:
            messagebox.showerror("Error", f"Cannot load image: {e}")
            return None

    def add_listbox(self, items=None, place=None, size=None, font=("Arial", 12), color=None):
        """
        إضافة Listbox إلى الواجهة مع دعم الإعدادات المخصصة
        :param items: قائمة العناصر المراد عرضها داخل الـ Listbox
        :param place: موقع الـ Listbox { "x": 10, "y": 10 }
        :param size: حجم الـ Listbox { "w": 20, "h": 10 } (عرض وعدد الأسطر)
        :param font: إعدادات الخط (نوع الخط، الحجم، التنسيق)
        :param color: إعدادات الألوان {"fg": "black", "bg": "white"}
        """
        if place is None:
            place = {"x": 10, "y": 10}  # موقع افتراضي
        if size is None:
            size = {"w": 20, "h": 10}  # حجم افتراضي
        if color is None:
            color = {"fg": "black", "bg": "white"}  # ألوان افتراضية

        x = place.get("x", 10)
        y = place.get("y", 10)

        listbox = tk.Listbox(
            self.root,
            width=size["w"],
            height=size["h"],
            font=font,
            fg=color["fg"],
            bg=color["bg"]
        )

        # إضافة العناصر إلى الـ Listbox
        if items:
            for item in items:
                listbox.insert(tk.END, item)

        # تحديد موقع الـ Listbox
        listbox.place(x=x, y=y)
        return listbox

    def add_radiobuttons(self, options, place=None, button_font=("Arial", 12), button_fg="black", button_bg="white",
                         text=None, default=None):
        """
        إضافة مجموعة من أزرار الراديو مع دعم النصوص بجانب الأزرار
        :param options: قاموس يحتوي على النصوص والإجراءات لكل زر { "Text": action_function }
        :param place: إحداثيات الزر الأول { "x": 10, "y": 10 }
        :param button_font: نوع وحجم الخط لأزرار الراديو
        :param button_fg: لون النص للأزرار
        :param button_bg: لون الخلفية للأزرار
        :param text: إعدادات النصوص بجانب الأزرار { "text_position": "right", "width": 50, "bg": "black", "font": "Tahoma", "fg": "yellow" }
        :param default: القيمة الافتراضية (None إذا لم يتم اختيار أي زر عند التشغيل)
        """
        if place is None:
            place = {"x": 10, "y": 10}  # موقع افتراضي
        x = place.get("x", 10)
        y = place.get("y", 10)

        # إعدادات النصوص الافتراضية
        text_defaults = {
            "text_position": "right",
            "width": 50,
            "bg": "white",
            "font": ("Arial", 12),
            "fg": "black"
        }
        if text:
            text_defaults.update(text)  # دمج الإعدادات المرسلة مع الافتراضية

        variable = tk.StringVar(self.root)  # متغير لمجموعة أزرار الراديو
        if default is not None:
            variable.set(default)  # تعيين القيمة الافتراضية
        else:
            variable.set("")  # عدم اختيار أي زر عند التشغيل

        buttons = []
        for text_label, action in options.items():
            # تحديد مكان النص بالنسبة للزر
            if text_defaults["text_position"] == "left":
                label_x = x + 30  # النص بجانب الزر على اليمين
                button_x = x
            elif text_defaults["text_position"] == "right":
                label_x = x  # النص على يسار الزر
                button_x = x + 100
            else:
                raise ValueError("text_position must be 'left' or 'right'")

            # إضافة النص بجانب الزر
            label = tk.Label(
                self.root,
                text=text_label,
                font=text_defaults["font"],
                fg=text_defaults["fg"],
                bg=text_defaults["bg"],
                width=text_defaults["width"]
            )
            label.place(x=label_x, y=y)

            # إضافة زر الراديو
            radiobutton = tk.Radiobutton(
                self.root,
                variable=variable,
                value=text_label,
                font=button_font,
                fg=button_fg,
                bg=button_bg,
                command=action
            )
            radiobutton.place(x=button_x, y=y)
            buttons.append(radiobutton)

            y += 30  # نقل الموقع العمودي للزر التالي

        return buttons

    def add_checkboxes(self, options, place=None, text_settings=None, default=None, pady=0):
        """
        إضافة مجموعة من أزرار الـ CheckBox مع دعم النصوص والإجراءات
        :param options: قاموس يحتوي على النصوص والإجراءات لكل زر { "Text": action_function }
        :param place: موقع أول زر { "x": 10, "y": 10 }
        :param text_settings: إعدادات النصوص بجانب الأزرار { "text_position": "right", "width": 20, "bg": "black", "font": ("Arial", 12), "fg": "yellow" }
        :param default: قائمة بالقيم الافتراضية للأزرار (None إذا كانت كلها غير محددة)
        :param pady: المسافة العمودية بين النصوص والأزرار
        """
        if place is None:
            place = {"x": 10, "y": 10}  # موقع افتراضي
        x = place.get("x", 15)
        y = place.get("y", 2)

        # إعدادات النصوص الافتراضية
        text_defaults = {
            "text_position": "right",  # النص بجانب الزر
            "width": 20,  # عرض النص
            "bg": "white",  # لون خلفية النص
            "font": ("Arial", 12),  # نوع الخط وحجمه
            "fg": "black"  # لون النص
        }
        if text_settings:
            text_defaults.update(text_settings)  # دمج الإعدادات المرسلة مع الافتراضية

        # إنشاء المتغيرات المرتبطة بكل CheckBox
        variables = {}
        for text, action in options.items():
            variable = tk.IntVar(value=0 if default is None else default.get(text, 0))
            variables[text] = variable

            # تحديد مكان النص بالنسبة للزر
            if text_defaults["text_position"] == "left":
                label_x = x+30
                button_x = x
            elif text_defaults["text_position"] == "right":
                label_x = x
                button_x = x + 100
            else:
                raise ValueError("text_position must be 'left' or 'right'")

            # إضافة النص بجانب الزر
            label = tk.Label(
                self.root,
                text=text,
                font=text_defaults["font"],
                fg=text_defaults["fg"],
                bg=text_defaults["bg"],
                width=text_defaults["width"]
            )
            label.place(x=label_x, y=y+3)

            # إضافة CheckBox
            checkbox = tk.Checkbutton(
                self.root,
                variable=variable,
                command=lambda var=variable, func=action: self.handle_checkbox(var, func),
                font=text_defaults["font"],
                fg=text_defaults["fg"],
                bg=text_defaults["bg"]
            )
            checkbox.place(x=button_x, y=y + pady)  # إضافة المسافة العمودية

            y += 30  # نقل الموقع العمودي للزر التالي

        return variables

    def handle_checkbox(self, variable, action):
        """
        دالة لمعالجة الضغط على CheckBox
        :param variable: المتغير المرتبط بالزر
        :param action: الإجراء المرتبط بالزر
        """
        print(f"قيمة CheckBox: {variable.get()}")
        if action:
            action()



    def draw_square(self, place, length, width, bg, border_thick, border_color):
        """رسم مربع"""
        self.t.penup()
        self.t.goto(place["x"], place["y"])
        self.t.pendown()
        self.t.color(border_color, bg)
        self.t.width(border_thick)
        self.t.begin_fill()
        for _ in range(4):
            self.t.forward(length)
            self.t.right(90)
        self.t.end_fill()

    def draw_rectangle(self, place, length, width, bg, border_thick, border_color):
        """رسم مستطيل"""
        self.t.penup()
        self.t.goto(place["x"], place["y"])
        self.t.pendown()
        self.t.color(border_color, bg)
        self.t.width(border_thick)
        self.t.begin_fill()
        for _ in range(2):
            self.t.forward(length)
            self.t.right(90)
            self.t.forward(width)
            self.t.right(90)
        self.t.end_fill()

    def draw_triangle(self, place, length, width, bg, border_thick, border_color):
        """رسم مثلث"""
        self.t.penup()
        self.t.goto(place["x"], place["y"])
        self.t.pendown()
        self.t.color(border_color, bg)
        self.t.width(border_thick)
        self.t.begin_fill()
        self.t.forward(length)
        self.t.right(120)
        self.t.forward(width)
        self.t.right(120)
        self.t.forward(width)
        self.t.end_fill()

    def draw_circle(self, place, radius, bg, border_thick, border_color):
        """رسم دائرة"""
        self.t.penup()
        self.t.goto(place["x"], place["y"] - radius)  # تعديل الموقع ليبدأ من المركز
        self.t.pendown()
        self.t.color(border_color, bg)
        self.t.width(border_thick)
        self.t.begin_fill()
        self.t.circle(radius)
        self.t.end_fill()

    def run_turtle(self):
        """تشغيل شاشة Turtle"""
        self.turtle_screen.mainloop()

    def run(self):
        """تشغيل التطبيق"""
        self.root.mainloop()
