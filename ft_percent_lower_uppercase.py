UPPERCASE = 'QWERTYUIOPASDFGHJKLZXCVBNMЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
LOWERCASE = 'qwertyuiopasdfghjklzxcvbnmёйцукенгшщзхъфывапролджэячсмитьбю'


def ft_percent_lower_uppercase(a):
    count_upp = 0
    count_low = 0
    for char in a:
        if char in UPPERCASE:
            count_upp += 1
        elif char in LOWERCASE:
            count_low += 1
    return count_low / count_upp
