from .cart import Cart


#Контекстный процессор(context processor) — это функция Python, которая принимает объект запроса в качестве аргумента и возвращает словарь,
#добавляемый в контекст запроса. Они удобны, когда необходимо сделать чтото доступным для всех шаблонов.
def cart(request):
    return {'cart': Cart(request)}