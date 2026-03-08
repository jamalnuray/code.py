#cari il
current_year=2026

#melumatlar
name = input("Adınızı daxil edin: ")
age = int(input("Yaşınızı daxil edin: "))
weight = float(input("Çəkinizi daxil edin (kg): "))
height = float(input("Boyunuzu daxil edin (metr): "))
hourly_salary = float(input("Saatlıq maaşınızı daxil edin: "))
worked_hours = float(input("İşlədiyiniz saat sayı: "))

#hesablamalar
birth_year = current_year - age 
bmi = weight / (height * height)
total_salary = hourly_salary * worked_hours

#neticeler
print(f"Ad:{name}")
print(f"Yaş:{age}")
print(f"Doğum ili:{birth_year}")
print(f"BMI:{bmi}")
print(f"Ümumi maaş:{total_salary}")