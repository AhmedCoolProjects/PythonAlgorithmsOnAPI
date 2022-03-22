from classes.theorie_des_jeux import TheorieDesJeux

my_input = {
    "Résidence":[550,110,-310],
    "Immeuble":[300,239,-100],
    "Appartement":[200,100,-32],
    "Aucun":[0,0,0]
}
my_input_proba = [0.4,0.5,0.1]
my_alpha = 0.3

# Start program
my_theorie = TheorieDesJeux(my_input, my_input_proba, my_alpha)
print(my_theorie.savageRegretMinimax())

