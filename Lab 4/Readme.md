## Files

- `lab4_astar_audit.py` – contains the A* and UCS search code, the frontier check, the heuristic audit, and the overestimate test.
- `Lab4_output.txt` – contains the output saved from running the program.
- `Lab4_Report.docx` – contains the lab report and discussion of the results.

## Setup and run

Python 3.8 or newer is required. No extra packages are needed; the program uses Python's built-in `math` module.

Run the program from the VS Code terminal:

```powershell
python lab4_astar_audit.py
```

To save the output in a text file, run:

```powershell
python lab4_astar_audit.py > Lab4_output.txt
```

To see the output in the terminal and save it at the same time, run:

```powershell
python lab4_astar_audit.py | Tee-Object -FilePath Lab4_output.txt
```

## What the code does

1. **Task 1:** Shows the frontier and the `g`, `h`, and `f` values for the first three expansions.
2. **Heuristic audit:** Checks whether each heuristic value is admissible and whether the heuristic is consistent across each edge.
3. **Task 2:** Runs A* and Uniform Cost Search (UCS) on the same graph and compares their paths, costs, and expanded nodes.
4. **Task 3:** Changes `h(C)` from `2` to `10`, runs A* again, and compares the result with the original run. An extra test uses `h(C) = 4`.

## Input

The graph, edge costs, heuristic values, start node, and goal node are based on the Lab 4 manual's supplied example (pages 16–17).

## Notes

- The program uses the same graph and start/goal nodes for the A* and UCS comparison.
- The output file is created in the current terminal folder.
- Check the actual program output before including results in the report.
- Do not include passwords, private data, or virtual-environment folders in the submission.
