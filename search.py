pol = [
'''2. Chemical properties of gases
 a. Reactivity
 i. Associates the use of certain gases in various applications with their chemical reactivity (e.g. argon in light bulbs, nitrogen in bags of chips, acetylene in welding torches)''',
'''2. Physical properties of gases
 a. Kinetic theory
 i. Explains the macroscopic behaviour of a gas (e.g. compressibility, expansion, diffusion) using kinetic theory''',
'''2. Physical properties of gases
 b. General gas law''',
'''1. Energy diagram
 b. Interprets the energy diagram of a chemical reaction''',
'''3. Enthalpy change
 a. Explains qualitatively the enthalpy change of substances during a chemical reaction''',
'''1. Factors that influence the reaction rate
 i. Determines experimentally the factors that influence the reaction rate
 a. Nature of the reactants
 i. Explains the effect of the nature of the reactants on the reaction rate
 b. Concentration
 i. Explains the effect of the concentration of the reactants on the reaction rate
 c. Surface area
 i. Explains the effect of the surface area of reactants on the reaction rate
 d. Temperature
 i. Explains the effect of the temperature of the reactants on the reaction rate''',
'''1. Factors that influence the reaction rate
 e. Catalysts
 i. Explains the effect of a catalyst on the reaction rate''',
'''1. Factors that influence the state of equilibrium
 i. Explains qualitatively the state of dynamic equilibrium''',
'''2. Le Chatelier’s Principle
 a. Predicts the direction of the shift in equilibrium of a system following a change in concentration, temperature or pressure''',
'''3. Equilibriumconstant
 a. Acidity and alkalinity constants
 i. Writes as an algebraic expression the equilibrium constant for the dissociation of an acid or a base''',
'''2. Physical properties of gases
 a. Kinetic theory
 i. Explains the macroscopic behaviour of a gas (e.g. compressibility, expansion, diffusion) using kinetic theory''',
 '''
 item 11 continued
 ''',
'''2. Physical properties of gases
 c. Ideal gas law
 ii. Applies the mathematical relationship between the pressure, volume and number of moles of a gas, the ideal gas constant and the temperature of a gas (pV = nRT)
 d. Dalton's law
 i. Applies the mathematical relationship between the total pressure of a mixture of gases and the partial pressures of the component gases (ptotal = ppA+ ppB+ ppC+ …)''',
'''2. Physical properties of gases
 c. Ideal gas law
 ii. Applies the mathematical relationship between the pressure, volume and number of moles of a gas, the ideal gas constant and the temperature of a gas (pV = nRT)
 f. Molar volume of a gas
 i. Calculates the molar volume of a gas at standard temperature and pressure''',
'''2. Physical properties of gases
 e. Avogadro’s hypothesis
 i. Uses Avogadro’s hypothesis to predict the number of molecules in equal volumes of gases subject to the same temperature and pressure''',
'''1. Energy diagram
 a. Produces an energy diagram representing the energy balance for a chemical reaction
 2. Activation energy
 a. Determines the activation energy for a reaction using its energy diagram
 3. Enthalpy Change
 b. Determines the enthalpy change of a reaction, using its energy diagram''',
'''4. Molar heat of reaction
 a. Determines the molar heat of a reaction using a calorimeter''',
'''4. Molar heat of reaction
 a. Determines the molar heat of a reaction using a calorimeter''',
'''4. Molar heat of reaction
 b. Determines the molar heat of a reaction using Hess’s Law or bonding enthalpies''',
'''4. Molar heat of reaction
 b. Determines the molar heat of a reaction using Hess’s Law or bonding enthalpies''',
'''2. Rate law
 i. Describes the relationship between the concentration of the reactants and the reaction rate using algebraic expressions
 ii. Determines the effect of a variation in the concentration of a reactant on the reaction rate, using the related algebraic expression''',
'''1. Factors that influence the state of equilibrium
 c. Concentration
 i. Explains the effect of a change in the concentration of a reactant or a product on a system’s state of equilibrium''',
'''2. Le Chatelier’s Principle
 a. Predicts the direction of the shift in equilibrium of a system following a change in concentration, temperature or pressure
 b. Predicts the effects of a shift in equilibrium on the concentrations of reactants and products''',
'''3. Equilibrium constant
 b. Solubility product constant
 i. Writes as an algebraic expression the equilibrium constant for the dissociation of various substances in water
 ii. Calculates the solubility product constant of a substance''',
'''3. Equilibriumconstant
 a. Acidity and alkalinity constants
 iii. Associates the strength of acids and bases with the value of their acidity or alkalinity constant''',
'''4. Relationship between the pH and the molar concentration of hydronium and hydroxide ions
 a. Describes the relationship between the pH and the molar concentration of hydronium and hydroxide ions
 b. Applies the relationship between the pH and the molar concentration of hydronium ions (pH = -log10 [H+])''',
 ]



find = str(input('Search for: '))

def lookup(find):
    # if any(find in p for p in pol):
        # print('yes')
    matching = [s for s in pol if any(f in s for f in find.split(' '))]
    # print(matching)
    return [pol.index(s) for s in pol if any(f in s for f in find.split(' '))]






lookup(find)
