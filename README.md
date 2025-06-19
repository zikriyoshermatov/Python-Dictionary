## 🟩 1. **Dictionary — Yaratish (Dictionary Creation)**

### 🎯 Task 1:

Bo‘sh `student` dict yarat va unga `name`, `age`, `grade` kalitlarini qiymatlari bilan qo‘sh.

### 🎯 Task 2:

Quyidagi ma’lumotdan foydalangan holda `book` nomli dict tuz:

```python
title: "Python Basics"
author: "Diyorbek Jumanov"
pages: 250
```

### 🎯 Task 3:

Ikki dict yarat: `user1`, `user2`. Har birida `name`, `email` bo‘lsin. So‘ng ular ro‘yxatga joylashtirilsin:

```python
users = [user1, user2]
```

---

## 🟩 2. **Dictionary Access Item**

### 🎯 Task 4:

Quyidagi dictdan `brand` va `color` ni alohida chop et:

```python
car = {"brand": "Chevrolet", "model": "Cobalt", "color": "white"}
```

### 🎯 Task 5:

`.get()` metodi orqali `year` degan kalitni o‘qishga harakat qil. U mavjud emas. Default qiymat ber.

### 🎯 Task 6:

Foydalanuvchidan `kalit` nomini input orqali so‘ra. Agar dictda shu kalit bo‘lsa, qiymatini chiqarsin, aks holda `"Topilmadi"` chiqarsin.

---

## 🟩 3. **Dictionary Change Item**

### 🎯 Task 7:

Quyidagi dictda `age` qiymatini `26` ga o‘zgartir:

```python
person = {"name": "Ali", "age": 25, "city": "Tashkent"}
```

### 🎯 Task 8:

`user` dict bor. Email noto‘g‘ri yozilgan. Uni `correct@email.com` ga almashtir.

### 🎯 Task 9:

Ro‘yxatdagi har bir `user` ning `active` qiymatini `False` qilib chiq:

```python
users = [
  {"id": 1, "active": True},
  {"id": 2, "active": True},
]
```

---

## 🟩 4. **Dictionary Add Item**

### 🎯 Task 10:

Quyidagi dictga `email` kalitini qo‘sh: `"email": "ali@example.com"`

```python
person = {"name": "Ali", "age": 25}
```

### 🎯 Task 11:

Bo‘sh `config` dict yarat. Foydalanuvchidan 3 ta `setting` nomi va qiymati so‘raladi. Ularni dictga joyla.

### 🎯 Task 12:

`inventory` dict bor. Agar mahsulot yo‘q bo‘lsa, uni `quantity = 0` bilan qo‘sh.

---

## 🟩 5. **Dictionary Remove Item**

### 🎯 Task 13:

Quyidagi dictdan `city` kalitini o‘chir:

```python
person = {"name": "Ali", "age": 25, "city": "Tashkent"}
```

### 🎯 Task 14:

`.pop()` metodi yordamida `age` ni olib tashla va qiymatini ekranga chiqar.

### 🎯 Task 15:

`clear()` metodidan foydalanib, `settings` dictni tozalang.

### 🎯 Task 16 (Muhim):

Foydalanuvchidan kalit nomi so‘raladi. Agar dictda mavjud bo‘lsa, o‘chiriladi. Aks holda `"Bunday kalit yo‘q"` chiqariladi.

---

## 🟩 6. **Dictionary Loop**

### 🎯 Task 17:

Quyidagi dictni `for` loop orqali chiqar: `kalit → qiymat` ko‘rinishida.

```python
student = {"name": "Ali", "age": 25, "grade": "A"}
```

### 🎯 Task 18:

`items()` yordamida barcha juftliklarni chiqar. Har bir kalitni katta harflarda chiqarsin:

```python
name → Ali  → NAME → Ali
```

### 🎯 Task 19:

Quyidagi dictdagi barcha `qiymat`lar soni bo‘lsa, ularni yig‘indisini hisobla:

```python
scores = {"math": 90, "english": 85, "science": 92}
```

### 🎯 Task 20 (Muhim):

Quyidagi dictda faqat qiymati `True` bo‘lgan kalitlarni chiqar:

```python
permissions = {"read": True, "write": False, "delete": True}
# chiqishi: read, delete
```

---

## 🧪 **10 ta aralash va chuqur dict amaliy mashq (function-based)**

---

### ✅ Task 21: Ismlar sonini sanash

**Funksiya yarat**:

```python
def count_names(names: list[str]) -> dict[str, int]:
```

**Shart**: Berilgan `names` ro‘yxatidagi har bir ism necha marta uchraganini hisoblab, dict qaytar.
✅ Natija: `{"Ali": 3, "Vali": 2, "Sami": 1}`

---

### ✅ Task 22: Talabalarni guruhlash

**Funksiya yarat**:

```python
def group_students(students: list[dict[str, str]]) -> dict[str, list[str]]:
```

**Shart**: Har bir talaba ismini u tegishli bo‘lgan `group` bo‘yicha dict shaklida qaytar.
✅ Natija: `{"A": ["Ali", "Soli"], "B": ["Vali", "Karim"]}`

---

### ✅ Task 23: Qiymatlar bo‘yicha indekslarni guruhlash

**Funksiya yarat**:

```python
def group_indices(numbers: list[int]) -> dict[int, list[int]]:
```

**Shart**: Har bir noyob son uchun u ro‘yxatda qayerda turganini ko‘rsatuvchi dict qaytar.
✅ Natija: `{1: [0, 2, 5], 2: [1, 4], ...}`

---

### ✅ Task 24: Eng ko‘p uchragan harfni topish

**Funksiya yarat**:

```python
def most_common_char(text: str) -> str:
```

**Shart**: Berilgan matndagi eng ko‘p uchraydigan bitta harfni qaytar.

---

### ✅ Task 25: Yosh bo‘yicha guruhlash

**Funksiya yarat**:

```python
def group_by_age(people: list[dict[str, int | str]]) -> dict[int, list[str]]:
```

**Shart**: Har bir odamni `age` bo‘yicha guruhlab, ismlarini list ko‘rinishida qaytar.

---

### ✅ Task 26: 2 ta dictni birlashtirish

**Funksiya yarat**:

```python
def merge_dicts(a: dict, b: dict) -> dict:
```

**Shart**: Berilgan ikkita dictni birlashtir. Agar bir xil kalit bo‘lsa, `b` dagi qiymat ustun bo‘lsin.

---

### ✅ Task 27: Telefon daftari (Mini loyihacha)

**Funksiya yarat**:

```python
def phonebook_menu(phonebook: dict[str, str]) -> None:
```

**Shart**:

* 1: Kontakt qo‘shish (`ism → telefon`)
* 2: Barcha kontaktlarni chiqarish
* 3: Ism bo‘yicha telefon qidirish

📌 `dict` bilan `menu` (input orqali) ishlash ko‘nikmasini beradi.

---

### ✅ Task 28: Satr uzunligi bo‘yicha guruhlash

**Funksiya yarat**:

```python
def group_by_length(words: list[str]) -> dict[int, list[str]]:
```

**Shart**: Har bir so‘zni uzunligiga qarab dict ichiga guruhlab joylashtir.

---

### ✅ Task 29: Active foydalanuvchilarni chiqarish

**Funksiya yarat**:

```python
def get_active_users(users: dict[str, dict[str, bool | str]]) -> list[str]:
```

**Shart**: Faqat `"active": True` bo‘lgan foydalanuvchilarning ismini ro‘yxat qilib qaytar.

---

### ✅ Task 30: Qiymati 0 bo‘lmagan elementlarni ajrat

**Funksiya yarat**:

```python
def filter_non_zero(d: dict[str, int]) -> dict[str, int]:
```

**Shart**: Faqat qiymati 0 dan farq qiladigan kalit-qiymat juftliklarini yangi dict sifatida qaytar.

---

## 🎁 Bonus (Challenge)

### ✅ Task 31: Harflar chastotasini hisoblash

**Funksiya yarat**:

```python
def count_letters(text: str) -> dict[str, int]:
```

**Shart**: Berilgan matndagi harflarning necha marta uchrashini hisoblab, dict qaytar.
✅ Masalan: `"assalomu alaykum"` → `{ 'a': 4, 's': 2, 'l': 2, ... }`

---
