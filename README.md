# How to set environment variable on windows
1. Hold Win and press Pause.

2. Click Advanced System Settings.

3. Click Environment Variables.

4. Append ;C:\python27 to the Path variable.

5. Restart Command Prompt.

# Debugging:

## How to set breakpoint in PyCharm

1. Run —> Toggle Breakpoint —> Line Breakpoint

2. Right Click -> Debug "your script"

3. Run —> Debugging Actions —> Step Over


(Line Breakpoint) you want the debugger to temporarily pause execution there so you can decide what to do. This is persistent while "Temporary Line Breakpoint" gets removed automatically after debugging.

(Step Into) A method is about to be invoked, and you want to debug into the code of that method, so the next step is to go into that method and continue debugging step-by-step.

(Step Over) A method is about to be invoked, but you're not interested in debugging this particular invocation, so you want the debugger to execute that method completely as one entire step.

(Step Return) You're done debugging this method step-by-step, and you just want the debugger to run the entire method until it returns as one entire step.

(Resume) You want the debugger to resume "normal" execution instead of step-by-step


```
public class testprog {
    static void f (int x) {
        System.out.println ("num is " + (x+0)); // <- STEP INTO
    }

    static void g (int x) {
->      f(x); //
        f(1); // <----------------------------------- STEP OVER
    }

    public static void main (String args[]) {
        g(2);
        g(3); // <----------------------------------- STEP OUT OF
    }
}

```
If you were to step into at that point, you will move to the println() line in f(), stepping into the function call.

If you were to step over at that point, you will move to the f(1) line in g(), stepping over the function call.
