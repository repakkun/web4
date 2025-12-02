from datetime import datetime

moscow_times_str = "Wednesday, October 2, 2002"
guardian_str = "Friday, 11.10.13"
daily_news_str = "Thursday, 18 August 1977"

moscow_times_date = datetime.strptime(moscow_times_str, "%A, %B %d, %Y")
guardian_date = datetime.strptime(guardian_str, "%A, %d.%m.%y")
daily_news_date = datetime.strptime(daily_news_str, "%A, %d %B %Y")

# Вывод результатов
print("The Moscow Times:", moscow_times_date)
print("The Guardian:", guardian_date)
print("Daily News:", daily_news_date)