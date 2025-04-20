# 🏫 School Report Card Generator (Python CLI App)

A smart, modular command-line application to manage students, track grades, attendance, and performance. Built using **OOP, JSON I/O, and CLI interaction**.

Perfect for small schools, tutors, or anyone who wants to practice Python and real-world software design!

---

## 📌 Features

✅ Add Students  
✅ Add Subject Grades  
✅ Show Class Average  
✅ View Student Performance  
✅ See Top Student (auto-ranked)  
✅ Save & Load All Data via JSON  
✅ CLI-based menu system

---

## 🧠 Concepts Used

- Python OOP (Inheritance, Encapsulation, Polymorphism)  
- Abstract Base Classes (`abc`)  
- `@property` decorators  
- File handling (`.json`, `.txt`)  
- CLI input/output  
- Class composition and modular design

---

## 📂 Project Structure

```bash
.
├── allfunctions.py     # All core classes and logic
├── script.py           # CLI interface
├── welcome.txt         # Fancy welcome screen
└── file.json           # Saved student data (auto-generated)
```

---

## 🚀 How to Run

```bash
git clone https://github.com/Bernardusz/School-Report-Card-Generator.git
cd School-Report-Card-Generator
python script.py
```

---

## 🧾 Sample Commands

```pgsql
Add Student
Add Grade
Show Class Average
Return Class Performance
Top Student
Save to JSON
Load from JSON
Exit
```

---

## 💾 JSON Format Example

```json
{
  "students": {
    "Bernardus": {
      "Name": "Bernardus",
      "Age": 15,
      "Grades": {
        "grades": {
          "Science": 100,
          "English": 100
        }
      },
      "Attendance": 20,
      "Average": true,
      "Excellent": true,
      "Exreacurricular Point": 20,
      "Average Grade": 100.0,
      "Subjects Total": 2
    }
  }
}
```

---

## ✨ Creator

Built with 🔥 and 4+ hours of grind by **Bernardus**

"More study = Bigger brain 💡"
