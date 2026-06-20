print("-----------TC7 PROGRESS BAR-----------")
chapters = {
"CHAPTER 1: FUNCTIONS, LIMITS, AND CONTINUITIES": {"total": 10, "completed": 1},
"CHAPTER 2: THE DERIVATIVE AND DIFFERENTIATION": {"total": 10, "completed": 0},
"CHAPTER 3: BEHAVIOR OF FUNCTIONS AND THEIR GRAPHS, EXTREME FUNCTION VALUES, AND APPROXIMATIONS": {"total": 10, "completed": 0},
"CHAPTER 5: LOGARITHMIC, EXPONENTIAL, INVERSE, TRIGONOMETRIC, AND HYPERBOLIC FUNCTIONS": {"total": 9, "completed": 0},
"CHAPTER 6: ADDITIONAL APPLICATIONS OF THE DEFINITE INTEGRAL": {"total": 5, "completed": 0},
"CHAPTER 7: TECHNIQUES OF INTEGRATION, INDETERMINATE FORMS, AND IMPROPER INTEGRALS": {"total": 10, "completed": 0},
"CHAPTER 8: POLYNOMIAL APPROXIMATIONS, SEQUENCES, AND INFINITE SERIES": {"total": 10, "completed": 0},
"CHAPTER 9: PARAMETRIC EQUATIONS, PLANE CURVES, AND POLAR GRAPHS": {"total": 5, "completed": 0},
}
bar_length = 20

for chapter, data in chapters.items():
	completed = data["completed"]
	total = data["total"]

	filled = int(20 * completed / total)
	bar = "█" * filled + "-" * (20 - filled)
	print(f"{chapter:7} [{bar}] {completed}/{total}")
