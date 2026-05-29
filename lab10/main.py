from dop import MMNMSystem

def main():
    print("Моделирование системы M/M/n/m")
    try:
        lambda_val = float(input("Введите lambda (интенсивность входа): "))
        mu_val = float(input("Введите mu (интенсивность обслуживания): "))
        n_servers = int(input("Введите количество серверов (n): "))
        queue_size = int(input("Введите размер очереди (m): "))
        T_val = float(input("Введите время моделирования (T): "))

        system = MMNMSystem(lambda_=lambda_val, mu=mu_val, n_servers=n_servers, queue_size=queue_size)
        res = system.simulate(T=T_val)

        print(f"Параметры: lambda={lambda_val}, mu={mu_val}, n={n_servers}, m={queue_size}")
        rho = lambda_val / (n_servers * mu_val)
        print(f"Загрузка системы (rho): {rho:.4f}")

        print(f"\nСтатистика заявок:")
        print(f"  Поступило:   {res['arrived']}")
        print(f"  Обслужено:   {res['served']}")
        print(f"  Потеряно:    {res['lost']}")
        print(f"  Вероятность отказа: {res['loss_prob']:.6f}")

        print(f"\nРаспределение числа заявок в системе (P_k):")
        sorted_states = sorted(res['distribution'].keys())
        for k in sorted_states:
            prob = res['distribution'][k]
            print(f"  P{k} (заявок в системе: {k}): {prob:.6f}")

    except ValueError as e:
        print(f"Ошибка ввода: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
