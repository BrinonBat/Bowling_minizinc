include "globals.mzn";

set of int:quilles=0..10;
set of int:lancers=1..21;
set of int:tours=1..10;
set of int:points=0..30;

%array[lancers] of quilles:init=[10,0,8,1,8,2,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0];

array[lancers] of var quilles:partie;
array[tours] of var points:score;
array[tours] of var points:bonus;
var int:score_total;
var int:nb_spares;
var int:nb_strikes;
var int:nb_fails; %nombre de lancer = 0 (pas après un strike)

%init
%constraint forall(l in lancers)(partie[l]=init[l]);

%contraintes de liaisons
constraint (score_total=sum(t in tours)(score[t])+sum(t in tours)(bonus[t]));
constraint forall( t in tours where t<10)(score[t]=partie[2*t-1]+partie[2*t]); %score simple de base sauf dernier coup


%les bonus
constraint forall(t in tours)((partie[2*t-1]+partie[2*t]<10)->(bonus[t]=0)); %pas de bonus 
constraint forall(t in tours)(((partie[2*t-1]+partie[2*t]=10)/\(partie[2*t-1]!=10))->(bonus[t]=partie[2*t+1])); %spare




%contraintes de jeu
constraint forall(t in tours where t<10)(partie[2*t-1]+partie[2*t]<=10);
constraint ((partie[19]!=10)->(partie[19]+partie[20]<=10));

%nombre de spares et de strikes et coups nuls
constraint nb_strikes=sum(t in tours)(bool2int(partie[2*t-1]=10));

%score souhaité
constraint (score_total=290);

%resolution

%solve::int_search(partie, dom_w_deg, indomain_max,complete) maximize(nb_fails);

%solve::int_search(partie, dom_w_deg, indomain_max,complete) minimize(abs(nb_spares-nb_strikes));

%solve::int_search(partie, dom_w_deg, indomain_max,complete) maximize(nb_spares);
solve::int_search(partie, first_fail, indomain_max,complete) satisfy;
%solve satisfy; 

            
output["Lancers : "]++[if ((l mod 2==0) /\ (fix(partie[l-1])=10)/\(l!=20)) then "X" else show(partie[l]) endif ++ if (l mod 2==0) then "|" else " " endif|l in 1..20]++[if ((fix(partie[21])=0) /\ (fix(partie[19])!=10)) then " " else show(partie[21]) endif]++["\nScores base : "]++[show(score[t])++" "|t in tours]++["\nBonus : "]++[show(bonus[t])++" "|t in tours]++["\nScore Total : "]++[show(score_total)]++["\nSpares : "]++[show(nb_spares)]++["\nStrikes : "]++[show(nb_strikes)]++["\nFails : "]++[show(nb_fails)];