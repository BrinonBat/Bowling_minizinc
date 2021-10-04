include"globals.mzn";
enum coup = {1,2,3,4,5,6,7,8,9,10,/,X};
array [1..10][1..2] of var coup;
% 10 carreaux (deux lancés pour 1 Carreau)

% en cas de strike, un X est sur le deuxième coup et il sera égale au nombre de quilles renversées sur les 2 prochains lancés (30 max)

% en cas de spare ( premier lancé suivi d'un / dansl a notation), on a 10 + nombre de quilles renversées sur le prochain lancé (20 max)

