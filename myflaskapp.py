from flask import Flask, render_template, url_for
import datetime
import numpy as np
app = Flask(__name__)

app.debug = True

def lookup(find, pol):
    # if any(find in p for p in pol):
        # print('yes')
    matching = [s for s in pol if any(f in s for f in find.split(' '))]
    # print(matching)
    return [pol.index(s) for s in pol if any(f in s for f in find.split(' '))]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inquiry')
def inquiry():
    videos = [
        {
            'title': 'LHC',
            'link': '<iframe width="100%" src="https://www.youtube.com/embed/qXWWgZ-nnEs?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>',
            'question': 'What is the LHC? What questions arose from this experiment?'
        },
        {
            'title': 'Quantum mechanics',
            'link':  '<iframe width="100%" src="https://www.youtube.com/embed/qO_W70VegbQ?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>',
            'question': 'What is quantum mechanics? Who thought of this first?'
        },
        {
            'title': 'Maximum heart rate',
            'link':  '<iframe width="100%" src="https://www.youtube.com/embed/0on5LV3k26o?showinfo=0", frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>',
            'question': 'What is the maximum heart rate? What is the role of the heart?'
        }
    ]
    return render_template('inquiry.html', videos = videos)

@app.route('/chem/<year>/<question>')
def chem(year, question):
    return render_template(f'chem/{year}/{question}.html')

# -----------------------------------------



@app.route('/search/<test>/<text>')
def search(test, text):

    # limit = lookup('solubility')

    test_info = [
    {
        'A11 concepts': ['Gases','Gases','Gases','Energy changes in reactions','Energy changes in reactions','Reaction rates','Reaction rates','Chemical equilibrium','Chemical equilibrium','Chemical equilibrium','Gases','Gases continuted','Gases','Gases','Gases','Energy changes in reactions','Energy changes in reactions','Energy changes in reactions','Energy changes in reactions','Energy changes in reactions','Reaction rates','Chemical equilibrium','Chemical equilibrium','Chemical equilibrium','Chemical equilibrium','Chemical equilibrium'],

        'POL':[
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
    },
    {
        'A11 concepts': [
        'Gases',
        'Gases',
        'Gases',
        'Energy changes in reactions',
        'Energy changes in reactions',
        'Reaction rates',
        'Reaction rates',
        'Chemical equilibrium',
        'Chemical equilibrium',
        'Chemical equilibrium',
        'Gases',
        'Gases',
        'Gases',
        'Gases',
        'Energy changes in reactions',
        'Energy changes in reactions',
        'Energy changes in reactions',
        'Energy changes in reactions',
        'Energy changes in reactions',
        'Reaction rates',
        'Chemical equilibrium',
        'Chemical equilibrium',
        'Chemical equilibrium',
        'Chemical equilibrium',
        'Chemical equilibrium'
        ],

        'POL':[
        '''2. Physical properties of gases
         a. Kinetic theory
         i. Explains the macroscopic behaviour of a gas (compressibility, expansion, diffusion) using kinetic theory''',
        '''2. Physical properties of gases
         b. General gas law''',
        '''2. Physical properties of gases
         c. Idealgas law
         ii. Applies the mathematical relationship between the pressure, volume and number of moles of a gas, the ideal gas constant and the temperature of a gas (pV = nRT)''',
        '''1. Energy diagram
         b. Interprets the energy diagram of a chemical reaction''',
        '''3. Enthalpy change
         a. Explains qualitatively the enthalpy change of substances during a chemical reaction''',
        '''1. Factors that influence the reaction rate
         i. Determines experimentally the factors that influence the reaction rate
         a. Nature of the reactants
         i. Explains the effect of the nature of the reactants on the reaction rate
         b. Concentration
         Explains the effect of the concentration of the reactants on the reaction rate
         c. Surface area
         i. Explains the effect of the surface area of reactants on the reaction rate''',
        '''2. Rate law
         a. Describes the relationship between the concentration of the reactants and the reaction rate using algebraic expressions''',
        '''1. Factors that influence the state of equilibrium
         i. Explains qualitatively the state of dynamic equilibrium''',
        '''2. Le Chatelier’s Principle
         a. Predicts the direction of the shift in equilibrium of a system following a change in concentration, temperature or pressure''',
        '''3. Equilibrium constant
         a. Acidity and alkalinity constants
         iii. Associates the strength of acids and bases with the value of their acidity or alkalinity constant''',
        '''2. Physical properties of gases
         a. Kinetic theory
         i. Explains the macroscopic behaviour of a gas (e.g. compressibility, expansion, diffusion) using kinetic theory''',
        '''2. Physical properties of gases
         d. Dalton's law
         i. Applies the mathematical relationship between the total pressure of a mixture of gases and the partial pressures of the component gases (ptotal = ppA+ ppB+ ppC+ …)''',
        '''2. Physical properties of gases
         c. Ideal gas law
         ii. Applies the mathematical relationship between the pressure, volume and number of moles of a gas, the ideal gas constant and the temperature of a gas (pV = nRT)''',
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
         b. Determines the molar heat of a reaction using Hess’s Law or bondingenthalpies''',
        '''4. Molar heat of reaction
         a. Determines the molar heat of a reaction using a calorimeter''',
        '''4. Molar heat of reaction
         a. Determines the molar heat of a reaction using a calorimeter''',
        '''4. Molar heat of reaction
         b. Determines the molar heat of a reaction using Hess’s Law or bonding enthalpies''',
        '''1. Factors that influence reaction rate
         b. Concentration
         i. Explains the effect of the concentration of the reactants on the reaction rate
         e. Catalyst
         i. Explains the effect of a catalyst on the reaction rate''',
        '''1. Factors that influence the state of equilibrium
         c. Concentration
         i. Explains the effect of a change in the concentration of a reactant or a product on a system’s state of equilibrium''',
        '''3. Equilibriumconstant
         a. Acidity and alkalinity constants
         ii. Experimentally determines the acidity or alkalinity constant of a system''',
        '''2. Le Chatelier’s Principle
         a. Predicts the direction of the shift in equilibrium of a system following a change in concentration, temperature or pressure
         b. Predicts the effects of a shift in equilibrium on the concentrations of reactants and products''',
        '''3. Equilibrium constant
         b. Solubility product constant
         i. Writes as an algebraic expression the equilibrium constant for the dissociation of various substances in water
         ii. Calculates the solubility product constant of a substance''',
        '''4. Relationship between the pH and the molar concentration of hydronium and hydroxide ions
         a. Describes the relationship between the pH and the molar concentration of hydronium and hydroxide ions
         b. Applies the relationship between the pH and the molar concentration of hydronium ions (pH = -log10 [H+])''',
        ]
    },
    {
        'A11 concepts': [
        'Gases',
        'Gases',
        'Gases',
        'Energy changes in reactions',
        'Energy changes in reactions',
        'Reaction rates',
        'Reaction rates',
        'Chemical equilibrium',
        'Chemical equilibrium',
        'Chemical equilibrium',
        'Gases',
        'Gases',
        'Gases',
        'Gases',
        'Energy changes in reactions',
        'Energy changes in reactions',
        'Energy changes in reactions',
        'Energy changes in reactions',
        'Energy changes in reactions',
        'Reaction rates',
        'Chemical equilibrium',
        'Chemical equilibrium',
        'Chemical equilibrium',
        'Chemical equilibrium',
        'Chemical equilibrium'
        ],

        'POL':[
        '''2. Physical properties of gases
         a. Kinetic theory
         i. Explains the macroscopic behaviour of a gas (compressibility, expansion, diffusion) using kinetic theory''',
        '''2. Physical properties of gases
         b. General gas law''',
        '''2. Physical properties of gases
         c. Idealgas law
         ii. Applies the mathematical relationship between the pressure, volume and number of moles of a gas, the ideal gas constant and the temperature of a gas (pV = nRT)''',
        '''1. Energy diagram
         b. Interprets the energy diagram of a chemical reaction''',
        '''3. Enthalpy change
         a. Explains qualitatively the enthalpy change of substances during a chemical reaction''',
        '''1. Factors that influence the reaction rate
         i. Determines experimentally the factors that influence the reaction rate
         a. Nature of the reactants
         i. Explains the effect of the nature of the reactants on the reaction rate
         b. Concentration
         Explains the effect of the concentration of the reactants on the reaction rate
         c. Surface area
         i. Explains the effect of the surface area of reactants on the reaction rate''',
        '''2. Rate law
         a. Describes the relationship between the concentration of the reactants and the reaction rate using algebraic expressions''',
        '''1. Factors that influence the state of equilibrium
         i. Explains qualitatively the state of dynamic equilibrium''',
        '''2. Le Chatelier’s Principle
         a. Predicts the direction of the shift in equilibrium of a system following a change in concentration, temperature or pressure''',
        '''3. Equilibrium constant
         a. Acidity and alkalinity constants
         iii. Associates the strength of acids and bases with the value of their acidity or alkalinity constant''',
        '''2. Physical properties of gases
         a. Kinetic theory
         i. Explains the macroscopic behaviour of a gas (e.g. compressibility, expansion, diffusion) using kinetic theory''',
        '''2. Physical properties of gases
         d. Dalton's law
         i. Applies the mathematical relationship between the total pressure of a mixture of gases and the partial pressures of the component gases (ptotal = ppA+ ppB+ ppC+ …)''',
        '''2. Physical properties of gases
         c. Ideal gas law
         ii. Applies the mathematical relationship between the pressure, volume and number of moles of a gas, the ideal gas constant and the temperature of a gas (pV = nRT)''',
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
         b. Determines the molar heat of a reaction using Hess’s Law or bondingenthalpies''',
        '''4. Molar heat of reaction
         a. Determines the molar heat of a reaction using a calorimeter''',
        '''4. Molar heat of reaction
         a. Determines the molar heat of a reaction using a calorimeter''',
        '''4. Molar heat of reaction
         b. Determines the molar heat of a reaction using Hess’s Law or bonding enthalpies''',
        '''1. Factors that influence reaction rate
         b. Concentration
         i. Explains the effect of the concentration of the reactants on the reaction rate
         e. Catalyst
         i. Explains the effect of a catalyst on the reaction rate''',
        '''1. Factors that influence the state of equilibrium
         c. Concentration
         i. Explains the effect of a change in the concentration of a reactant or a product on a system’s state of equilibrium''',
        '''3. Equilibriumconstant
         a. Acidity and alkalinity constants
         ii. Experimentally determines the acidity or alkalinity constant of a system''',
        '''2. Le Chatelier’s Principle
         a. Predicts the direction of the shift in equilibrium of a system following a change in concentration, temperature or pressure
         b. Predicts the effects of a shift in equilibrium on the concentrations of reactants and products''',
        '''3. Equilibrium constant
         b. Solubility product constant
         i. Writes as an algebraic expression the equilibrium constant for the dissociation of various substances in water
         ii. Calculates the solubility product constant of a substance''',
        '''4. Relationship between the pH and the molar concentration of hydronium and hydroxide ions
         a. Describes the relationship between the pH and the molar concentration of hydronium and hydroxide ions
         b. Applies the relationship between the pH and the molar concentration of hydronium ions (pH = -log10 [H+])''',
        ]
    },
    {
        'concepts': [
        'Gases',
        'Gases',
        'Gases',
        'Energy changes in reactions',
        'Energy changes in reactions',
        'Reaction rates',
        'Reaction rates',
        'Chemical equilibrium',
        'Chemical equilibrium',
        'Chemical equilibrium',
        'Gases',
        'Gases',
        'Gases',
        'Gases',
        'Energy changes in reactions',
        'Energy changes in reactions',
        'Energy changes in reactions',
        'Energy changes in reactions',
        'Energy changes in reactions',
        'Reaction rates',
        'Chemical equilibrium',
        'Chemical equilibrium',
        'Chemical equilibrium',
        'Chemical equilibrium',
        'Chemical equilibrium'
        ],

        'POL':[
        '''2. Physical properties of gases
         a. Kinetic theory
         i. Explains the macroscopic behaviour of a gas (compressibility, expansion, diffusion) using kinetic theory''',
        '''2. Physical properties of gases
         b. General gas law''',
        '''2. Physical properties of gases
         c. Idealgas law
         ii. Applies the mathematical relationship between the pressure, volume and number of moles of a gas, the ideal gas constant and the temperature of a gas (pV = nRT)''',
        '''1. Energy diagram
         b. Interprets the energy diagram of a chemical reaction''',
        '''3. Enthalpy change
         a. Explains qualitatively the enthalpy change of substances during a chemical reaction''',
        '''1. Factors that influence the reaction rate
         i. Determines experimentally the factors that influence the reaction rate
         a. Nature of the reactants
         i. Explains the effect of the nature of the reactants on the reaction rate
         b. Concentration
         Explains the effect of the concentration of the reactants on the reaction rate
         c. Surface area
         i. Explains the effect of the surface area of reactants on the reaction rate''',
        '''2. Rate law
         a. Describes the relationship between the concentration of the reactants and the reaction rate using algebraic expressions''',
        '''1. Factors that influence the state of equilibrium
         i. Explains qualitatively the state of dynamic equilibrium''',
        '''2. Le Chatelier’s Principle
         a. Predicts the direction of the shift in equilibrium of a system following a change in concentration, temperature or pressure''',
        '''3. Equilibrium constant
         a. Acidity and alkalinity constants
         iii. Associates the strength of acids and bases with the value of their acidity or alkalinity constant''',
        '''2. Physical properties of gases
         a. Kinetic theory
         i. Explains the macroscopic behaviour of a gas (e.g. compressibility, expansion, diffusion) using kinetic theory''',
        '''2. Physical properties of gases
         d. Dalton's law
         i. Applies the mathematical relationship between the total pressure of a mixture of gases and the partial pressures of the component gases (ptotal = ppA+ ppB+ ppC+ …)''',
        '''2. Physical properties of gases
         c. Ideal gas law
         ii. Applies the mathematical relationship between the pressure, volume and number of moles of a gas, the ideal gas constant and the temperature of a gas (pV = nRT)''',
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
         b. Determines the molar heat of a reaction using Hess’s Law or bondingenthalpies''',
        '''4. Molar heat of reaction
         a. Determines the molar heat of a reaction using a calorimeter''',
        '''4. Molar heat of reaction
         a. Determines the molar heat of a reaction using a calorimeter''',
        '''4. Molar heat of reaction
         b. Determines the molar heat of a reaction using Hess’s Law or bonding enthalpies''',
        '''1. Factors that influence reaction rate
         b. Concentration
         i. Explains the effect of the concentration of the reactants on the reaction rate
         e. Catalyst
         i. Explains the effect of a catalyst on the reaction rate''',
        '''1. Factors that influence the state of equilibrium
         c. Concentration
         i. Explains the effect of a change in the concentration of a reactant or a product on a system’s state of equilibrium''',
        '''3. Equilibriumconstant
         a. Acidity and alkalinity constants
         ii. Experimentally determines the acidity or alkalinity constant of a system''',
        '''2. Le Chatelier’s Principle
         a. Predicts the direction of the shift in equilibrium of a system following a change in concentration, temperature or pressure
         b. Predicts the effects of a shift in equilibrium on the concentrations of reactants and products''',
        '''3. Equilibrium constant
         b. Solubility product constant
         i. Writes as an algebraic expression the equilibrium constant for the dissociation of various substances in water
         ii. Calculates the solubility product constant of a substance''',
        '''4. Relationship between the pH and the molar concentration of hydronium and hydroxide ions
         a. Describes the relationship between the pH and the molar concentration of hydronium and hydroxide ions
         b. Applies the relationship between the pH and the molar concentration of hydronium ions (pH = -log10 [H+])''',
        ]
    },
    {
        'concepts': [
        'Gases',
        'Gases',
        'Gases',
        'Energy changes in reactions',
        'Energy changes in reactions',
        'Reaction rates',
        'Reaction rates',
        'Chemical equilibrium',
        'Chemical equilibrium',
        'Chemical equilibrium',
        'Gases',
        'Gases',
        'Gases',
        'Gases',
        'Energy changes in reactions',
        'Energy changes in reactions',
        'Energy changes in reactions',
        'Energy changes in reactions',
        'Energy changes in reactions',
        'Reaction rates',
        'Chemical equilibrium',
        'Chemical equilibrium',
        'Chemical equilibrium',
        'Chemical equilibrium',
        'Chemical equilibrium'
        ],

        'POL':[
        '''2. Physical properties of gases
         a. Kinetic theory
         i. Explains the macroscopic behaviour of a gas (compressibility, expansion, diffusion) using kinetic theory''',
        '''2. Physical properties of gases
         b. General gas law''',
        '''2. Physical properties of gases
         c. Idealgas law
         ii. Applies the mathematical relationship between the pressure, volume and number of moles of a gas, the ideal gas constant and the temperature of a gas (pV = nRT)''',
        '''1. Energy diagram
         b. Interprets the energy diagram of a chemical reaction''',
        '''3. Enthalpy change
         a. Explains qualitatively the enthalpy change of substances during a chemical reaction''',
        '''1. Factors that influence the reaction rate
         i. Determines experimentally the factors that influence the reaction rate
         a. Nature of the reactants
         i. Explains the effect of the nature of the reactants on the reaction rate
         b. Concentration
         Explains the effect of the concentration of the reactants on the reaction rate
         c. Surface area
         i. Explains the effect of the surface area of reactants on the reaction rate''',
        '''2. Rate law
         a. Describes the relationship between the concentration of the reactants and the reaction rate using algebraic expressions''',
        '''1. Factors that influence the state of equilibrium
         i. Explains qualitatively the state of dynamic equilibrium''',
        '''2. Le Chatelier’s Principle
         a. Predicts the direction of the shift in equilibrium of a system following a change in concentration, temperature or pressure''',
        '''3. Equilibrium constant
         a. Acidity and alkalinity constants
         iii. Associates the strength of acids and bases with the value of their acidity or alkalinity constant''',
        '''2. Physical properties of gases
         a. Kinetic theory
         i. Explains the macroscopic behaviour of a gas (e.g. compressibility, expansion, diffusion) using kinetic theory''',
        '''2. Physical properties of gases
         d. Dalton's law
         i. Applies the mathematical relationship between the total pressure of a mixture of gases and the partial pressures of the component gases (ptotal = ppA+ ppB+ ppC+ …)''',
        '''2. Physical properties of gases
         c. Ideal gas law
         ii. Applies the mathematical relationship between the pressure, volume and number of moles of a gas, the ideal gas constant and the temperature of a gas (pV = nRT)''',
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
         b. Determines the molar heat of a reaction using Hess’s Law or bondingenthalpies''',
        '''4. Molar heat of reaction
         a. Determines the molar heat of a reaction using a calorimeter''',
        '''4. Molar heat of reaction
         a. Determines the molar heat of a reaction using a calorimeter''',
        '''4. Molar heat of reaction
         b. Determines the molar heat of a reaction using Hess’s Law or bonding enthalpies''',
        '''1. Factors that influence reaction rate
         b. Concentration
         i. Explains the effect of the concentration of the reactants on the reaction rate
         e. Catalyst
         i. Explains the effect of a catalyst on the reaction rate''',
        '''1. Factors that influence the state of equilibrium
         c. Concentration
         i. Explains the effect of a change in the concentration of a reactant or a product on a system’s state of equilibrium''',
        '''3. Equilibriumconstant
         a. Acidity and alkalinity constants
         ii. Experimentally determines the acidity or alkalinity constant of a system''',
        '''2. Le Chatelier’s Principle
         a. Predicts the direction of the shift in equilibrium of a system following a change in concentration, temperature or pressure
         b. Predicts the effects of a shift in equilibrium on the concentrations of reactants and products''',
        '''3. Equilibrium constant
         b. Solubility product constant
         i. Writes as an algebraic expression the equilibrium constant for the dissociation of various substances in water
         ii. Calculates the solubility product constant of a substance''',
        '''4. Relationship between the pH and the molar concentration of hydronium and hydroxide ions
         a. Describes the relationship between the pH and the molar concentration of hydronium and hydroxide ions
         b. Applies the relationship between the pH and the molar concentration of hydronium ions (pH = -log10 [H+])''',
        ]
    },
    {
        'concepts': [
        'Gases',
        'Gases',
        'Gases',
        'Energy changes in reactions',
        'Energy changes in reactions',
        'Reaction rates',
        'Reaction rates',
        'Chemical equilibrium',
        'Chemical equilibrium',
        'Chemical equilibrium',
        'Gases',
        'Gases',
        'Gases',
        'Gases',
        'Energy changes in reactions',
        'Energy changes in reactions',
        'Energy changes in reactions',
        'Energy changes in reactions',
        'Energy changes in reactions',
        'Reaction rates',
        'Chemical equilibrium',
        'Chemical equilibrium',
        'Chemical equilibrium',
        'Chemical equilibrium',
        'Chemical equilibrium'
        ],

        'POL':[
        '''2. Physical properties of gases
         a. Kinetic theory
         i. Explains the macroscopic behaviour of a gas (compressibility, expansion, diffusion) using kinetic theory''',
        '''2. Physical properties of gases
         b. General gas law''',
        '''2. Physical properties of gases
         c. Idealgas law
         ii. Applies the mathematical relationship between the pressure, volume and number of moles of a gas, the ideal gas constant and the temperature of a gas (pV = nRT)''',
        '''1. Energy diagram
         b. Interprets the energy diagram of a chemical reaction''',
        '''3. Enthalpy change
         a. Explains qualitatively the enthalpy change of substances during a chemical reaction''',
        '''1. Factors that influence the reaction rate
         i. Determines experimentally the factors that influence the reaction rate
         a. Nature of the reactants
         i. Explains the effect of the nature of the reactants on the reaction rate
         b. Concentration
         Explains the effect of the concentration of the reactants on the reaction rate
         c. Surface area
         i. Explains the effect of the surface area of reactants on the reaction rate''',
        '''2. Rate law
         a. Describes the relationship between the concentration of the reactants and the reaction rate using algebraic expressions''',
        '''1. Factors that influence the state of equilibrium
         i. Explains qualitatively the state of dynamic equilibrium''',
        '''2. Le Chatelier’s Principle
         a. Predicts the direction of the shift in equilibrium of a system following a change in concentration, temperature or pressure''',
        '''3. Equilibrium constant
         a. Acidity and alkalinity constants
         iii. Associates the strength of acids and bases with the value of their acidity or alkalinity constant''',
        '''2. Physical properties of gases
         a. Kinetic theory
         i. Explains the macroscopic behaviour of a gas (e.g. compressibility, expansion, diffusion) using kinetic theory''',
        '''2. Physical properties of gases
         d. Dalton's law
         i. Applies the mathematical relationship between the total pressure of a mixture of gases and the partial pressures of the component gases (ptotal = ppA+ ppB+ ppC+ …)''',
        '''2. Physical properties of gases
         c. Ideal gas law
         ii. Applies the mathematical relationship between the pressure, volume and number of moles of a gas, the ideal gas constant and the temperature of a gas (pV = nRT)''',
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
         b. Determines the molar heat of a reaction using Hess’s Law or bondingenthalpies''',
        '''4. Molar heat of reaction
         a. Determines the molar heat of a reaction using a calorimeter''',
        '''4. Molar heat of reaction
         a. Determines the molar heat of a reaction using a calorimeter''',
        '''4. Molar heat of reaction
         b. Determines the molar heat of a reaction using Hess’s Law or bonding enthalpies''',
        '''1. Factors that influence reaction rate
         b. Concentration
         i. Explains the effect of the concentration of the reactants on the reaction rate
         e. Catalyst
         i. Explains the effect of a catalyst on the reaction rate''',
        '''1. Factors that influence the state of equilibrium
         c. Concentration
         i. Explains the effect of a change in the concentration of a reactant or a product on a system’s state of equilibrium''',
        '''3. Equilibriumconstant
         a. Acidity and alkalinity constants
         ii. Experimentally determines the acidity or alkalinity constant of a system''',
        '''2. Le Chatelier’s Principle
         a. Predicts the direction of the shift in equilibrium of a system following a change in concentration, temperature or pressure
         b. Predicts the effects of a shift in equilibrium on the concentrations of reactants and products''',
        '''3. Equilibrium constant
         b. Solubility product constant
         i. Writes as an algebraic expression the equilibrium constant for the dissociation of various substances in water
         ii. Calculates the solubility product constant of a substance''',
        '''4. Relationship between the pH and the molar concentration of hydronium and hydroxide ions
         a. Describes the relationship between the pH and the molar concentration of hydronium and hydroxide ions
         b. Applies the relationship between the pH and the molar concentration of hydronium ions (pH = -log10 [H+])''',
        ]
    }

    ]
    if test == 'A11':
        t = 0
    elif test == 'A09':
        t = 1
    elif test == 'A05':
        t = 2
    elif test == 'A04':
        t = 3
    elif test == 'A03':
        t = 4
    elif test == 'A02':
        t = 5

    l = np.unique(lookup(text, test_info[t]['POL']))
    return render_template(f'zoom.html', test_info = test_info, l=l, t=t, test=test)
    # this get the list l of found searched POL's and sends it to the page.










# ------------------------------------------

@app.route('/assessments/<test>')
def assessments(test):

    # limit = lookup('solubility')

    test_info = [
    {
        'concepts': ['Gases','Gases','Gases','Energy changes in reactions','Energy changes in reactions','Reaction rates','Reaction rates','Chemical equilibrium','Chemical equilibrium','Chemical equilibrium','Gases','Gases continuted','Gases','Gases','Gases','Energy changes in reactions','Energy changes in reactions','Energy changes in reactions','Energy changes in reactions','Energy changes in reactions','Reaction rates','Chemical equilibrium','Chemical equilibrium','Chemical equilibrium','Chemical equilibrium','Chemical equilibrium'],

        'POL':[
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
    },
    {
        'concepts': [
        'Gases',
        'Gases',
        'Gases',
        'Energy changes in reactions',
        'Energy changes in reactions',
        'Reaction rates',
        'Reaction rates',
        'Chemical equilibrium',
        'Chemical equilibrium',
        'Chemical equilibrium',
        'Gases',
        'Gases',
        'Gases',
        'Gases',
        'Energy changes in reactions',
        'Energy changes in reactions',
        'Energy changes in reactions',
        'Energy changes in reactions',
        'Energy changes in reactions',
        'Reaction rates',
        'Chemical equilibrium',
        'Chemical equilibrium',
        'Chemical equilibrium',
        'Chemical equilibrium',
        'Chemical equilibrium'
        ],

        'POL':[
        '''2. Physical properties of gases
         a. Kinetic theory
         i. Explains the macroscopic behaviour of a gas (compressibility, expansion, diffusion) using kinetic theory''',
        '''2. Physical properties of gases
         b. General gas law''',
        '''2. Physical properties of gases
         c. Idealgas law
         ii. Applies the mathematical relationship between the pressure, volume and number of moles of a gas, the ideal gas constant and the temperature of a gas (pV = nRT)''',
        '''1. Energy diagram
         b. Interprets the energy diagram of a chemical reaction''',
        '''3. Enthalpy change
         a. Explains qualitatively the enthalpy change of substances during a chemical reaction''',
        '''1. Factors that influence the reaction rate
         i. Determines experimentally the factors that influence the reaction rate
         a. Nature of the reactants
         i. Explains the effect of the nature of the reactants on the reaction rate
         b. Concentration
         Explains the effect of the concentration of the reactants on the reaction rate
         c. Surface area
         i. Explains the effect of the surface area of reactants on the reaction rate''',
        '''2. Rate law
         a. Describes the relationship between the concentration of the reactants and the reaction rate using algebraic expressions''',
        '''1. Factors that influence the state of equilibrium
         i. Explains qualitatively the state of dynamic equilibrium''',
        '''2. Le Chatelier’s Principle
         a. Predicts the direction of the shift in equilibrium of a system following a change in concentration, temperature or pressure''',
        '''3. Equilibrium constant
         a. Acidity and alkalinity constants
         iii. Associates the strength of acids and bases with the value of their acidity or alkalinity constant''',
        '''2. Physical properties of gases
         a. Kinetic theory
         i. Explains the macroscopic behaviour of a gas (e.g. compressibility, expansion, diffusion) using kinetic theory''',
        '''2. Physical properties of gases
         d. Dalton's law
         i. Applies the mathematical relationship between the total pressure of a mixture of gases and the partial pressures of the component gases (ptotal = ppA+ ppB+ ppC+ …)''',
        '''2. Physical properties of gases
         c. Ideal gas law
         ii. Applies the mathematical relationship between the pressure, volume and number of moles of a gas, the ideal gas constant and the temperature of a gas (pV = nRT)''',
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
         b. Determines the molar heat of a reaction using Hess’s Law or bondingenthalpies''',
        '''4. Molar heat of reaction
         a. Determines the molar heat of a reaction using a calorimeter''',
        '''4. Molar heat of reaction
         a. Determines the molar heat of a reaction using a calorimeter''',
        '''4. Molar heat of reaction
         b. Determines the molar heat of a reaction using Hess’s Law or bonding enthalpies''',
        '''1. Factors that influence reaction rate
         b. Concentration
         i. Explains the effect of the concentration of the reactants on the reaction rate
         e. Catalyst
         i. Explains the effect of a catalyst on the reaction rate''',
        '''1. Factors that influence the state of equilibrium
         c. Concentration
         i. Explains the effect of a change in the concentration of a reactant or a product on a system’s state of equilibrium''',
        '''3. Equilibriumconstant
         a. Acidity and alkalinity constants
         ii. Experimentally determines the acidity or alkalinity constant of a system''',
        '''2. Le Chatelier’s Principle
         a. Predicts the direction of the shift in equilibrium of a system following a change in concentration, temperature or pressure
         b. Predicts the effects of a shift in equilibrium on the concentrations of reactants and products''',
        '''3. Equilibrium constant
         b. Solubility product constant
         i. Writes as an algebraic expression the equilibrium constant for the dissociation of various substances in water
         ii. Calculates the solubility product constant of a substance''',
        '''4. Relationship between the pH and the molar concentration of hydronium and hydroxide ions
         a. Describes the relationship between the pH and the molar concentration of hydronium and hydroxide ions
         b. Applies the relationship between the pH and the molar concentration of hydronium ions (pH = -log10 [H+])''',
        ]
    },
    {
        'concepts': [
        'Gases',
        'Gases',
        'Gases',
        'Gases',
        'Energy Changes in Reactions',
        'Reaction Rates',
        'Reaction Rates',
        'Chemical Equilibrium',
        'Chemical Equilibrium',
        'Chemical Equilibrium',
        'Gases',
        'Gases',
        'Gases',
        'Energy Changes in Reactions',
        'Energy Changes in Reactions',
        'Energy Changes in Reactions',
        'Energy Changes in Reactions',
        'Energy Changes in Reactions',
        'Energy Changes in Reactions',
        'Reaction Rates',
        'Chemical Equilibrium',
        'Chemical Equilibrium',
        'Chemical Equilibrium',
        'Chemical Equilibrium',
        'Chemical Equilibrium'
        ],

        'POL':[
        '''1. Chemical properties of gases
         a. Reactivity
         i. Associates the use of certain gases in various applications with their chemical reactivity (e.g. argon in light bulbs, nitrogen in bags of chips, acetylene in welding torches).''',
        '''2. Physical properties of gases
         a. Kinetic theory
         i. Explains the macroscopic behaviour of a gas (e.g. compressibility, expansion, diffusion) using kinetic theory.''',
        '''2. Physical properties of gases
         e. Avogadro’s hypothesis
         i. Uses Avogadro’s hypothesis to predict the number of molecules in equal volumes of gases subjected to the same temperature and pressure.''',
        '''2. Physical properties of gases
         b. General gas law
         i. Determines the relationship between the pressure of a gas and its volume when the temperature and number of moles of gas are kept constant.
         ii. Determines the relationship between the pressure of a gas and its temperature when the number of moles of gas and the volume are kept constant.
         iii. Determines the relationship between the volume of a gas and its temperature when the pressure and the number of moles of gas are kept constant.''',
        '''3. Enthalpy change
         a. Explains qualitatively the enthalpy change of substances during a chemical reaction.''',
        '''2. Rate law
         a. Describes the relationship between the concentration of the reactants and the reaction rate using algebraic expressions.''',
        '''2. Rate law
         Determines the effect of a variation in the concentration of a reactant on the reaction rate, using the related algebraic expression.''',
        '''2. Le Chatelier’s Principle
         a. Predicts the direction of the shift in equilibrium of a system following a change in concentration, temperature or pressure.''',
        '''3. Equilibrium constant
         a. Acidity and alkalinity constants
         i. Writes as an algebraic expression the equilibrium constant for the dissociation of an acid or a base.''',
        '''3. Equilibrium constant
         c. Water ionization constant
         i. Calculates the molar concentration of hydronium and hydroxide ions, using the water ionization constant at 25°C.''',
        '''2. Physical properties of gases
         b. General gas law
         ii. Determines the relationship between the pressure of a gas and its temperature when the number of moles of gas and the volume are kept constant.''',
        '''2. Physical properties of gases
         c. Ideal gas law
         ii. Applies the mathematical relationship between the pressure, volume and number of moles of a gas, the ideal gas constant and the temperature of a gas (pV = nRT).
         d. Dalton’s law
         ii. Applies the mathematical relationship between the total pressure of a mixture of gases and the partial pressures of the component gases (ptotal = ppA+ ppB+ ppC+ …).''',
        '''2. Physical properties of gases
         c. Ideal gas law
         ii. Applies the mathematical relationship between the pressure, volume and number of moles of a gas, the ideal gas constant and the temperature of a gas (pV = nRT).''',
        '''1. Energy diagram
         a. Produces an energy diagram representing the energy balance for a chemical reaction.
         3. Enthalpy change
         b. Determines the enthalpy change of a reaction, using its energy diagram.''',
        '''4. Molar heat of reaction
         b. Determines the molar heat of a reaction using Hess’s Law or bonding enthalpies.''',
        '''4. Molar heat of reaction
         a. Determines the molar heat of a reaction using a calorimeter (combustion).''',
        '''4. Molar heat of reaction
         a. Determines the molar heat of a reaction using a calorimeter (neutralization).''',
        '''4. Molar heat of reaction
         a. Determines the molar heat of a reaction using a calorimeter (dissolution).''',
        '''1. Energy diagram
         b. Interprets the energy diagram of a chemical reaction.''',
        '''1. Factors that influence the reaction rate
         d. Temperature
         i. Explains the effect of the temperature of the reactants on the reaction rate.
         e. Catalyst
         i. Explains the effect of a catalyst on the reaction rate.''',
        '''1. Factors that influence the state of equilibrium
         a. Temperature
         i. Explains the effect of a temperature change on a system’s state of equilibrium.''',
        '''2. Le Chatelier’s Principle
         b. Predicts the effects of a shift in equilibrium on the concentrations of reactants and products.''',
        '''1. Factors that influence the state of equilibrium
         a. Temperature
         i. Explains the effect of a temperature change on a system’s state of equilibrium.
         2. Le Chatelier’s Principle
         a. Predicts the direction of the shift in equilibrium of a system following a change in concentration, temperature or pressure.''',
        '''2. Equilibrium constant
         a. Acidity and alkalinity constants
         iii. Associates the strength of acids and bases with the value of their acidity or alkalinity constant.''',
        '''3. Equilibrium constant
         b. Solubility product constant
         ii. Calculates the solubility product constant of a substance.'''
        ]
    },
    {
        'concepts': ['Gases','Gases','Gases','Energy changes in reactions','Energy changes in reactions','Reaction rates','Reaction rates','Chemical equilibrium','Chemical equilibrium','Chemical equilibrium','Gases','Gases','Gases','Gases','Energy changes in reactions','Energy changes in reactions','Energy changes in reactions','Energy changes in reactions','Reaction rates','Chemical equilibrium','Chemical equilibrium','Chemical equilibrium','Chemical equilibrium','Chemical equilibrium'],

        'POL':[]
    },
    {
        'concepts': ['Gases','Gases','Gases','Energy changes in reactions','Energy changes in reactions','Reaction rates','Reaction rates','Chemical equilibrium','Chemical equilibrium','Chemical equilibrium','Gases','Gases','Gases','Gases','Energy changes in reactions','Energy changes in reactions','Energy changes in reactions','Energy changes in reactions','Reaction rates','Chemical equilibrium','Chemical equilibrium','Chemical equilibrium','Chemical equilibrium','Chemical equilibrium'],

        'POL':[]
    },

    ]

    l = lookup('Solubility reactions', test_info[0]['POL'])
    return render_template(f'{test}.html', test_info = test_info, l=l)
    # this get the list l of found searched POL's and sends it to the page.



if __name__ == '__main__':
    app.run()
