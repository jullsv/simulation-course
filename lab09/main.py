from mmm import MM1System


def main():
    print("Моделирование системы M/M/1")
    
    try:
        lambda_val = float(input("Введите lambda (интенсивность входа): "))
        mu_val = float(input("Введите mu (интенсивность обслуживания): "))
        T_val = float(input("Введите T (время моделирования): "))

        system = MM1System(lambda_=lambda_val, mu=mu_val)
        
        res = system.simulate(T=T_val)

        print(f"Параметры: lambda={lambda_val}, mu={mu_val}")
        print(f"Время моделирования: {T_val}")

        print(f"\nЗаявки:")
        print(f"  Поступило:   {res['arrived']}")
        print(f"  Обслужено:   {res['served']}")
        print(f"  Потеряно:    {res['lost']}")
        
        print(f"  Вероятность отказа: {res['loss_prob']:.6f}")
        print(f"  Вероятность принятия: {res['accept_prob']:.6f}")

    except ValueError as e:
        print(f"Ошибка ввода: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
