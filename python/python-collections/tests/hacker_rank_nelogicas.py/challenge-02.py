def count_by_prefix_name(prefix_query,names_list):
    names_prefix_finded = 0

    for name in names_list:
        for prefix in prefix_query:
            if name.startswith(prefix):
                if len(prefix_query) < len(name):
                    names_prefix_finded += 1

    return names_prefix_finded

# Exemplo de uso:
names_list = ['João', 'Maria', 'José', 'Carlos', 'Joaquim', 'Marcela']
   
prefix_query = ['Jo', 'Ma', 'mini']

if prefix_query in names_list:
    raise Exception

resultado = count_by_prefix_name(prefix_query=prefix_query, names_list=names_list, )

print(resultado)