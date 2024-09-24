import file_operations
import random
import os
from faker import Faker


def main():
    skills = [
        "Стремительный прыжок", 
        "Электрический выстрел", 
        "Ледяной удар", 
        "Стремительный удар", 
        "Кислотный взгляд",
        "Тайный побег",
        "Ледяной выстрел",
        "Огненный заряд",
    ]
    
    alphabet = {
        'а': 'а͠', 
        'б': 'б̋', 
        'в': 'в͒͠',
        'г': 'г͒͠', 
        'д': 'д̋', 
        'е': 'е͠',
        'ё': 'ё͒͠', 
        'ж': 'ж͒', 
        'з': 'з̋̋͠',
        'и': 'и', 
        'й': 'й͒͠', 
        'к': 'к̋̋',
        'л': 'л̋͠', 
        'м': 'м͒͠', 
        'н': 'н͒',
        'о': 'о̋', 
        'п': 'п̋͠', 
        'р': 'р̋͠',
        'с': 'с͒', 
        'т': 'т͒', 
        'у': 'у͒͠',
        'ф': 'ф̋̋͠', 
        'х': 'х͒͠', 
        'ц': 'ц̋',
        'ч': 'ч̋͠', 
        'ш': 'ш͒͠', 
        'щ': 'щ̋',
        'ъ': 'ъ̋͠', 
        'ы': 'ы̋͠', 
        'ь': 'ь̋',
        'э': 'э͒͠͠', 
        'ю': 'ю̋͠', 
        'я': 'я̋',
        'А': 'А͠', 
        'Б': 'Б̋', 
        'В': 'В͒͠',
        'Г': 'Г͒͠', 
        'Д': 'Д̋', 
        'Е': 'Е',
        'Ё': 'Ё͒͠', 
        'Ж': 'Ж͒', 
        'З': 'З̋̋͠',
        'И': 'И',
        'Й': 'Й͒͠', 
        'К': 'К̋̋',
        'Л': 'Л̋͠', 
        'М': 'М͒͠', 
        'Н': 'Н͒',
        'О': 'О̋', 
        'П': 'П̋͠', 
        'Р': 'Р̋͠',
        'С': 'С͒', 
        'Т': 'Т͒', 
        'У': 'У͒͠',
        'Ф': 'Ф̋̋͠', 
        'Х': 'Х͒͠', 
        'Ц': 'Ц̋',
        'Ч': 'Ч̋͠', 
        'Ш': 'Ш͒͠', 
        'Щ': 'Щ̋',
        'Ъ': 'Ъ̋͠', 
        'Ы': 'Ы̋͠', 
        'Ь': 'Ь̋',
        'Э': 'Э͒͠͠', 
        'Ю': 'Ю̋͠', 
        'Я': 'Я̋',
        ' ': ' ',
    }
    
    if os.path.isdir("cards") == False:
        os.makedirs("cards", mode=0o777, exist_ok=False) 

    generic_name = Faker("ru_RU")

    for number in range(10):
        male_first_name = generic_name.first_name_male()
        male_last_name = generic_name.last_name_male()

        female_first_name = generic_name.first_name_female()
        female_last_name = generic_name.last_name_female()

        gender = random.choice(["M", "F"])

        if gender == "M": 
            first_name, last_name = male_first_name, male_last_name
        elif gender == "F":
            first_name, last_name = female_first_name, female_last_name
    
        player_skills = random.sample(skills, 3)
        runic_skills = []
    
        for skill in player_skills:
            for letter in alphabet:
                skill = skill.replace(letter, alphabet[letter])
            runic_skills.append(skill)
    
        player_data = {
            "first_name":first_name,
            "last_name":last_name,
            "town":generic_name.city(), 
            "job":generic_name.job(),
            "strength":random.randint(3,18),
            "agility":random.randint(3,18),
            "endurance":random.randint(3,18),
            "intelligence":random.randint(3,18),
            "luck":random.randint(3,18),
            "skill_1":runic_skills[0],
            "skill_2":runic_skills[1],
            "skill_3":runic_skills[2],
        }

        file_operations.render_template("charsheet.svg", f"cards/charsheet{number+1}.svg", player_data)
 
    
if __name__ == '__main__':
    main()

