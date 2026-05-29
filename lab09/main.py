from mmm import MM1System


def main():
    print("Моделирование системы M/M/1")
    
    try:
        lambda_val = float(input("Введите lambda (интенсивность входа): "))
        mu_val = float(input("Введите mu (интенсивность обслуживания): "))
        T_val = float(input("Введите T (время моделирования): "))

        system = MM1System(lambda_=lambda_val, mu=mu_val)
        
        res = system.simulate(T=T_val)

        print(f"\nСтатистика заявок:")
        print(f"  Поступило:   {res['arrived']}")
        print(f"  Обслужено:   {res['served']}")
        print(f"  Потеряно:    {res['lost']}")
        
        print(f"\nВероятности:")
        print(f"  Эмпирическая вероятность отказа: {res['loss_prob_empirical']:.6f}")
        
    
        rho = res['rho']
        theoretical_loss = rho / (1 + rho)
        print(f"  Теоретическая вероятность отказа: {theoretical_loss:.6f}")

        print(f"\nРаспределение времени состояний (P_k):")
        for k in sorted(res['distribution'].keys()):
            prob = res['distribution'][k]
            print(f"  P{k} (клиентов в системе: {k}): {prob:.6f}")

    except ValueError as e:
        print(f"Ошибка ввода: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
