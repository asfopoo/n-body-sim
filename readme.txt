1. Author: Edward Nardo, JHED ID: C2FFF9
2. Module Info: Module 4, N-Body simulation, due: Sunday, February 21, 2021
3. Approach:

nbody.py - I started by declaring all of the constants in the setup.  These include total time, time delta, G,
the lists of planets, and the list containing the lists of planets.  Then, using the psuedo-code, I implemented each
section of the calculation.  Starting with a while loop which starts at time 0 and executes until the total time reaches
some arbitrary time, it loops the list of lists called planets, skipping the 3rd element (the sun), and does the calculations.
I used a string of all hashes, or comment blocks, to separate each section of the calculation for better readability.  I
started with calculating radius, then using the radius to calculate the pairwise force F.  From there I calculated
the force of the x and y component.  Then the acceleration of the x and y component.  From there I calculated the
resulting velocity and then the resulting position.  Once the while loop finishes I create a list called pretty_list
and append each list individually so that I can format the output in a way that is more readable.

4. Known bugs: The first few iterations of the time steps are very close to what it should be, with what looks like small
rounding errors.  As the time steps progress, the errors get further and further from the actual answer.  Attached
in my image of the output, I ran the program twice, once with total time = 50000 and time delta = 25000.  In this first
run you can see the output is VERY similar to what it should be given in the assignment outline.
The second run has the total time as 157788000 and time delta as 25000, which has drastically skewed the final output.