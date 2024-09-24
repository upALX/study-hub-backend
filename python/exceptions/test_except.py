
try: 
    x = 10 / 0


except ZeroDivisionError as ex:
    print(f'Error syntax message: {str(ex)}')

except Exception as ex:
    raise ex from None