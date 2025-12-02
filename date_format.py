import csv

purchase_dict = {}

with open('purchase_log.csv', 'r', encoding='utf-8') as f_purchases:
    reader = csv.DictReader(f_purchases)
    for row in reader:
        user_id = row['user_id']
        category = row['category']
        purchase_dict[user_id] = category

with open('visit_log.csv', 'r', encoding='utf-8') as f_visits, \
     open('funnel.csv', 'w', encoding='utf-8', newline='') as f_funnel:

    visits_reader = csv.DictReader(f_visits)
    fieldnames = visits_reader.fieldnames + ['category']

    funnel_writer = csv.DictWriter(f_funnel, fieldnames=fieldnames)
    funnel_writer.writeheader()
    for row in visits_reader:
        user_id = row['user_id']
        if user_id in purchase_dict:
            row['category'] = purchase_dict[user_id]
            funnel_writer.writerow(row)
