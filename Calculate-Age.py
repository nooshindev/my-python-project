from datetime import datetime

# دریافت سال تولد از کاربر
birth_year = int(input("Enter your birth year: "))

# سال فعلی
current_year = datetime.now().year

# محاسبه‌ی سن به سال
age_years = current_year - birth_year

# تبدیل سن به واحدهای کوچکتر
age_days = age_years * 365        # برای سادگی، سال کبیسه لحاظ نشده
age_hours = age_days * 24
age_minutes = age_hours * 60
age_seconds = age_minutes * 60

# نمایش نتایج
print(f"\nYou are approximately {age_years} years old.")
print(f"That’s about {age_hours:,} hours.")
print(f"Or about {age_minutes:,} minutes.")
print(f"And around {age_seconds:,} seconds.")
