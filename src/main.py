from graph import MinCostFlowSolver

def main():
    solver = MinCostFlowSolver(4)
    solver.add_edge(0, 1, 2, 1)
    solver.add_edge(0, 2, 1, 5)
    solver.add_edge(1, 2, 1, 1)
    solver.add_edge(1, 3, 1, 6)
    solver.add_edge(2, 3, 2, 1)

    flow, cost = solver.solve(0, 3)
    print(f"Максимальный поток: {flow}")
    print(f"Минимальная стоимость: {cost}")

if __name__ == "__main__":
    main()