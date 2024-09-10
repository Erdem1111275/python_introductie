import time


def sieve_from_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    current_prime = 2

    while current_prime * current_prime <= limit:
        if is_prime[current_prime]:
            for multiple in range(current_prime * current_prime, limit + 1, current_prime):
                is_prime[multiple] = False
                
        current_prime += 1

    prime_numbers = []

    for number in range(2, limit + 1):
        if is_prime[number]:
            prime_numbers.append(number)

    return prime_numbers


def search_prime_numbers(number):
    if number in faculty_cache:
        print("Resultaat gevonden in cache")

        return faculty_cache[number]
    
    else:
        print("Resultaat niet gevonden in cache")
        result = sieve_from_eratosthenes(number)
        faculty_cache[number] = result

        return result


faculty_cache = {}

while True:
    prime_numbers_target = input("Geef een getal om de priemgetallen van te bereken of geef [Enter] om te stoppen: ")
    if prime_numbers_target == "":
        break

    timer = time.time()
    prime_number_result = search_prime_numbers(int(prime_numbers_target))
    result_time = time.time() - timer

    print(f"De priemgetallen onder de {prime_numbers_target} zijn:")

    for prime_number in prime_number_result:
        print(prime_number)

    print(f"Resultaat duurde: {result_time:.2f} seconden")

print("Tot ziens!")
