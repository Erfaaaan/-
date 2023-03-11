

import fuzzylite as fl
import numpy as np
#Declaring and Initializing the Fuzzy Engine
engine = fl.Engine(name="predection with fuzzy", description="we want to know realation betwwen relation between our factor to know our prouduct")

#Defining the Input Variables (Fuzzification)
engine.input_variables = [
    fl.InputVariable(
        name="Harvested",
        description="",
        enabled=True,
        minimum=0.000,
        maximum=1.000,
        lock_range=False,
        terms=[
            fl.Triangle("kam", 0.000, 0.250, 0.500), #Triangular Membership Function defining "Dark"
            fl.Triangle("motavaset", 0.250, 0.500, 0.750), #Triangular Membership Function defining "Medium"
            fl.Triangle("ziad", 0.500, 0.750, 1.000) #Triangular Membership Function defining "Bright"
        ]
    ),
    fl.InputVariable(
        name="Popultion",
        description="",
        enabled=True,
        minimum=0.000,
        maximum=1.000,
        lock_range=False,
        terms=[
            fl.Triangle("kam", 0.000, 0.250, 0.500), #Triangular Membership Function defining "Dark"
            fl.Triangle("motavaset", 0.250, 0.500, 0.750), #Triangular Membership Function defining "Medium"
            fl.Triangle("ziad", 0.500, 0.750, 1.000) #Triangular Membership Function defining "Bright"
        ]
    ),
    fl.InputVariable(
        name="Yeild",
        description="",
        enabled=True,
        minimum=0.000,
        maximum=1.000,
        lock_range=False,
        terms=[
            fl.Triangle("kam", 0.000, 0.250, 0.500), #Triangular Membership Function defining "Dark"
            fl.Triangle("motavaset", 0.250, 0.500, 0.750), #Triangular Membership Function defining "Medium"
            fl.Triangle("ziad", 0.500, 0.750, 1.000) #Triangular Membership Function defining "Bright"
        ]
    )
]

#Defining the Output Variables (Defuzzification)
engine.output_variables = [
    fl.OutputVariable(
        name="production",
        description="",
        enabled=True,
        minimum=0.000,
        maximum=1.000,
        lock_range=False,
        aggregation=fl.Maximum(),
        defuzzifier=fl.Centroid(200),
        lock_previous=False,
        terms=[
            fl.Triangle("LOW", 0.000, 0.250, 0.500), #Triangular Membership Function defining "LOW Light"
            fl.Triangle("MEDIUM", 0.250, 0.500, 0.750), #Triangular Membership Function defining "MEDIUM light"
            fl.Triangle("HIGH", 0.500, 0.750, 1.000) #Triangular Membership Function defining "HIGH Light"
        ]
    )
]

#Creation of Fuzzy Rule Base
engine.rule_blocks = [
    fl.RuleBlock(
        name="",
        description="",
        enabled=True,
        conjunction=None,
        disjunction=None,
        implication=fl.Minimum(),
        activation=fl.General(),
        rules=[
            fl.Rule.create("if harvest is kam then production is kam", engine),
            fl.Rule.create("if yeild is kam then prouduction is kam", engine),
            fl.Rule.create("if population is kam then production is kam", engine)
            fl.Rule.create("if harvest is ziad then production is ziad", engine),
            fl.Rule.create("if yeild is ziad then production is ziad", engine),
            fl.Rule.create("if population is ziad then production is ziad", engine),
            fl.Rule.create("if harvest is motvaset then production is motvaset", engine),
            fl.Rule.create("if yield is motvaset then production is motvaset", engine),
            fl.Rule.create("if population is motvaset then production is motvaset", engine),
        ]
    )
]

#bayd be jaye arrange az matris ige estfade mishod ke daryaft nashod
for i in np.arange(0,1.1,0.1):
    #Set input
    #baraye har dade bayd shomare on dar matris gharar migereft
    engine.input_variable("Yeild").value = i[0]
    engine.input_variable("Harvest").value = i[1]
    engine.input_variable("Ambient").value = i[2]
    #run Engine
    engine.process()
    #Print output
    print(engine.output_variable("prouduction").value)
