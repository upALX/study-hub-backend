#Rupal has a huge collection of country stamps. [Rupal possui um enorme acervo de selos country.] She decided to count the total number of distinct country stamps in her collection. [Ela decidiu contar o número total de selos de países distintos em sua coleção.] She asked for your help. [Ela pediu sua ajuda.] You pick the stamps one by one from a stack of  country stamps [Você escolhe os selos um por um em uma pilha de selos de países] .

if __name__ == "__main__": 
    total_countries = int(input())
    
    list_countries = []
    for _ in range(total_countries):
        country_name = input()
        list_countries.append(country_name)
        
    only_countries_dont_repeat = set(list_countries)
    
    print(len(only_countries_dont_repeat))