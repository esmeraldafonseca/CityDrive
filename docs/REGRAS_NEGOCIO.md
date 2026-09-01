# CityDrive — Regras de negócio

1. O início deve ser anterior ao fim.
2. A viatura deve existir e estar ativa.
3. A estação deve existir e estar ativa.
4. A reserva deve respeitar o horário de funcionamento da estação.
5. Não pode existir sobreposição com outra reserva ativa da mesma viatura.
6. O fim de uma reserva pode coincidir com o início da seguinte.
7. Reservas CANCELADA e CONCLUIDA não bloqueiam a viatura.
8. O cliente deve existir.
9. Uma reserva confirmada ocupa a viatura no intervalo [inicio, fim).
10. Exemplo: 06:30–12:00 bloqueia a viatura até às 12:00; às 12:00 pode existir uma nova reserva.

Estados: PENDENTE, CONFIRMADA, EM_CURSO, CONCLUIDA, CANCELADA.
