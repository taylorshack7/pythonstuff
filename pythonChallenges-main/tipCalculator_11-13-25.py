full_dot = '●'
empty_dot = '○'


def create_character(name, strength, intelligence, charisma):
    # Check if applicable string for variable name
    if not (isinstance(name, str)):
        return 'The character name should be a string'
    if name == '':
        return 'The character should have a name'
    if len(name) > 10:
        return 'The character name is too long'
    if ' ' in name:
        return 'The character name should not contain spaces'
    # Check if applicable integer for variables charisma, strength, and intelligence
    if not (isinstance(charisma, int)) or not (isinstance(strength, int)) or not (isinstance(intelligence, int)):
        return 'All stats should be integers'
    if charisma < 1 or strength < 1 or intelligence < 1:
        return 'All stats should be no less than 1'
    if charisma > 4 or strength > 4 or intelligence > 4:
        return 'All stats should be no more than 4'
    if (charisma + strength + intelligence) > 7 or (charisma + strength + intelligence) < 7:
        return 'The character should start with 7 points'
    strength_dots = (strength * full_dot) + ((10 - strength) * empty_dot)
    charisma_dots = (charisma * full_dot) + ((10 - charisma) * empty_dot)
    intelligence_dots = (intelligence * full_dot) + ((10 - intelligence) * empty_dot)

    return (name + '\nSTR ' + strength_dots + '\nINT ' + intelligence_dots + '\nCHA ' + charisma_dots)


character_name = input('Enter a character name: ')

character_strength = int(input(
    '\nNow it is time to set your charcater stats. Charcater stats cannot be <1 & cannot be >4. They also must add up to be 7 (i.e. 4 - Strength, 2 - intelligence, 1 - Charisma)\n\nEnter your character\'s strength: '))

character_intelligence = int(input('Enter your character\'s intelligence : '))

character_charisma = int(input('Enter your character\'s charisma: '))

print(create_character(character_name, character_strength, character_intelligence, character_charisma))
