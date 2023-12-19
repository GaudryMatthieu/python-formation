#Create a loop that prints all prime numbers between 1 and 50.

def sieve_of_eratosthenes():
    num = []
    primes = []
    for i in range(2, 50):
        num.append(i)
        primes.append(i)

    for check in range(len(num)):
        for index in num:
           if num[check] % index == 0:
               if num[check] != index:
                    try :
                        primes.remove(num[check])
                    except ValueError:
                        None

    return primes


def main():
    result = sieve_of_eratosthenes()
    print(result)

if __name__ == "__main__":
    main()