# ShGUI_KW

EasyGraphics مكتبة لإنشاء واجهات رسومية بسهولة باستخدام Tkinter و Turtle. 
توفر المكتبة أدوات لإضافة الأزرار، الحقول النصية، القوائم، والرسم باستخدام Turtle.
تستخدم المكتبة فقط للأغراض الشخصية وليست التجاريه ولا للبيع ولا للتقليد دون ابلاغي بذلك

## كيفية الاستخدام
```python
from ShGUI_KW import EasyGraphics

app = EasyGraphics(title="تطبيقي", size=(500, 500))
app.add_button(text="اضغطني", command=lambda: print("تم الضغط!"))
app.run()
