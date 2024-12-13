raças_disponiveis = ["labrador", "bulldog", "beagle", "poodle", "vira-lata"]
raça_procurada = input("Qual a raça do cão que você está procurando? ").lower()

if raça_procurada in raças_disponiveis:
    print("Sim, temos essa raça disponível!")
else:
    print("Desculpe, não temos essa raça disponível no momento.")